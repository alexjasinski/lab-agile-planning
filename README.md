# lab-agile-planning
## Counter service

Flask service that stores a counter in Redis (key `counter`), so the count survives restarts.

- `GET /counter` returns the current count
- `POST /counter/increment` increments it

Run: `pip install -r requirements.txt && python app.py` (env: `REDIS_HOST`, `REDIS_PORT`, `PORT`).
Test: `pip install -r requirements-dev.txt && pytest`
