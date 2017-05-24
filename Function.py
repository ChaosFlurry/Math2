import re
import math


class Function:
    # Unsupported Functions:
    # factorial, absolute value, logs which are not of base e or 10, complex numbers
    # TODO develop system to generate functions for unit tests
    
    def __init__(self, equation):
        self.input_equation = str.strip(str.lower(equation))
        if self.is_valid() is False:
            raise FunctionError("Function contains invalid keyword.")
        self.parsed_equation = self.parse_equation()
        
    def is_valid(self):
        pattern = re.compile("^([0-9]|\.||x|\+|-|\*|/|\^|\(|\)|sqrt|log|ln|(arc)?("
                             "sin|cos|tan)h?|)+$")
        if pattern.match(self.input_equation):
            return True
        return False
    
    def parse_equation(self):
        replace_table = {
            "\^": "**",
            "(?<!math\.)(pi)": "math.pi",
            "(?<!math\.)(e)": "math.e",
            "(?<!math\.)(sqrt)": "math.sqrt",
            "(?<!math\.)(ln)": "math.log",
            "(?<!math\.)(log)": "math.log10",
            "(?<!math\.)(?<!arc)(sin)(?!h)": "math.sin",
            "(?<!math\.)(?<!arc)(cos)(?!h)": "math.cos",
            "(?<!math\.)(?<!arc)(tan)(?!h)": "math.tan",
            "(?<!math\.)(arcsin)(?!h)": "math.asin",
            "(?<!math\.)(arccos)(?!h)": "math.acos",
            "(?<!math\.)(arctan)(?!h)": "math.atan",
            "(?<!math\.)(?<!arc)(sinh)": "math.sinh",
            "(?<!math\.)(?<!arc)(cosh)": "math.cosh",
            "(?<!math\.)(?<!arc)(tanh)": "math.tanh",
            "(?<!math\.)(arcsinh)": "math.asinh",
            "(?<!math\.)(arccosh)": "math.acosh",
            "(?<!math\.)(arctanh)": "math.atanh"
        }
        
        parsed_equation = self.input_equation
        for original, replacement in replace_table.items():
            pattern = re.compile(original)
            parsed_equation = re.sub(pattern, replacement, parsed_equation)
        return parsed_equation
    
    def f(self, x):
        fx = str.replace(self.parsed_equation, "x", str(x))
        return eval(fx)
    
    def get_area(self, lower, upper):
        dx = (upper - lower) / 1000000
        x = lower
        area = 0
        while x < upper:
            area += self.f(x) * dx
            x += dx
        return area
        

class FunctionError(Exception):
    """Basic exception for errors raised by Functions"""
    def __init__(self, message):
        self.message = message
