from ._Util import sudo_setattr

def map_to_list_impl(self):
    return list(self)

def filter_to_list_impl(self):
    return list(self)

def _patch_misc():
    sudo_setattr(map, "to_list", map_to_list_impl)
    sudo_setattr(filter, "to_list", filter_to_list_impl)

__all__ = []