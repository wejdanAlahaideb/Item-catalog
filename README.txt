Item catalog project contains:-
•	templates folder: contains all html pages
•	static folder: contain Style sheet for wbsite
•	catalogDB_setup.py: code responsible to setup and create database 
•	database_seeder.py: code responsible to seed database with categories to be used by users to added items
•	catalogApp.py: code responsible to fetch records from new database
•	client_secrets.json: contains the Google API credentials  required for login and logout through Google

Instructions:-
1.	Clone vagrant machine from repository: git clone https://github.com/udacity/fullstack-nanodegree-vm/tree/master/vagrant 
2.	Navigate to vagrant folder
3.	Run vagrant up
4.	Run vagrant ssh
5.	Run cd /vagrant/catalog
6.	Clone project repository using: git clone https://github.com/wejdanAlahaideb/Item-catalog.git
7.	To create database and seed it: Run python database_seeder.py
8.	To open Item catalog website run: python catalogApp.py
9.	From your browser visit: http://localhost:5000/ 

Note:
I have used Bootstrap template for styling website from: https://www.w3schools.com/bootstrap/bootstrap_templates.asp 
