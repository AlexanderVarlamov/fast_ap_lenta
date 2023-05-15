from abc import ABC, abstractmethod

from controllers.actions import lenta_ru_news, news_ru_news, rambler_news


class NewsGetter(ABC):
    @abstractmethod
    async def get_news(self) -> list[str]:
        pass


class LentaNewsGetter(NewsGetter):
    async def get_news(self):
        return await lenta_ru_news()


class NewsRuGetter(NewsGetter):
    async def get_news(self):
        return await news_ru_news()


class RamblerGetter(NewsGetter):
    async def get_news(self):
        return await rambler_news()


class SourceNewsGetter:
    def __init__(self, source: NewsGetter):
        self.source = source

    async def __call__(self):
        return await self.source.get_news()
