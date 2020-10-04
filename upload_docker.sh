#!/usr/bin/env bash
# This file tags and uploads an image to Docker Hub

# Assumes that an image is built via `run_docker.sh`

# Step 1:
# Create dockerpath
dockerpath=cazacov/learning:mlk8s

# Step 2:  
# Authenticate & tag
echo "Docker ID and Image: $dockerpath"

# Authenticate
docker login -u cazacov

# Tag
docker tag mlk8s $dockerpath

# Step 3:
# Push image to a docker repository
docker push $dockerpath