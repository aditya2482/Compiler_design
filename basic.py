###########
# TOKENS - words represented by type:value ie [int:123]
###########

TT_int = "int"
TT_float = "float"
TT_str = "str"
TT_plus = "plus"
TT_minus = "minus"
TT_divide = "divide"
TT_multiply = "multiply"
TT_lparanthesis = "lparanthesis"
TT_rparanthesis = "rparanthesis"


class tokens:
    def __init__(self,type_,value):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f"{self.type}:{self.value}"
        return f"{self.type}"
    

###########################
# Lexer
###########################

