# Website

* [Data survey form](http://chumpitazdiaz.com)

------------------------------------------------------------

## Built With

* [Vue JS](https://vuejs.org/) - Front end framework
* [BootstrapVue](https://bootstrap-vue.org/) - For templates
* [Vee validate](https://logaretm.github.io/vee-validate/) - Vue validations
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) -Python variables as html templates
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Used to serve as REST API server
* [Gunicorn](https://gunicorn.org) - Used to handle our HTTP server
* [NGINX](https://nginx.org/en/) - Used to handle our HTTP proxy server

------------------------------------------------------------

# Deploy on your computer

## Clone the repository
```
git clone https://github.com/luisdiaz1997/VueJS-works
cd UI-project
```

## Installation
Install miniconda in your system
https://docs.conda.io/en/latest/miniconda.html

Then create new environment

```
conda env create -f UI.yml
```

Activate the environment
```
conda activate UI
```
---------------------------------------
## Deployment

```
gunicorn --bind 0.0.0.0:5000 wsgi:app
```

---------------------------------------
