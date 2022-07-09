from dataclasses import dataclass
from typing import Dict, List, Optional

import pytest
from dacite import from_dict
from pydantic import BaseModel


class TestModel(BaseModel):
    id: int
    name: str
    tags: Optional[List[str]]


@dataclass
class TestDataClass:
    id: int
    name: str
    tags: Optional[List[str]]


class Test:
    def __init__(self, id: str, name: str, tags: Optional[List[str]]):
        self.id = id
        self.name = name
        self.tags = tags

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(id=data.get("id"), name=data.get("name"), tags=data.get("tags"))


@pytest.fixture
def dict_data():
    return [
        {"id": 1, "name": "foo", "tags": None},
        {"id": 2, "name": "bar", "tags": ["a"]},
    ]


@pytest.fixture
def pydantic_data(dict_data: List[Dict]):
    return [TestModel.parse_obj(obj) for obj in dict_data]


@pytest.fixture
def dataclass_data(dict_data: List[Dict]):
    return [from_dict(data_class=TestDataClass, data=obj) for obj in dict_data]


@pytest.fixture
def popo_data(dict_data: List[Dict]):
    return [Test.from_dict(obj) for obj in dict_data]


@pytest.fixture
def table():
    with open("tests/fixtures/table.txt") as f:
        return f.read().strip()


@pytest.fixture
def table_without_index():
    with open("tests/fixtures/table_without_index.txt") as f:
        return f.read().strip()
