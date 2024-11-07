# Step 1: Use an official Python runtime as a parent image
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY . /app

# Step 4: Install any dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose port 5000 for Flask
EXPOSE 5000

# Step 6: Set the environment variable to specify the app entry point
ENV FLASK_APP=app.py

# Step 7: Run the Flask app when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]

