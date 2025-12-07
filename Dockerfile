FROM python:3.13-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl gcc && rm -rf /var/lib/apt/lists/*

ENV POETRY_VERSION=2.2.1
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

ENV POETRY_VIRTUALENVS_IN_PROJECT=true

WORKDIR /build

# Metadata first
COPY pyproject.toml poetry.lock* ./
COPY README.md ./

RUN poetry install --no-root

COPY fifteen ./fifteen
COPY tests ./tests


FROM python:3.13-slim AS runtime

WORKDIR /app

COPY --from=builder /build/.venv /app/.venv
COPY --from=builder /build/fifteen ./fifteen

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1

CMD ["python", "fifteen/run.py"]
