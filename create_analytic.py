import alteia



sdk = alteia.SDK(config_path='./config-connections-setec.json')


analytic = sdk.analytics.search(name="seteccapture/pcdiff_setec")
if len(analytic)>0:
	analytic=analytic[0]
	sdk.analytics.delete(analytic=analytic.id)

sdk.analytics.create(name="seteccapture/pcdiff_setec",
	version="1.0.0",
	display_name="pcdiff",
	description="Generates a difference Point Cloud, from a Point Cloud to a Reference",
	docker_image="registry-1.docker.io/michaeldelagarde/pcdiff_setec:latest",
	company="61386c9dd215430006a73e57",
	instance_type='small',
	volume_size=20,
	inputs=[{
		"name": "input_pc",
		"display_name": "input point cloud",
		"description": ".las file",
		"scheme": {
			"type": "string", "pattern": "^[0-9a-f]{24}$"
		},
		"source": {
			"service": "data-manager",
			"resource": "dataset",
			"scheme": {
				"type": "object",
				"properties": {"type": {"const": "pcl"}},
				"required": ["type"]
			},
		},
		"required": True
	},
	{
		"name": "ref_pc",
		"display_name": "reference point cloud",
		"description": ".las file",
		"scheme": {
			"type": "string", "pattern": "^[0-9a-f]{24}$"
		},
		"source": {
			"service": "data-manager",
			"resource": "dataset",
			"scheme": {
				"type": "object",
				"properties": {"type": {"const": "pcl"}},
				"required": ["type"]
			},
		},
		"required": True
	},],
	parameters=[
	 {
		"name": "max_dist",
		"display_name": "max distance",
		"description": "max distance between point clouds to be displayed (default 1m)",
		"required": False,
		"scheme": {
			"type": "string"#, "pattern": "^[0-9]$"
		}
	 }],
	deliverables=[
	{
		"name": "output",
		"display_name": "output_pcdiff",
		"description": "output_pcdiff",
		"scheme": {
			"type": "string", "pattern": "^[0-9a-f]{24}$"
		},
		"source": {
			"service": "data-manager",
			"resource": "dataset",
			"scheme": {
				"type": "object",
				"properties": {"type": {"const": "pcl"}},
				"required": ["type"]
			},
		},
		"required": True
	}
	],
	groups=["UTILS"])