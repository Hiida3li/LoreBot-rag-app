from fastapi import FastAPI, APIRouter, Depends
import os
from helpers.config import get_settings, Settings

base_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],

)