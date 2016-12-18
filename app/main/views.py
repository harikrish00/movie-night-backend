from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import NameForm
from app import db
# from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    pass
