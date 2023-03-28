# STARTUP STEPS

You should first make sure you have Python installed on your computer. Refer to the official [python](https://www.python.org/) website for more info.

## TL;DR

```shell
# Clone the repo
git clone https://github.com/Di-void/e-lib.git e-library

# Enter project directory
cd e-library

# Install pipenv:
pip install pipenv

# Install dependencies
pipenv install

# Activate virtualenv
pipenv shell

# Run migrations
py manage.py makemigrations
py manage.py migrate

# Run application
py manage.py runserver
```

## DEVELOPER GUIDE

### SETTING UP THE ENVIRONMENT

Please use the default terminal for your respective operating systems e.g (**cmd** for **windows**).

**_PS: Make sure you have cloned the repo before going on._**

For this project, we used the `pipenv` package for managing our virtual environments as it is easier to use. To get started, run the following command to ensure you have `pipenv` installed.

```shell
pip install pipenv
```

After that, you should have `pipenv` installed on your local. Now you can simply run:

```shell
pipenv install
```

## CREATING THE ADMIN USER

For and admin user, to gain access to the admin interface, a "superuser" first needs to be created. You can create the admin user by running the following command on the root directory of the project in the terminal:

```shell
py manage.py createsuperuser
```

This would install all the project's dependencies needed as specified by the `Pipflie` into a virtual environment on your computer. This is where all your dependencies would live.

To activate this project's virtualenv, run:

```shell
pipenv shell
```

After running the above, you should be able to run any django-admin related commands using the manage.py file like running migrations and so on.

To exit the shell, run:

```shell
exit
```
