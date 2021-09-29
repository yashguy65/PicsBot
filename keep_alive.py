from flask import Flask, redirect
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Your bot is alive!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()

@app.route('/invite')
def invite():
    return redirect('https://discord.com/api/oauth2/authorize?client_id=890910438710198292&permissions=0&scope=bot%20applications.commands')

