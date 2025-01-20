# How to run the application on Kubernetes (Minikube)
### 1. Dockerize the Application
### 2. Install Minikube
### 3. Run the following codes:
- `minikube start`
- `minikube kubectl -- get po -A`
- `alias kubectl="minikube kubectl --"`
- `kubectl apply -f deployment.yaml`
    ```
    deployment.apps/flask-tdd-deployment created
    service/flask-tdd-service created
    ```
- Get running pods `>>> kubectl get po`
    ```
    NAME                                    READY   STATUS    RESTARTS   AGE
    flask-tdd-deployment-6d48786764-kkrnj   1/1     Running   0          5m33s
    flask-tdd-deployment-6d48786764-p54ms   1/1     Running   0          5m33s
    ```

- Check the service by this command `>>> kubectl get svc` or, `kubectl get service`
  ```
    NAME                TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
    flask-tdd-service   ClusterIP   10.99.175.108   <none>        8000/TCP   6m42s
    kubernetes          ClusterIP   10.96.0.1       <none>        443/TCP    14m
  ```
- To see the deployment `>>> kubectl get deployment`
    ```
    NAME                   READY   UP-TO-DATE   AVAILABLE   AGE
    flask-tdd-deployment   2/2     2            2           11m
    ```
### Accessing the containerized application

<p>You will expose the flask-tdd-service to access the application outside the Minikube Kubernetes Cluster. You will use an external IP address and access the application on the web browser. To expose the service, use the following minikube command:
</p>

- `minikube service flask-tdd-service`
    ```
    |-----------|-------------------|-------------|---------------------------|
    | NAMESPACE |       NAME        | TARGET PORT |            URL            |
    |-----------|-------------------|-------------|---------------------------|
    | default   | flask-tdd-service |        8000 | http://192.168.58.2:30007 |
    |-----------|-------------------|-------------|---------------------------|
    🏃  Starting tunnel for service flask-tdd-service.
    |-----------|-------------------|-------------|------------------------|
    | NAMESPACE |       NAME        | TARGET PORT |          URL           |
    |-----------|-------------------|-------------|------------------------|
    | default   | flask-tdd-service |             | http://127.0.0.1:37143 |
    |-----------|-------------------|-------------|------------------------|
    🎉  Opening service default/flask-tdd-service in default browser...
    👉  http://127.0.0.1:37143
    ❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
    ```

- you can get the Minikube IP and access it via the NodePort:
  `minikube ip  # Get the Minikube node IP`
  Then, you can access the service at http://minikube-ip:30007.
