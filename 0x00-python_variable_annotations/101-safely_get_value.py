#!/usr/bin/env python3

"""
Given the parameters and the return values,
add type annotations to the function
"""

from types import NoneType
from typing import Mapping, Any, Union
from typing_extensions import _T

def safely_get_value(d: Mapping, key: Any, default: Union[Any, NoneType]=None) -> Union[Any, None]:
    """
    Given the parameters and the return values,
    """
    if key in d:
        return d[key]
    else:
        return default
