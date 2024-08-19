from enum import Enum
from termcolor import colored

class Type(Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"

    @classmethod
    def is_error_type(cls,type_):
        if isinstance(type_,cls):
            type_=type_.value.upper()
        if type_ in Type.__members__:
            return True
        return False
    
class ErrorDict(dict):
    def __setitem__(self,k,v):
        if Type.is_error_type(k):
            super().__setitem__(Type(k),v)
        else:
            raise KeyError(f"Type {k} is not valid")

    def __getitem__(self,k):
        if isinstance(k,str):
            k = Type(k.upper())
        return super().__getitem__(k)


error_color_mapping = ErrorDict()
error_color_mapping[Type.ERROR] = "red"
error_color_mapping[Type.WARNING] = "yellow"
error_color_mapping[Type.INFO] = "blue"

def log(type_,message):
    print(f"[{colored(type_.value.capitalize(),error_color_mapping[type_])}] {message}")