l = [1,2,3,3,2]

def delete(m):
    m = list(set(m))
    return m

delete(l)
print(l)