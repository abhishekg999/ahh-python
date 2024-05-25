from ._Util import sudo_setattr

"""
Patches to builtins.map.
    - to_list: Converts the map object to a list.
"""
def map_to_list_impl(self):
    return list(self)

def _patch_map():
    sudo_setattr(map, "to_list", map_to_list_impl)


def filter_to_list_impl(self):
    return list(self)

def _patch_filter():
    sudo_setattr(filter, "to_list", filter_to_list_impl)

def _patch_misc():
    _patch_map()
    _patch_filter()

__all__ = []