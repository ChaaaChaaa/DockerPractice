#FROM python:3.8-slim
#WORKDIR /app
#COPY . /app
#RUN pip install --no-cache-dir -r requirements.txt
#EXPOSE 5000
#ENV NAME dockertest
#CMD ["python","./app.py"]

# Use the official Python image as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for the app name
ENV NAME dockertest

# Run app.py when the container launches
CMD ["python", "app.py"]



