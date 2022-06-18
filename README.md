# Hangman
“Hangman” is a classic word game. The concept is to guess the correct word with minimum attempts possible. The user will be penalized for each incorrect guess by the appearance of apparatus for hanging in a step-by-step fashion finally culminating with the appearance of a hanging man. I have developed this game based on computer word list. This game has been developed with Python. 


![Screenshot_front](https://user-images.githubusercontent.com/97182442/173900203-68d3fd57-ce2f-4c29-86aa-dfd839f3b552.png)


## UX (User Experience)

### User stories

#### User Goals

- As a first time visitor, I want to understand the rules to play the game.

- I want to be able to replay the game without repeating the same word each time.

- I want to build my vocabulary in computer field.

- I want to have a positive response to my interaction with the game.

- I want to have a leisurely engagement with a fun game.

- As a user I can give my name and the game welcomes with a greeted message.

- For invalid inputs I will be notified with an error message.

- The game counts down the number of tries remaining for the user.

- The game indicates the user what action must take in each step.


### Technologies Used

### Languages Used

 1. Python

#### Git

Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

#### GitHub

GitHub is used to store the projects code after being pushed from Git.

#### Balsamiq Wireframes

Downloadable software to create the wireframe mockups.


#### Lucidchart

Web-based diagramming application used to build flowchart.


### Wireframes

1. Wireframe of the welcome page


![Welcome page](https://user-images.githubusercontent.com/97182442/173900280-4cc9dcf0-33fc-45be-b952-81d09f8614cd.png)


2. Wireframe of the game page


![Game page](https://user-images.githubusercontent.com/97182442/173900346-dfa2f941-f821-4216-89a2-7ac00c817ee1.png)


### Flowchart




![Flowchart](https://user-images.githubusercontent.com/97182442/173900409-b148170c-1c21-4bb7-9614-fabc782319e0.png)


### Features

#### Existing features

1. The start screen will display an option to enter player name.
![welcome_game](https://user-images.githubusercontent.com/97182442/174427530-c1ddc450-6cc4-4bf9-bfdb-2b0166a151b7.png)



![Welcome_user](https://user-images.githubusercontent.com/97182442/174427541-e4ddac8b-5ddb-4165-a02c-6c11caa82a34.png)

2. Option for user to access game rules has been provided including the theme i.e., computer word list.


![rules](https://user-images.githubusercontent.com/97182442/174427554-49b3d8cc-c354-4cae-898f-959337c53f33.png)


3. The player has 5 attempts to guess the right word from the computer vocabulary.


![hangman stage_1](https://user-images.githubusercontent.com/97182442/174427563-cb71231a-d7cf-49aa-aba1-944a4e317a13.png)


4. Each wrong attempt will be penalized by a step-by-step appearance of a hanging man.



![stage_2](https://user-images.githubusercontent.com/97182442/174427576-ddb1fb39-7fdc-4009-8736-50a0ac3d09c7.png)


![last stage](https://user-images.githubusercontent.com/97182442/174427584-8c21b091-0b57-4cd2-af52-16b7b916f1dd.png)

5. Each correct guess (alphabet) will appear in the blank spaces in the correct order of the words in the computer vocabulary. 


![letter dispaly_correct guess](https://user-images.githubusercontent.com/97182442/174427592-fc7a04b6-719c-401e-9006-4b693264efa7.png)


6. In case the player fails and ends the game, the correct answer will be displayed.

![last stage](https://user-images.githubusercontent.com/97182442/174427596-8f697da0-a543-485a-9047-d0a46d13e5f9.png)

7. If the player wishes to continue, after each play he/she can do so by clicking the yes button.



![ask to play game again](https://user-images.githubusercontent.com/97182442/174427727-8530099c-f8c0-4590-8918-97178f6c26e8.png)



## Testing!


For this project I have done the following tests:

- Passed the code through a PEP8 liner and confirmed there are no errors.

- Using directional key inputs'.

- Tested in my local terminal and Code Institute Heroku terminal


#### Validator testing

- PEP8 No errors were found in PEP8online.com


![PEP8 result](https://user-images.githubusercontent.com/97182442/174427750-5f3924f4-170d-414d-8958-f30f41e4dbf1.png)


- The code was also passed throuth Pylint. I encountered some warnings related to global
  variables. To solve this issue, I installed pylintrc in my gitpod.
  
  ![Pylint test result](https://user-images.githubusercontent.com/97182442/174427746-949951f1-3840-45f4-9bbe-275928a9efff.png)

  


### Deployment

This project was deployed using Code Insitute's mock terminal for Heroku.

#### Steps for deployment

1. Fork or clone the repository.

2. Create a new Heroku app.

3. Set the buildbacks to Python and NodeJS in that order.

4. Link Heroku app to the repository using Gitpod terminal
   - heroku login -i
   - enter personal email
   - enter pasword using API Key from Heroku
   - Got the app name from Heroku by typing in the command "heroku apps".
   - Set heroku remote by typing heroku "git:remote -a python-portfolio-  project".
   - Add and commit to GitHub and Heroku by typing "git add . && git commit -m "Deploy to Heroku via CLI"".
   - Pushed to both GitHub and Heroku by typing "git push origin main" and "git push heroku main".



## Credits

- Code Institute for the deployment terminal and template
- My mentor, Narendar Singh for his valuable advice and feedback.
- Words were generated from https://www.enchantedlearning.com/wordlist/computer.shtml
- I have referred w3scools.com
- For writing the code, I have referred https://www.chegg.com/homework-help/questions-and-answers/write-program-called-hangmanpy-expands-upon-tutorial-8-problem-3-following-changes-made-pr-q88357648










