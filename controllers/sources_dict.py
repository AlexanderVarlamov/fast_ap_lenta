from typing_extensions import Type

from controllers.news_classes import *

sources: dict[str, Type[NewsGetter]] = {
    "lenta_ru": LentaNewsGetter,
    "news_ru": NewsRuGetter,
    "rambler": RamblerGetter
}
