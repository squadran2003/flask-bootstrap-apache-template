## flask-bootstrap-apache-template
A base template with correct folder structure for a flask app,the template also has all the css files for twitter bootstrap, also included a wsgi file for deployment to a apache server.

## Motivation
  The idea for this template came from building a few flask web apps. I found it a bit tedious to recreate all the folders,html files etc. This template aims to also make deployment to a apache2 server easy. The one aspect of coding that made me want to pull my hair out was deployment. I hope this template and guide makes using and deploying flask apps easier for other developers.
  
## Example

```python

Folder Hiearchy

YourApp
   templates
   static
     css
      .css files
     js
       .js files
   app.py
   yourapp.wsgi

```

## Guide

1) Download the zip file and extract to the location of choice

2) Navigate to your YourApp/venv and edit the requirements.txt file to include the packages your app requires.

3) Rename the folder called YourApp to your app name.

4) Rename the .wsgi file to your app name, preferably in lowercase to the app name

For example lets say we had a folder called FlaskApp which holds all your flask apps on the server, and your app your are deploying was called TEST, your folder structure on the server should look like this once deployed.

```python

FlaskApp
  TEST
    static
    templates
    venv
    app.py (*** rename this to __init__.py when the folder is deployed to the server)
  test.wsgi

```  


5)Once your folder is deployed to the server, navigate to TEST/venv and type the
  command virtualenv.(the period represents the current directory) and will install all python dependencies in the venv folder. 

6)Still in the folder venv type the command source bin/activate which will activate the virtualenv.
  Then install all packages required by your app by running the command pip install -r requirements.txt.

7)Edit the test.wsgi file and change the commands as required  

The wsgi file for deploying this app would look like this if your app was called TEST.

```python

#!/usr/bin/python
import sys
import logging

activate_this = '/var/www/FlaskApp/TEST/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from TEST import app as application
application.secret_key = 'Add your secret key'

```

8) Next create a .conf file in your site-available folder by running the following command below.

```python

nano /etc/apache2/sites-available/TEST.conf  where TEST is the name of the app

```

####example content for the TEST.conf file

```python

<VirtualHost *:80>
		ServerName mywebsite.com
		ServerAdmin admin@mywebsite.com
		WSGIScriptAlias / /var/www/FlaskApp/test.wsgi
		<Directory /var/www/FlaskApp/TEST/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/FlaskApp/TEST/static
		<Directory /var/www/FlaskApp/TEST/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

```

9) then run the command a2ensite TEST.

10) Lastly we need to give apache access to the folders. navigate to
    
    /var/www/FlaskApp and type the command

    chown -R www-data:www-data TEST

11) run the command
  
    service apache2 reload

This should be all your need to deploy your app to a apache server.

