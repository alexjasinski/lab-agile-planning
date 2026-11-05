import os

import redis
from flask import Flask, jsonify

COUNTER_KEY = "counter"


def create_app(redis_client=None):
    app = Flask(__name__)
    store = redis_client or redis.Redis(
        host=os.environ.get("REDIS_HOST", "localhost"),
        port=int(os.environ.get("REDIS_PORT", "6379")),
        decode_responses=True,
    )

    @app.get("/counter")
    def get_counter():
        return jsonify(count=int(store.get(COUNTER_KEY) or 0))

    @app.post("/counter/increment")
    def increment():
        return jsonify(count=store.incr(COUNTER_KEY))

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
