
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
```ini
[webservers]
10.1.1.1

[dbserver]
11.1.1.1
```





