from collections.abc import Iterable


def each(elements, iteratee):
    if not _iterable(elements):
        raise TypeError(f'{type(elements)} object is not iterable')
    if not callable(iteratee):
        raise TypeError(f'{type(iteratee)} object is not callable')
    list(map(iteratee, elements))


def _iterable(obj):
    return isinstance(obj, Iterable)


