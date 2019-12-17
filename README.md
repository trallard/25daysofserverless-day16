## #25DaysofServerless - Day 16th "Let the posadas begin"
![License](https://img.shields.io/badge/License-BSD%203--Clause-gray.svg?colorA=2D2A56&colorB=7A76C2&style=flat.svg)

![Bit Xmas](https://thepracticaldev.s3.amazonaws.com/i/6z5dct67wfpfbxnmivht.jpg)

- [#25DaysofServerless - Day 16th &quot;Let the posadas begin&quot;](#25daysofserverless---day-16th-quotlet-the-posadas-beginquot)
- [What is in this repo?](#what-is-in-this-repo)
- [Resources/Tools Used 🚀](#resourcestools-used-%f0%9f%9a%80)
  - [Getting started with Azure Functions for Python](#getting-started-with-azure-functions-for-python)
  - [Continuous integration and delivery](#continuous-integration-and-delivery)
  - [Developer Tools](#developer-tools)
- [Next Steps 🏃](#next-steps-%f0%9f%8f%83)
- [License 📖](#license-%f0%9f%93%96)

This challenge and the solutions are part of the [#25DaysOfServerless](https://25daysofserverless.com).

:sparkles: You can find the challenge here 👉🏼 <https://25daysofserverless.com/calendar/16>.

📝 The article with the detailed explanation of the solutions can be found at <https://dev.to/azure/let-the-posadas-begin-day-16-of-the-25daysofserverles-challenge-57hm>

## What is in this repo?

- An Http triggered Azure function written in Python. Where the user can either pass a day as a query string or submit a simple GET request to the main endpoint to see all the posadas locations.

💻 See it in [./posadas](./posadas/)

Sample outputs:

- All dates query

![day query](assets/api.png)

- Single date query

![day query](assets/api2.png)


- Workflows for GitHub actions to deploy the Azure function to Azure 

💻 See it in [.github/workflows](.github/workflows)

## Resources/Tools Used 🚀

### Getting started with Azure Functions for Python
* **[Azure Functions Python](https://docs.microsoft.com/azure/azure-functions/functions-reference-python?WT.mc_id=25daysofserverless-github-cxa)**

### Continuous integration and delivery 
* **[GitHub Actions](https://help.github.com/en/actions/automating-your-workflow-with-github-actions)**
* **[Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/?view=azure-devops/?WT.mc_id=25daysofserverless-github-cxa)**
* **[Getting started with Azure Pipelines](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python?view=azure-devops?WT.mc_id=25daysofserverless-github-cxa)**
* **[Azure Functions Continuous delivery using Azure DevOps](https://docs.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops/?WT.mc_id=25daysofserverless-github-cxa)**
* **[Azure FunctionsContinuous delivery using GitHub actions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-how-to-github-actions/?WT.mc_id=25daysofserverless-github-cxa)**


### Developer Tools
* **[Visual Studio Code](https://code.visualstudio.com/?WT.mc_id=25daysofserverless-github-cxa)** 
* **[Visual Studio Code Azure Functions Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions&WT.mc_id=25daysofserverless-github-cxa)** 
* **[Visual Studio Code Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=25daysofserverless-github-cxa)**

## Next Steps 🏃

Learn more about serverless with Free Training! 

- ✅ **[Serverless Free Courses](https://docs.microsoft.com/learn/browse/?term=azure%20functions&WT.mc_id=25daysofserverless-github-cxa)** 

## License 📖

All the code containing in this repository is licensed under the [BSD-3 clause OSI license](https://opensource.org/licenses/BSD-3-Clause).