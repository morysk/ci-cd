from flask import Flask
import redis
import os  

app = Flask(__name__)

# connect to redis (configurable)
redis_host = os.environ.get('REDIS_HOST', 'localhost')
client = redis.Redis(host=redis_host, port=6379)

# stage 1: Route for welcome message
@app.route('/')
def welcome():
    return "Welcome to my App!"

#stage 2: Route for visitor count and increment message
@app.route('/count')
def count():
    count = client.incr('visitor_count')
    return f'You are Visitor number: {count}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
