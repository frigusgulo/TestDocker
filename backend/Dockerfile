# FROM nvidia/cuda:11.2.0-runtime-ubuntu20.04

# # Install utilities
# RUN apt-get update && \
#     apt-get install --no-install-recommends -y curl

# # Set environment variables
# ENV CONDA_AUTO_UPDATE_CONDA=false \
#     PATH=/opt/miniconda/bin:$PATH

# # Install Miniconda
# RUN curl -sLo ~/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-py38_4.9.2-Linux-x86_64.sh \
#     && chmod +x ~/miniconda.sh \
#     && ~/miniconda.sh -b -p /opt/miniconda \
#     && rm ~/miniconda.sh \
#     && sed -i "$ a PATH=/opt/miniconda/bin:\$PATH" /etc/environment


FROM python:latest

RUN apt-get update && \
    apt-get install --no-install-recommends -y curl

# Installing python dependencies
RUN python3 -m pip --no-cache-dir install --upgrade pip && \
    python3 --version && \
    pip3 --version

# RUN pip3 --timeout=300 --no-cache-dir install torch==1.10.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html

COPY ./requirements.txt .
RUN pip3  --no-cache-dir install -r requirements.txt

# Copy the application code
COPY ./app /app

# Set the working directory to /app
WORKDIR /app

# Define an environment variable for the port (with a default value)
ENV PORT 8080

# Expose the port as defined by the PORT environment variable
EXPOSE $PORT

# Make the start.sh script executable

# Run the start.sh script with the specified port

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

