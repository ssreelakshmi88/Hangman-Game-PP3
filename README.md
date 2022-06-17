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

2. Option for user to access game rules has been provided including the theme i.e., computer word list.

3. The player has 5 attempts to guess the right word from the computer vocabulary.

4. Each wrong attempt will be penalized by a step-by-step appearance of a hanging man. 

5. Each correct guess (alphabet) will appear in the blank spaces in the correct order of the words in the computer vocabulary. 

6. In case the player fails and ends the game, the correct answer will be displayed.

7. If the player wishes to continue, after each play he/she can do so by clicking the yes button.


## Testing

For this project I have done the following tests:

- Passed the code through a PEP8 liner and confirmed there are no errors.

- Using directional key inputs'.

- Tested in my local terminal and Code Institute Heroku terminal


#### Validator testing

- PEP8 No errors were found in PEP8online.com

- The code was also passed throuth Pylint. I encountered some warnings related to global
  variables. To solve this issue, I installed pylintrc in my gitpod.


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










