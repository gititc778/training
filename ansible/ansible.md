
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

###### You can simplify command-line usage by creating an ansible.cfg file in the project root:
```ini
[defaults]
inventory = inventory.ini
host_key_checking = False
retry_files_enabled = False
ansible all -m ping
```
####### This lets you run commands like:without needing the -i inventory.ini every time.

##### check disk space
```bash
ansible all -i inventory.ini -m shell -a "df -h"
```
##### Check uptime
```bash
ansible all -i inventory.ini -m shell -a "uptime"
```
##### check hostname
```bash
ansible all -i inventory.ini -m command -a "hostname"
```

###### Installing Nginx using playbook
```bash
---
- name: Install nginx web server
  hosts: webservers
  become: yes

  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
        update_cache: yes
```

##### install git
```bash
---
- name: Install git
  hosts: all
  become: yes

  tasks:
    - name: Install git package
      apt:
        name: git
        state: present
```
##### verify the playbook
```bash
ansible-playbook playbook.yml --check
```

###### Running a playbook
```bash
ansible-playbook -i inventory.ini playbook.yml
```
###### Using variables
```bash
- name: Install common packages
  hosts: all
  become: true  # Use sudo to install packages
  vars:
    packages_to_install:
      - git
      - curl
      - htop

  tasks:
    - name: Install packages
      package:
        name: "{{ packages_to_install }}"
        state: present
```

###### Install packages one-by-one
```bash
- name: Install common packages
  hosts: all
  become: true  # Use sudo to install packages
  vars:
    packages_to_install:
      - git
      - curl
      - htop

  tasks:

    - name: Install packages one by one
      package:
        name: "{{ item }}"
        state: present
      loop: "{{ packages_to_install }}"
```

