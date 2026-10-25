from itertools import combinations_with_replacement

# Arithmetic constraints for eight-face {k,3} closed orientable surfaces.
admissible=[]
for k in range(3, 61):
    if (8*k) % 3 == 0 and 4*k >= 28:
        E=4*k
        V=8*k//3
        g=2*k//3-3
        D=E-28
        admissible.append((k,E,V,g,D))
assert admissible[0] == (9,36,24,3,8)
assert all(k % 3 == 0 and k >= 9 for k,_,_,_,_ in admissible)

# Minimal local excess: each 9-gon sees seven mandatory neighbours.
assert 9-7 == 2

# Cycle-size partitions of 8 for a simple 2-regular graph: all parts >= 3.
def parts(total, lo=3):
    if total == 0:
        yield ()
        return
    for x in range(lo, total+1):
        for rest in parts(total-x, x):
            yield (x,)+rest

cycle_types=set(parts(8))
assert cycle_types == {(8,), (3,5), (4,4)}
print('VERIFY_OK minimal=(k,E,V,g,D)=(9,36,24,3,8) cycle_types=8,5+3,4+4')
