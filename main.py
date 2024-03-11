from flask import Flask
from flask import request, redirect
from json import dumps

app = Flask('PIDOR')

@app.route('/')
def check():
    hdrs = request.headers
    args = request.args
    ip = request.remote_addr
    user_agent = request.user_agent
    cookies = request.cookies
    print("\n\n===========================================\n\n")
    print(f"REQUEST IP - {ip}\nUser-Agent - {user_agent}", flush=True)

    print("HEADERS:", flush=True)
    for hdri, hdr in hdrs.items():
        print(f'\t{hdri}: {hdr}', flush=True)

    print("ENVIRON", flush=True)
    for hdri, hdr in request.environ.items():
        print(f'\t{hdri}: {hdr}', flush=True)

    print("DATA" + request.data.decode(), flush=True)

    print(f"AUTORIZATION: {request.authorization}", flush=True)
    print(f'REMOTE USER: {request.remote_user}', flush=True)


    return "STH"




app.run('0.0.0.0', 80)
