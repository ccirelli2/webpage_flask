"""
References:
    Tutorial: https://flask.palletsprojects.com/en/2.0.x/tutorial/database/
"""
###############################################################################
# Import Libraries
###############################################################################
import os
import sys
from flask import Flask
from flask import render_template, url_for
import numpy as np
import pandas as pd


###############################################################################
# Declare Directories
###############################################################################
dir_base=r'/home/cc2/Desktop/repositories/webpage_flask/flask-tutorial/flaskr'
dir_app=os.path.join(dir_base, 'webpage_flask', 'flask-tutorial', 'flaskr')
dir_static=os.path.join(dir_app, 'static')
[sys.path.append(d) for d in [dir_base, dir_app]]

###############################################################################
# Import Modules
###############################################################################
import funct_table as f_table
import db

###############################################################################
# Import Modules
###############################################################################
def create_app(test_config=None):
    # Create & Configure App
    app=Flask(__name__, instance_relative_config=True,
              static_folder=dir_static)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        #load instance config
        app.config.from_pyfile('config.py', silent=True)
    else:
        #load the test config if passed in
        app.config.from_mapping(test_config)
    # ensure the folder exists
    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass
    # a simple page that says hello
    @app.route('/')
    def root_page():
        return '<h1>Welcome to the root page</h1>'
    # Example creating a table
    @app.route('/table')
    def pd_table():
        items=[f_table.Item('Name1', 'Description1')]
        #items=[dict(name='Name1', description='Description1')]
        table=f_table.ItemTable(items)
        return table.__html__()
    # Example Hello
    @app.route('/hello')
    def hello():
        return 'Hello World'
    # Nubia's Web Page
    @app.route('/NubiaCirelliRealEstate')
    def greeting():
        content_html='''
        <h1> Welcome to my real estate page!</h1>
        '''
        return content_html
    @app.route('/images')
    def img():
        return render_template("ex_template.html")

    # Create Database
    db.init_app(app)

    return app






