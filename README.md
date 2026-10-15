# CloudDeploy — Containerized Flask Application on AWS EC2

A lightweight Python Flask web application containerized with Docker, published to Docker Hub, and deployed on Amazon EC2. This project demonstrates the fundamentals of containerization, cloud deployment, network configuration, application health checks, and source-code version control using Git and GitHub.

## Project Overview

CloudDeploy is a simple web application designed to demonstrate how a containerized application can be deployed and accessed over the internet using AWS infrastructure.

The application is packaged into a Docker image, stored in Docker Hub, and executed inside a Docker container on an Amazon Linux 2023 EC2 instance.

## Architecture

```text
Developer
   |
   v
VS Code + Python Flask
   |
   v
Docker Image
   |
   v
Docker Hub
   |
   v
Amazon EC2
(Amazon Linux 2023)
   |
   v
Docker Container
   |
   v
Flask Application
   |
   +----> Homepage (/)
   |
   +----> Health Check (/health)
```

GitHub stores the application source code and project documentation. Docker Hub stores the built container image, while Amazon EC2 provides the cloud server that runs the container.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application programming language |
| Flask | Web application framework |
| Gunicorn | Production-oriented WSGI application server |
| Docker | Application containerization |
| Docker Hub | Container image registry |
| Amazon EC2 | Cloud compute infrastructure |
| Amazon Linux 2023 | EC2 operating system |
| Git and GitHub | Source control and code hosting |
| Visual Studio Code | Development environment |

## Features

- Lightweight Flask web application.
- Docker-based packaging and deployment.
- Non-root user inside the Docker container.
- Gunicorn application server.
- Dedicated application health endpoint.
- Automatic container restart policy.
- Cloud deployment using Amazon EC2.
- Public access through the EC2 public IPv4 address.
- Version-controlled source code on GitHub.

## Project Structure

```text
clouddeploy-containerized-app/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

- `app.py` — Flask application and routes.
- `requirements.txt` — Python dependencies.
- `Dockerfile` — Instructions for building the Docker image.
- `.dockerignore` — Files and directories excluded from the Docker build context.
- `.gitignore` — Files excluded from Git tracking.
- `README.md` — Project documentation.

## Application Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Displays the application homepage |
| `/health` | Returns a JSON health response |

The health endpoint can be used to verify that the Flask application responds to requests.

## Run Locally

### Prerequisites

Install the following tools:

- Python 3.12 or compatible environment.
- Docker Desktop.
- Git (optional for cloning the repository).

### 1. Clone the repository

```bash
git clone https://github.com/vivekgaikwad-droid/clouddeploy-containerized-app.git
cd clouddeploy-containerized-app
```

### 2. Build the Docker image

```bash
docker build -t clouddeploy:1.0 .
```

### 3. Run the container

```bash
docker run -d --name clouddeploy -p 5000:5000 clouddeploy:1.0
```

### 4. Test the application

Open these URLs in your browser:

- Homepage: `http://localhost:5000/`
- Health check: `http://localhost:5000/health`

### 5. View the running container

```bash
docker ps
```

To stop and remove the local container:

```bash
docker stop clouddeploy
docker rm clouddeploy
```

## Docker Hub

The built image is published to Docker Hub.

**Repository:** [vivekgaikwad2309/clouddeploy](https://hub.docker.com/r/vivekgaikwad2309/clouddeploy)

**Image tag:** `1.0`

Pull the image:

```bash
docker pull vivekgaikwad2309/clouddeploy:1.0
```

Run it:

```bash
docker run -d --name clouddeploy -p 5000:5000 vivekgaikwad2309/clouddeploy:1.0
```

## AWS EC2 Deployment

The application is deployed directly on an Amazon EC2 instance in the Asia Pacific (Sydney) region (`ap-southeast-2`).

### Deployment procedure

1. Launch an Amazon Linux 2023 EC2 instance.
2. Configure a security group for SSH access and application traffic.
3. Install Docker on the EC2 instance.
4. Pull the published image from Docker Hub.
5. Run the container and map host port `5000` to container port `5000`.
6. Access the application through the instance's public IPv4 address.

### Docker deployment commands

Run the following commands on the EC2 instance after Docker is installed:

```bash
sudo systemctl enable --now docker

sudo docker pull vivekgaikwad2309/clouddeploy:1.0

sudo docker run -d --restart unless-stopped \
  --name clouddeploy \
  -p 5000:5000 \
  vivekgaikwad2309/clouddeploy:1.0
```

### Access the deployed application

Replace `EC2_PUBLIC_IP` with the current public IPv4 address of your instance.

- Homepage: `http://EC2_PUBLIC_IP:5000/`
- Health check: `http://EC2_PUBLIC_IP:5000/health`

The instance's public IP can change after a stop/start cycle unless a persistent Elastic IP is configured.

## Testing and Verification

The following checks were performed during deployment:

- Docker image built successfully.
- Local Docker container started successfully.
- Container image pushed to Docker Hub.
- Amazon EC2 instance launched successfully.
- Application accessed through the EC2 public address.
- Homepage and health endpoint opened successfully.

## Security Considerations

- Never commit AWS access keys, private keys, passwords, or authentication tokens.
- Keep SSH access restricted to trusted IP addresses.
- Expose only the ports required by the application.
- Port `5000` is used for demonstration and should not be exposed publicly longer than necessary.
- For production use, configure HTTPS, appropriate access controls, monitoring, and a production-ready network architecture.
- Review AWS billing and terminate unused resources.

## Limitations

- The application runs on a single EC2 instance.
- High availability and automatic scaling are not configured.
- HTTPS and a custom domain are not configured.
- Application updates currently require rebuilding and publishing the Docker image, then updating the running deployment.
- ECS orchestration and automated CI/CD are not part of the current implementation.

## Future Enhancements

- Automate image builds and publishing using GitHub Actions.
- Implement automated deployment to EC2.
- Add HTTPS using a domain and reverse proxy.
- Introduce application monitoring and centralized logs.
- Add automated tests and container image scanning.
- Explore Amazon ECS for managed container orchestration.

## Author

**Vivek Gaikwad**

GitHub: [vivekgaikwad-droid](https://github.com/vivekgaikwad-droid)

Project repository: [clouddeploy-containerized-app](https://github.com/vivekgaikwad-droid/clouddeploy-containerized-app)

## License

No license has been added yet. Add an appropriate open-source license if you intend to permit others to reuse or modify this project.
