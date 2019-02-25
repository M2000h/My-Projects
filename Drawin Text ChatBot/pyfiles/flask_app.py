
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, json, Response
import messageHandler
from settings import *
import pickle
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'This is bot server'

@app.route('/', methods=['POST'])
def processing():
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        if data["group_id"] == <TYPE HERE GROUP_ID HERE>:
            return <TYPE HERE SECRET API KEY>


    #######################################################################################################################################################
    return 'ok'
    #######################################################################################################################################################







