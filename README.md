# MIMS Catalog
A search interface to the public catalogue of the Marine Information Management System.

The MIMS is funded by the Department of Forestry, Fisheries and the Environment.

## Deployment (back-end)

### Prerequisites
* Git
* Docker with Compose plugin

### New installation
Initialize the git repository:
```shell
git clone https://github.com/SAEON/mims-catalog.git --recurse-submodules
```
Create an environment config file:
```shell
cp .env.example .env
```
Edit `.env` and set URLs, secrets, etc, as applicable.

#### Generating secrets
Use the Python `secrets` module to create cryptographically strong secrets.
For example, in a Python console:
```python
>>> import secrets
>>> secrets.token_urlsafe()
'amDo7G_bhlyg4HhecG7neK231Wcb7pq7QvjPzDjwqyw'
```

### Upgrading an existing installation
Update the repository:
```shell
git pull --recurse-submodules
git submodule update --recursive
```
Check and update settings in the `.env` config file, as necessary.

### Build and run the MIMS catalogue
```shell
docker compose build
docker compose up -d
```

## Deployment (front-end)

### Prerequisites
* Nginx

### Web server setup
Nginx configuration example:
```nginx
upstream mims_catalog {
    server 127.0.0.1:4023;  # replace with back-end IP address
    keepalive 2;
}
server {
    ...
    location /mims/ {
        proxy_pass http://mims_catalog/;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header Connection "";
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Prefix /mims;
    }
}
```
