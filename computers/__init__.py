from .proverka import bar 
def foo(N, A, B, C):
    if bar(N, A, B, C):
        i = 1 + (C * 2) + (B * 1)
        if i > N:
            return N 
        else:
            return i 