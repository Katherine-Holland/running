# Guided Trail Running

![Responsive image here](static/images/moors.jpeg)

Take a look at the deployed site here: [Guided Trail Running](https://trailrunning-f565347cbca0.herokuapp.com).

### Getting Started

#### Forking the Repository
1. Go to the GitHub repository: [Open in GitHub](https://github.com/Katherine-Holland/running).
2. Click the **Fork** button in the upper right corner of the page to create a copy of the repository under your own GitHub account.
3. After forking, you can open it in Gitpod using the button above.

#### Cloning the Repository
If you are working locally, you can clone the repository:
1. Open your terminal or command prompt.
2. Run the following command to clone the repository:
   ```bash
   git clone https://github.com/Katherine-Holland/running.git
   
   and navigate to the directory using this command in the terminal:
   cd running

You can then set up your environment and run the project locally.



#### Clone the Repository - Alternative Method

Click on the green Code button at the top right of the repository and copy the URL that appears.
In your terminal, use the following command to clone the repository:
bash
Copy code
git clone https://github.com/Katherine-Holland/running.git
Replace <URL> with the URL you copied from GitHub, which should look like https://github.com/Katherine-Holland/running.git.
Navigate to the Project Directory
After cloning, navigate into the project directory by running:

bash
Copy code
cd repository-name

Install Project Dependencies
Make sure to install any project dependencies as specified in the repository’s documentation. Often, projects will include a requirements.txt file or package.json for this.

Running the Project
Follow the instructions in the repository for running the project locally using Django. This project uses: python manage.py runserver.




# Project Aim

Guided Trail Running is a blog for like minded trail runners to come together and discuss trail running. The blog also acts as a marketing tool to allow the site owner to encourage runners to sign up to their guided running holidays. The site is designed to grow into an informative resource for trail runners.

#Project Aim & UX Goals

##Project Goals: The website is aimed at bringing together trail runners and facilitating community engagement. The aim is to provide an informative experience for trail runners and the option to meet up together via trail running holidays.

##User Experience: I kept the navigation simple and intuitive as this was my first project using Django. I created an easy registration process and kept a welcoming design that feels aligned with the outdoors.

## Target Audience
The target audience are both people new to trail running and those with trail running experience. The audience for trail running holidays is usually mixed, however, more women tend to sign up to holidays and the site reflects this, with images of groups of people and women represented in the images presented.

## Planning
I created ERD diagrams and planned the site layout. I used Balsamiq to create wireframes. I then created a Repository in GitHub and set up GitHub Issues and created a Kanban Board following an Agile methodology. The steps are below:

## Creating a Repo in GitHub
Step 1: Create a GitHub Repository
Go to GitHub and log into your account.
In the top-right corner, click the + icon, then select New repository.
Name your repository and add an optional description.
Choose the repository's visibility: Public or Private.
Initialize the repository with a README and .gitignore.
Click Create repository.
Step 2: Enable Gitpod for the Repository

## Setting up GitHub Issues
Go to your GitHub repository.
Click on the Issues tab in the top menu.
Click New Issue to create an issue.
Title: Give each issue a clear title, like "User Registration Form".
Description: Add details about the issue, including the requirements or acceptance criteria, so it’s clear what needs to be done.
Label the Issue:For Agile, you might use labels like "Backlog," "In Progress," "Review," or "Done."

## Create a Kanban Board in GitHub

Go to the "Projects" tab of your repository.
Click New Project to create a project board.
Select “Table or Board” view, which will help structure your tasks into columns for better tracking.
Name Your Board (e.g., "Project Kanban Board") and add an optional description.

Step 4: Link Issues to the Kanban Board

Go back to the Issues tab and open an issue you’d like to add to the Kanban board.
In the right sidebar of the issue, find Projects and select your new Kanban board from the dropdown.
The issue will now appear in your board’s Backlog column (or wherever you choose to place it initially).
Step 5: Manage Workflow with Agile Methodology

Prioritize the Backlog: Review and prioritize the issues in the Backlog column based on your project’s needs (use MoSCoW prioritization here if it applies).
Move Issues Through the Board:
At the start of each sprint or iteration, move items from Backlog to To Do.
As team members start working on an issue, drag it to In Progress.
When an issue is ready for review, move it to In Review.
After successful review and testing, move the issue to Done.
Track Progress: Monitor the board daily to see the status of each task, ensuring work is progressing according to plan.
Close Issues When Complete: Once an issue is in the Done column and confirmed complete, close the issue in GitHub to keep the backlog manageable.

## MoSCoW Prioritization

- I used MoSCoW prioritization to rank how essential each feature would be. See image below for my user stories and how I labelled them. 

![MoSCoW Prioritization](static/images/)

MoSCoW prioritization is a technique used to categorize project requirements into levels of importance. Each letter represents a different priority:

Must-Have: These are essential features without which the project would be incomplete or fail to meet its core purpose. For your site, this might include basic navigation, user authentication, and the ability to create and view posts.

Should-Have: These features are important but not essential for a working release. They add significant value but won’t stop the project from functioning if left out. For instance, you might classify the weather integration feature as a "Should-Have" if it's not central to your app's primary function.

Could-Have: These are desirable features that would enhance user experience but are not critical. They might be planned for a later release if there is time. Examples could be additional styling elements, an animated typewriter effect, or extra filters in your blog view.

Won't-Have (for now): These features are acknowledged but intentionally deferred for a later phase. This could include advanced search features or more complex social login options.

This prioritization helps focus development efforts on what will deliver the most value and keeps the project on track. 

## User Stories

1. Open a post
As a site user I can click on a post so that I can read the full text.
AC1 When a blog post title is clicked on a detailed view of the post is seen.

2. View Comments 
As a Site User/Admin I can view comments on an individual post so that I can read the conversation.
AC1 Given one or more user comments the admin can view them.
AC2 Then a site user can click on the comment thread to read the conversation.

3. Account Registeration
As a Site User I can register an account so that I can comment on a post.
AC1 Given an email a user can register an account.
AC2 Then the user can log in.
AC3 When the user is logged in they can comment.

4. Comment on a post
As a Site User I can **leave comments on a post ** so that I can be involved in the conversation.
AC1 When a user comment is approved.
AC2 Then a user can reply.
AC3 Given more than one comment then there is a conversation thread.

5. Modify or Delete Comment on a post
As a Site User I can *modify or delete my comment on a post so that I can be involved in the conversation.
AC1 Given a logged in user, they can modify their comment.
AC2 Given a logged in user, they can delete their comment.

6. Manage Posts
As a Site Admin I can create, read, update and delete posts so that I can manage my blog content.
AC1 Given a logged in user, they can create a blog post.
AC2 Given a logged in user, they can read a blog post.
AC3 Given a logged in user, they can update a blog post.
AC4 Given a logged in user, they can delete a blog post.

7. Create Drafts
As a Site Admin I can create draft posts so that I can finish writing the content later.
AC1 Given a logged in user, they can save a draft blog post.
AC2 Then they can finish the content at a later time.

8. Approve Comments
As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments.
AC1 Given a logged in user, they can approve a comment.
AC2 Given a logged in user, they can disapprove a comment.

9. View a Paginated list
As a User I can view a paginated list of posts so that I can discover the post I want to read easily.

10. Create a Contact Us form
As a Potential Customer, I can send the site owner a message so that I can find out more about the holidays and potentially book.
AC1 A user can submit a request for more information without logging in.
AC2 A user can see a confirmation message that the submission has been successful.

As a Site Owner, I can store booking messages in the database so I can review them and respond.
AC1 A Site Owner can see the booking messages in the admin area.
AC2 A Site Owner can mark messages as "read" to allow for processing unread messages and avoiding missing requests.


## Home Page


![Home Page](static/images/)


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
Lighthouse testing was successful for all pages, meeting accessibility requirements.
![Lighthouse Test](static/images)


# Forking




# Cloning




# Bugs
1. Using the dev tools I noticed an error for get element by id was null for editing a post. I realised that get attribute was not complete.

# Credits

- My Mentor Spencer
- Code Institute Walkthrough Projects.


# Future features 
- Adding the option for a social sign in to improve user experience.
- Add a booking feature to allow users to book holidays.
- Add a more comprehensive weather outlook for each area
