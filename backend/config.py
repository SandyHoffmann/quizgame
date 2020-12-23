from flask import Flask, jsonify, request, send_file
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import func, update
import random
app = Flask(__name__)
arquivobd = "/quiz.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from datetime import datetime
import hashlib