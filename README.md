# MIMS Catalog
A search interface to the public catalogue of the Marine Information Management System.

The MIMS is funded by the Department of Forestry, Fisheries and the Environment.

## Deployment: application server
N.B. The application server MUST NOT be web-facing.

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

## Deployment: proxy server
This is a web-facing server.

### Prerequisites
* Nginx

### Web server setup
Nginx configuration example:
```nginx
upstream mims_catalog {
    server APP_SERVER_IP:4023;  # replace with app server IP address
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

## Authorization: ODP server config
The MIMS catalogue requires two client configurations on the ODP server,
in order to access the ODP API.

### Anonymous API access
    Client id:            MIMS.Catalog.CI
    Client name:          MIMS Catalogue Client Interface
    Client secret:        <value for MIMS_CATALOG_CI_CLIENT_SECRET in .env>
    Collection-specific:  true
    Collections:          MIMS, SADCO
    Scope:                odp.catalog:read, odp.catalog:search, odp.vocabulary:read
    Grant types:          client_credentials

### User-authenticated API access
    Client id:                  MIMS.Catalog.UI
    Client name:                MIMS Catalogue User Interface
    Client secret:              <value for MIMS_CATALOG_UI_CLIENT_SECRET in .env>
    Collection-specific:        true
    Collections:                MIMS, SADCO
    Scope:                      odp.token:read, offline_access, openid
    Grant types:                authorization_code, refresh_token
    Response types:             code
    Redirect URIs:              https://SERVER_NAME/mims/oauth2/logged_in
    Post-logout redirect URIs:  https://SERVER_NAME/mims/oauth2/logged_out
