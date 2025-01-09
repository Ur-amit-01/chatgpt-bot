# Use the latest Python 3.12 slim image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Upgrade pip and install the required Python packages
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port your app will run on
EXPOSE 8000

# Start the Gunicorn server and run the bot script
CMD ["gunicorn", "app:app", "&", "python3", "bot.py"]
