from fastapi import APIRouter, HTTPException
from starlette.responses import HTMLResponse

from models.models import NewsTypeRequestModel, NewsReturnModel, RawNewsReturnModel
from controllers.req_processors import process_news_request, process_raw_news_request
from controllers.sources_dict import sources
from conf import port

routes = APIRouter()


@routes.post(
    '/getnews',
    response_model=NewsReturnModel,
    status_code=200
)
async def get_last_news(item: NewsTypeRequestModel) -> NewsReturnModel:
    news = await process_news_request(item.sources)
    print(news)
    if news:
        return NewsReturnModel(news=news)
    else:
        raise HTTPException(status_code=422,
                            detail=f'Такой опции не предусмотрено. Допустимые источники: {sources.keys()}, либо all')


@routes.get(
    "/",
    status_code=200,
    response_class=HTMLResponse
)
async def start_page():
    return f'''
    <h2>There is no frontend yet</h2>
    <body>
    Please, use the <a href="http://127.0.0.1:{port}/docs">Swagger</a>
    </body>'''


@routes.post(
    '/getnews_raw',
    response_model=RawNewsReturnModel,
    status_code=200
)
async def get_raw_last_news(item: NewsTypeRequestModel) -> RawNewsReturnModel:
    news = await process_raw_news_request(item.sources)
    print(news)
    if news:
        return RawNewsReturnModel(news=news)
    else:
        raise HTTPException(status_code=422,
                            detail=f'Такой опции не предусмотрено. Допустимые источники: {sources.keys()}, либо all')
