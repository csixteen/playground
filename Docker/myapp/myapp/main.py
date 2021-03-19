#!/usr/bin/env python3

import sys

import uvicorn  # type: ignore
from fastapi import APIRouter, Depends, FastAPI, Form, Request
from loguru import logger


logger.remove()
logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time:HH:mm:ss}</green> | {level} | <level>{message}</level>",
)

app = FastAPI()
router = APIRouter()


async def logging_dependency(request: Request):
    logger.debug(f"{request.method} {request.url}")

    logger.debug("Params:")
    for name, value in request.path_params.items():
        logger.debug(f"\t{name}: {value}")

    logger.debug("Headers:")
    for name, value in request.headers.items():
        logger.debug(f"\t{name}: {value}")


@router.get("/")
async def root():
    return { "message": "Hello, world" }


app.include_router(router, dependencies=[Depends(logging_dependency)])


def main():
    uvicorn.run("myapp.main:app", host="0.0.0.0", port=8000, reload=True, workers=2)


if __name__ == "__main__":
    main()
