import alteia



def upload_dataset(file_path, project_id, mission_id, script_dir):

	sdk = alteia.SDK(config_path=script_dir+'/config-connections.json')

	new_dataset = sdk.datasets.create_raster_dataset(	name='output_dsm',
														project=project_id,
														mission=mission_id,
														categories=['dsm'])

	sdk.datasets.upload_file(dataset=new_dataset.id,
							 component='raster',
							 file_path=file_path)


if __name__ == "__main__":

	upload_dataset('../work_dir/max.tif', '61c1d5a73e614e00085c6a01', '61c4aeffd730570008b5e7c9', './')