# Use an official Python runtime as a parent image
FROM python:3.11.6-alpine3.18

# install utilities
RUN apt-get update && \
    apt-get install --no-install-recommends -y curl

RUN python3 -m pip --no-cache-dir install --upgrade pip && \
    python3 --version && \
    pip3 --version

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Define an environment variable for the port (with a default value)
ENV PORT 80

# Expose the port as defined by the PORT environment variable
EXPOSE $PORT

# Define environment variable (if needed)
ENV NAME World

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT"]