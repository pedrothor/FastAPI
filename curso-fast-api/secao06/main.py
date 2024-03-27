from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)



if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='127.0.0.1', port=8000, log_level='info', reload=True)

"""
Token: "
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzEyMDIxMzc1LCJpYXQiOjE3MTE0MTY1NzUsInN1YiI6IjIifQ.HfIGDiDSKrsjvYWeXVF3IkxyzdlPj76kNfNzdKoAbC0
"
Tipo: bearer




Token 2
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzEyMDI5Mjg3LCJpYXQiOjE3MTE0MjQ0ODcsInN1YiI6IjMifQ.AXCGtNgnqjF0RILYy82Ethj6eYdEtWmgNttj2y_N_E8
"""