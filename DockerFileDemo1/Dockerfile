#Deriving the latest base image
FROM python:3.9


#Labels as key value pair
LABEL Maintainer="nikita"


# Set the working directory in the container
WORKDIR /app

# Copy only the requirements.txt (or other dependency files) first, install the dependencies,
# and then copy the rest of the source code. This avoids re-installing packages if only the application code changes.

COPY requirements.txt .
# Upgrade pip and install dependencies
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#Copy all files in the current directory to the container
COPY . .

# Set an environment variable (optional)
ENV NAME world

# Run the Python script
CMD ["python3", "./hello_world.py"]
