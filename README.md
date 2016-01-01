# flask-bootstrap-apache-template
A base template for flask app with all the css files included for twitter bootstrap, also included a wsgi file for deployment to a apache server.

##Motivation
  The idea for this template came from building a few flask web apps. I found it a bit tedious re creating all the folders,html files etc. This template aims to also make deployment to a apache2 server easy.
  
## Example

```python
Folder Hiearchy

templates
static
  css
    .css files
  js
    .js files
app.py
flaskapp.wsgi

```

## Guide

1) The folders are setup to so you can follow the below tutorial. See link below
 https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
 This tutorial will help with deploying your app to a apache2 server.

## Useful Tips
1) Remember to make www-data the owner and group for your app folder and any other folders there after.
   you can do this with the command chown www-data:wwwdata /var/www/yourappfolder 