"""
version 
@author varlamov.a
@email varlamov.a@rt.ru
@date 29.05.2023
@time 9:35
"""
from unittest.mock import MagicMock

import aiohttp
import pytest
from fastapi import HTTPException
import os

os.chdir('..')
import models as m
import controllers as c
import views as v



@pytest.mark.asyncio
class TestNews:
    async def test_unexisting_source(self):
        with pytest.raises(HTTPException):
            item = m.NewsTypeRequestModel.parse_raw('{"sources": ["wrong_source"]}')
            await v.get_last_news(item)

    async def test_lenta_ru(self):
        news_title = 'Джордж Байден выпил 500 граммов "Крота" и записался в реюнион группы На-На'
        item = m.NewsTypeRequestModel.parse_raw('{"sources": ["lenta_ru"]}')
        mock = aiohttp.ClientSession
        mock.get = MagicMock()
        mock.get.return_value.__aenter__.return_value.text.return_value = f"""
            <?xml version="1.0" encoding="UTF-8"?>
            <rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
                <channel>
                    <language>ru</language>
                    <title>Lenta.ru</title>
                    <description>Новости, статьи, фотографии, видео. Семь дней в неделю, 24 часа в сутки.</description>
                    <link>https://lenta.ru</link>
                    <item>
                        <guid>https://lenta.ru/news/2023/05/29/podpisal/</guid>
                        <author>Александр Варламов</author>
                        <title>{news_title}</title>
                    </item>
                </channel>
            </rss>
  """
        print('\n', item)
        res = await v.get_last_news(item)
        assert res.news == [{'lenta_ru': [f'{news_title}']}], "Получение новостей с lenta_ru не работает"

    async def test_news_ru(self):
        pass

    async def test_rambler_ru(self):
        news_title = 'Филипп Киркоров объявил о регистрации брака с Юрием Хованским'
        item = m.NewsTypeRequestModel.parse_raw('{"sources": ["rambler"]}')
        mock = aiohttp.ClientSession
        mock.get = MagicMock()
        mock.get.return_value.__aenter__.return_value.text.return_value = f"""
                  <?xml version="1.0" encoding="UTF-8"?>
                  <rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
                      <channel>
                          <language>ru</language>
                          <title>Lenta.ru</title>
                          <description>Новости, статьи, фотографии, видео. Семь дней в неделю, 24 часа в сутки.</description>
                          <link>https://lenta.ru</link>
                          <item>
                              <guid>https://lenta.ru/news/2023/05/29/podpisal/</guid>
                              <author>Александр Варламов</author>
                              <title>{news_title}</title>
                          </item>
                      </channel>
                  </rss>
        """
        print('\n', item)
        res = await v.get_last_news(item)
        assert res.news == [{'rambler': [f'{news_title}']}], "Получение новостей с rambler не работает"

