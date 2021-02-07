# Building a CI/CD Pipeline

badges
------

<github actions link here>
 
[![CircleCI](https://circleci.com/gh/jfcb853/Udacity-DevOps-Azure-Project-2.svg?style=svg)](https://app.circleci.com/pipelines/github/jfcb853/Udacity-DevOps-Azure-Project-2)

[![AzurePipelines](https://dev.azure.com/javiercaparo574/test-udacity/_apis/build/status/jfcb853.Udacity-DevOps-Azure-Project-2?branchName=main)]



In this project, you will build a Github repository from scratch and create a scaffolding that will assist you in performing both Continuous Integration and Continuous Delivery. You'll use Github Actions along with a Makefile, requirements.txt and application code to perform an initial lint, test, and install cycle. Next, you'll integrate this project with Azure Pipelines to enable Continuous Delivery to Azure App Service.

## Project Plan

* Link to a Trello board for the project - (https://trello.com/b/BBqfWn2b/dashboard-ml-product)
* Link to a spreadsheet - <link here>


## Pre requisites

* An Azure Account ( https://portal.azure.com/)
* A GitHub Account ( http://github.com/)
* A CircleCi Account (https://circleci.com/ )
* An Azure DevOps Account (https://dev.azure.com/)


## First: CI Pipeline with GitHub Actions

### Architectural Diagram

* Architectural Diagram - ![alt text](<link here>)

### Instructions

* Enter to Azure Portal with your Accoutn and open a Azure Cloud shell ( use Bash)
 - If you are not created one , just follow the first creation and wait a seconds to get your Cloud Shell 
 
* First of all set up SSH Keys in your azure cloud shell, add the rsa.pub key to your GitHub repor ( ssh keys)  and then clone the project there.

```sh
ssh-keygen -t rsa
 
```

![alt text](<Link here>)

* Change to branch "hello-github-actions" 
```sh
 git checkout hello-github-actions
```

* Project Scaffolding ( files):

| Plugin | README |
| ------ | ------ |
| Makefile | to create shortcuts to build, test, and deploy a project|
| requirements.txt| to list what packages a project needs |
| hello.py | a basic python app |
| test_hello.py | the test python file to above app|


* Create a virtual environment for your application.
```sh
python3 -m venv ~/.myrepo
source ~/.myrepo/bin/activate
```

* Run `make all` which will install, lint, and test code
```sh
make all
```

![alt text](<link here>)


* Next set up Github Actions in your repo by adding the `main.yml file present in the .github/workflows folder.

```sh
ls -lasth .github/workflows/main.yml
```
![alt text](<link here>)

Note: We’ve created a simple Gighub Action in the repo which automates the lint  and test of our app.
Note: You can add the GitHub Actions badge to you README.md ( it's a good practice to do that)

* (OPTIONAL but HIGHLY Recommended) - Also you can add a CI pipeline with CircleCI.

- Open your account in CircleCI , add your repo and copy the `config.yml` of directory `.circleci`
```sh
ls -lasth .circleci/config.yml
```
Note:  this article that Noah wrote on the topic ( https://circleci.com/blog/increase-reliability-in-data-science-and-machine-learning-projects-with-circleci/) 


## Second : CI?CD Pipeline with AZURE DEVOPS

* Return to the `main` branch
```sh
git checkout main
git branch
```

* Go to Azure Deveops page  and sign in it, create a new Project inside your organization ( if you dont have an organization create one first).

* In your new Project in Azure DevOps, go to Project Settings and create a new `Pipeline --> Service Connection` as is explained on the Youtube video below ( Service Connection must be of Type Azure Resource Manager)

Note 1 : Name your Service Connection `AZServiceConnection`
Note 2: Use a link of as this `https://dev.azure.com/<organization>/<project_name>/_apis/serviceendpoint/endpoints?api-version=5.0-preview.2`  to find your ServiceConnectionID ( take note of this number since you will needed in the yaml file to build the pipeline). Replace the alues for the ones that you created for your organziation and project name.
Note3: the ServiceConnection ID is the number before the name `AZServiceConnection` of the above link.

* In  your new Project in Azure DevOps, go to Pipelines -->New Pipeline --> GitHub --> Select Your Repo --. select an Existing YAML file'
- Choose the `main` branch and the file named `azure-pipelines.yml` as is showed on the fiure below

![alt text](<link here>)

* After successfully configuring Azure pipelines and github actions check that if you make any commit then the pipeline is triggered and it runs successfully.

![alt text](<link here>)

NOTE: As first attempt the Pipeline must fails !!!!

NOTE: Why , cause 2 importnat things. You are not created your webapp yet in azure , and you must modify the ServiceConnection and the name of your webapp on the `azure-pipelines.yml` file for the ones that you got.


* Deploy the flask-sklearn app to Azure app Service ( using Plan B1)  with this command ( Create a webapp and deploy code from a local workspace to the app):
```sh
az webapp up -n <name of webapp> --location southcentralus --sku B1
```

Note: If you don't choose the sku , the default will be `P1V2(Premium V2 Small)` ( with more costs associated)
Note: the name of your app must be unique!!!
Note: This operation can take a while to complete ...


![alt text](<insert here>)

*  Update the `azure-pipelines.yml` with the name of your webapp and your service connection point ( Check youtube video for a detailed explanation)
- Modifications at variables webAppName & environmentName

* Your service URL  will be something like this : https://<name of webapp>.azurewebsites.net/

* Update the file `make_predict_azure_app.sh` with your end point
```sh
grep https make_predict_azure_app.sh
```

* perform a cosmetic change to your app.py , so you can see your CI/CD piepline in action on Azure DevOps/

- On file `app.py` change this line
```sh
html = "<h3">Sklearn Prediction Home</h3>"
```

for this one:
```sh
html = "<h2>Sklearn Prediction Home App RestAPI</h2>"
```
and then perofrm a quick lint and push the changes to your repo:
```sh
amek lint
git add .
git commit -m "app.py updated"
git push origin main
```
* When the app is successfully deployed then update the app service endpoint in the code and then run script `./make_predict_azure_app` file to make a prediction.

* You will be able to see the successfull prediction made. 
```sh
./make_predict_azure_app.sh
```
Answer:
```sh
Port: 443
{"prediction":[20.35373177134412]}
```

![alt text](<link here>)


- You can check on webapp log tail `az webapp log tail` , this answer:
```sh
2021-02-07T05:01:07.528670565Z /antenv/lib/python3.7/site-packages/sklearn/ensemble/gradient_boosting.py:34: DeprecationWarning: `np.bool` is a deprecated alias for the builtin `bool`. To silence this warning, use `bool` by itself. Doing this will not modify any behavior and is safe. If you specifically wanted the numpy scalar type, use `np.bool_` here.
2021-02-07T05:01:07.528708467Z Deprecated in NumPy 1.20; for more details and guidance: https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations
2021-02-07T05:01:07.528714768Z   from ._gradient_boosting import predict_stages
2021-02-07T05:01:07.528719468Z /antenv/lib/python3.7/site-packages/sklearn/ensemble/gradient_boosting.py:34: DeprecationWarning: `np.bool` is a deprecated alias for the builtin `bool`. To silence this warning, use `bool` by itself. Doing this will not modify any behavior and is safe. If you specifically wanted the numpy scalar type, use `np.bool_` here.
2021-02-07T05:01:07.528725368Z Deprecated in NumPy 1.20; for more details and guidance: https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations
2021-02-07T05:01:07.528729969Z   from ._gradient_boosting import predict_stages
2021-02-07T05:01:07.528734269Z [2021-02-07 05:01:07,528] INFO in app: JSON payload: %s json_payload
2021-02-07T05:01:07.595625682Z [2021-02-07 05:01:07,595] INFO in app: inference payload DataFrame: %s inference_payload
2021-02-07T05:01:07.596822066Z [2021-02-07 05:01:07,595] INFO in app: Scaling Payload: %s payload
2021-02-07T05:01:07.771026138Z 172.16.0.1 - - [07/Feb/2021:05:01:07 +0000] "POST /predict HTTP/1.1" 200 35 "-" "curl/7.64.0"
```

* Run locust command in your project to perform a load test on the API. You can see an output like this.

- Azure cloud Shell is not enough good to perform locust there, so use a VM or your own machine to perform locust

- copy both files and run the `loadtesting.sh` file and open the broser on `http://localhost:8089/`
```sh
./loadtesting.sh
```

- form there you can see how the load testing is performing and how you app established on a # of RPS 
- This is good to know how good is your webapp and your plan to manage the requets. So you can decide to scale up the plan service of your webapp for example.
- Locust coudl generate a stats report.


![alt text](<link here>)

Remaining screenshots can be checked in the screenshot folder.

## CLEAN OUT

* delete the resource group of your webapp created 
- At portal enter to yoour webapp service , locate teh reosurce group
- Go to that resource group and delete it


## Future Enhancements

* Adding more test cases.
* Creating a UI for making predictions.
* Using Github Actions instead of Azure pipelines.
* Run the app on Kubernetes cluster

## Demo 

Link for Demo Video -> <link here>


# License
---------

MIT


**Free Software, Hell Yeah!**
