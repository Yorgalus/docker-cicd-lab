import os
import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(
    host=os.environ.get("REDIS_HOST", "redis"),
    port=6379,
    password=os.environ.get("REDIS_PASSWORD", ""),
)

@app.route("/")
def index():
    visites = r.incr("visites")
    return f"Nombre de visites : {visites}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
