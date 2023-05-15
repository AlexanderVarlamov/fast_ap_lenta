from controllers.news_classes import SourceNewsGetter
from controllers.sources_dict import sources


async def process_news_request(lst: list[str]) -> list:
    if lst == ['all']:
        news_to_get = sources.keys()
    else:
        news_to_get = [item for item in lst if item in sources.keys()]

    news_to_return = []
    for one_source in news_to_get:
        source_getter = sources[one_source]()
        news_getter = SourceNewsGetter(source_getter)
        news_from_source = await news_getter()
        news_to_return.append({one_source: news_from_source})

    return news_to_return
