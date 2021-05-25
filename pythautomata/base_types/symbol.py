from abc import ABC, abstractproperty
from typing import Any

class Symbol(ABC):
    """Abstract class representing symbols.
    """
    @abstractproperty
    def value(self) -> Any:
        raise NotImplementedError

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return self.value

    def __eq__(self, other):
        return isinstance(other, Symbol) and self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value
    
    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other


class SymbolStr(Symbol):
    """Symbol specification using string as a representation.
    """
    def __init__(self, value: str):
        self._value = value

    @property
    def value(self):
        return self._value

    def __repr__(self):
        return str(self.value)

class SymbolInfinity(Symbol):
    """Symbol that represents infinity, not part of any alphabet. Used on interval guards
    """
    @property
    def value(self):
        return self

    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return u"\u221E"

    def __eq__(self, other):
        return False

    def __lt__(self, other):
        return False

    def __gt__(self, other):
        return True


class SymbolNegativeInfinity(Symbol):
    """Symbol that represents negative infinity, not part of any alphabet. Used on interval guards
    """
    @property
    def value(self):
        return self

    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return u"-\u221E"

    def __eq__(self, other):
        return False

    def __lt__(self, other):
        return True

    def __gt__(self, other):
        return False