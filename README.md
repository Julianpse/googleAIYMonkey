# googleAIYMonkey
Digital Crafts Project 1 - Modifying google assistant API

MVP Goals

1. Have Google assistant recognize custom voice commands 
and complete specific scripts based on the commands given.
2. Have Google assistant connect to and modify the database.
3. Have a front end web interface connected to the database displaying a to-do list.

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Stretch Goals
1. Have Google assistant recognize custom commands to modify specific users data.
2. Allow modification of database from front end.
3. Add more functionality aside from to-do app ( create dashboard of user interests such as sports teams followed, scores, etc.)

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

GitHub project URL:

https://github.com/Julianpse/googleAIYMonkey

To install/run the app you can fork the project listed above to a Google AIY voice
kit, and go to the live Heroku deployment at:

http://voice-monkey.herokuapp.com/

In order to add data to the database you will need a Google AIY voice kit running
the aiy_voice_app.py

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Tools Used:

PostgreSQL, Tornado/Python, Jinja, Psycopg2, HTML, CSS, Javascript, jQuery, Heroku, Google Assistant API, Google AIY, Voice Kit


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Challenges/Lessons Learned:

We accidentally pushed our credentials files into GitHub, fortunately it was
very early in the project so we were able to rebuild the repo easily and set
custom git ignore information.

Managing access to the .env file remotely across a team.

Utilizing pip files to get dependencies for all users was very helpful once
we remembered it was there to help us.

Manipulating data into multiple TYPE formats from the database through to the front end.

jQuery manipulation of database data through tornado proved to be a big challenge
that Julian kicked in the face.

Utilizing a hardware component ate up a lot of time. The raspberry pi was fun to work
with but presented a lot of roadblocks along the way, often stemming from us having the 
pi zero which we were unable to get a GUI interface running on. We had to interface with
the device solely through command line and nano. 

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Team Members
Julian Se, Bobby Neelon, Nick Schmidt, Dalton