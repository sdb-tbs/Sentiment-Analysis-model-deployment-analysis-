FROM python:3.8-slim

WORKDIR /app

# Install any needed packages specified in requirements.txt
# First, copy only requirements.txt to leverage Docker cache
COPY requirements.txt /app/
RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . /app

EXPOSE 8000

ENV NAME World

CMD ["gunicorn", "-w", "4", "--threads", "2", "-b", "0.0.0.0:8000", "main:app"]
