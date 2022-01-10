# local_run.sh does the following:

# build and run the docker locally with the following features:
#     - host machine work_dir mapped to /home/work_dir in the docker
#     - env variable DELAIRSTACK_PROCESS_WORKDIR set to /home/work_dir/

# please note that simu_work_dir should contain a simulated inputs.json file as it will be set when running the docker on Alteia



docker build -t pcvs3d .
docker run -it -v work_dir:/home/work_dir --env DELAIRSTACK_PROCESS_WORKDIR='/home/work_dir/' --name pcvs3d_1 pcvs3d


docker run -it -v C:\Users\michael.delagarde\Documents\DEV\CustomAnalytics\pcvs3d\work_dir:/home/work_dir -e DELAIRSTACK_PROCESS_WORKDIR='/home/work_dir/' --name pcvs3d_1 pcvs3d
docker run -it -v C:\Users\michael.delagarde\Documents\DEV\CustomAnalytics\pcvs3d\python:/home/python -e DELAIRSTACK_PROCESS_WORKDIR='/home/work_dir/' --name pcvs3d_1 pcvs3d
docker run -it -v C:\Users\michael.delagarde\Documents\DEV\CustomAnalytics\pcvs3d\python:/home/python -e DELAIRSTACK_PROCESS_WORKDIR='/home/work_dir/' --name ccd_1 ccd


xvfb-run CloudCompare -SILENT \
-O ./untitled1.obj \
-SAMPLE_MESH POINTS 500000