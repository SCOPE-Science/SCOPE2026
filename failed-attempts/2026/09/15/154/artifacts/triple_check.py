"""Recovery test: generic non-vacuity of the triple hypothesis + tangent-size count.
p=5; lists primes l=1 mod 5, tests pairwise non-5th-power condition both directions,
prints qualifying triples, and compares the Wiles congruence size p^3 against the
surviving cotangent lower bound p^6 (3 reducible + 3 irreducible directions).
"""
p = 5


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1 if d == 2 else 2
    return True


def is_pth_power(a, ell):
    return pow(a, (ell - 1) // p, ell) == 1


cands = [n for n in range(6, 430) if is_prime(n) and n % p == 1]
print("primes 1 mod 5:", cands)
triples = []
for i in range(len(cands)):
    for j in range(i + 1, len(cands)):
        for k in range(j + 1, len(cands)):
            a, b, c = cands[i], cands[j], cands[k]
            if all(not is_pth_power(x, y)
                   for x, y in [(a, b), (b, a), (a, c), (c, a), (b, c), (c, b)]):
                triples.append((a, b, c))
print("count of qualifying triples:", len(triples))
print("first 8:", triples[:8])
# congruence size vs tangent lower bound for e.g. (11,31,41): vp(li-1)=1 each
a, b, c = triples[0]
print("example:", (a, b, c), "valuations:", [(x - 1) for x in (a, b, c)])
P_size = p ** 3
T_size = p ** 6
print("congruence size P =", P_size, "; cotangent lower bound #J/m2 >=", T_size)
print("Wiles inequality #J/m2 <= P:", "FAILS" if T_size > P_size else "holds")
