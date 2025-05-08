#### emptyDir

```bash
apiVersion: v1
kind: Pod
metadata:
  name: my-emptydir-pod
spec:
  containers:
    - name: my-container
      image: nginx
      volumeMounts:
        - mountPath: /tmp
          name: emptydir-storage
  volumes:
    - name: emptydir-storage
      emptyDir: {}
```

#### hostPath

```bash
apiVersion: v1
kind: Pod
metadata:
  name: my-hostpath-pod
spec:
  containers:
    - name: my-container
      image: nginx
      volumeMounts:
        - mountPath: /host
          name: hostpath-storage
  volumes:
    - name: hostpath-storage
      hostPath:
        path: /path/on/host
        type: Directory
```

#### configMap

```bash
apiVersion: v1
kind: Pod
metadata:
  name: my-configmap-pod
spec:
  containers:
    - name: my-container
      image: nginx
      volumeMounts:
        - mountPath: /etc/config
          name: configmap-storage
  volumes:
    - name: configmap-storage
      configMap:
        name: my-configmap
```

#### secret

```bash
apiVersion: v1
kind: Pod
metadata:
  name: my-secret-pod
spec:
  containers:
    - name: my-container
      image: nginx
      volumeMounts:
        - mountPath: /etc/secret
          name: secret-storage
  volumes:
    - name: secret-storage
      secret:
        secretName: my-secret
```

#### azureDisk / azureFile

```bash
apiVersion: v1
kind: Pod
metadata:
  name: my-azuredisk-pod
spec:
  containers:
    - name: my-container
      image: nginx
      volumeMounts:
        - mountPath: /mnt/disks/azure
          name: azure-disk
  volumes:
    - name: azure-disk
      azureDisk:
        diskName: my-disk
        diskURI: https://myazureaccount.blob.core.windows.net/mydisk
        cachingMode: ReadOnly
        fsType: ext4
```

#### awsElasticBlockStore (EBS)

```bash
apiVersion: v1
kind: Pod
metadata:
  name: my-ebs-pod
spec:
  containers:
    - name: my-container
      image: nginx
      volumeMounts:
        - mountPath: /mnt/disks/ebs
          name: ebs-storage
  volumes:
    - name: ebs-storage
      awsElasticBlockStore:
        volumeID: vol-12345
        fsType: ext4

```