k3d registry create my-registry --port 5000
k3d cluster create -c "/home/nobel/Downloads/platfrom-engineer-test-new (1)/platform-engineer-test/infra-k8s/k3d-config.yaml"
# docker push
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
sleep 180
kubectl port-forward svc/argocd-server -n argocd 8085:443
argocd admin initial-password -n argocd
kubectl config set-context --current --namespace=argocd
argocd cluster add k3d-fido-exam
kubectl config set-context --current --namespace=default
kubectl apply -f "/home/nobel/Downloads/platfrom-engineer-test-new (1)/platform-engineer-test/manifests/"
kubectl apply -f "/home/nobel/Downloads/platfrom-engineer-test-new (1)/platform-engineer-test/manifests/nginx-helm.yaml"
kubectl port-forward svc/nginx 8087:80
cd "/home/nobel/Downloads/platfrom-engineer-test-new (1)/platform-engineer-test/my-service"
kubectl create configmap ms-env --from-env-file=.env #--dry-run=client -o yaml > configmap.yaml
k3d image import my-service:latest --cluster fido-exam
kubectl apply -f "/home/nobel/Downloads/platfrom-engineer-test-new (1)/platform-engineer-test/manifests/ms-app.yaml"
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcmdvY2QiLCJzdWIiOiJpbWFnZS11cGRhdGVyOmFwaUtleSIsIm5iZiI6MTczOTQ1ODEwMCwiaWF0IjoxNzM5NDU4MTAwLCJqdGkiOiJpbWFnZS11cGRhdGVyIn0.Osu4lbXvQAUlqxVPIpmQ-XoFrj7tGsmh2DHToLxgFfM
docker pull nginx:latest
docker tag nginx:latest k3d-my-service.local:44003/nginx:latest
docker push k3d-registry.localhost:12345/nginx:latest
curl argocd-server.argocd.svc.cluster.local/api/v1/applications
curl -k https://argocd-server.argocd.svc.cluster.local/api/v1/list_projects
helm repo add bitnami https://charts.bitnami.com/bitnami
helm search hub nginx
helm pull bitnami/nginx --untar=true