import os

import tornado.ioloop
import tornado.web
import tornado.log

from jinja2 import \
 Environment, PackageLoader, select_autoescape

import psycopg2

import aiy_voice_app.psycopg2

from os import environ

# Global vars below
  
username = environ.get('DATABASE_USERNAME', None)
access_key = environ.get('DATABASE_PASS', None)
database_endpoint= environ.get('DATABASE_ENDPOINT', None)


ENV = Environment(
    loader=PackageLoader('voiceapp', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
    
)

# These variables open the database connection
conn = psycopg2.connect("dbname='{}', user='voicemonkey' host='{}' password='{}'".format(username, password))
cur = conn.cursor()


class TemplateHandler(tornado.web.RequestHandler):
    def initialize(self):
        try:
            conn
            cur
        except:
            print("I am unable to connect to the database, please check your connection")

    def render_template (self, tpl, context):
        template = ENV.get_template(tpl)
        context['page'] = self.request.path
        self.write(template.render(**context))

class MainHandler(TemplateHandler):
    def get(self):
        self.set_header(
            'Cache-Control',
            'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("", {})

        
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (
          r"/static/(.*)",
          tornado.web.StaticFileHandler,
          {'path': 'static'}
        ),
    ], autoreload=True)

if __name__ == "__main__":
    tornado.log.enable_pretty_logging()

    app = make_app()
    PORT = int('8000')
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()