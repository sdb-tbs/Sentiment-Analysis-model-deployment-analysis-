# Sentiment Analysis Service

This project provides a sentiment analysis service using a Flask application with a Gunicorn server, containerized using Docker, and served behind an NGINX reverse proxy. The sentiment analysis is done by a pre-trained model from the Hugging Face model hub, capable of processing multiple parallel incoming requests efficiently.

## About The Model
DistilBERT is a faster and lighter version of the BERT model. It is designed to provide a good balance between performance and size, making it more accessible for use on devices with limited resources or for applications that require faster processing.
distilbert/distilbert-base-uncased-finetuned-sst-2-english is a fine-tune checkpoint of DistilBERT-base-uncased, fine-tuned on SST-2. This model is not too large and considering the aim of task (containarizing), it can be a light and easy choice for showcase.
More information : [huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english)





## Architecture

- **Flask Application**: Serves as the backend API, providing sentiment analysis through a POST endpoint.
- **Gunicorn**: WSGI server for running the Flask application, allowing concurrent processing of requests.
- **NGINX**: Acts as a reverse proxy, forwarding client requests to Gunicorn/Flask and enhancing performance and security.
- **Docker**: Containers for each component ensure isolated and consistent environments.
- **Docker Compose**: Orchestrates the multi-container setup, managing configurations and interactions.

## Setup Instructions

### Prerequisites

- Docker
- Docker Compose
- Python 

### Build and Run Containers

Use Docker Compose to build and run the application.

```bash
docker-compose up --build
```

### Testing the Application
You can use a Jupyter notebook to send requests and display responses. 

### Maintenance and Logs

Check the application logs using Docker Compose:
```bash
docker-compose logs
```
To stop the service:
```bash
docker-compose down
```
For updating the application or dependencies, rebuild the containers:
```bash
docker-compose up --build
```
### Files and Directories
- Dockerfile: Contains instructions to build the Docker image for the Flask application.
- docker-compose.yml: Defines the multi-container setup with NGINX and the Flask application.
- requirements.txt: Lists the Python dependencies
- nginx.conf: Configuration file for the NGINX server.
- notebook/: Directory containing the Jupyter notebook demonstration.

### Contact
For any questions or support please contact:
soodabeh.tabarsaee@gmail.com