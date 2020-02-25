# JS style functions
from typing import Iterable, List, Callable, Iterator, Union

def _checkIter(list_: Iterable):
    try:
        _ = (e for e in list_)
    except TypeError:
        raise Exception(list_, 'is not iterable')
        return None



def concat(delimeter: str = '', *args: str) -> str:
    return delimeter.join(args)


# Expression 2 value clamp
def clamp(val: Union[int, float], min: Union[int, float], max: Union[int, float]):
    if val < min:
        val = min
    elif val > max:
        val = max
    return val


# JS array.prototype.every equivalent (ES6)
def every(list_: Iterable, pred: Callable) -> bool:
    _checkIter(list_)
    return all(pred(x) for x in list_)


# JS array.prototype.some equivalent (ES6)
def some(list_: Iterable, pred: Callable) -> bool:
    _checkIter(list_)
    return any(pred(x) for x in list_)


# JS array.prototype.filter equivalent (ES6)
def filter(list_: Iterable, pred: Callable) -> List:
    _checkIter(list_)
    return [x for x in list_ if pred(x)]


# JS array.prototype.find equivalent (ES6)
def find(list_: Iterable, pred: Callable):
    _checkIter(list_)
    for x in list:
        if pred(x):
            return x
            break
        else:
            x = None


# JS array.prototype.findIndex equivalent (ES6)
def findIndex(list_: Iterable, pred: Callable) -> int:
    _checkIter(list_)
    for x, i in enumerate(list):
        if pred(x):
            return i
            break
        else:
            i = None


# returns indexes
def findIndexes(list_: Iterable, pred: Callable) -> List:
    _checkIter(list_)
    return [i for i in range(len(list_)) if pred(list_[i])]
