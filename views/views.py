from fastapi import APIRouter, HTTPException

from models.models import NewsTypeRequestModel, NewsReturnModel
from controllers.req_processors import process_news_request
from controllers.sources_dict import sources

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
