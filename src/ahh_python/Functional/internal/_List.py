from ._Util import sudo_setattr

from functools import reduce 

def list_map_impl(self, func):
    return map(func, self)

def list_filter_impl(self, func):
    return filter(func, self)

def list_reduce_impl(self, func, initial=None):
    return reduce(func, self, initial)

def _patch_list():
    sudo_setattr(list, "map", list_map_impl)
    sudo_setattr(list, "filter", list_filter_impl)
    sudo_setattr(list, "reduce", list_reduce_impl)


__all__ = []
