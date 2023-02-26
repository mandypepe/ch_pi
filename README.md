# Reto
Build a microservice that must have a REST endpoint named: /DevOps (use any preferred programming language or framework).
You must comply with the following requirements:
```
    ● The microservice must be containerized and can be deployed on any machine or in the cloud.
    ● It is required to use a load balancer with a minimum of two nodes with the same microservice.
    ● The infrastructure code must be versionated.
    ● The pipeline should be configured as a code and needs to be stored in a repository.
```
Minimum requirements for the pipeline:
```
    ● Use of Dependency Management
    ● It should have two stages at minimum: “build” and “test”, and can have the stages that you want.
    ● Must be automatic and can be executed by any branch, the master branch always deploys to the
    production environment. If it is required you can create more environments: development or testing. Additionally you could execute the pipeline on demand and you can deploy any version of the microservice (In the case that more than one version exists)
    ● The pipeline should be configured as a code and needs to be stored in a repository. 
```
The project must include:
```
    ● Automatic testing of any type.
    ● Static code revision.
    ● Dynamic grow.
    ● API Manager for API key and JWT
```
# Descripción
Este proyecto se despliega sobre AWS usando CDK

### Instalación
Instalar librerías y dependencias necesarias

```
pip install -r requirements.txt
```
#### Configurar los parámetros de la conexión


##### Env vars:
```
  REPO_NAME: ${{ github.event.repository.name }}
  AWS_DEFAULT_REGION: us-east-1
```

##### Secrets DOCKER HUB:
```
${{ secrets.DOCKERHUB_USERNAME }}
${{ secrets.DOCKER_PASSWORD }}
```
##### App params 
```
${{ secrets.SECRET_KEY }}
${{ secrets.SECRET_EMAIL }}
${{ secrets.SECRET_PASSW }}
```

##### Secrets AWS params 
```
 ${{ secrets.AWS_ACCESS_KEY_ID }}
 ${{ secrets.AWS_SECRET_ACCESS_KEY }}
 ${{ env.AWS_DEFAULT_REGION }}
```
### EndPoints

- GET: 
  - '/'
- POST:
  - '/api/auth'
  - /Devops
  
### Tecnologías
- Python 3.9
- Flask
- CDK

### URL

- Se genera dinamica : 
  - Output CDK:  "Load_balancer_dns_name"



