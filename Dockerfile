# Code runtime ----> AKA python Interpreter
FROM python:slim

# Set working directoty inside the container
WORKDIR /code/app/

# Copy requirements file into the container
COPY requirements.txt /code/app/requirements.txt

# Install the packages and dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the app into the conatainer path
COPY app.py /code/app/

# Expose port for the the flask application
EXPOSE 5000

# Run the flask app using app.py
CMD ["python3", "app.py"]
