# Guided Trail Running

![Responsive image here](static/images/moors.jpeg)

Take a look at the deployed site here [Guided Trail Running](https://trailrunning-f565347cbca0.herokuapp.com).

# Project Aim

Guided Trail Running is a blog for like minded trail runners to come together and discuss trail running. The blog also acts as a marketing tool to allow the site owner to encourage runners to sign up to their guided running holidays. The site is designed to be an informative resource for trail runners.


# User Experience (UX)


## Project Goals




## Target Audience


## User Stories


## Kanban Board


![Kanban Board](static/images/)


## MoSCoW Prioritization

- I used MoSCoW prioritization to rank how essential each feature would be. See image below for my user stories and how I labelled them. 

![MoSCoW Prioritization](static/images/)



# Features


### All "Must Have" features were implemented. 


## Landing Page


![Landing Page](static/images/)


## Navbar and Navbar links


![NavBar](static/images/png)


## Login Status


![Login Status](static/images/.png)


## Create, Read, Update, Delete (CRUD) Functionality


![CRUD Example](static/images/png)


## Register / Sign In / Sign Out

![SignUp Form](static/images/png)

- See below for Sign In form. 

![SignIn Form](static/images/.png)

- See below for Sign Out screen.
![SignOut Screen](static/images/.png)


## Feedback messages to user upon user actions (i.e deleting a post)


![Delete post](static/images/e.png)

![Sign In and reflects username](static/images/.png)

![Post Created](static/images/.png)

![Comment Deleted](static/images/.png)

![Post Deleted](static/images/.png)

![Signed Out](static/images.png)


# Design


 ### I kept the design simple and easy to navigate:**

clear top navigation

## Technologies Used

- HMTL, CSS, JavaScript, Python and Django.

- [Balsamiq Wireframes.](https://balsamiq.com/) 

- Heroku was used for deployment.

- GitHub was used for storing all of my files and READme. 

- Git was used for version control --> "git add . " --> "git commit -m "**message**" --> "git push".

- [Google Fonts was used to import fonts for the project.](https://fonts.google.com/) 

- [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/).

- [The Code Institute database maker was also used](https://dbs.ci-dbs.net/).

- [Cloudinary](https://cloudinary.com/).

- Django Aullauth was used for handling the forms and allowing users to register and sign in.


## Typography



## Color Palette

I chose a simple colour scheme of greys and greens to match the feel of the environment found in Trail Running. This simple design also helped the user to navigate easily around the site.




## Wireframes (include different screen sizes)



## Post Feed Wireframe



## Landing Page Wireframe


![Landing Page](static/images.png)


## Signup Form Wireframe


![Signup Form](static/images/.png)


# Testing

## User Story Testing



## Browser Compatibility

The site works as intended on Google Chrome and Safari.


## Validations

HTML Validation

| Directory  | File                    | Result |
|------------|-------------------------|--------|
| blog       | create_post.html        | PASS   |
| blog       | edit_post.html          | PASS   |
| blog       | post_detail.html        | PASS   |
| blog       | post_list.html          | PASS   |
| home       | home.html               | PASS   |
| signup     | login.html              | PASS   |
| signup     | logout.html             | PASS   |
| signup     | signup.html             | PASS   |

- JavaScript validation

![JavaScript Validation](static/images/j.png)

- CSS Validation

Directory	File	Result

|   Directory   	|   File       	|   Result  	|
|---------------	|--------------	|-----------	|
|   static/css  	|   style.css  	|      	|

- Python Validations

| blog     	| apps.py     	| PASS  	|
|----------	|-------------	|-------	|
| blog     	| forms.py    	|   	|
| blog     	| models.py   	|   	|
| blog     	| urls.py     	|   	|
| blog     	| views.py    	|   	|
|          	|             	|       |
| running   | settings.py   |FAIL (line too long)|
| running   | urls.py.      |PASS                |

| home     	| __init__.py 	| 
| home     	| admin.py    	|   	|
| home     	| apps.py     	| 	|
| home     	| forms.py    	|   	|
| home     	| models.py   	|  	|
| home     	| urls.py     	|   	|
| home     	| views.py    	|   	|
|          	|             	|       	|
|          	|             	|       	|
| signup   	| __init__.py 	|   	|
| signup   	| admin.py    	|   	|
| signup   	| apps.py     	|   	|
| signup   	| forms.py    	|   	|
| signup   	| models.py   	|   	|
| signup   	| urls.py     	| 	|
| signup   	| views.py    	|   	|
|          	|             	|       	|
|          	|             	|       	|
| 	| __init__.py 	|  	|
|  	| asgi.py     	|  	|
|  	| settings.py 	|   	|
|  	| urls.py     	|  	|
| 	| wsgi.py     	|  	|


## Lighthouse Testing (Desktop and Mobile)




# Forking

- Forking a repository on GitHub essentially means creating a copy of someone else's project repository. One benefit of this would be that you can make changes to the project without affecting the original repo. To fork a repo, **please follow the below steps:**

1. On GitHub, navigate to the GitHub repository you would like to fork. 

2. In the top right hand corner, you will see a fork button, click this to fork the desired repo. (note: you cannot fork your own repo's so this button will be greyed out on your own repo's).

3. Once you hit the fork button, it will bring you to the **"Create a new fork screen"**. 

4. You can then hit the green **"Create fork"** button. 

# Cloning

- Cloning a repo means copying the entire project repository to your machine. To clone a repo, **please follow the below steps:**

1. Navigate to the repository you want to clone. 

2. Click the green code button. 

3. You will see three subheadings of HTTPS, SSH and GitHub CLI. Copy the URL under the HTTPS subheading. 

4. Open the terminal in your IDE (e.g VS Code or GitPod). 

5. Type the command "git clone" with the URL you copied in the step 3. 

6. Finally, hit Enter. 

# Bugs


# Credits

- My Mentor Spencer
- Code Institute Walkthrough Projects.


# Future features 
-Social sign in
-Booking feature to allow users to book holidays.