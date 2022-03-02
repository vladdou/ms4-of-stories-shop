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
When running the js files through JShint the linter throws a warning regarding an undefined variable. This is because the $ sign is jQuery syntax and the linter is checking for ES6 syntax which jQuery operators aren't a part of.

<br>
<img src="static/README/bugs/jshint.png" width="300" height= auto />
<br>  

---  

## Testing User Stories

*1. As a shopper I want to be able to view all the products so that I can select some to purchase.*

- All users who visits the website can view all the products without having an account or log in. 

![user_story_1](static/README/user_stories/user-stories-1.png)  

---  

*2. As a shopper I want to be able to view details about a product so that I can identify the price, product description and image.*

- By clicking on the image or titel of a product the user gets to the products detail page where they can view the price, description and a larger image of the product.

![user_story_2](static/README/user_stories/user-stories-2.png)  
  
---

*3. As a shopper I want to be able to view the rating of a product so that I can see what others think of the product I'm interested in.*

- The rating of a product is shown on the products card and on the detailed products page.

![user_story_3](static/README/user_stories/user-stories-3.png)  

---

*4. As a shopper I want to be able to view the total price in my shopping bag so that I can be aware of how much money I'm spending.*

- The shopping bag is available at all time in the navbar where the user can see the total amount spent

![user_story_4](static/README/user_stories/user-stories-4.png)  

---

*5. As a site user I want to be able to find useful information about the products and their origins so that I can learn more about the products and the values of the company.*

- Users can find information through the blog that is located in the navbar

![user_story_5](static/README/user_stories/user-stories-5.png)  

---

*6. As a site user I want to be able to register for an account so that I can have a personal account and be able to view my profile.*

- A link to the sign up form where users can register for an account is available through the navbar

![user_story_6](static/README/user_stories/user-stories-6.png)  

---

*7. As a site user I want to be able to log in/log out so that I can access my personal account information*	

- A link to the log in form where users can log in is available through the navbar

![user_story_7](static/README/user_stories/login.png)  

- Once the user is logged in, a link to the log out page appears in the navbar

![user_story_7](static/README/user_stories/logout.png) 

---

*8. As a site user I want to be able to recover my password in case I forget it so that I can regain access to my account.*

- On the log in page is a link for resetting the password

![user_story_8](static/README/user_stories/user-stories-8.png) 
![user_story_8](static/README/user_stories/password-reset.png)  

---

*9. As a site user I want to be able to receive email confirmation after registering so that I can know my account registration was successful.*

- The user will receive a email confirmation after signing up for an account

![user_story_9](static/README/user_stories/user-stories-9.png)  

---

*10. As a site user I want to be able to have a personalized user profile so that I can view my order history and save my payment information.*

- When a user is registered they will have a personalized profile page that will be available through the navbar

![user_story_10](static/README/user_stories/my-profile.png)  

---

*11. As a shopper I want to be able to sort the list of products so that I can identify the product that is best rated or has the best price.*

- On the product page there is a selector dropdown where the user can choose to sort the products by price, name etc.

![user_story_11](static/README/user_stories/user-stories-11.png)  

---

*12. As a shopper I want to be able to search for a product by name or description so that I can find a specific product that I'm looking for.*

- In the navbar is a search input field where the user can search for products on the site

![user_story_12](static/README/user_stories/user-stories-12.png)  

---

*13. As a shopper I want to be able to see what I have searched for and the number of results so that I can	see if the product I'm looking for is available.*

- The search result is shown on the product page with a heading telling the user what they've searched for and the number of results found


![user_story_13](static/README/user_stories/user-stories-13.png)  

---

*14. As a shopper I want to be able to look for products sorted by category so that I can find the type of product that I'm looking for.*

- Users can choose a category they're intrested in through the **SHOP** dropdown link in the navbar

![user_story_14](static/README/user_stories/user-stories-14.png)  

- They can also navigate through the links available on the home page.

![user_story_14](static/README/user_stories/product-categories.png) 

---

*15. As a shopper I want to be able to access the shop quick and easy so that I can purchase the products that I'm interested in.*

- Users can access the shop quickly by clicking the call to action buttons on the home page

![user_story_15](static/README/user_stories/user-stories-15.png)

- They can also go straight to the shop through the **SHOP** link available in the navbar

![user_story_15](static/README/user_stories/shop-access.png)  


---

*16. As a shopper I want to be able to select the quantity of a product that I want to buy so that I can ensure I order the amount I want.*

- On the product detail page there is a quantity selector to easy choose the number of products to buy

![user_story_16](static/README/user_stories/user-stories-16.png)  

---

*17. As a shopper I want to be able to view all items in my shopping bag so that I can make sure I've got the things I wanted to order and identify the cost.*

- On the shopping bag page the user will have a overview on all the items in the bag and the bag total 

![user_story_17](static/README/user_stories/user-stories-17.png)  

---

*18. As a shopper I want to be able to easily enter payment information so that I can checkout quick and easy.*

- The checkout page contains a payment form making it easy for the user to add their information and to save it to their profile for even easier checkouts in the future

![user_story_18](static/README/user_stories/user-stories-18.png)  

---

*19. As a shopper I want to be able to view an order confirmation after checkout so that I can verify that I didn't make any mistakes.*

- After checkout the user is sent to a checkout success page that shows the order information

![user_story_19](static/README/user_stories/user-stories-19.png)  

---

*20. As a shopper I want to be able to receive a confirmation email after checkout so that I can keep information about my order.*

- The user will receive a confirmation email after the checkout is completed

