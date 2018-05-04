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
    def post(self):
        insert_task_input = self.get_body_argument('task_input')
        if insert_task_input:
            insertTask(insert_task_input)
            self.redirect(r"/success")
        else:
            self.redirect(r"/error")


    def get(self):
        open_tasks = openTasks(self.cur)
        closed_tasks = closedTasks(self.cur)

        self.set_header(
            'Cache-Control',
            'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("index.html", {'open_tasks' : open_tasks, 'closed_tasks' : closed_tasks})

        self.cur.close()
        self.conn.close()


class DeleteHandler(MainHandler):
    def post(self):
        delete_object = int(tornado.escape.json_decode(self.request.body))
        removeTask(delete_object)
        print('Delete data received' + str(delete_object))



class StatusHandler(MainHandler):
    def post(self):
        data_object = int(tornado.escape.json_decode(self.request.body))
        changeStatus(data_object)
        print('Change data received' + str(data_object))



class ErrorHandler(TemplateHandler):
    def get (self):
        self.set_header(
            'Cache-Control',
            'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("error.html", {})



class SuccessHandler(TemplateHandler):
    def get (self):
        self.set_header(
            'Cache-Control',
            'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("success.html", {})



def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/status", StatusHandler),
        (r"/deleted", DeleteHandler),
        (r"/error", ErrorHandler),
        (r"/success", SuccessHandler),
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
