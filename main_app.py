import os

import tornado.ioloop
import tornado.web
import tornado.log
from database import *

from jinja2 import \
 Environment, PackageLoader, select_autoescape

import psycopg2
import requests
import json

from os import environ


ENV = Environment(
    loader=PackageLoader('voiceapp', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),

)

def escapejs(val):
    return json.dumps(str(val))

def jsonvalue(val):
    return json.dumps(val)

ENV.filters['escapejs'] = escapejs
ENV.filters['jsonvalue'] = jsonvalue

class TemplateHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.conn, self.cur = connect_to_postgres()

    def render_template (self, tpl, context):
        template = ENV.get_template(tpl)
        context['page'] = self.request.path
        self.write(template.render(**context))

class MainHandler(TemplateHandler):
    def get(self):
        # insert_tasks = insertTask("feed the cat")
        # change_status = changeStatus(2)
        # remove_task = removeTask(self.cur)
        open_tasks = openTasks(self.cur)
        closed_tasks = closedTasks(self.cur)

        self.set_header(
            'Cache-Control',
            'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("index.html", {'open_tasks' : open_tasks, 'closed_tasks' : closed_tasks})

        # self.render_template("index.html", {'open_tasks' : open_tasks, 'closed_tasks' : closed_tasks, 'insert_tasks' : insert_tasks,\
        #  'change_status' : change_status, 'remove_task' : remove_task})

        self.cur.close()
        self.conn.close()

class StatusHandler(MainHandler):
    def post(self):
        data_object = tornado.escape.json_decode(self.request.body)
        print('Post data received')

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/status", StatusHandler),
        (r"/static/(.*)",
          tornado.web.StaticFileHandler,
          {'path': 'static'}
        ),
    ], autoreload=True)

if __name__ == "__main__":
    tornado.log.enable_pretty_logging()

    app = make_app()
    app.listen(int(os.environ.get('PORT', '8000')))
    tornado.ioloop.IOLoop.current().start()
