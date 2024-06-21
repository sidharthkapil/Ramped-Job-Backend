# Ramped-Job-Backend

start-server:
	uvicorn app.main:app --reload

install-modules:
	pip install fastapi[all] fastapi-mail fastapi-jwt-auth[asymmetric] passlib[bcrypt] pymongo

Mongodb
    Require running mongodb server    