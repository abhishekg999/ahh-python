from .internal._List import _patch_list
from .internal._Misc import _patch_misc
from .internal._Builtins import _patch_builtins

def install():
    """
    This function installs the necessary patches for the Functional module.
    """
    _patch_list()
    _patch_misc()
    _patch_builtins()

__all__ = ["install"]
