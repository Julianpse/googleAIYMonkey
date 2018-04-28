import os

import tornado.ioloop
import tornado.web
import tornado.log

from jinja2 import \
 Environment, PackageLoader, select_autoescape

import psycopg2

import aiy_voice_app.psycopg2


ENV = Environment(
    loader=PackageLoader('voiceapp', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

# These variables open the database connection
conn = psycopg2.connect("dbname='voice_monkey', user='voicemonkey' host='dcgroupproject.cszqs53dxn5e.us-east-2.rds.amazonaws.com' password='helloWorld'")
cur = conn.cursor()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        
def make_app():