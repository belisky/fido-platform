k3d cluster create -c "/home/nobel/Downloads/platfrom-engineer-test-new (1)/platform-engineer-test/infra-k8s/k3d-config.yaml" --registry-config "/home/nobel/Downloads/platfrom-engineer-test-new (1)/platform-engineer-test/infra-k8s/k3d-registries.yaml"
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
sleep 180
kubectl port-forward svc/argocd-server -n argocd 8085:443
argocd admin initial-password -n argocd
argocd cluster add k3d-fido-exam
kubectl apply -f "/home/nobel/Downloads/platfrom-engineer-test-new (1)/platform-engineer-test/manifests/nginx-app.yaml"
kubectl port-forward svc/nginx 8087:80