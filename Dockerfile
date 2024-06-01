FROM python:3-alpine
WORKDIR /app

RUN pip install virtualenv
RUN source .venv/pythonbin/activate

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

RUN apk add git

EXPOSE 8000

COPY . .