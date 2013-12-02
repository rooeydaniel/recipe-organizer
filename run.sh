#!/bin/bash

django-admin.py collectstatic --noinput --pythonpath=$PWD --settings=project.settings.test
django-admin.py runserver 0.0.0.0:8001 --pythonpath=$PWD --settings=project.settings.test