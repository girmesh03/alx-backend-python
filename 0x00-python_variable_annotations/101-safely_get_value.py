#!/usr/bin/env python3

"""11. More involved type annotations"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Return the value associated with the key
    from the dictionary, or the default value if the key is not found."""
    if key in dct:
        return dct[key]
    else:
        return default
