from stem import Signal
from stem.control import Controller
import requests
import time
import socks
import socket


with Controller.from_port(port = 9051) as controller:
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket
    controller.authenticate()
    while True:
        print("Success!")
        controller.signal(Signal.NEWNYM)
        print("New Tor connection processed")
        p=requests.get("https://internetpositif.neocities.org/")
        print(p.status_code)
        time.sleep(controller.get_newnym_wait())
