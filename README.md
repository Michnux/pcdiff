## Description of the Analytic:

Generates a difference Point Cloud, from a Point Cloud to a reference (that can be a Point Cloud or onother 3d format)


## Inputs:

The PointCloud (.las) 
The reference (.las)


## Parameters:

Min: Min distance to display in the Difference Point Cloud
Max: Max distance to display in the Difference Point Cloud


## Outputs:

A difference Point Cloud (.las)


## Analytics creation

create_analytic.py allows to create the analytics without using the CLI
This requires credentials to be added to the project dir in a file named : config-connections.json
with the follwing structure:

{
	"user":"jjj@fff.com",
	"password":"pass",
	"url":"https://app.alteia.com"
}

Credentials to access the docker registry used still have to be created from the CLI


## Fix-me:

The scripts generates a raster (output.las) as a final result.
A dataset is created and the output.las component uplaoded from the docker using the SDK (cf. uplaod_dataset.py file)
This requires credentials to be added to the script_dir in a file named : config-connections.json
with the follwing structure:

{
	"user":"jjj@fff.com",
	"password":"pass",
	"url":"https://app.alteia.com"
}

this is a quick-fix as the transfert of the generated results (as described in the outputs.json file) doesn't seem to work properly
