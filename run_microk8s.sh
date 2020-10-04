#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub
# Step 1:
# This is your Docker ID/path
dockerpath=cazacov/learning:mlk8s

# Step 2
# Run the Docker Hub container with kubernetes
microk8s kubectl run mlk8s \
    --generator =run-pod/v1 \
    --image=$dockerpath \
    --port=80 --labels app=mlk8s

# Step 3:
# List kubernetes pods
microk8s kubectl get pods

# Step 4:
# Forward the container port to a host
echo "Waiting 5 seconds to start the pod..."
sleep 5
microk8s kubectl get pods

microk8s kubectl port-forward mlk8s 8000:80


