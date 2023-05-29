"""
version 
@author varlamov.a
@email varlamov.a@rt.ru
@date 29.05.2023
@time 9:35
"""
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
            item = m.NewsTypeRequestModel.parse_raw('{"sources": ["fault_source"]}')
            await v.get_last_news(item)

