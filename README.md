# spa-flask-vue

My repo when I worked through Testdriven.io's article, [Developing-a-single-page-app-with-flask-and-vuejs](https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/?utm_source=realpython).

Article: [Source Repo](https://github.com/testdrivenio/flask-vue-crud)

-----

### Developing a Single Page App with Flask and Vue.js

### Want to learn how to build this?

Check out the [post](https://testdriven.io/developing-a-single-page-app-with-flask-and-vuejs).

## Want to use this project?

1. Fork/Clone

1. Run the server-side Flask or Fastapi app in one terminal window:
    
    ### Fastapi
    ```sh
    $ cd fastapi
    $ pipenv --python 3.7
    $ pipenv shell
    $ pipenv install
    (fastapi)$ ./start.sh
    ```
    ### Flask
    ```sh
    $ cd flask
    $ pipenv --python 3.7
    $ pipenv shell
    $ pipenv install
    (flask)$ ./start.sh
    ```

    Navigate to [http://localhost:5000](http://localhost:5000)

1. Run the client-side Vue app in a different terminal window:

    ```sh
    $ cd client
    $ yarn install
    $ yarn serve
    ```

    Navigate to [http://localhost:8080](http://localhost:8080)
