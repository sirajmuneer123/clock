# Clock Test Application
 
## Installation Steps

* clone repo
* create virtual environment 
    ``` javascript
        $> virtualenv <folder_name> -p python3
        $> cd <folder_name>
        $> source bin/activate
    ```
* install all requirement by typing
     ``` javascript
        $> pip install -r requirement.txt
        $> python manage.py migrate
        $> python manage.py createsuperuser
    ```
    this commoan prompt for username, email and password, give valid entries..
    then run
    
    ``` javascript
        $> python manage.py runserver
    ```

    then follow the url  [Click Here](http://127.0.0.1:8000)