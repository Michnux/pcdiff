# local_run.sh does the following:

# build and run the docker locally with the following features:
#     - host machine work_dir mapped to /home/work_dir in the docker
#     - env variable DELAIRSTACK_PROCESS_WORKDIR set to /home/work_dir/

# please note that simu_work_dir should contain a simulated inputs.json file as it will be set when running the docker on Alteia



docker build -t pcdiff .
docker run -it -v work_dir:/home/work_dir --env DELAIRSTACK_PROCESS_WORKDIR='/home/work_dir/' --name pcdiff_1 pcdiff


docker run -it -v C:\Users\michael.delagarde\Documents\DEV\CustomAnalytics\pcdiff\work_dir:/home/work_dir -e DELAIRSTACK_PROCESS_WORKDIR='/home/work_dir/' --name  pcdiff_1 pcdiff
docker run -it -v C:\Users\michael.delagarde\Documents\DEV\CustomAnalytics\pcdiff\python:/home/python -e DELAIRSTACK_PROCESS_WORKDIR='/home/work_dir/' --name  pcdiff_1 pcdiff

