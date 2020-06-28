def tokenize(chars: str) -> list:
    "Convert a string of characters into a list of tokens."
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()

program = "(begin (define r 10) (* pi (* r r)))"
a=tokenize(program)
print(a)