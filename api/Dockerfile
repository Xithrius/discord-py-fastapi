FROM python:3.11 as builder

RUN pip install -U pip setuptools wheel
RUN pip install pdm

COPY pyproject.toml pdm.lock /project/
COPY app/ /project/app

WORKDIR /project
RUN mkdir __pypackages__ && pdm sync --prod --no-editable

FROM python:3.11

ENV PYTHONPATH=/project/pkgs
COPY --from=builder /project/__pypackages__/3.11/lib /project/pkgs

COPY --from=builder /project/__pypackages__/3.11/bin/* /bin/

COPY prisma/ /project/prisma

ENTRYPOINT ["/bin/bash", "-c"]
CMD ["prisma db push --schema project/prisma/schema.prisma --accept-data-loss && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
