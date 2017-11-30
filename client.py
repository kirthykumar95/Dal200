import argparse
import random
import os
import time

from tornado import websocket, web, ioloop
from pythonosc import osc_message_builder
from pythonosc import udp_client

class IndexHandler(web.RequestHandler):
    def get(self):
            self.render("index.html")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default = "127.0.0.1",
        help="The ip of the OSC server")

    parser.add_argument("--port", type = int , default = 5007,
        help = 'The port the OSC server is listening on')

    args = parser.parse_args()

    client = udp_client.SimpleUDPClient("127.0.0.1", 5007)

    for x in range(10):
        client.send_message("/DTDT", random.random())
        time.sleep(1)
