# AWARDS


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
 


# Project prompt
    At Moringa school you create a lot of projects (IPs, Mid-week projects) but you never know how those projects rate with your peers. Your objective is to create an application like Awwards (Links to an external site.)Links to an external site. (It doesn't necessarily have to be exactly the same). The application will allow a user to post a project he/she has created and get it reviewed by his/her peers.

A project can be rated based on 3 different criteria

    Design
    Usability
    Content
    These criteria can be reviewed on a scale of 1-10 and the average score is taken.

# User stories
As a user, you can:

    View posted projects and their details.
    Post a project to be rated/reviewed
    Rate/ review other users' projects
    Search for projects 
    View projects overall score
    View my profile page.

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


# Getting Started.

    These instructions will get you a copy of the project up and running on a local host.

    Step 1: git clone
    Step 2: Enter the Project root folder

    cd gallery/
    install virtual environment (venv) without pip

    python3.6 -m venv --without-pip virtual
    Step 3: Activate virtual environment

    source virtual/bin/activate
    install pip using curl


## Deployment

    Deploying the Django Apps to Heroku to view.

## Built With

    Python3.9.5 - Python is a programming language that lets you work quickly and integrate systems more effectively
    Django - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design
    postgresql - PostgreSQL is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.
    Versioning
    version 1.0.0

## Bugs

    If you encounter any bugs, email me on melissamalala@gmail.com. If you would like to add some changes, please feel free to
fork the project and make a pull request.

## Live site

Find the live site a href="#" target="_blank">github</a> pull  here.

## Authors

Chepngetich Edah

## License

This project is licensed under the MIT License




