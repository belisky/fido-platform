#!/bin/bash

kubectl create namespace argocd
# Wait for the argocd namespace to be created
while ! kubectl get namespace argocd &> /dev/null; do
  echo "Waiting for 'argocd' namespace to be created..."
  sleep 2
done

# Install ArgoCD
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

echo "Installing ArgoCD... Monitoring pod status."

# Periodically check the pod status
while true; do
  clear  # Clears the terminal for a fresh output
  echo "Checking ArgoCD installation status..."
  kubectl get pods -n argocd
  
  # Check if all pods are running
  NOT_READY_PODS=$(kubectl get pods -n argocd --no-headers | grep -v 'Running' | wc -l)
  
  if [ "$NOT_READY_PODS" -eq 0 ]; then
    echo "✅ All ArgoCD pods are running!"
    break
  else
    echo "⏳ Waiting for all pods to be in 'Running' state..."
  fi
  
  sleep 10
done
