from fastapi import APIRouter

from .ping import router as ping_router

v0 = APIRouter(prefix="/v1")

v0.include_router(ping_router, prefix="/ping")
