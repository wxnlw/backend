# LB1

## Structure

```text
backend/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── services/
│   │   └── database_info_service.py
│   └── dto/
│       ├── server_info.py
│       ├── client_info.py
│       └── database_info.py
├── .env.example
├── requirements.txt
└── README.md
```

## Run Without Docker

1. Create and activate a virtual environment.
2. Install dependencies.
3. Create `.env` from `.env.example`.
4. Start the app.

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
copy .env.example .env
python -m uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```

## API Check

```bash
curl http://localhost:8080/info/server
curl http://localhost:8080/info/client
curl http://localhost:8080/info/database
```

### Unsafe User-Agent Check

```bash
curl -i -H "User-Agent: <script>alert(1)</script>" http://localhost:8080/info/client
```
