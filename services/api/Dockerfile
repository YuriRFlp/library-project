
# =============================================================================
# BASE - Python e dependências
# =============================================================================
FROM python:3.9 AS base
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip && pip install poetry
WORKDIR /code
COPY pyproject.toml poetry.lock /code/
RUN poetry config virtualenvs.create false

# =============================================================================
# dev - Instala dependências de dev e copia o código fonte
# =============================================================================
FROM base AS dev
RUN poetry install --no-root
COPY . /code/

# =============================================================================
# CodeFmt - verifica se o código segue o estilo black
# =============================================================================
FROM dev AS CodeFmt
RUN black --check --diff .
