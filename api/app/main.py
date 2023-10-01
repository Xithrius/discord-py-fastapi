from fastapi import FastAPI
from loguru import logger as log
from prisma import Prisma

from .routers import v0

app = FastAPI()
app.include_router(v0)
prisma = Prisma(auto_register=True)


@app.on_event("startup")
async def startup_event() -> None:
    log.info("Startup event triggered.")

    await prisma.connect()


@app.on_event("shutdown")
async def shutdown_event() -> None:
    log.info("Shutdown event triggered.")

    if prisma.is_connected():
        await prisma.disconnect()
