FROM python:3.7.3-stretch

## Step 1:
# Create a working directory
WORKDIR /app

## Step 2:
# Install packages from requirements.txt
# hadolint ignore=DL3013
COPY requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install --trusted-host pypi.python.org -r requirements.txt


## Step 3:
# Copy source code to working directory
COPY . app.py /app/

## Step 4:
# Expose port 80
EXPOSE 80

## Step 5:
# Run app.py at container launch
CMD ["python", "app.py"]
