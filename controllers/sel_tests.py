import asyncio

from arsenic import get_session
from arsenic.browsers import Chrome
from arsenic.services import Chromedriver

from conf import chromedriver_path
from actions import *




async def get_content():
    async with get_session(Chromedriver(binary=chromedriver_path), Chrome()) as session:
        await session.get(r'https://news.ru/rss/type/post/')
        content = await session.get_page_source()

    return content

# opt = webdriver.ChromeOptions()
# opt.add_argument('headless')
# opt.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36')
# browser = webdriver.Chrome(options=opt)
# browser.get('https://news.ru/rss/type/post/')
#
# content = browser.page_source
# browser.close()
# # print(content)
#
# titles = parse_rss(content)
# print(titles)

loop = asyncio.get_event_loop()

cont = loop.run_until_complete(get_content())
titles = parse_rss(cont)
print(titles)