FROM python:3.8
#FROM pdal/pdal:2.3

COPY requirements.txt ./
RUN python -m pip install --trusted-host=pypi.org --trusted-host=files.pythonhosted.org -r requirements.txt

COPY script_dir /home/script_dir/
#COPY python /home/python/

#CMD ["python", "/home/script_dir/main.py"]
CMD ["sleep", "1d"]
