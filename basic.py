######
# Digits
######

digits = "01234567890"

########
# Error
########

class errors:
    def __init__(self,error_details,error_name):
        self.error_details = error_details
        self.error_name = error_name

    def __repr__(self):
        return f"Encountered {self.error_name} -- {self.error_details}"


###########
# TOKENS - words represented by type:value ie [int:123]
###########

TT_int = "int" # Token Type
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

class lexer:
    def __init__(self,text):
        self.text = text
        self.pos = -1
        self.current_char = None

    
    def advance(self):
        self.pos +=1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_token(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in "/t":
                self.advance()
            elif self.current_char in "/n":
                self.advance()
            elif self.current_char == "+":
                tokens.append(tokens(TT_plus))
                self.advance()
            elif self.current_char == "-":
                tokens.append(tokens(TT_minus))
                self.advance()
            elif self.current_char == "/":
                tokens.append(tokens(TT_divide))
                self.advance()
            elif self.current_char == "*":
                tokens.append(tokens(TT_multiply))
                self.advance()
            elif self.current_char == "(":
                tokens.append(tokens(TT_lparanthesis))
                self.advance()
            elif self.current_char == ")":
                tokens.append(tokens(TT_rparanthesis))
                self.advance()
            elif self.current_char in digits:
                tokens.append(self.make_digits())
                self.advance()
            else:
                print()
                # if any uniden character present - will raise error
            

    def make_digits(self):
        num_str = ''
        dot_count = 0
        while self.current_char in digits +'.' and self.current_char != None:
            if self.current_char == ".":
                if dot_count == 1:
                    break
                else:
                    dot_count+=1
                    num_str+="."
            else:
                num_str+=self.current_char
            self.advance()
            

            if dot_count == 0:
                return tokens(TT_int,int(num_str))
            else:
                return tokens(TT_float,float(num_str))









        return tokens



    