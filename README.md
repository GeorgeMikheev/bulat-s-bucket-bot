## How to use

To run:
`docker compose up -d`

Site available on 8000 port.

You can make any changes in code, they will appear automatically. If you want to execute something with manage.py use:

```sh
docker compose exec app python3 manage.py migrate
docker compose exec app python3 manage.py makemigrations
docker compose exec app python3 manage.py createsuperuser
```

and so on.
