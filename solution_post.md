---
title: Let the posadas begin - Day 16 of the #25DaysOfServerles challenge
published: false
cover_image: https://thepracticaldev.s3.amazonaws.com/i/6z5dct67wfpfbxnmivht.jpg
description: TODO:CHALLENGE DESCRIPTION HERE
tags: 25daysofserverless, serverless, azure, Python, continuous integration, continuous delivery, GitHub actions
---

This article is part of [#25DaysOfServerless](https://25daysofserverless.com). New challenges will be published every day from Microsoft Cloud Advocates throughout the month of December. Find out more about how Microsoft Azure enables your [Serverless functions](https://docs.microsoft.com/azure/azure-functions/?WT.mc_id=25days_devto-blog-cxa).

Have an idea or a solution? <a class="twitter-share-button" href="https://twitter.com/intent/tweet?text=I'm joining the @azureadvocates %2325DaysOfServerless challenge!! Learn more at https://aka.ms/25daysofserverless or see solutions at https://dev.to/search?q=25DaysOfServerless! Join me!" data-url="https://aka.ms/25daysofserverless' " data-hashtags="25DaysOfServerless"> Share your thoughts on Twitter! 
</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<hr/>

It's the 16th of December, which can only mean one thing: Posadas are finally starting in Mexico! Everyone is already preparing for the following nine days of posadas and deciding on venues all across Mexico City for this festive tradition. 

A couple of months back, Xanath offered to put together a list of hosts and locations so that all her friends and family had the details for each posada. With all the servers missing and so little time to collect the sites and inform everyone Xanath has asked some friends for help.
They will all be working together to make a solution to help folks to find the location of the next posada.

## The challenge

Your challenge is to create a simple solution for Xanath's friends and family to find the locations of the upcoming posadas as well as the name of the person hosting.
Since there will be several people working on the project and adding locations at the same time, you need to make sure that the solution is accordingly updated and deploy to reflect these changes. 

## Tips:

1. To allow for the solution and data to be updated as fast as possible, the deployment should be made automatically after a Pull Request has been merged. You can achieve this using services like GitHub Actions or Azure Pipelines.
2. You can specify the locations in any way you prefer (i.e. addresses, latitude and longitude pairs). Still, you need to make sure that every place added adheres to the same format.
3. There are many ways in which you can implement this solution; we recommend you start with a simple one, implement your CI/CD pipeline and refine later.

## A solution
In this particular challenge, the main focus is setting up a CI/CD pipeline for an Azure Function, so I decided to use Python for this challenge.
Since the main focus is not the function itself, I am going to summarise the process quite a bit. Still, you can follow [this tutorial](https://docs.microsoft.com/en-us/azure/python/tutorial-vs-code-serverless-python-01/?WT.mc_id=25days_devto-blog-cxa) in case you want a step-by-step guide on how to create an Http Triggered Azure Function in Python.

I used VS Code and the Azure functions extension to create a Python Http triggered function with the predefined templates as the starting point.

The next step is to decide on the format for the locations for the challenge. In my case, I created a `locations.json` file which looks something like this:
```json
{
 "locations": [
    {
       "name": "Bellas Artes",
       "date": "December 16, 2019",
       "host": "Tania Allard",
       "type": "geopoint",
       "location": {
       "lon": 19.4352,
       "lat": 99.1412
       }
    },
    {
       "name": "Museo de Antropologia",
       "date": "December 17, 2019",
       "host": "Tania Allard",
       "type": "geopoint",
       "location": {
       "lon": 19.4260,
       "lat": 99.1863
       }
    }
 ]
}
```
And I modified the `__init__.py` script accordingly:
```python
import datetime
import json
import logging
from pathlib import Path

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
 logging.info("Someone is looking for a posada! ✨")

 day = req.params.get("day")
 if not day:
 locations = json_locations()
 return func.HttpResponse(f"{json.dumps(locations)}", status_code=200)

 if day:
 locations = json_locations()
 posada = get_loc(day, locations)
 return func.HttpResponse(f"{json.dumps(posada)}", status_code=200)
 else:
 return func.HttpResponse("Please pass a day", status_code=400)


def json_locations():
 """Function to parse the json file with the locations,
 we use Pathlib to resolve the full path of the file
 """
 loc_path = Path("./posadas/data/locations.json").resolve()
 with open(loc_path, "r") as json_file:
 locations = json.load(json_file)
 return locations.get("locations")


def get_loc(day, locations):
 """This function searches for the location corresponding to the 
 query day. 
 We need to make sure the dates are actually converted into DateTime objects.
 """
 for posada in locations:

 date = datetime.datetime.strptime(posada.get("date"), "%B %d, %Y").date()
 if date.day == int(day):
 return posada

```
The code above allows the user to:
1. Provide a day as a query string to the function API in which case it only returns the details for the corresponding day (e.g. `https://posadastrallard.azurewebsites.net/api/posadas/?day=16`).
2. Submit a GET request to the primary endpoint so that it returns all of the dates and locations in the locations file. 

After testing locally running `func host start` and making sure everything was working, I deployed my function app to Azure. I like using the Azure CLI for this kind of things (again a step-by-step can be found [here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-python/?WT.mc_id=25days_devto-blog-cxa)).
If you have the Azure Functions extension for VS Code Installed, you can publish your app directly from there too, and it will save you some time.

After deploying, I made sure that my function by performing a GET request:

![api call](https://github.com/trallard/25daysofserverless-challenges/blob/master/assets/api.png?raw=true)

Once the function is deployed, we can go ahead and create the CI/CD pipeline. For this challenge, I decided to use [GitHub actions](https://help.github.com/en/actions/automating-your-workflow-with-github-actions). To do so, we need to follow the next steps:
1. Create a [service principal](https://docs.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals#service-principal-object/?WT.mc_id=25days_devto-blog-cxa). This will allow us to deploy our function using GitHub actions. 
 If you are using your command line with the Azure CLI or the Azure Cloud shell, you can use the following command:
 ```
 az ad sp create-for-rbac --name "myApp" \
 --role contributor \
 --scopes /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.Web/sites/<APP_NAME> --sdk-auth
 ```
 Note that we are giving it only `contributor` access to restrict the scope of this access.
2. Now make sure to copy the output of the above command as you will need it. Head over to your GitHub repository where you have your function code go to **Settings > Secrets** 
![api call](https://raw.githubusercontent.com/trallard/25daysofserverless-challenges/master/assets/secrets.png)
Paste the output from when you created your service principal (note that you will need to add your subscription id too).
3. Now back in your local repository, we are going to create a `.github/workflows` directory. That is the location where all of our CI/CD pipeline definitions will be located for GitHub to be able to find them. Now let's create a `python_function.yaml` file (you can change the name).

I am going to explain the content, so you know what this is doing. 

We want the pipeline to trigger at a push on the master branch. Also, we first need to check out our repository, so we use `actions/checkout@master`.

```
name: Python function

on:
 push:
 branches:
 - master

jobs:
 build-and-deploy:
 runs-on: ubuntu-latest
 steps:
 - name: "Checkout GitHub Action"
 uses: actions/checkout@master
```
Next, we login to Azure and set our Python environment. Here is where you also install dependencies.

```
 - name: "Login via Azure CLI"
 uses: azure/login@v1
 with:
 creds: ${{ secrets.AZURE_CREDENTIALS }}

 - name: Setup Python 3.7
 uses: actions/setup-python@v1
 with:
 python-version: 3.7

 - name: "Run pip"
 shell: bash
 run: |
 pushd .
 python -m pip install --upgrade pip
 pip install -r requirements.txt --target=".python_packages/lib/python3.7/site-packages"
 popd
```

Finally we publish our function:
```
 - name: "Run Azure Functions Action"
 uses: Azure/functions-action@v1
 id: fa
 with:
 app-name: posadastrallard
 package: "."

```
Now if we do `git add .github/workflows/python_function.yaml` and push we should see the workflow running straightaway under **Actions**:

![pipelines actions](https://raw.githubusercontent.com/trallard/25daysofserverless-challenges/master/assets/actions2.png)

Finally, you can make an update to the locations file, wait for the deployment to complete and see your app updated!

![api updated](https://raw.githubusercontent.com/trallard/25daysofserverless-challenges/master/assets/api2.png)

You can see the final Python Http Triggered function as well as the GitHub actions workflows in the [GitHub repository](https://github.com/trallard/25daysofserverless-challenges).

Success!

<hr/>
Want to submit your solution to this challenge? Build a solution locally and then [submit an issue](https://github.com/microsoft/25-days-of-serverless/issues/new?assignees=&labels=challenge-submission&template=challenge-solution-submission.md&title=%5BCHALLENGE+SUBMISSION%5D+). If your solution doesn't involve code you can record a short video and submit it as a link in the issue desccription. Make sure to tell us which challenge the solution is for. We're excited to see what you build! Do you have comments or questions? Add them to the comments area below.

<hr/>
Watch for surprises all during December as we celebrate 25 Days of Serverless. Stay tuned here on dev.to as we feature challenges and solutions! Sign up for a [free account on Azure](https://azure.microsoft.com/free/?WT.mc_id=25days_devto-blog-cxa) to get ready for the challenges!

