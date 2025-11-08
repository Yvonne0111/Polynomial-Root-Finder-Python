def is_valid_number(num: str) -> bool:
    """
    Returns True if and only if num is represents a valid number.
    See the corresponding .pdf for a definition of what a valid number
    would be.

    >>> is_valid_number("10")
    True
    >>> is_valid_number("-124")
    True
    >>> is_valid_number("12.9")
    True
    >>> is_valid_number("12.9.0")
    False
    >>> is_valid_number("abc")
    False
    """
    s = num.strip()
    if s == "" or s == "+" or s == "-":
        return False
    if "+" == s[0] or "-" == s[0]:
        s = s[1:]
    if s == "":
        return False
    if "." not in s:
        return s.isdigit()
    parts = s.split(".")
    if len(parts) != 2:
        return False
    int_part, mantissa = parts
    if mantissa == "" or not mantissa.isdigit():
        return False
    return (int_part == "" or int_part.isdigit())
    



def is_valid_term(term: str) -> bool:
    """
    Returns True if and only if num is represents a valid term.
    See the corresponding .pdf for a definition of a valid term.

    >>> is_valid_term("44.4x^6")
    True
    >>> is_valid_term("-7x")
    True
    >>> is_valid_term("9.9")
    True
    >>> is_valid_term("7y**8")
    False
    >>> is_valid_term("7x^8.8")
    False
    >>> is_valid_term("7*x^8.8")
    False
    >>> is_valid_term("7x^ 8.8")
    False
    """
    t = term.strip()
    if t == "":
        return False
    if "x" not in t:
        return is_valid_number(t)
    x_index = t.find("x")
    coeff_part = t[:x_index]
    if not is_valid_number(coeff_part):
        return False
    after_x = t[x_index + 1:]
    if after_x == "":
        return True
    if after_x[0] != "^":
        return False
    exp_part = after_x[1:]
    if exp_part == "" or not exp_part.isdigit():
        return False
    if exp_part == "0":
        return False
        
    return True

    
def approx_equal(x: float, y: float, tol: float) -> bool:
    """
    Returns True if and only if x and y are within tol of each other.

    >>> approx_equal(5, 4, 1)
    True
    >>> approx_equal(5, 3, 1)
    False
    >>> approx_equal(0.999, 1, 0.0011)
    True
    >>> approx_equal(0.999, 1, 0.0001)
    False
    """
    
    return abs(x-y) <= tol




def degree_of(term: str) -> int:
    """
    Returns the degree of term, it is assumed that term is a valid term.
    See the corresponding .pdf for a definition of a valid term.

    >>> degree_of("55x^6")
    6
    >>> degree_of("-1.5x")
    1
    >>> degree_of("252.192")
    0
    """
    t = term.strip()
    if "x" not in t:
        return 0
    if "^" not in t:
        return 1
    return int(t.split("^",1)[1])


def get_coefficient(term: str) -> float:
    """
    Returns the coefficient of term, it is assumed that term is a valid term.
    See the corresponding .pdf for a definition of a valid term.

    >>> get_coefficient("55x^6")
    55
    >>> get_coefficient("-1.5x")
    -1.5
    >>> get_coefficient("252.192")
    252.192
    """
    t = term.strip()
    if "x" not in t:
        return float(t)
    coeff_str = t.split("x", 1)[0]
    if coeff_str == "" or coeff_str == "+":
        return 1.0
    if coeff_str == "-":
        return -1.0

    
    return float(coeff_str)






if __name__ == "__main__":
    print("Testing is_valid_number:")
    print(is_valid_number("10"))          # True
    print(is_valid_number("-124"))        # True
    print(is_valid_number("12.9"))        # True
    print(is_valid_number("12.9.0"))      # False
    print(is_valid_number("abc"))         # False

    print("\nTesting is_valid_term:")
    print(is_valid_term("44.4x^6"))       # True
    print(is_valid_term("-7x"))           # True
    print(is_valid_term("9.9"))           # True
    print(is_valid_term("7y**8"))         # False
    print(is_valid_term("7x^8.8"))        # False
    print(is_valid_term("7*x^8.8"))       # False
    print(is_valid_term("7x^ 8.8"))       # False
    print(is_valid_term("-x"))            # True
    print(is_valid_term("x^6"))           # True
    print(is_valid_term("x^0"))           # False

    print("\nTesting approx_equal:")
    print(approx_equal(5, 4, 1))          # True
    print(approx_equal(5, 3, 1))          # False
    print(approx_equal(0.999, 1, 0.0011)) # True
    print(approx_equal(0.999, 1, 0.0001)) # False

    print("\nTesting degree_of:")
    print(degree_of("55x^6"))             # 6
    print(degree_of("-1.5x"))             # 1
    print(degree_of("252.192"))           # 0

    print("\nTesting get_coefficient:")
    print(get_coefficient("55x^6"))       # 55.0
    print(get_coefficient("-1.5x"))       # -1.5
    print(get_coefficient("252.192"))     # 252.192
    print(get_coefficient("x"))           # 1.0
    print(get_coefficient("-x^3"))        # -1.0
