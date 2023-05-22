import aiohttp

from arsenic import get_session
from arsenic.browsers import Chrome
from arsenic.services import Chromedriver
from rss_parser import Parser

from conf import chromedriver_path

async def get_xml_with_chrome(rss_url):
    browser = Chrome()
    browser.capabilities = {
        "goog:chromeOptions": {"args": ["--headless",
                                        "--disable-gpu",
                                        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"]}
    }
    async with get_session(Chromedriver(binary=chromedriver_path), browser) as session:
        await session.get(rss_url)
        content = await session.get_page_source()

    return content


async def get_xml(rss_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=rss_url, ssl=False) as response:
            xml = await response.text()
    return xml


def parse_rss(xml):
    parser = Parser(xml=xml)
    feed = parser.parse()
    return [item.title for item in feed.feed]


async def lenta_ru_news() -> list[str]:
    rss_url = "https://lenta.ru/rss/last24"
    xml = await get_xml(rss_url)
    titles = parse_rss(xml)
    return titles


async def news_ru_news() -> list[str]:
    rss_url = "https://news.ru/rss/type/post/"
    xml = await get_xml_with_chrome(rss_url)
    titles = parse_rss(xml)
    return titles


async def rambler_news() -> list[str]:
    rss_url = "https://news.rambler.ru/rss/world/"
    xml = await get_xml(rss_url)
    titles = parse_rss(xml)
    return titles
