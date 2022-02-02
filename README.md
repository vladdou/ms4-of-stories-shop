
Welcome flisanp,

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------
-save info box does not work
-can't search for test product
-url not found products/add
-media files not showing on deployed site

-local variable 'order_form' referenced before assignment
solution: You had the else block that rendered the form within the block of code that run only on GET requests, I have corrected the indentation.
it was an indentation error, as the form was nested in the GET block: when a POST request is made to the view it cannot find the form as value is only assigned upon a GET request.
It was pointing to line 130 as that is where the context is being passed to the template (the context variables gets passed to the template on both GET and POST request) and with the indentation error order_form had no value on POST

-templatedoesnotexist - forgot *Blog*/blog.html

-When I wanted to reach a add_blog page I got: Page not found , 404 error
Moved url above the other.
It is most likely Django tried the patterns in order and found a "match" before the intended
-New error when I tried to add a blogpost:


Credits
https://djangocentral.com/building-a-blog-application-with-django/