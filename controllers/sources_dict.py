from controllers.news_classes import *

sources: dict[str, NewsGetter] = {
    "lenta_ru": LentaNewsGetter,
    "news_ru": NewsRuGetter,
    "rambler": RamblerGetter
}
