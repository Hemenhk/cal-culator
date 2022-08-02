# CalCulator

This is an app that calculates the basal metabolic rate (BMR), which is caloric expenditure that a person's body burns when only doing basal tasks. 

This is a simplistic calculation that takes a few different variables: height, weight and age of the user, and then calculates their BMR. 

[Live Version Of The App](https://cal-culators.herokuapp.com/)

## How to use

CalCulator consists of four different inputs, where the user enters some personal data which will be used to calculate their BMR. The data is age in years, weight in kilograms, height in centimetres and their gender (male or female).

## Features

![feature.1](readme-img/start-calc.png)

- Prints a message welcoming the user to the app, and giving quick instructions.
- The computer automatically starts asking the user to enter their information to use for the calculation.

![feature.2](readme-img/enter-variables.png)

- The user is asked to enter their gender, which is necessary to determine their basal metabolic rate.

![feature.3](readme-img/end-calc.png)

- Finally the computer generates the user's basal metabolic rate. In the example above, a 25 yeard old male, standing at 181 cm tall and weighing 94 kg, has a bmr of 2074 calories.
- With this information the user is able to determine how many calories they need to consume to either gain or lose weight, depending on their goal.


### Technologies Used

- [Python](https://www.python.org/)
- [Heroku](https://www.heroku.com/)

### Testing

- Manually tested the code and no bugs were found.

### Validator Testing

- The code was passed through [Pep8online](http://pep8online.com/), with only two errors. These were found on lines 39 and 41, as they were too long. However, due to the fact that these are equations, there is no suitable reason to shorten them.

### Deployment

- Deploying the project to [Heroku](https://dashboard.heroku.com/)

1. Go to Gitpod CLI and create a "requirements" file by typing "pip freeze --local > requirements.txt" in the root directory.
2. Then, create the "Procfile" by typing "echo web: python app.py > Procfile" into the CLI root directory.
3. Open the "Procfile" and type in "web: python3 app.py", and delete any blank lines at the bottom, then save this file. 
4. Add, commit and push these files to Github.
5. Next, go to Heroku and create your account.
6. When logged in, click on "create new app", then select the region which is closest to your actual location, as there are only two options available: "North America" and "Europe".
7. Select "Github" as your deployment method, and within the profile enter the name of your repository which is to be deployed and click "search".
8. When Heroku has found the repository, click to connect the app. 
9. Go to the "settings" tab and click on "Add buildpack". Here, add python and nodejs, then save. 
10. Next, click on "Reveal Config Vars" and in the "KEY" tab, type "PORT". In the "Value" tab, type "8000", then add.
11. Click "deploy".
12. Once it has been deployed, your app is runnable by clicking "Open app". 

### Credits

- Code Institute
- Heroku