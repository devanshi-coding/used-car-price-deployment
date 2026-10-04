# Used Car Price Prediction API

An end-to-end Machine Learning pipeline and REST API deployed on AWS EC2 using Docker and FastAPI. The model predicts the resale price of used cars based on vehicle attributes such as make, model, condition, mileage, and transmission.

---

## Tech Stack & Architecture

* **Language:** Python 3.11
* **Machine Learning:** scikit-learn (v1.6.1), category-encoders (v2.6.3), pandas, joblib
* **API Framework:** FastAPI, Uvicorn, Pydantic
* **Containerization:** Docker
* **Cloud Infrastructure:** AWS EC2 (Ubuntu 24.04 LTS, t2.micro)

---

## API Endpoints

* `GET /` - Health check route
* `GET /docs` - Interactive Swagger UI documentation
* `POST /predict` - Predict car price based on input JSON

---

## Sample Request & Response

### Request (`POST /predict`)

```json
{
  "make": "Toyota",
  "model": "Camry",
  "trim": "LE",
  "body": "Sedan",
  "transmission": "automatic",
  "state": "CA",
  "condition": 4,
  "odometer": 45000,
  "color": "black",
  "interior": "black",
  "car_age": 5
}

```

### Response (`200 OK`)

```json
{
  "predicted_price": 10872.68,
  "currency": "USD"
}

```

---

## Local Setup & Execution

### 1. Clone the Repository

```bash
git clone https://github.com/devanshi-coding/used-car-price-deployment.git
cd used-car-price-deployment

```

### 2. Build and Run via Docker

```bash
docker build -t used-car-price-api .
docker run -d -p 8000:8000 --name car-api used-car-price-api

```

### 3. Access API Documentation

Open your browser and navigate to `http://localhost:8000/docs`.

---

## Deployment Guide (AWS EC2)

1. Launch an AWS EC2 instance (`t2.micro`, Ubuntu 24.04 LTS).
2. Configure Security Group inbound rules:
* **SSH:** Port 22
* **Custom TCP:** Port 8000 (for FastAPI)


3. SSH into the EC2 instance and install Docker:
```bash
sudo apt update -y && sudo apt install docker.io git -y
sudo systemctl start docker

```


4. Clone repo, build image, and launch container:
```bash
git clone https://github.com/devanshi-coding/used-car-price-deployment.git
cd used-car-price-deployment
sudo docker build -t used-car-price-api .
sudo docker run -d -p 8000:8000 --name car-api used-car-price-api

```
