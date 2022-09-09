Worldwide mortality dashboard
===

## Heroku App
The repository is associated with an application deployed on Heroku at the following adress : [https://mortality-dashboard.herokuapp.com/visualization/graphs](https://mortality-dashboard.herokuapp.com/visualization/graphs).

## Content of the repository

**The app is composed of several python files. app.py is the main one, and other scripts are pages called by it.**

app.py - Main script
pages folder - Accompagning scripts
assets - Store accessory files
- Data - Storage of the data called by the app
- Github logo to illustrate the app

Procfile, requirements.txt are files required to run the app on the heroku server.

## Content of the App

The dasboard has been created based on the data collected in the context of the WHO's mortality database. 

**The main components are a worlwide map, and line graphs.**
The map allows the comparision between the countries of the age-standardized death rate. One can also select a type of cause to compare the countries different profiles.
The line graphs are more free. They can be controlled by a diversity of options (sex, age group, country, world region, year). One shows the evolution of the death rate depending on the time, and the other depending of the age group.
