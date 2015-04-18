#!/usr/bin/env python

from flask import Flask
import socket,redis,os

r=redis.Redis(host=os.getenv("REDIS_PORT_6379_TCP_ADDR"),port=os.getenv("REDIS_PORT_6379_TCP_PORT"))
r.set("count",0)

app = Flask(__name__)

@app.route("/")
def index():
    r.incr("count")
    return "Visit number %d\nHostname: %s\n" % (int(r.get("count")),socket.gethostname())

if __name__ == "__main__" :
    app.run(host="0.0.0.0")
