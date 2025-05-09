from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings, Settings
from controllers import DataController


data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],

)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile,
                            app_settings: Settings=Depends(get_settings)):

     # validate the file properities                  
    
    is_valide, result_signal =  DataController().validate_upload_file(file=file)

    if not is_valide:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": result_signal
            }


        )

                             