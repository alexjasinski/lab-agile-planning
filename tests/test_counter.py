import fakeredis

from app import create_app


def test_counter_starts_at_zero():
    client = create_app(fakeredis.FakeRedis(decode_responses=True)).test_client()
    assert client.get("/counter").get_json() == {"count": 0}


def test_counter_persists_after_restart():
    redis_db = fakeredis.FakeRedis(decode_responses=True)
    client = create_app(redis_db).test_client()
    client.post("/counter/increment")
    assert client.post("/counter/increment").get_json() == {"count": 2}

    restarted = create_app(redis_db).test_client()
    assert restarted.get("/counter").get_json() == {"count": 2}
