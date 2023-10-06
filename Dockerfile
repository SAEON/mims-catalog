FROM python:3.10

ARG CA_CERT_URL
RUN if [ -n "${CA_CERT_URL}" ]; then curl ${CA_CERT_URL} -k -o /usr/local/share/ca-certificates/saeon-ca.crt; fi
RUN if [ -n "${CA_CERT_URL}" ]; then update-ca-certificates; fi

WORKDIR /srv/mims-catalog
COPY odp-core odp-core/
COPY odp-ui odp-ui/
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY mims mims/

CMD ["gunicorn", "mims.ui.catalog:create_app()", "--bind=0.0.0.0:4023", "--workers=4"]
