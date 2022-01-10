#freely inspired from https://github.com/alteia-ai/rust-detector/blob/master/detect_rust.py#L5
import json
import logging
import os
from pathlib import Path
import sys
from DrawRaster import scatter_geotiff

import time

from upload_dataset import upload_dataset


LOG_FORMAT = '[%(levelname)s] %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=LOG_FORMAT)



def load_inputs(input_path):
	inputs_desc = json.load(open(input_path))
	inputs = inputs_desc.get('inputs')
	parameters = inputs_desc.get('parameters')
	return inputs, parameters


def main():

	SCRIPT_DIR = Path(__file__).parent.resolve()
	WORKING_DIR = os.getenv('DELAIRSTACK_PROCESS_WORKDIR')
	if not WORKING_DIR:
		raise KeyError('DELAIRSTACK_PROCESS_WORKDIR environment variable must be defined')
	WORKING_DIR = Path(WORKING_DIR).resolve()

	logging.debug('WORKING_DIR :')	
	logging.debug(WORKING_DIR)


	logging.debug('Extracting inputs and parameters...')
	# Retrieve inputs and parameters from inputs.json
	inputs, parameters = load_inputs(WORKING_DIR / 'inputs.json')

	logging.debug('inputs :')	
	logging.debug(inputs)
	logging.debug('parameters :')	
	logging.debug(parameters)

	# file_path = WORKING_DIR / inputs.get('input_pc').get('components')[0]['filename']
	input_path = inputs.get('input_pc').get('components')[0]['path']
	ref_path = inputs.get('ref_pc').get('components')[0]['path']
	project_id = inputs.get('input_pc').get('project')
	mission_id = inputs.get('input_pc').get('mission')
	hsrs = inputs.get('input_pc').get('horizontal_srs_wkt')
	vsrs = inputs.get('input_pc').get('vertical_srs_wkt')

	pcdiff(input_path, ref_path, work_dir)

	logging.debug('Generating outputs.json file...')

	outpath = WORKING_DIR / 'output.las'
	output = {
		"outputs": {
			"output": {  # Must match the name of deliverable in rust-detector.yaml
				"type": "pcl",
				"format": "las",
				# "categories": ["DSM"],
				"name": "output",
				"components": [
					{
						"name": "output",
						# "filename": "output.tif",
						"path": str(outpath)
					}
				]
			}
		},
		"version": "v1.0"
	}
	with open(WORKING_DIR / 'outputs.json', 'w+') as f:
		json.dump(output, f)

	script_dir = str(SCRIPT_DIR)
	upload_dataset(str(outpath), project_id, mission_id, script_dir, hsrs, vsrs)

	logging.debug('End.')




if __name__ == "__main__":

	main()