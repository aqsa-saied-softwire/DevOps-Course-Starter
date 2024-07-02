FROM python:3 as base

RUN pip install poetry
COPY . /app
WORKDIR /app
RUN poetry install
EXPOSE 8000

FROM base as production
ENV FLASK_DEBUG=false
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0", "--port=8000"]

FROM base as development
ENV FLASK_DEBUG=true
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0", "--port=8000"]

FROM base as test
ENTRYPOINT poetry run pytest
