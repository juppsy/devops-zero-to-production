# Base Image
FROM python:3.14-slim

# Working Directory
WORKDIR /app

# Copy Dependencies
COPY requirements.txt .

# Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Application Code
COPY . .

# Expose Port
EXPOSE 8000

# Command to Run the Application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
