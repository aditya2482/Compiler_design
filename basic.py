###########
# TOKENS - words represented by type:value ie [int:123]
###########

TT_int = "int"
TT_float = "float"
TT_str = "str"
TT_int = "int"
TT_int = "int"
TT_int = "int"


class tokens:
    def __init__(self,type_,value):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f"{self.type}:{self.value}"
        return f"{self.type}"