# StudioGhibliMovieList:
An application to demonstrate caching and locust tests

## What is the purpose?
The purpose is to demonstrate and introduce caching with redis, so that every user can access the data that's no older than 1 min.

## Statistics:
- Since NGINX is not optimised, the system can currently take on only a default value of **500** people
- Redis is programmed to invalidate it's cache every 45 secs.

## How to run the application:
1. Use docker, and install docker first :) 
2. `docker-compose up` will start redis, django and nginx
3. You can access the movies list using `http://127.0.0.1:8000/movies/`
4. A basic HTML UI will be waiting for you, Django templating is used.

## How to run Locust tests:
My favorite bit :tada:
1. `pip install locust`
2. `cd locust/` 
3. Start locust by `locust` 
4. nginx/web/redis should be up and running
5. Log in to `http://127.0.0.1:8089/` and set the number of users to 500 and the relative fields.
6. Let locust do it's thing 

Note: (the api had a failrate of %3 while I was checking, most of them are 499 or 301's. the 499 are most probably due to locust configurations, and 301 due to nginx configurations)

## Improvements:
- Should mess and optimise the nginx conf
- Should tweak locust as well
- Fill in unit tests 
