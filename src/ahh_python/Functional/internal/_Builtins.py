"""
Patch builtin functions to support piping using @ operator.
Each builtin will be a class with a defined matmul.
"""

import builtins

_to_patch = [
    "print",
]

# TODO: Replace the __getattribute__ functionality instead so other stuff will always work
def _patch_builtins():
    for key in _to_patch:
        _val = getattr(builtins, key)
        setattr(
            builtins,
            key,
            type(
                key,
                (),
                {
                    "__rmatmul__": (lambda func: lambda self, other: func(other))(_val),
                    "__call__": (
                        lambda func: lambda self, *args, **kwargs: func(*args, **kwargs)
                    )(_val),
                },
            )(),
        )

__all__ = ["_patch_builtins"]