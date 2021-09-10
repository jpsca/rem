# Relationship Management

A *Proper* web application for making friends, not just contacts.


## Installation

1. Create a virtualenv and activate it
2. `make setup`
3. Run with `make run`


## Manage requirements

This project uses [pip-tools](https://github.com/jazzband/pip-tools/) to manage its requirements and pin them to specific versions. Using the specific versions of the libraries that we know work, makes our builds are predictable and deterministic.

### To add a new requirement

1. Edit the `requirements/requirements.ini` file and add a new requirement to the list (e.g. `rq`).
  You can optionally add constraints to which versions are acceptable, e.g.: `rq <3.0`
2. Run `make reqs`

### To upgrade a requirement

To upgrade a requirement to its latest version run:

`pip-compile --upgrade-package NAME requirements/requirements.ini`


Person \
  first_name:string-100 \
  middle_name:string-100:nullable \
  last_name:string-100:nullable \
  nickname:string-100:nullable \
  birthdate:date:nullable \
  estimated_age:string-20:nullable \
  contact_info:ContactInfo:person \
  addresses:Address:person \
  relations:Relation:person

(type = URL,phone,email)
ContactInfo \
  name:string-100 \
  type:string-10 \
  value:string-100

Address \
  name:string-100 \
  country:string-20 \
  region:string-20 \
  value:text person_id:integer:foreign-users.id

Relation \
  name:string-100 \
  value:string-100 \
  person_id:integer:foreign-users.id \
  rel_person_id:integer:foreign-users.id
