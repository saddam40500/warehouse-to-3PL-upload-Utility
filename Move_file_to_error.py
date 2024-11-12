from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from configparser import ConfigParser
from datetime import datetime, timedelta
import csv
#from csv import delimiter, quotechar
import pandas as pd
import os
import shutil
import openpyxl
app = Flask(__name__)
socketio = SocketIO(app)
CORS(app)


Base_dir = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(Base_dir, 'uploads')
Input_folder = os.path.join(UPLOAD_FOLDER, 'Input')
Backup_folder = os.path.join(UPLOAD_FOLDER, 'Backup')
Archives_folder = os.path.join(UPLOAD_FOLDER, 'Archives')
Error_folder = os.path.join(UPLOAD_FOLDER, 'Error')
ALLOWED_EXTENSIONS = {'xls', 'xlsx'}
app.config['UPLOAD_FOLDER'] = Archives_folder

def move_error_file(filename):
    #rename filename by adding current date & time
    current_date = datetime.now().strftime("%Y%m%d")
    print(current_date)
    current_time = datetime.now().strftime("%H%M%S")
    print(current_time)
    #new_filename should be filename without extension + current date + current time
    new_filename = filename.split('.')[0] + "_" + current_date + "_" + current_time + "." + filename.split('.')[1]
    print(new_filename)
    current_file = os.path.join(Input_folder, filename)
    #move file to Error folder
    shutil.move(current_file, Error_folder)
    #rename file
    os.rename(os.path.join(Error_folder, filename), os.path.join(Error_folder, new_filename))
    print("File moved to Error folder")


def move_file_backup(filename,allocation_number):
    new_filename = filename.split('.')[0] + "_" + allocation_number + "." + filename.split('.')[1]
    print(new_filename)
    current_file = os.path.join(Input_folder, filename)
    print(current_file)
    #move file to Error folder
    shutil.move(current_file, Backup_folder)
    #rename file
    os.rename(os.path.join(Backup_folder, filename), os.path.join(Backup_folder, new_filename))
    print("File moved to Backup folder")

move_file_backup("Upload 1.xlsx","16824")