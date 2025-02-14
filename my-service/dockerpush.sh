#!/bin/bash

# Finds my-registry port number
PORT=$(docker ps --filter "name=my-registry" --format "{{.Ports}}" | awk -F'[:>-]' '{print $2}' | sed 's/-$//')

echo "The port number of my-registry is: $PORT"

# Set variables
IMAGE_NAME=${1:-"my-service"}      
TAG_VERSION=${2:-"latest"}    
REGISTRY_HOST=${3:-"my-registry.local"}  
REGISTRY_PORT=$PORT   

# Build the Docker image
echo "Building Docker image: $IMAGE_NAME:$TAG_VERSION"
docker build . -t $IMAGE_NAME:$TAG_VERSION

# Tag the image for the local registry
IMAGE_TAG="$REGISTRY_HOST:$REGISTRY_PORT/$IMAGE_NAME:$TAG_VERSION"
echo "Tagging image as: $IMAGE_TAG"
docker tag $IMAGE_NAME:$TAG_VERSION $IMAGE_TAG

# Push the image to the local registry
echo "Pushing image to registry: $IMAGE_TAG"
docker push $IMAGE_TAG

if docker push $IMAGE_TAG; then
    echo "Docker image pushed successfully!"
else
    echo "Docker push failed!" >&2
fi

# Imports docker image into cluster
k3d image import my-service:latest --cluster fido-exam
if k3d image import my-service:latest --cluster fido-exam; then
    echo "image imported Successfully!!!"
else
    echo "import failed"
fi

# creates configmap for container
kubectl create configmap ms-env --from-env-file=.env
# docker run -p 8092:8000 --name ms --env-file .env $IMAGE_NAME:$TAG_VERSION 
# docker exec ms env
# echo "Docker container can be accessed at localhost:8092 successfully!"