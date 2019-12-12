#!/bin/bash

# sets the different Aliases being you can use
alias runweb="python manage.py runserver"
alias mm="python manage.py makemigrations"
alias migrate="python manage.py migrate"

# activates the venv

# if [[ == ${VIRTUAL_ENV}  ]] "*Software-Development-Project/env" 
# then
#     source  ../env/bin/activate
# else
#     echo "venv already active"
# fi
# runs migrations saves any changes made to the db from current user
# mm & migrate

# # freezes the current packages installed on the venv in by updating the requirements.txt files
# echo 'updating the requirements.txt'
# pip freeze > requirements.txt

# # run a git pull
# echo "Run a git pull"

# # run migrations made by other users.
# echo "then ensure the db is up to date by running 'mm & migrate' "
