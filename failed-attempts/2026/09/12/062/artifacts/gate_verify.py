"""Preliminary-gate verification for 43a1 / K=Q(sqrt(-11)) / p=31. Pure Python, exact integer arithmetic."""
def leg(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

def count_E(p):
    # E: y^2+y = x^3+x^2 over F_p (p odd): for each x, disc D=1+4*t, #y = 1+leg(D)
    s = 0
    for x in range(p):
        t = (x**3 + x**2) % p
        s += leg(1 + 4 * t, p)
    return 1 + p + s

def trace(l):
    return l + 1 - count_E(l)

p = 31
N = count_E(p)
a31 = p + 1 - N
print("N(E/F31) =", N, "a31 =", a31, "ordinary:", a31 % 31 != 0)
print("(-11/43) =", leg(-11, 43), "(inert iff -1)")
print("(-11/31) =", leg(-11, 31), "(split iff +1)")
for l in [2, 3, 5, 7, 11, 13, 17, 19, 29]:
    if l == 2:
        n = 1 + sum(1 for x in [0, 1] for y in [0, 1] if (y*y + y + x**3 + x**2) % 2 == 0)
        print("l=2 N=", n, "a=", 3 - n)
    else:
        print(f"l={l} a={trace(l)}")
# mod-31 irreducibility witnesses: Frob_2 poly x^2+2x+2 disc -4=27; Frob_17 poly x^2+3x+17 disc -59=3
print("disc2 =", (-4) % 31, "legendre:", leg(-4, 31))
print("disc17 =", (9 - 68) % 31, "legendre:", leg((9 - 68) % 31, 31))
# singular point at 43: node (28,21); smooth projective count 44 = 43+2 -> nonsplit, a43=-1
l = 43
nsing = [(x, y) for x in range(l) for y in range(l)
         if (y*y + y - (x**3 + x**2)) % l == 0
         and not ((2*y + 1) % l == 0 and (3*x*x + 2*x) % l == 0)]
print("smooth proj pts mod43:", len(nsing) + 1)
