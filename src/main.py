import os
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status

from src.models.pydantic import ResultsAverageResponseModel, TimeRangeParams
from src.operations.get_results_average import GetResultsAverage

DEBUG = os.getenv("SUPERBENCHMARK_DEBUG", "True").lower() == "true"
app = FastAPI()


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


@app.get("/results/average", response_model=ResultsAverageResponseModel)
async def get_average():
    if not DEBUG:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="This feature is not ready for live yet",
        )

    return GetResultsAverage().execute()


@app.get(
    "/results/average/{start_time}/{end_time}",
    response_model=ResultsAverageResponseModel,
)
async def get_average_in_window(time_range: Annotated[TimeRangeParams, Depends()]):
    if not DEBUG:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="This feature is not ready for live yet",
        )

    return GetResultsAverage(
        start_time=time_range.start_time, end_time=time_range.end_time
    ).execute()
