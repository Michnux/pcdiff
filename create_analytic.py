import alteia



sdk = alteia.SDK(config_path='./config-connections.json')


analytic = sdk.analytics.search(name="alteiademo/pcdiff")
if len(analytic)>0:
	analytic=analytic[0]
	sdk.analytics.delete(analytic=analytic.id)

sdk.analytics.create(name="alteiademo/pcdiff",
	version="1.0.0",
	display_name="Point Clouds Difference",
	description="Generates a difference Point Cloud, from a Point Cloud to a Reference",
	docker_image="registry-1.docker.io/michaeldelagarde/pcdiff:latest",
	company="5c1a2567b3c575583e8a650d",
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
	tags=["croquette"],
	groups=["UTILS"])