from typing import Any, Dict, List

import pytest

from kuromon import __version__, to_table
from kuromon.errors import InvalidDataFormatError


def test_version():
    assert isinstance(__version__, str)


def test_to_table_with_dict(dict_data: List[Dict], table: str):
    assert to_table(dict_data) == table


def test_to_table_with_dataclass(dataclass_data: List[Any], table: str):
    assert to_table(dataclass_data) == table


def test_to_table_with_pydantic(pydantic_data: List[Any], table: str):
    assert to_table(pydantic_data) == table


def test_to_table_with_popo(popo_data: List[Any], table: str):
    assert to_table(popo_data) == table


def test_to_table_with_dict_without_index(
    dict_data: List[Dict], table_without_index: str
):
    assert to_table(dict_data, index=False) == table_without_index


@pytest.mark.parametrize("data", [("a"), (["a"]), ([{"a": "b"}, 1])])
def test_invalid_data(data: Any):
    with pytest.raises(InvalidDataFormatError):
        to_table(data)
