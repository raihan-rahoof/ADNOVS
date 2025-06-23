#1. Base Image
FROM python:3.10-slim

#2. Environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#3. Set Working Directory
WORKDIR /app

#4. Install system-level dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

#5. Copy Python dependency file
COPY requirements.txt .

#6. Install Python Packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


#7. Copy Project
COPY . .

#8. Expose Port
EXPOSE 8000

#9. Run Entrypoint
CMD ["gunicorn", "crud.wsgi:application", "--bind", "0.0.0.0:8000", "--reload"]
