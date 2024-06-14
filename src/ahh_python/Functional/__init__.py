from .internal._List import _patch_list
from .internal._Misc import _patch_misc


def install():
    """
    This function installs the necessary patches for the Functional module.
    """
    _patch_list()
    _patch_misc()

__all__ = ["install"]
