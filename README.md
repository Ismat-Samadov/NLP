# home-price-predicition

## Deployment to Heroku Instructions (Heroku Git)
1.  Sign up for a free heroku account if you havent already done so
2.  Create app ie. myapp #name of app
3.  Type heroku login --> This will take you to a web based login page
4.  cd to your directory on your local drive
5.  Type 'git init'
6.  Type 'heroku git:remote -a home-price-predicition'
7.  Type 'git add .'
8.  Type ' git commit -am "version 1"'
9.  Type 'git push heroku master'
10. Now you need to allocate a dyno to do the work. Type 'heroku ps:scale web=1'
11. If you want to check the logs to make sure its working type 'heroku logs --tail'
12. Now your code will continue to run until you stop the dyno. To stop it scale it down using the command 'heroku ps:scale worker=0'
---------------
---------------