

## Check Docker version
```bash
docker --version
```

## Add your user to Docker group to run Docker commands without Sudo
```bash
sudo usermod -aG docker $USER
```

## Pull an image from Docker hub
```bash
docker pull <image>
```

## List all images on your system
```bash
docker images
```

## Run a container
```bash
docker run <image>
```

## Run a container with options
```bash
docker run -d -p 80:80 --name nginx-server nginx
```

## List running containers
```bash
docker ps
```

## Stop a container
```bash
docker stop <container ID>
```

## Data persistence
### You can mount volumes in two main ways in Docker
#### 1 - Bind Mounts (Host Directory → Container)
##### Mounts a specific path from the host into the container.
```bash
docker run -v /host/path:/container/path nginx
```
#### 2. Named Volumes (Docker-managed)
##### Docker creates and manages this volume.
##### Data is stored under /var/lib/docker/volumes/ on the host.
```bash
docker run -v myvolume:/container/path nginx
```

## Build a Docker Image from Dockerfile
##### . Refers to the current directory (Dockerfile context).
##### By default Docker will look for a file name exactly as Dockerfile
```bash
docker build .
```





