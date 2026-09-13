"""Exp2: find supersingular E/F13 (#=14, t=0) systematically."""
p = 13
QR = {pow(a, 2, p) for a in range(p)}
def chi(a):
    a %= p
    if a == 0: return 0
    return 1 if a in QR else -1
def count(a, b):  # y^2 = x^3 + a x + b
    n = 1
    for x in range(p):
        n += 1 + chi(x**3 + a*x + b)
    return n
found = []
for a in range(p):
    for b in range(p):
        if (4*a**3 + 27*b**2) % p == 0: continue
        if count(a, b) == 14:
            found.append((a, b))
print("num ss j-models:", len(found))
print(found[:20])
# j invariants
def jinv(a, b):
    return (1728 * 4 * a**3) % p * pow((4*a**3 + 27*b**2) % p, -1, p) % p
print(sorted(set(jinv(a, b) for a, b in found)))
