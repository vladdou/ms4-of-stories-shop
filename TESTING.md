# Testing  

## Validator Testing  


### HTML Testing
[W3C Markup Validation](https://validator.w3.org/) was used to validate HTML.  
No errors were found  

### CSS Testing 

[W3C CSS Markup Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate CSS.  
No errors were found 


### Python
[PEP8 online](http://pep8online.com/) was used to validate Python.  
No errors were found


### JS Testing  
[JShint](https://jshint.com/) was used to validate JavaScript.  



<br>
<img src="https://github.com/flisanp/ms3-baby-food-recipes/blob/main/static/images/README/bugs/jshint.png" width="300" height= auto />
<br>  

---  

## Testing User Stories

*1. As a shopper I want to be able to view all the products so that I can select some to purchase.*

![user_story_1](static/README/user_stories/)  

![user_story_1](static/README/user_stories/)  

---  

*2. As a shopper I want to be able to view details about a product so that I can	identify the price, product description and image.*

![user_story_2](static/README/user_stories/)  
  

![user_story_2](static/README/user_stories/)  
    

![user_story_2](static/README/user_stories/)  

---

*3. As a shopper I want to be able to view the rating of a product so that I can see what others think of the product I'm interested in.*

![user_story_3](static/README/user_stories/)  

---

*4. As a shopper I want to be able to view the total price in my shopping bag so that I can avoid spending too much.*

![user_story_4](static/README/user_stories/)  

---

*5. As a site user I want to be able to find information about the company and their products so that I can	learn more about things that could be of interest.*

![user_story_5](static/README/user_stories/)  

---

*6. As a site user I want to be able to register for an account so that I can have a personal account and be able to view my profile.*

![user_story_6](static/README/user_stories/)  

---

*7. As a site user I want to be able to log in/log out so that I can access my personal account information*	

![user_story_7](static/README/user_stories/)  

---

*8. As a site user I want to be able to recover my password in case I forget it so that I can recover access to my account.*

![user_story_8](static/README/user_stories/)  

---

*9. As a site user I want to be able to recieve email confirmation after registering so that I can know my account registration was successful.*

![user_story_9](static/README/user_stories/)  

---

*10. As a site user I want to be able to have a personalized user profile so that I can view my order history and save my payment information.*

![user_story_10](static/README/user_stories/)  

---

*11. As a shopper I want to be able to sort the list of products so that I can identify the product that is best rated or has the best price.*

![user_story_11](static/README/user_stories/)  

---

*12. As a shopper I want to be able to search for a product by name or description so that I can	find a specific product that I'm looking for.*

![user_story_12](static/README/user_stories/)  

---

*13. As a shopper I want to be able look for products sorted by category so that I can find the product type that I'm looking for.*

![user_story_13](static/README/user_stories/)  

---

*14. As a shopper I want to be able to see what I have searched for and the number of results so that I can	see if the product I'm looking for is available.*

![user_story_14](static/README/user_stories/)  

---

*15. As a shopper I want to be able to access the shop quick and easy so that I can purchase the products that I'm looking for.*

![user_story_15](static/README/user_stories/)  

---

*16. As a shopper I want to be able to select the quantity of a product that I want to buy so that I can	ensure I order the amount I want.*

![user_story_16](static/README/user_stories/)  

---

*17. As a shopper I want to be able to view all items in my shopping bag so that I can make sure I've got the things I wanted to order and identify the cost.*

![user_story_17](static/README/user_stories/)  

---

*18. As a shopper I want to be able to easily enter payment information so that I can checkout quick and easy.*
![user_story_18](static/README/user_stories/)  

---

*19. As a shopper I want to be able to view an order confirmation after checkout so that I can verify that I didn't make any mistakes.*

![user_story_19](static/README/user_stories/)  

---

*20. As a shopper I want to be able to recieve confirmation email after checkout so that I can keep information about my order.*

![user_story_20](static/README/user_stories/)  

---

*21. As a store owner I want to be able to add products to the site so that I can add new products to the shop.*

![user_story_21](static/README/user_stories/)  

---

*22. As a store owner I want to be able to edit and update a product so that I can change products descriptions, prices and so on.*

![user_story_22](static/README/user_stories/)  

---

*23. As a store owner I want to be able to delete a product so that I can remove items that are no longer for sale.*		

![user_story_23](static/README/user_stories/)  

---

*24. As a store owner I want to be able to add a blog post so that I can	give information to shoppers about the products and the company.*	

![user_story_24](static/README/user_stories/)  

---

*25. As a store owner I want to be able to delete a blog post so that I can delete information that are no longer relevant.*			

![user_story_25](static/README/user_stories/)  

---



  
---   
  
## During Development I Fixed The Following Bugs

 - When I clicked on the checkout button I got an error saying "local variable 'order_form' referenced before assignment" and it said the issue was in checkout views. 

<br>
<img src="static/README/bugs/local_variable_bug.png" width="500" height="300"/>
<br>

When I googled the issue it says that this occurs when some variable is referenced before assignment within a function’s body. It turned out it was a small indentation error. The form was nested in the GET block: when a POST request is made to the view it cannot find the form as value is only assigned upon a GET request. I had the else block that rendered the form within the block of code that run only on GET requests, 
and with the indentation error order_form had no value on POST

---

- When I wanted to reach the add_blog page I got: Page not found , 404 error. 

<br>
<img src="static/README/bugs/page_not_found.png" width="500" height="300"/>
<br>

I moved the url above the other ones and it worked perfecly. It was most likely that Django tried the patterns in order and found a "match" before the intended.

---

- I get a 500 error when I click on the blog page in my deployed heroku app

<br>
<img src="static/README/bugs/blog_error.png" width="600" height="300"/>
<br>



### Responsiveness issues  

---

## Lighthouse Testing

---  

## I Manually Tested The Following Features  

- Navbar
    - All links in navbar takes you to the correct pages
    - Search function finds the correct products
    - Hover effect on links in navbar
- Footer
    - All links to social media platforms in footer opens in a new tab window   
    - Hover effect on links in footer
- Home 
    - Button "Shop now" takes you to the products page
    - Category buttons on images takes you to the correct pages respectively
- Shop
    - Sort selector sorts products correctly
    - Links to products detail page
    - Edit button opens prefilled form and saves changes to database
    - Delete button opens confirmation page - Yes button deletes product from database
    - Breadcrumb links
    - Quantity function
    - Adds to bag
- Blog
    - Links to full blog post
    - Edit blogpost opens prefilled form and saves changes to database
    - Delete button opens confirmation page - Yes button deletes blogpost from database
- Sign Up
    - Input fields displays the text to the user and hides the password
    - Error message "A user with that username already exists" displays if you try to type in an already existing username
    - Verification email being sent upon registration 
    - Link "Log In" leads to Log In page
- Log In
    - Input fields displays the text to the user and hides the password
    - Input fields are prefilled
    - "Log In" button redirects to Home page
    - Link "Register Now" leads to Sign Up page
- My profile
   - Shows default delivery information
   - Shows order history
- Log Out
    - User being logged out from My profile and redirected to Home page
- Admin
    - Only visible when superuser is logged in
    - Add products page displays a form when filled out correctly adds a product to the database
    - Add blog post page displays a form when filled out correctly adds a blog post to the database
  

## Testing Responsiveness  

---  


