import alteia




def main():

	sdk = alteia.SDK(config_path='./config-connections.json')

	projects = sdk.projects.search(name = 'Delair_BIM')

	print(projects)

	project = projects[0]

	# missions = sdk.missions.search(project=project.id)
	# # print([mission.name for mission in missions])
	# mission = missions[0]
	# help(sdk.datasets.search)

	datasets = sdk.datasets.search(filter={	'project': {'$eq':project.id},
											# 'mission': {'$eq':mission.id},
											'name': {'$eq':'sampled point cloud'}
											})
	# datasets = sdk.datasets.search(project=project.id)

	for ds in datasets:
		print(ds.__dict__)

	dataset = datasets[0]

	# file_name = dataset.components[0]['filename']


	print('####################################')




	datasets = sdk.datasets.search(filter={	'project': {'$eq':project.id},
											# 'mission': {'$eq':mission.id},
											'name': {'$eq':'Point Cloud'}
											})
	# datasets = sdk.datasets.search(project=project.id)

	for ds in datasets:
		print(ds.__dict__)

	dataset = datasets[0]

	# file_name = dataset.components[0]['filename']




	# hsrs = dataset.horizontal_srs_wkt
	# vsrs = dataset.vertical_srs_wkt
	# offset = dataset.offset
	# # print(offset, hsrs, vsrs)

	# # help(sdk.datasets.download_component)

	# for comp in dataset.components:
	# 	obj = sdk.datasets.download_component(dataset=dataset.id, component=comp.get("name"), overwrite=True)




if __name__ == "__main__":

	main()