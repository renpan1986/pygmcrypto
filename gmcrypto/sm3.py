# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_sm3', [dirname(__file__)])
        except ImportError:
            import _sm3
            return _sm3
        if fp is not None:
            try:
                _mod = imp.load_module('_sm3', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _sm3 = swig_import_helper()
    del swig_import_helper
else:
    import _sm3
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SM3(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SM3, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SM3, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _sm3.new_SM3(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sm3.delete_SM3
    __del__ = lambda self : None;
    def update(self, *args): return _sm3.SM3_update(self, *args)
    def digest(self): return _sm3.SM3_digest(self)
    def hexdigest(self): return _sm3.SM3_hexdigest(self)
    def copy(self): return _sm3.SM3_copy(self)
    __swig_getmethods__["block_size"] = _sm3.SM3_block_size_get
    if _newclass:block_size = _swig_property(_sm3.SM3_block_size_get)
    __swig_getmethods__["digest_size"] = _sm3.SM3_digest_size_get
    if _newclass:digest_size = _swig_property(_sm3.SM3_digest_size_get)
    __swig_getmethods__["digestsize"] = _sm3.SM3_digestsize_get
    if _newclass:digestsize = _swig_property(_sm3.SM3_digestsize_get)
    __swig_getmethods__["name"] = _sm3.SM3_name_get
    if _newclass:name = _swig_property(_sm3.SM3_name_get)
SM3_swigregister = _sm3.SM3_swigregister
SM3_swigregister(SM3)
cvar = _sm3.cvar

def new(key):
    return SM3(key)  


# This file is compatible with both classic and new-style classes.


