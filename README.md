# **Platform Engineer Exam**

## **Introduction**

Welcome to the  **Platform Engineer Exam** . The purpose of this test is to assess your  **hands-on skills in Kubernetes, ArgoCD, GitOps, FastAPI development, and CI/CD workflows** .

### **Exam Overview**

This exam consists of the following key components:

1. **Environment Setup**
   * Set up a local Kubernetes cluster using K3D.
   * Install essential tools required for the exam.
   * Configure a local container registry for pushing images.
2. **ArgoCD Installation & GitOps Setup**
   * Install ArgoCD as a CD system for your local Kubernetes cluster.
   * Deploy an **Nginx application** using **GitOps principles** via ArgoCD.
3. **Code Assignment**
   * Complete a **FastAPI-based microservice** that interacts with ArgoCD.
   * Implement two API routes to fetch **ArgoCD application statuses** and  **ArgoCD project metadata** .
4. **Dockerization & Deployment**
   * Build and **push a Docker image** of your service to the  **local registry** .
   * Deploy the service to Kubernetes as an  **ArgoCD application** .

### **Submission Guidelines**

* Your **final solution must be uploaded to a GitHub repository** under your own account.
* The structure of your repository should match the paths provided in each task.
* All required components ( **Kubernetes manifests, application code, configuration files, Dockerfiles** ) should be included in your repository.
* Use best practices for  **Git commits, repository organization, and Kubernetes deployments** .

> 🚀 **Note:** Before starting the tasks, ensure you have installed all required tools listed in the pre-requisites section below.

---

## **Pre-requisites**

To complete this exam, you must have the following tools installed on your system:

* **GitHub account** (for hosting your solution)
* **[K3D](https://k3d.io/stable/)** (to set up a local Kubernetes cluster)
* **[Poetry](https://python-poetry.org/docs/)** (for Python dependency management)
* **[Kubectl](https://kubernetes.io/docs/reference/kubectl/)** (to interact with the Kubernetes cluster)

Ensure that each of these tools is installed and correctly configured before proceeding.

---

## **Environment Setup**

### **GitHub Setup**

1. Unzip the exam folder:
   ```bash
   unzip platform-engineer-test.zip
   ```
2. Create a dedicated **Git repository** under your GitHub account and push the contents of the extracted folder.

### **Local Kubernetes Cluster Setup**

1. Install your local Kubernetes cluster using  **K3D** :

   ```bash
   k3d cluster create -c k3d-config.yaml --registry-config k3d-registries.yaml
   ```
2. Wait for all cluster components to be ready:

   ```bash
   kubectl get pods --all-namespaces --watch
   ```

   Your environment is considered **ready** once you see output similar to:

   ```json
   kube-system   coredns-7b98449c4-z64bm                   1/1     Running     0          15m
   kube-system   helm-install-traefik-bt6wp                0/1     Completed   2          15m
   kube-system   helm-install-traefik-crd-82nw6            0/1     Completed   0          15m
   kube-system   local-path-provisioner-595dcfc56f-6lmpf   1/1     Running     0          15m
   kube-system   metrics-server-cdcc87586-hc9zp            1/1     Running     0          15m
   kube-system   svclb-traefik-97509331-htwzd              2/2     Running     0          15m
   kube-system   svclb-traefik-97509331-l6bps              2/2     Running     0          15m
   kube-system   svclb-traefik-97509331-m4ltx              2/2     Running     0          15m
   kube-system   svclb-traefik-97509331-p7vmm              2/2     Running     0          15m
   kube-system   traefik-d7c9c5778-xzz4c                   1/1     Running     0          15m
   ^C%  
   ```

### **Local Registry Setup**

1. Add the following entry to `/etc/hosts`:

   ```json
   127.0.0.1 my-registry.local
   ```
2. Verify that the local Docker registry is running:

   ```
   docker ps | grep registry
   ```

   Expected output:

   ```json
   69b0319f571f   registry:2   "/entrypoint.sh /etc…"   Up 15 minutes   0.0.0.0:59462->5000/tcp   my-registry
   ```

---

## **Exam Tasks**

1. **Install ArgoCD** in your local cluster in the `argocd` namespace.
2. **Deploy Nginx as an ArgoCD-managed application** in a GitOps manner.
   * Store the **Nginx manifests** in your Git repository.
   * Store the **ArgoCD application manifest** in Git.
3. **Develop a FastAPI service** that interacts with ArgoCD.
   * Implement two **API endpoints** to list **ArgoCD applications** and  **ArgoCD projects** .
4. **Build and push a Docker image** of the FastAPI service to the  **local registry** .
5. **Deploy the FastAPI service** as an  **ArgoCD application** .

---

## **Tasks Breakdown**

### **1️⃣ ArgoCD Installation**

**Task Definition:**
Install and configure ArgoCD as your Kubernetes CD system.

**Instructions:**

* Install **[ArgoCD](https://argo-cd.readthedocs.io/en/stable/)** in your local cluster under the `argocd` namespace.
* Use **Kustomize or Helm** to manage your Kubernetes manifests.
* Connect ArgoCD to your  **GitHub repository** .

**Notes:**

* Ensure your solution is stored under:
  ```bash
  platform-engineer-test/infra-k8s/k8s-apps
  ```

---

### **2️⃣ Deploy Nginx as an ArgoCD Application**

**Task Definition:**
Deploy Nginx using **GitOps principles** via ArgoCD.

**Instructions:**

* Create **Kubernetes manifests** for Nginx:
  * **Deployment**
  * **Service**
  * **Traefik Ingress**
* Create an **ArgoCD application** that deploys Nginx from Git.
* Expose it at  **`nginx.local`** .

---

### **3️⃣ Code Assignment (FastAPI Service)**

**Task Definition:**
Complete `my-service` by adding **two FastAPI routes** to interact with ArgoCD.

**Instructions:**

* Implement the following API routes:
  * GET `/api/v1/argocd/application_status  `
    Expected response:

    ```json
    curl http://127.0.0.1:8080/api/v1/argocd/application_status | jq .


    {
      "applications": [
        {
          "application_name": "my-service",
          "status": "Synced"
        },
        {
          "application_name": "nginx",
          "status": "Synced"
        }
      ]
    }
    ```
  * **GET `/api/v1/argocd/list_projects`**

    ```bash
    curl http://127.0.0.1:8080/api/v1/argocd/list_projects | jq .
    ```

    Expected output:

    ```json
    {
      "projects": [
        {
          "project_name": "default",
          "namespace": "argocd"
        }
      ]
    }
    ```

---

### **4️⃣ Build and Push Docker Image for `my-service`**

**Instructions:**

```bash
docker build . -t <YOUR_TAG_VERASION>
docker tag <YOUR_TAG_VERASION> my-registry.local:<LOCAL_REGISTRY_PORT>/<YOUR_TAG_VERASION>
docker push my-registry.local:<LOCAL_REGISTRY_PORT>/<YOUR_TAG_VERASION>
```

---

### **5️⃣ Deploy `my-service` as an ArgoCD Application**

**Instructions:**

* Create **Kubernetes manifests** for `my-service` (deployment, service, ingress)
* Create an  **ArgoCD application** .
* Expose it at  **`my-service.local`** .
* Run curl command

---

 **GOOD LUCK!** 🚀
