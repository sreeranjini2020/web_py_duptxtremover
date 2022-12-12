# web_py_duptxtremover

1. Create an environment
   Create a project folder and a venv folder within:
     > mkdir myproject
     > cd myproject
     > py -3 -m venv venv
     
2. Activate the environment
   Before you work on your project, activate the corresponding environment:
     > venv\Scripts\activate
  Your shell prompt will change to show the name of the activated environment.
  
3. Install Flask
   Within the activated environment, use the following command to install Flask:
     > pip install Flask
     
4. open your editor:

5. A Flask application looks something like this:
     First we imported the Flask class. An instance of this class will be our WSGI application.Next we create an instance of this class. The first argument is the name of the application’s module or package. __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.We then use the route() decorator to tell Flask what URL should trigger our function.The function returns the message we want to display in the user’s browser. The default content type is HTML, so HTML in the string will be rendered by the browser.Save it as dupremover.py or something similar. Make sure to not call your application flask.py because this would conflict with Flask itself.

6. To run the application, use the flask command or python -m flask. You need to tell the Flask where your application is with the --app option.
      > flask --app dupremover run
      * Serving Flask app 'dupremover'
      * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
      
7. To enable debug mode, use the --debug option.

      > flask --app dupremover --debug run
      * Serving Flask app 'dupremover'
      * Debug mode: on
      * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
      * Restarting with stat
      * Debugger is active!
      * Debugger PIN: nnn-nnn-nnn

   
