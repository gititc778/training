
## Listing Volumes
``` bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible
```
```bash
mkdir ansible-project
cd ansible-project
```
## Create the following inside this directory
#### inventory.ini: your list of managed nodes
#### playbook.yml: your Ansible instructions
#### group_vars/ or host_vars/: variable definitions
#### roles/: reusable role directories

## Write an inventory file
##### Create a file name inventory.ini in the root of your project

```ini
[webservers]
10.1.1.1

[dbserver]
11.1.1.1
```
##### ansible stores the default inventory file at /etc/ansible/hosts
##### use -i flag to provide your own inventory file

```bash
ansible -i inventory.ini all -m ping
```

### Setup SSH
```bash
ssh-keygen -t ed25519
ssh-copy-id user@10.1.1.1
```

### Allow password less login on the remote server
```bash
sudo nano /etc/ssh/sshd_config
```
##### change PubkeyAuthentication to yes
##### change PasswordAuthentication yes

```bash
sudo systemctl restart sshd
```




