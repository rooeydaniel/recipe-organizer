===============================================
Dojo Dev Camp - Recipe Organizer
===============================================

Create a searchable Web application for recipes.  If times allows, this Web application will integrate with Yummly.com to allow for a more broad range of recipe searching.

Inspiration for the project - https://onetsp.com/

Deploying to Heroku
-------------------
- Create a new heroku account at heroku.com
- Open up your terminal
- Run the following commands

```
cd /path/to/your/repository
heroku create # this will create a new heroku app and attach it as a remote repository
# You could also say - heroku create [NAME]
```

- Copy the heroku app domain to the ALLOWED_HOSTS array in project/settings/test.py

```
git commit -a -m "Updating ALLOWED_HOSTS for new Heroku domain" project/settings/test.py
git push heroku master
heroku open # run this once the previous command finishes, it may take a minute
```