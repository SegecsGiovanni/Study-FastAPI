from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router

app = FastAPI(title="Curso API - Segurança")
app.include_router(api_router, prefix=settings.API_V1_STR)



if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level='info', reload=True)


"""
Token (bearer):
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzY0MTE2NzQ5LCJpYXQiOjE3NjM1MTE5NDksInN1YiI6IjIifQ.ab5uX6f0m2Pi4Hn6trwMBZfXyXMCBuKD1soUrOQletE

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzY0MjA1NTM1LCJpYXQiOjE3NjM2MDA3MzUsInN1YiI6IjMifQ.HMdmWrA1LUENMGfxNwBOiDJTHIO4WDLf84TxxmH6pbs
"""