###### Creating Docker credentials in Jenkins
```ini
Log in to Jenkins
click on manage jenkins
then go to credentials and click on domain
add credentials

add a username and password 

un: dockeritc778
pw: PAT  (however password will also work)

###### adding K8s credentials in Jenkins
 type of credential

 secret text.

 upload kubeconfig file in jenkins

###### For GitHub → Jenkins Webhook

if you are not able to see  add web hook in git hub go to this url
    https://github.com/gititc778/sampleApp/settings/hooks/new

git hub webhook for jenkins
Get Jenkins URL
	format
		http://<jenkins-url>/github-webhook/
        http://18.170.23.150:8080

Configure Your Jenkins Job
Go to yosur job → Configure Under Build Triggers, check:  GitHub hook trigger for GITScm polling


Add Webhook in GitHub
Go to your GitHub repository → Settings → Webhooks  Click Add webhook 
	Payload URL: http://<jenkins-url>/github-webhook/
	Content type: application/json
	Secret: (optional, must match Jenkins secret if used)
	Events: Choose: Just the push event
	Click Add webhook
	
Test the Webhook
	Push a commit to your GitHub repo
	Jenkins should trigger the build automatically

to test the push you can add/remove pizza
    /sampleApp/Services/PizzaService.cs

```