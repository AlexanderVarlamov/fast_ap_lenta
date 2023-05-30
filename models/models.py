from pydantic import BaseModel, Field


class NewsTypeRequestModel(BaseModel):
    sources: list[str] = Field(...)


class NewsReturnModel(BaseModel):
    news: list[dict[str, list[str]]] = Field(...)


