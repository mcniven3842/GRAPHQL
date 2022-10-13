# TP2 GRAPHL

## Info
The project consists of 4 services, the services are:
* [movie]
* [showtime]
* [booking]
* [user]

The files inside the folder are:

*[Main server file (*.py)]
*[Dockerfile to build service image]
*[Python library requirements (requirements.txt)]
*[data folder with the .json file that holds the service data]
*[Resolver.py]
*[movie.graphql]
## Technologies
***
* [Python]: Version 3.10 
* [Docker]

# Clone this project
$ git clone https://github.com/MohammedAymane/UE-AD-A1-REST

# Access
$ cd ue-ad-a1-rest

# Install dependencies
$ pip -r requirements.txt

# Run a specific microservice (movie for example)
$ cd movie
$ python movie.py
$ pymon movie.py (in developpment mode)


# The movie service will initialize in the <http://localhost:3200>
```
## :checkered_flag: Containerizing the application ##
```bash
# Creating the containers
$ cd movie
$ docker build .

# Running the containers
$ cd UE-AD-A1-REST
$ docker-compose up
