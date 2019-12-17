## #25DaysofServerless - Day 16th "Let's the posadas begin"
![License](https://img.shields.io/badge/License-BSD%203--Clause-gray.svg?colorA=2D2A56&colorB=7A76C2&style=flat.svg)

![Bit Xmas](https://thepracticaldev.s3.amazonaws.com/i/6z5dct67wfpfbxnmivht.jpg)

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

## License

All the code containing in this repository is licensed under the [BSD-3 clause OSI license](https://opensource.org/licenses/BSD-3-Clause).