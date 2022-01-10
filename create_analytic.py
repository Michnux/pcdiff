import alteia



sdk = alteia.SDK(config_path='./config-connections.json')


analytic = sdk.analytics.search(name="alteiademo/pcvs3d")
if len(analytic)>0:
	analytic=analytic[0]
	sdk.analytics.delete(analytic=analytic.id)

sdk.analytics.create(name="alteiademo/pcvs3d",
	version="1.0.0",
	display_name="pcvs3d",
	description="Generates a difference Point Cloud, from a Point Cloud to a Reference (that can be a Point Cloud or another 3d file",
	docker_image="registry-1.docker.io/michaeldelagarde/pcvs3d:latest",
	company="5c1a2567b3c575583e8a650d",
	instance_type='small',
	volume_size=20,
	inputs=[{
		"name": "input_pc",
		"display_name": "input_pc",
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
		"name": "reference",
		"display_name": "ref_pc",
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
	parameters=[{
		"name": "min",
		"display_name": "min",
		"description": "min distance to be displayed",
		"required": True,
		"scheme": {
			"type": "string"#, "pattern": "^[0-9]$"
		}
	 },
	 {
		"name": "max",
		"display_name": "max",
		"description": "max distance to be displayed",
		"required": True,
		"scheme": {
			"type": "string"#, "pattern": "^[0-9]$"
		}
	 }],
	deliverables=[
	# {
	# 	"name": "outputtif",
	# 	"display_name": "outputtif",
	# 	"description": "outputtif",
	# 	"scheme": {
	# 		"type": "string", "pattern": "^[0-9a-f]{24}$"
	# 	},
	# 	"source": {
	# 		"service": "data-manager",
	# 		"resource": "dataset",
	# 		"scheme": {
	# 			"type": "object",
	# 			"properties": {"type": {"const": "raster"}},
	# 			"required": ["type"]
	# 		},
	# 	},
	# 	"required": False
	# }
	],
	tags=["croquette"],
	groups=["UTILS"])