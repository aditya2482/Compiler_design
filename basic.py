######
# Digits
######

digits = '1234567890'


########
strings = 'qwertyuiopasdfghjklzxcvbnm'
#######



########
# Error
########

class Error:
    def __init__(self,error_details,error_name):
        self.error_details = error_details
        self.error_name = error_name

    def as_string(self):
        return f"Encountered {self.error_name} -- {self.error_details}"


class IllegalTokens(Error):
    def __init__(self,details):
        self.dets = details
        super().__init__("(-) Illegal Token recieved",self.dets)

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



class token:
    def __init__(self,type_,value=None):
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
        self.advance()
    
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
                tokens.append(token(TT_plus))
                self.advance()
            elif self.current_char == "-":
                tokens.append(token(TT_minus))
                self.advance()
            elif self.current_char == "/":
                tokens.append(token(TT_divide))
                self.advance()
            elif self.current_char == "*":
                tokens.append(token(TT_multiply))
                self.advance()
            elif self.current_char == "(":
                tokens.append(token(TT_lparanthesis))
                self.advance()
            elif self.current_char == ")":
                tokens.append(token(TT_rparanthesis))
                self.advance()
            elif self.current_char in digits:
                tokens.append(self.make_digits())
                # self.advance()
            elif self.current_char in strings:
                tokens.append(self.make_str())
            else:
                current_token = self.current_char
                self.advance()
                return [],IllegalTokens(""+current_token+"")
        
        return tokens,None

    def make_digits(self):
        num_str = ''
        dot_count = 0
        while self.current_char != None and self.current_char in digits + ".":
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
            return token(TT_int,int(num_str))
        else:
            return token(TT_float,float(num_str))
        
    def make_str(self):
        inp_str = ''
        while self.current_char != None and self.current_char in strings:
            inp_str += self.current_char
            self.advance()

        return token(TT_str,inp_str)

        
###############
# Run
##############

def run(text):
    lex = lexer(text)
    tokensx,error = lex.make_token()

    return tokensx, error
