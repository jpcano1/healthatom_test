FROM python:3.10 AS base-image

WORKDIR /tmp

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.6.1 \
    POETRY_HOME="/opt/poetry" \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | python3 -

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export --only=main -f requirements.txt --output requirements.txt --without-hashes --without-urls
RUN poetry export --only=dev -f requirements.txt --output requirements-dev.txt --without-hashes

FROM python:3.10

COPY --from=base-image /tmp/requirements.txt ./requirements.txt
COPY --from=base-image /tmp/requirements-dev.txt ./requirements-dev.txt

# Upgrade pip version
RUN pip install -U -q pip

RUN pip install --no-cache-dir --disable-pip-version-check --progress-bar off -q -r requirements.txt

ARG ENV
RUN if [ "$ENV" = "dev" ] ; then pip install --no-cache-dir --disable-pip-version-check --progress-bar off -q -r requirements-dev.txt; fi

WORKDIR /app

COPY . .

ENTRYPOINT ["/bin/bash", "-l", "-c"]
