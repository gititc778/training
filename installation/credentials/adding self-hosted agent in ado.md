### Installing self-hosted agent in azure devops
download the agent with wget <url>
./config.sh
<provide all the details>
after its completed run
sudo ./svc.sh install
sudo ./svc.sh start
sudo ./svc.sh status

###### to remove
sudo ./svc.sh stop
sudo ./svc.sh uninstall
Organization Settings → Agent Pools >  Delete