from fastapi import FastAPI

from views.views import routes

def get_app():
    app = FastAPI(title='important_news')
    app.include_router(routes, prefix='/v1', tags=["today's news"])
    return app

