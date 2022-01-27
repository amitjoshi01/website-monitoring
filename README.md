# website-monitoring
1. clone this code to your weork directory. update the  file website_list.txt in your working directory.
2. Run a website locally e.g. keycloak using following command
docker run -p 8080:8080 -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD=admin quay.io/keycloak/keycloak:12.0.2
(if 8080 is occupied then you can replace it with any port that is available on your machine.)
3. Use dockerfile to build and push your image to docker hub
4. Run the docker command with --network="host" and mount your working directory to /opt to run the monitoring tool
5. you can see the logs in logfile.txt that is created and updated in your work directory
