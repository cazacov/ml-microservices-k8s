#!/usr/bin/env bash

# Prerequisites: microK8s with built-in image repository
# https://microk8s.io/docs/registry-built-in

# Step 1 
# Build and tag container
docker build . -t mlk8s
docker build . -t localhost:32000/mlk8s

# Step 2
# Push it to the local image repo
docker push localhost:32000/mlk8s