# Use an official Python runtime as a parent image
FROM python:latest

# install utilities
RUN apt-get update && \
    apt-get install --no-install-recommends -y curl

RUN python3 -m pip --no-cache-dir install --upgrade pip && \
    python3 --version && \
    pip3 --version

COPY ./requirements.txt .
RUN pip3  --no-cache-dir install -r requirements.txt

COPY ./app /app
# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
# Define an environment variable for the port (with a default value)
ENV PORT 8081

# Expose the port as defined by the PORT environment variable
EXPOSE $PORT

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]