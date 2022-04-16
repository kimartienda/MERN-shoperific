# Python: 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)]
# Library: lxml, version: 4.6.1
# Module: lxml.objectify, version: 4.6.1
import typing
import builtins as _mod_builtins
import lxml.etree as _mod_lxml_etree

class BoolElement(IntElement):
    "Boolean type base on string values: 'true' or 'false'.\n\n    Note that this inherits from IntElement to mimic the behaviour of\n    Python's bool type.\n    "
    def __bool__(self) -> bool:
        'self != 0'
        ...
    
    __dict__: typing.Dict[str, typing.Any]
    def __eq__(self, value) -> bool:
        'Return self==value.'
        ...
    
    def __ge__(self, value) -> bool:
        'Return self>=value.'
        ...
    
    def __gt__(self, value) -> bool:
        'Return self>value.'
        ...
    
    def __hash__(self) -> int:
        'Return hash(self).'
        ...
    
    def __init__(self) -> None:
        'ElementBase(*children, attrib=None, nsmap=None, **_extra)\n        '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __le__(self, value) -> bool:
        'Return self<=value.'
        ...
    
    def __lt__(self, value) -> bool:
        'Return self<value.'
        ...
    
    def __ne__(self, value) -> bool:
        'Return self!=value.'
        ...
    
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    def __str__(self) -> str:
        'Return str(self).'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _init(self) -> typing.Any:
        ...
    
    @property
    def pyval(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

def DataElement(_value, attrib, nsmap, **_attributes) -> typing.Any:
    "DataElement(_value, attrib=None, nsmap=None, _pytype=None, _xsi=None, **_attributes)\n\n    Create a new element from a Python value and XML attributes taken from\n    keyword arguments or a dictionary passed as second argument.\n\n    Automatically adds a 'pytype' attribute for the Python type of the value,\n    if the type can be identified.  If '_pytype' or '_xsi' are among the\n    keyword arguments, they will be used instead.\n\n    If the _value argument is an ObjectifiedDataElement instance, its py:pytype,\n    xsi:type and other attributes and nsmap are reused unless they are redefined\n    in attrib and/or keyword arguments.\n    "
    ...

def E() -> typing.Any:
    'ElementMaker(self, namespace=None, nsmap=None, annotate=True, makeelement=None)\n\n    An ElementMaker that can be used for constructing trees.\n\n    Example::\n\n      >>> M = ElementMaker(annotate=False)\n      >>> attributes = {\'class\': \'par\'}\n      >>> html = M.html( M.body( M.p(\'hello\', attributes, M.br, \'objectify\', style="font-weight: bold") ) )\n\n      >>> from lxml.etree import tostring\n      >>> print(tostring(html, method=\'html\').decode(\'ascii\'))\n      <html><body><p style="font-weight: bold" class="par">hello<br>objectify</p></body></html>\n\n    To create tags that are not valid Python identifiers, call the factory\n    directly and pass the tag name as first argument::\n\n      >>> root = M(\'tricky-tag\', \'some text\')\n      >>> print(root.tag)\n      tricky-tag\n      >>> print(root.text)\n      some text\n\n    Note that this module has a predefined ElementMaker instance called ``E``.\n    '
    ...

def Element(_tag, attrib, nsmap, **_attributes) -> typing.Any:
    'Element(_tag, attrib=None, nsmap=None, _pytype=None, **_attributes)\n\n    Objectify specific version of the lxml.etree Element() factory that\n    always creates a structural (tree) element.\n\n    NOTE: requires parser based element class lookup activated in lxml.etree!\n    '
    ...

class ElementMaker(_mod_builtins.object):
    'ElementMaker(self, namespace=None, nsmap=None, annotate=True, makeelement=None)\n\n    An ElementMaker that can be used for constructing trees.\n\n    Example::\n\n      >>> M = ElementMaker(annotate=False)\n      >>> attributes = {\'class\': \'par\'}\n      >>> html = M.html( M.body( M.p(\'hello\', attributes, M.br, \'objectify\', style="font-weight: bold") ) )\n\n      >>> from lxml.etree import tostring\n      >>> print(tostring(html, method=\'html\').decode(\'ascii\'))\n      <html><body><p style="font-weight: bold" class="par">hello<br>objectify</p></body></html>\n\n    To create tags that are not valid Python identifiers, call the factory\n    directly and pass the tag name as first argument::\n\n      >>> root = M(\'tricky-tag\', \'some text\')\n      >>> print(root.tag)\n      tricky-tag\n      >>> print(root.text)\n      some text\n\n    Note that this module has a predefined ElementMaker instance called ``E``.\n    '
    def __call__(self, *args, **kwargs) -> typing.Any:
        'Call self as a function.'
        ...
    
    def __getattr__(self) -> typing.Any:
        ...
    
    def __getattribute__(self, name) -> typing.Any:
        'Return getattr(self, name).'
        ...
    
    def __init__(self, namespace=..., nsmap=..., annotate=..., makeelement=...) -> None:
        'ElementMaker(self, namespace=None, nsmap=None, annotate=True, makeelement=None)\n\n    An ElementMaker that can be used for constructing trees.\n\n    Example::\n\n      >>> M = ElementMaker(annotate=False)\n      >>> attributes = {\'class\': \'par\'}\n      >>> html = M.html( M.body( M.p(\'hello\', attributes, M.br, \'objectify\', style="font-weight: bold") ) )\n\n      >>> from lxml.etree import tostring\n      >>> print(tostring(html, method=\'html\').decode(\'ascii\'))\n      <html><body><p style="font-weight: bold" class="par">hello<br>objectify</p></body></html>\n\n    To create tags that are not valid Python identifiers, call the factory\n    directly and pass the tag name as first argument::\n\n      >>> root = M(\'tricky-tag\', \'some text\')\n      >>> print(root.tag)\n      tricky-tag\n      >>> print(root.text)\n      some text\n\n    Note that this module has a predefined ElementMaker instance called ``E``.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class FloatElement(NumberElement):
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self) -> None:
        'ElementBase(*children, attrib=None, nsmap=None, **_extra)\n        '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _init(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class IntElement(NumberElement):
    __dict__: typing.Dict[str, typing.Any]
    def __index__(self) -> int:
        'Return self converted to an integer, if self is suitable for use as an index into a list.'
        ...
    
    def __init__(self) -> None:
        'ElementBase(*children, attrib=None, nsmap=None, **_extra)\n        '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _init(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class LongElement(NumberElement):
    __dict__: typing.Dict[str, typing.Any]
    def __index__(self) -> int:
        'Return self converted to an integer, if self is suitable for use as an index into a list.'
        ...
    
    def __init__(self) -> None:
        'ElementBase(*children, attrib=None, nsmap=None, **_extra)\n        '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _init(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class NoneElement(ObjectifiedDataElement):
    def __bool__(self) -> bool:
        'self != 0'
        ...
    
    __dict__: typing.Dict[str, typing.Any]
    def __eq__(self, value) -> bool:
        'Return self==value.'
        ...
    
    def __ge__(self, value) -> bool:
        'Return self>=value.'
        ...
    
    def __gt__(self, value) -> bool:
        'Return self>value.'
        ...
    
    def __hash__(self) -> int:
        'Return hash(self).'
        ...
    
    def __init__(self) -> None:
        'ElementBase(*children, attrib=None, nsmap=None, **_extra)\n        '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __le__(self, value) -> bool:
        'Return self<=value.'
        ...
    
    def __lt__(self, value) -> bool:
        'Return self<value.'
        ...
    
    def __ne__(self, value) -> bool:
        'Return self!=value.'
        ...
    
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    def __str__(self) -> str:
        'Return str(self).'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def pyval(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class NumberElement(ObjectifiedDataElement):
    def __abs__(self) -> NumberElement:
        'abs(self)'
        ...
    
    def __add__(self, value) -> NumberElement:
        'Return self+value.'
        ...
    
    def __and__(self, value) -> NumberElement:
        'Return self&value.'
        ...
    
    def __bool__(self) -> bool:
        'self != 0'
        ...
    
    def __complex__(self) -> typing.Any:
        ...
    
    __dict__: typing.Dict[str, typing.Any]
    def __eq__(self, value) -> bool:
        'Return self==value.'
        ...
    
    def __float__(self) -> float:
        'float(self)'
        ...
    
    def __ge__(self, value) -> bool:
        'Return self>=value.'
        ...
    
    def __gt__(self, value) -> bool:
        'Return self>value.'
        ...
    
    def __hash__(self) -> int:
        'Return hash(self).'
        ...
    
    def __init__(self) -> None:
        'ElementBase(*children, attrib=None, nsmap=None, **_extra)\n        '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __int__(self) -> int:
        'int(self)'
        ...
    
    def __invert__(self) -> NumberElement:
        '~self'
        ...
    
    def __le__(self, value) -> bool:
        'Return self<=value.'
        ...
    
    def __lshift__(self, value) -> NumberElement:
        'Return self<<value.'
        ...
    
    def __lt__(self, value) -> bool:
        'Return self<value.'
        ...
    
    def __mod__(self, value) -> NumberElement:
        'Return self%value.'
        ...
    
    def __mul__(self, value) -> NumberElement:
        'Return self*value.'
        ...
    
    def __ne__(self, value) -> bool:
        'Return self!=value.'
        ...
    
    def __neg__(self) -> NumberElement:
        '-self'
        ...
    
    def __or__(self, value) -> NumberElement:
        'Return self|value.'
        ...
    
    def __pos__(self) -> NumberElement:
        '+self'
        ...
    
    def __pow__(self, value, mod) -> NumberElement:
        'Return pow(self, value, mod).'
        ...
    
    def __radd__(self, value) -> NumberElement:
        'Return value+self.'
        ...
    
    def __rand__(self, value) -> NumberElement:
        'Return value&self.'
        ...
    
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    def __rlshift__(self, value) -> NumberElement:
        'Return value<<self.'
        ...
    
    def __rmod__(self, value) -> NumberElement:
        'Return value%self.'
        ...
    
    def __rmul__(self, value) -> NumberElement:
        'Return value*self.'
        ...
    
    def __ror__(self, value) -> NumberElement:
        'Return value|self.'
        ...
    
    def __rpow__(self, value, mod) -> NumberElement:
        'Return pow(value, self, mod).'
        ...
    
    def __rrshift__(self, value) -> NumberElement:
        'Return value>>self.'
        ...
    
    def __rshift__(self, value) -> NumberElement:
        'Return self>>value.'
        ...
    
    def __rsub__(self, value) -> NumberElement:
        'Return value-self.'
        ...
    
    def __rtruediv__(self, value) -> NumberElement:
        'Return value/self.'
        ...
    
    def __rxor__(self, value) -> NumberElement:
        'Return value^self.'
        ...
    
    def __str__(self) -> str:
        'Return str(self).'
        ...
    
    def __sub__(self, value) -> NumberElement:
        'Return self-value.'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outc