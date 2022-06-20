# Django React Template
Just a proof of concept to integrate Django and React

## Concept
We use WebPack to build a django template. Webpack is configured to inject all dependancies these dependancies are built
into `frontend/static/dist` which is collected by python's `collectstatic`.

NB: We can update the build directory by setting the `BUILD_PATH` environment variable. So for example
if we want to build directly into the global static folder and not use `collectstatic` we'd set it to

```dotenv
BUILD_PATH=../static/dist
```
BUILD_PATH is reletive to the `/frontend` folder

## Running
When you run the python server `/` is configured to be the React app, so you can just.
`python manage.py runserver`
And it works.

But you will not have hot reload and all those frontend dev goodies. 
To get those you need to run the webpack dev server which is a matter of `yarn && yarn start`

