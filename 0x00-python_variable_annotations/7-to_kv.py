#!/usr/bin/env python3
"""function annotation"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ this function retuns a tuple and it takes
    a string and a integer or float"""
    x = (k, v*v)
    return x
