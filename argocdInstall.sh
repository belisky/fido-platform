k3d cluster create -c "/home/nobel/Downloads/platfrom-engineer-test-new (1)/platform-engineer-test/infra-k8s/k3d-config.yaml" --registry-config "/home/nobel/Downloads/platfrom-engineer-test-new (1)/platform-engineer-test/infra-k8s/k3d-registries.yaml"
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
sleep 180
kubectl port-forward svc/argocd-server -n argocd 8085:443
argocd admin initial-password -n argocd
argocd cluster add k3d-fido-exam
kubectl apply -f "/home/nobel/Downloads/platfrom-engineer-test-new (1)/platform-engineer-test/manifests/nginx-app.yaml"
kubectl port-forward svc/nginx 8087:80
kubectl create configmap ms-env --from-env-file=.env --dry-run=client -o yaml > configmap.yaml
kubectl config set-context --current --namespace=argocd
argocd cluster add k3d-fido-exam
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcmdvY2QiLCJzdWIiOiJpbWFnZS11cGRhdGVyOmFwaUtleSIsIm5iZiI6MTczOTQ1ODEwMCwiaWF0IjoxNzM5NDU4MTAwLCJqdGkiOiJpbWFnZS11cGRhdGVyIn0.Osu4lbXvQAUlqxVPIpmQ-XoFrj7tGsmh2DHToLxgFfM

docker pull nginx:latest
docker tag nginx:latest k3d-my-service.local:44003/nginx:latest
docker push k3d-registry.localhost:12345/nginx:latest
