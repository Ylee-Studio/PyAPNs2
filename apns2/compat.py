"""Shim for legacy PyPI `hyper` / `hyperframe` on Python 3.10+ (collections ABCs)."""

import collections
import collections.abc

_REEXPORT = (
    ('Iterable', collections.abc.Iterable),
    ('Mapping', collections.abc.Mapping),
    ('MutableSet', collections.abc.MutableSet),
    ('MutableMapping', collections.abc.MutableMapping),
    ('Sequence', collections.abc.Sequence),
)
for _name, _obj in _REEXPORT:
    if not hasattr(collections, _name):
        setattr(collections, _name, _obj)
