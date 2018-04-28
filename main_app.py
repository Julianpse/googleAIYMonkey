import os

import tornado.ioloop
import tornado.web
import tornado.log
from database import *

from jinja2 import \
 Environment, PackageLoader, select_autoescape

import psycopg2

import aiy_voice_app.psycopg2

from os import environ




ENV = Environment(
    loader=PackageLoader('voiceapp', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
    
)




class TemplateHandler(tornado.web.RequestHandler):
    def initialize(self):
        connect_to_postgres()

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