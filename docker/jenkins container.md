
### Create a volume
```bash
docker volume create jenkins_home
```
### Running Jenkins container
```bash
docker run -d \
  --name jenkins \
  --network host \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts
```
### Getting password
```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```