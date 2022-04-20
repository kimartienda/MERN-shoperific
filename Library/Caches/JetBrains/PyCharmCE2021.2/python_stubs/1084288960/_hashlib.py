# encoding: utf-8
# module _hashlib
# from /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/lib-dynload/_hashlib.cpython-38-darwin.so
# by generator 1.147
# no doc
# no imports

# functions

def hmac_digest(*args, **kwargs): # real signature unknown
    """ Single-shot HMAC. """
    pass

def new(*args, **kwargs): # real signature unknown
    """
    Return a new hash object using the named algorithm.
    
    An optional string argument may be provided and will be
    automatically hashed.
    
    The MD5 and SHA1 algorithms are always supported.
    """
    pass

def openssl_md5(*args, **kwargs): # real signature unknown
    """ Returns a md5 hash object; optionally initialized with a string """
    pass

def openssl_sha1(*args, **kwargs): # real signature unknown
    """ Returns a sha1 hash object; optionally initialized with a string """
    pass

def openssl_sha224(*args, **kwargs): # real signature unknown
    """ Returns a sha224 hash object; optionally initialized with a string """
    pass

def openssl_sha256(*args, **kwargs): # real signature unknown
    """ Returns a sha256 hash object; optionally initialized with a string """
    pass

def openssl_sha384(*args, **kwargs): # real signature unknown
    """ Returns a sha384 hash object; optionally initialized with a string """
    pass

def openssl_sha512(*args, **kwargs): # real signature unknown
    """ Returns a sha512 hash object; optionally initialized with a string """
    pass

def pbkdf2_hmac(*args, **kwargs): # real signature unknown
    """ Password based key derivation function 2 (PKCS #5 v2.0) with HMAC as pseudorandom function. """
    pass

# classes

class HASH(object):
    """
    A hash is an object used to calculate a checksum of a string of information.
    
    Methods:
    
    update() -- updates the current digest with an additional string
    digest() -- return the current digest value
    hexdigest() -- return the current digest as a string of hexadecimal digits
    copy() -- return a copy of the current hash object
    
    Attributes:
    
    name -- the hash algorithm being used by this object
    digest_size -- number of bytes in this hashes output
    """
    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the hash object. """
        pass

    def digest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a bytes object. """
        pass

    def hexdigest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a string of hexadecimal digits. """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """ Update this hash object's state with the provided string. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

openssl_md_meth_names = None # (!) real value is "frozenset({'md5-sha1', 'sha384', 'dsaWithSHA', 'sha256', 'ripemd160', 'sha1', 'ecdsa-with-SHA1', 'GOST 28147-89 MAC', 'sha224', 'dsaEncryption', 'GOST R 34.11-94', 'md5', 'sha512', 'md4', 'GOST R 34.11-2012 (256 bit)', 'GOST R 34-11-2012 (512 bit)', 'whirlpool'})"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x102e3b760>'

__spec__ = None # (!) real value is "ModuleSpec(name='_hashlib', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x102e3b760>, origin='/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/lib-dynload/_hashlib.cpython-38-darwin.so')"