![user_story_20](static/README/user_stories/user-stories-20.png)  

---

*21. As a store owner I want to be able to add products to the site so that I can update my shop with new items.*

- When the superuser is logged in it's possible to access a form for adding products through the navbar

![user_story_21](static/README/user_stories/user-stories-21.png)  

---

*22. As a store owner I want to be able to edit and update a product so that I can change the products description, price and so on.*

- When the superuser is logged in it's possible to edit a product via a link on the products page 

![user_story_22](static/README/user_stories/user-stories-22.png) 
![user_story_22](static/README/user_stories/edit-product.png)  

---

*23. As a store owner I want to be able to delete a product so that I can remove items that are no longer for sale.*		

- When the superuser is logged in it's possible to delete a product via a link on the products page

![user_story_23](static/README/user_stories/user-stories-23.png)
![user_story_23](static/README/user_stories/delete-product.png)  

---

*24. As a store owner I want to be able to add a blog post so that I can share useful information about the products and the company.*	

- When the superuser is logged in it's possible to access a form for adding blog posts through the navbar

![user_story_24](static/README/user_stories/user-stories-24.png)  

---

*25. As a store owner I want to be able to edit and delete a blog post so that I can update or delete information that are no longer relevant.*			

- When the superuser is logged in it's possible to edit and delete a blog post via a link on the blog post page

![user_story_25](static/README/user_stories/user-stories-25.png)
![user_story_25](static/README/user_stories/edit-blog.png)
![user_story_23](static/README/user_stories/delete-blog.png)  
  
---   
  
## During Development I Fixed The Following Bugs

 - When I clicked on the checkout button I got an error saying "local variable 'order_form' referenced before assignment" and it said the issue was in checkout views. 

<br>
<img src="static/README/bugs/local_variable_bug.png" width="auto" height="300"/>
<br>

When I googled the issue it says that this occurs when some variable is referenced before assignment within a function’s body. It turned out it was a small indentation error. The form was nested in the GET block: when a POST request is made to the view it cannot find the form as value is only assigned upon a GET request. I had the else block that rendered the form within the block of code that run only on GET requests, 
and with the indentation error order_form had no value on POST

<br>
<img src="static/README/bugs/order_form.png" width="auto" height="300"/>
<br>

---

- I've got a Page not found , 404 error on the add_blog page 

<br>
<img src="static/README/bugs/page_not_found.png" width="auto" height="300"/>
<br>

I moved the url above the other ones and then it worked perfecly. It was most likely that Django tried the patterns in order and found a "match" before the intended.

---

- I've got a 500 error on two of my pages, the blog and the shop in my deployed heroku app. 

<br>
<img src="static/README/bugs/blog_error.png" width="auto" height="300"/>
<br>
 
I put a DEVELOPMENT variable in my Heroku config vars to get a better idea of what's going on. The error showing was:

<br>
<img src="static/README/bugs/programming_error.png" width="auto" height="300"/>
<br>

To fix this problem I needed to run migrations on the postgres database:

1. logged in to the heroku cli in my workspace terminal: heroku login -i
2. then, I migrate with: heroku run python3 manage.py migrate

---

- The footer didn't stick to the bottom of the page if there wasn't enough content

<br>
<img src="static/README/bugs/footer-bug.png" width="auto" height="300"/>
<br>

This issue was solved by adding 
`<div class=content> </div>`
around the block content in base.html and adding this styling to css:

`html, body {
  height: 100%;
}`

`body {
  display: flex;
  flex-direction: column;
}`

`.content {
  flex: 1 0 auto;
}`

`.footer {
  flex-shrink: 0;
}`

Now everything was working except on the index page where the footer now was in the middle of the page below the hero image. 

<br>
<img src="static/README/bugs/footer-bug-mid-page.png" width="auto" height="100"/>
<br>

It turned out I had added h-100 to my index-hero container class and it was setting the element to be 100% of device height and not allowing the div to stretch for full content. I already had the height set to 100vh in base.css on index-hero so it was extra anyway. When I removed this everything worked.


### Responsiveness issues  

- When I test the responsiveness on Nest Hub and Ipad Mini in landscape mode I get issues with the search bar. The button appears underneath the input field instead of next to it. When I remove flex-flow: row wrap; in DevTools they're aligned but since this only appears on screensizes between 992px - 1120px and deadline is coming up I've decided to keep it like that for the time beeing and fix it in the future.

<br>
<img src="static/README/bugs/nest-hub.png" width="auto" height="300"/>
<br>

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
    - Delete button opens confirmation page - *No* button takes you back to the product, *Yes* button deletes product from database
    - Breadcrumb links
    - Quantity function
    - Adds to bag
- Blog
    - Links to full blog post
    - Edit blog post opens prefilled form and saves changes to database
    - Delete button opens confirmation page - *No* button takes you back to the blog post, *Yes* button deletes blog post from database
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
- Contact Form
    - Showing signed in users emailaddress prefilled
    - Sending emails to site owner
- Shopping bag
    - Shopping bag showing info about product(s)
    - Quantity function
    - Remove from bag function
    - Delivery cost showing under $50 and is removed above
    - Checkout button
- Checkout
    - Delivery information is prefilled if saved to My profile
    - Order summary shows
    - Complete order with stripe
    - Showing information of order
    - Recieving confirmation email
    - Order being created in database

---

## Testing Responsiveness  

To make sure that the site is responsive:
 - I manually tested it on all available devices in Google Chrome DevTools
 - I've used the site [Responsinator](http://www.responsinator.com/?url=of-stories.herokuapp.com%2F)

---  


