from python:3.8.2-slim

ENV djangoSERVERLESS /app
WORKDIR ${APP_HOME}

COPY . ./

RUN pip install pip --upgrade
RUN  djangoSERVERLESS install --skip-lock --system --dev
RUN chmod +x ./scripts/entrypoint.sh

CMD ["./scripts/entrypoint.sh"]