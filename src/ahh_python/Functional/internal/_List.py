from ._Util import sudo_setattr

from functools import reduce 

"""
Patches to builtins.list.
    - map: Maps a function to each element of the list.
    - filter: Filters the list based on a function.
    - reduce: Reduces the list to a single value.
    - forEach: Applies a function to each element of the list.
    - groupBy: Groups the list by a function.
    - chunk: Chunks the list into smaller lists.
    - all: Checks if all elements satisfy a condition.
    - any: Checks if any element satisfies a condition.

    - to_map: Converts the list to a dictionary of index to value.
    - to_set: Converts the list to a set.    

"""
def list_map_impl(self, func):
    return map(func, self)

def list_filter_impl(self, func):
    return filter(func, self)

def list_reduce_impl(self, func, initial=None):
    return reduce(func, self, initial) if initial is not None else reduce(func, self)

def list_for_each_impl(self, func):
    for i in self:
        func(i)
    
def list_group_by_impl(self, func):
    d = {}
    for i in self:
        key = func(i)
        if key in d:
            d[key].append(i)
        else:
            d[key] = [i]
    return d

def list_chunk_impl(self, size):
    return [self[i:i + size] for i in range(0, len(self), size)]

def list_all_impl(self, func):
    return all(func(i) for i in self)

def list_any_impl(self, func):
    return any(func(i) for i in self)

def list_to_map_impl(self):
    return {i: self[i] for i in range(len(self))}

def list_to_set_impl(self):
    return set(self)

def _patch_list():
    sudo_setattr(list, "map", list_map_impl)
    sudo_setattr(list, "filter", list_filter_impl)
    sudo_setattr(list, "reduce", list_reduce_impl)
    sudo_setattr(list, "for_each", list_for_each_impl)
    sudo_setattr(list, "group_by", list_group_by_impl)
    sudo_setattr(list, "chunk", list_chunk_impl)
    sudo_setattr(list, "all", list_all_impl)
    sudo_setattr(list, "any", list_any_impl)

    sudo_setattr(list, "to_map", list_to_map_impl)
    sudo_setattr(list, "to_set", list_to_set_impl)


__all__ = []
