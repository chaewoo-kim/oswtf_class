# 프론트
ARG NODE_VERSION=20.11.1

FROM node:${NODE_VERSION}-alpine

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json ./app/frontend/
RUN npm ci --omit=dev

COPY frontend/ ./
RUN npm run build


# 서버
FROM python:3.9

WORKDIR /app

COPY backend/ ./

RUN pip install -r requirements.txt


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]