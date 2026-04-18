FROM --platform=linux/amd64 python:3.14-rc-slim

# Create a working directory
WORKDIR /app

# Copy the requirements file into the image
COPY requirements.txt web.py app.py /app/
COPY templates /app/templates
COPY static /app/static
# Environment variables can be set at container startup 
# without copying the .env file into the container.
#COPY .env /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8081

# Set the entrypoint for the container
ENTRYPOINT ["python", "web.py"]