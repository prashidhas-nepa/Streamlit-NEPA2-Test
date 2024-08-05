# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port Streamlit will run on
EXPOSE 4370

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=4370", "--server.address=0.0.0.0"]
