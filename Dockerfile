# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . /app

# Expose the port Streamlit will run on
EXPOSE 8501

# Command to run the Streamlit app on port 8501
ENTRYPOINT [ "streamlit", "run" ]
CMD ["app.py"]