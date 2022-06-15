# AWARDS
[![Screenshot-from-2022-06-15-06-21-51.png](https://i.postimg.cc/CxCpB3s1/Screenshot-from-2022-06-15-06-21-51.png)](https://postimg.cc/68QmF1SJ)


## API Endpoints (url / uri)
    - CRUD : Create, Retrieve, Update, Delete 
    - Create List and Search

## HTTP methods (client side)
    - GET, POST, PUT, MATCH, DELETE    
    
## Data Types and Validation
    Use a serializer for consistency 
    JSON -> Serializer
    Validation -> Serializer
    
    
    
## Awwards
This is an application which allows users to post their projects and allow other users to rate as well as view and rate other people's projects.


# References
 <ul>
  <li>W3schools</li>
  <li>Python documentation</li>
  <li>Django documentation</li>

</ul>






# User stories
As a user, you can:

    View posted projects and their details.
    Post a project to be rated/reviewed
    Rate/ review other users' projects
    Search for projects 
    View projects overall score
    View my profile page.
    A project can be rated based on 3 different criteria:
    Design
    Usability
    Content
    These criteria can be reviewed on a scale of 1-10 and the average score is taken.

## System Features/Objectives
     Projects
Projects should have a Title, an image of the project's landing page, a detailed description of the project, a link to the live site.

     Profile
Your project should have a user profile that at least the following information:

    Profile picture of the user.
    User Bio
    Projects the user has posted
    A contact information of the user. 
 An Authentication System 
    Your application should have a solid authentication system that allows users to sign up or log in to the application before posting or rating a project.

     Rating/ Review
Projects will be rated/reviewed based on the following criteria:

 
##  API Endpoints
    You should create an API so that users can access data from your application. You can create two API endpoints:

Profile - This endpoint should return all the user profiles with information such as the username, bio, projects of the user and profile picture
Projects- This endpoint should return information pertaining to all the projects posted in your application.


## Setup/Installation Requirements

<h3>Clone the repository below.</h3>

`git clone https://github.com/edah-hub/AWARDS.git`

<h3>Create a virtual environment and activate it.</h3>

`python -m venv <name-of-environment>`<br>
`source venv/bin/activate (Linux)`<br>
`source venv/Scripts/activate (Windows)`

<h3>Install the requirements.</h3>

`pip install -r requirements.txt.`

<h3>Create environmental variable file and add database configurations.</h3>

`touch .env`

<h3>Make a migrations.</h3>

`python manage.py makemigrations`<br>
`python manage.py migrate`

<h3>Run the application.</h3>

`python manage.py runserver.`


## Deployment

    Deploying the Django Apps to Heroku to view.

## Built With

    Python3.9.5 - Python is a programming language that lets you work quickly and integrate systems more effectively
    Django -Python3 Framework
    postgresql - Database
## Bugs

    If you encounter any bugs, email me on cheruiyotedah@gmail.com. If you would like to add some changes, please feel free to
fork the project and make a pull request.

## Live site

View the website <a href="#">Here</a>

## Authors

Chepngetich Edah

## License

The MIT License (MIT) Copyright (c) 2022 Chepngetich Edah.




