# Use the latest Python 3.12 slim image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the required Python packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Start the Gunicorn server and run the bot script
CMD gunicorn app:app & python3 bot.py
