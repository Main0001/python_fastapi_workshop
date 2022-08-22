from fastapi import FastAPI
from .api import router


tags_metadata = [
    {
        'name': 'auth',
        'description': 'Авторизация и регистрация'
    },
    {
        'name': 'operations',
        'description': 'Операции'
    },
    {
        'name': 'reports',
        'description': 'Отчеты'
    },
]


app = FastAPI(
    title='First project (workshop)',
    description='description',
    version='1.0.0',
    openapi_tags=tags_metadata
)
app.include_router(router)



# @app.get('/')
# def root():
#     return {"message": "Hello"}