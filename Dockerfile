FROM python:3

# to skip buffering
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# Created a directory in the container 
# ( use any name, make sure to change it in below lines as well )
RUN mkdir /app

# set as working directory
WORKDIR /app

# copy the contents of entire directory to the directory in the container 
COPY . /app/

# install package in the container
RUN pip install -r requirements.txt
