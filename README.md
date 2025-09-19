## Assignment: Write a Dockerfile to Containerize a Python App

### Objective
Create a Dockerfile to containerize the provided Python app.

### Requirements
- The app should run on `port 5000`.
- Use Python 3.9 or higher as the base image.
- Install dependencies using `requirements.txt`.
- The final image should have minimal size (use best practices).

### Steps
1. Write a `Dockerfile` to build the image.
2. Build the Docker image suing this command: _docker build -t python-docker-app ._
3. Run the container: _docker run -p 5000:5000 python-docker-app_
4. Verify the app is accessible at `http://localhost:5000`.

### Submission
- Push your `Dockerfile` to the repository.
- Ensure it works as described above.
- Thank you.
