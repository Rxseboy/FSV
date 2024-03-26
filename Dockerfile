# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9.6
expose 8501
cmd mkdir -p /app
WORKDIR /app
copy requirements.txt ./requirements.txt
run pip3 install -r requirements.txt
copy . .
ENTRYPOINT [ "streamlit", "run" ]
CMD ["app.py"]
#Expose port 8501
#EXPOSE 8501

#upgrade pip
#RUN python -m pip install --upgrade pip

#Copy Requirements.txt file into app directory
#COPY requirements.txt app/requirements.txt

#install all requirements in requirements.txt
#RUN pip3 install -r app/requirements.txt

#Copy all files in current directory into app directory
#COPY . /app

#Change Working Directory to app directory
#WORKDIR /app

#Run the application on port 8501
#ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]