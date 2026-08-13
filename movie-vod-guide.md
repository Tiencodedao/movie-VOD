# Movie VOD - Project Setup

## PostgreSQL

- Host: localhost
- Port: 5432
- Database: vod_db
- Username: admin123
- Password: 12345678

## Django Admin

Tạo tài khoản:

```bash
python manage.py createsuperuser
```

Đăng nhập:

- URL: http://127.0.0.1:8000/admin
- Username: admin
- Password: admin123

## Chạy dự án

```bash
docker compose up -d
python manage.py migrate
python manage.py runserver
```