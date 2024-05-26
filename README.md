## Keycloak Stack
This project provides all the required resources to build a local stack with OICD authentication for all stack backend resources.  
Note: You must build the flask auth image prior to running the compose file.  
WARNING: This is for local testing only and runs over HTTP and not HTTPS. Further changes would be required for a production environment.  

Note: Ensure All Hosts provided in compose.yml are added to the client machine host list located C:\Windows\System32\drivers\etc on Windows  
  
For this example the following host should be added to the host file (NOTE! 10.10.90.90 should be updated to your machine IP):  
10.10.90.90 example.com
10.10.90.90 keycloak.example.com
10.10.90.90 whoami.example.com
10.10.90.90 auth.example.com
10.10.90.90 traefik.example.com


cd into a new project folder and clont the repo

```
$git clone https://github.com/tomreising/KCSecuredDockerStack.git

```

cd into the new cloned repot and run

```
docker compose up -d

```

Once the stack is up go to Keycloak and create a realm, client and user.  
Note: Keycloak will require the password to be changed on initial login go into the user profile and disable this for this example.  
After completing update the env settings for the flaskauth service and rerun the compose up command.  

```
docker compose up -d

```

Once you are done playing around you can close and remove the services with the following command

```
docker compose rm -v -s

```
