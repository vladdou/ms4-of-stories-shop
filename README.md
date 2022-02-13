# Of Stories Webshop  

[A live version of the page can be viewed here](https://of-stories.herokuapp.com/home)  

![mockup image](static/images/README/mockup.png)  

This is a webshop for my own brand Of Stories that sells collections of handmade goods for your home.   

---  

## UX  

### The Goals For This Website Is To:  

- Give users the possibility to find small collections with handmade items for their home
- Be able to create an account for a smooth and easy shopping experience
- Share stories about the company and their products through the blog
- Make it easy for users to navigate the site on any device   

### User Stories  
![user stories](static/README/user_stories/user-stories-MS4.png)

### Design   

![color palette](static/images/README/.png) 

#### Colors  


![color palette](static/images/README/color-palette.png)

#### Typography
 

### Wireframes  

Wireframes can be viewed [here](static/README/wireframes/MS4-wireframes.pdf)  

---

## Features
### Existing Features

- **Navbar**   
    Each page features a responsive Bootstrap navbar that’s collapsed to a burger icon when viewing on smaller screens. The navbar has a hover effect so when the user hovers over the different pages the text changes color. In the left corner there is a logo with a link that takes you to the landing page.
    - Users that are not logged in have the following pages in the navbar:
        - HOME
        - SHOP
        - STORIES
        - SIGN UP
        - LOG IN
        - CONTACT  
    - Users that are logged in have the following pages in the navbar:
        - HOME
        - SHOP
        - STORIES
        - MY PROFILE
        - LOG OUT  
    - Admin that are logged in have the following pages in the navbar:
        - HOME
        - SHOP
        - STORIES
        - ADMIN - ADD PRODUCT - ADD BLOGPOST
        - MY PROFILE
        - LOG OUT  

- **Footer**  
    The footer is displayed on all pages and features links to the companys social media accounts.

- **Home**  
    The landing page features a background image with a call to action button with the text *shop now* that leads to the page with all the products so that users have an easy and quick way of finding it.




### Features Left To Implement  


- The possibility for users to delete their own account
 

---

## Database   

Diagram of my database:

![database](static/images/README/database.png)  

---  

## Technologies Used  

### Languages  

- HTML5, CSS3, Javascript, Python and with Python framework Django

### Frameworks and Libraries  

- [Bootstrap](https://getbootstrap.com/) 
- [FontAwesome](https://fontawesome.com) 
- [Google Fonts](https://fonts.google.com) 

### All other tools  

- [Heroku PostgresSQL](https://www.postgresql.org/) - used for relational database storage
- [Heroku](https://dashboard.heroku.com/) - used to deploy the live site
- [GitPod](https://www.gitpod.io) - used for their IDE while building the website
- [GitHub](https://github.com) - used to store repository
- [Balsamiq](https://balsamiq.com) - used to create wireframes
- [DevTools](https://developers.google.com/web/tools/chrome-devtools) - used to test responsiveness 
- [Lighthouse](https://developers.google.com/web/tools/lighthouse) - used to improve performance
- [Tinypng](https://tinypng.com) - used to compress images
- [Freeformatter](https://www.freeformatter.com/) - used to beautify code
- [Coolors](https://coolors.co) - used to create color palette
- [dbdiagarm](https://dbdiagram.io/home) - used to create database diagram 
- [Am I Responsive](http://ami.responsivedesign.is/#) - used to create the mockup image in the beginning of this README file.
- [AWS S3 Bucket](https://aws.amazon.com/) - was used for storing static and media files
- [W3C Markup Validation Service](https://validator.w3.org) - used to check the HTML pages
- [W3C CSS Markup Validation Service](https://jigsaw.w3.org/css-validator/) - used to check the CSS file
- [JSHint](https://jshint.com) - used to check the script.js file
- [PEP8 online](http://pep8online.com) - used to check the app.py file  

---

## Testing  

Testing information can be found [here](TESTING.md)  

---

## Deployment  

### Create Project  

This project was created on Github using the following steps: 
1. Navigate to [GitHub](https://github.com/) and sign in
2. On the left hand side above the list of your repositories click on the green button that says "New", this will create a new repository
3. From the drop down menu that says "Repository templates" I choose the Code Institute Template  
4. Enter a name for the project and then click on the green button that says "Create Repository"

Before creating the Heroku app you need to add the following files in Gitpod:

 - To create your requirements file, type this in the terminal:
    - pip3 freeze > requirements.txt
 - Install Gunicorn
 - Create a Procfile and make sure it contains the following line: web: gunicorn [YOUR APP NAME].wsg:application (and that it is no blank line after it).

### Deployment to Heroku  

This project was deployed through Heroku using the following steps:
1. Navigate to [Heroku](https://dashboard.heroku.com/login) and sign in
2. On the top right corner there is a button that says "New". Click this button and choose the option "Create New App"
3. Choose a name for the App and what region that are closest to your location, click "Create App"
4. Click on the tab saying "Deploy" and select GitHub, Connect to GitHub
5. Enter the name of your repository on GitHub and click search
6. When the repository is found, click the "Connect" button
7. Click on the tab saying "Resources" and go to "Add-ons"
8. Search for Heroku Postgres and choose it in the appearing list
9. Select the plan named "Hobby Dev - Free" and click Submit order form
7. Click on the tab saying "Settings" and then click on the button saying "Reveal config vars"

8. Add these variables:

    - AWS_ACCESS_KEY_ID <br>
    - AWS_SECRET_ACCESS_KEY<br>
    - DATABASE_URL<br>
    - EMAIL_HOST_PASS<br>
    - EMAIL_HOST_USER<br>
    - SECRET_KEY<br>
    - STRIPE_PUBLIC_KEY<br>
    - STRIPE_SECRET_KEY<br>
    - STRIPE_WH_SECRET<br>
    - USE_AWS<br>

The value of these keys depends on the users personal setup and will not be added here due to security reasons

9. Click on the "Deploy" tab and scroll down to the section "Automatic Deployment"
10. Choose the branch you want to deploy from and then click "Enable Automatic Deploys"

### How To Run The Code Locally  

1. Log in to Github.
2. Navigate to the [repository](https://github.com/flisanp/ms4-of-stories-shop)
3. Click the tab that says "Code" and from the dropdown menu choose copy Git URL
4. Open Git and type "git clone" in the terminal followed by the URL you just copied, press enter to create your local clone
5. To install the packages listed in the requirements file type the following in the terminal: 
pip3 install -r requirements.txt

### Fork Project  

To fork the project follow these steps:

1. Log in to Github
2. Navigate to the [repository](https://github.com/flisanp/ms4-of-stories-shop)
3. Locate the "Fork" button on the top right corner of the page
4. A duplicate of the original repository is now in your Github account

---

## Credits

### Code

https://djangocentral.com/building-a-blog-application-with-django/


### Content  
 

### Media

  

---

## Acknowledgements



