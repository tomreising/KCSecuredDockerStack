## Keycloak Stack
This project provides all the required resources to build a local stack with OICD authentication for all stack backend resources.  
Note: You must build the flask auth image prior to running the compose file.  
WARNING: This is for local testing only and runs over HTTP and not HTTPS. Further changes would be required for a production environment.  

Note: Ensure All Hosts provided in KC-compose.yml are added to the client machine host list located C:\Windows\System32\drivers\etc on Windows

cd into prebuild_images and run
```
docker build -t flaskauth .

```

After the build is complete cd back into the parent directory and run

```
docker compose -f KC-compose.yml up -d

```

Once the stack is up go to Keycloak and create a realm, client and user.  
Then remove the flaskauthyml service by running  

```
docker compose -f KC-compose.yml down flaskauthyml

```

Once the service is stopped and removed update the client realm and secrete then run

```
docker compose -f KC-compose.yml up -d flaskauthyml

```

Note: Any service in the compose file can be removed and added back in in the same way.
