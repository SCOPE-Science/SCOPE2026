from math import factorial

def irreducible_types(max_rank=20):
    out = []
    # A_r exponents 1,...,r
    for r in range(1, max_rank + 1):
        out.append((f"A{r}", list(range(1, r + 1))))
    # B_r and C_r exponents 1,3,...,2r-1
    for r in range(2, max_rank + 1):
        exps = list(range(1, 2*r, 2))
        out.append((f"B{r}", exps))
        out.append((f"C{r}", exps))
    # D_r exponents 1,3,...,2r-3 plus r-1
    for r in range(4, max_rank + 1):
        exps = list(range(1, 2*r-2, 2)) + [r-1]
        exps.sort()
        out.append((f"D{r}", exps))
    out.extend([
        ("G2", [1,5]),
        ("F4", [1,5,7,11]),
        ("E6", [1,4,5,7,8,11]),
        ("E7", [1,5,7,9,11,13,17]),
        ("E8", [1,7,11,13,17,19,23,29]),
    ])
    return out

types = irreducible_types()
checks = 0
for name, exps in types:
    N = sum(exps)
    W = 1
    for e in exps:
        W *= e + 1
        assert e + 1 <= 2 ** e
    if N >= 4:
        assert factorial(N) > 2 ** N >= W
    checks += 1

small = {
    "A1": ([1], "<"),
    "A1xA1": ([1,1], "<"),
    "A1xA1xA1": ([1,1,1], "<"),
    "A2": ([1,2], "="),
}
for name, (exps, sign) in small.items():
    N = sum(exps)
    W = 1
    for e in exps:
        W *= e + 1
    if sign == "<":
        assert factorial(N) < W
    else:
        assert factorial(N) == W

# Low-dimensional product census from irreducible components with N <= 6.
atoms = [(name, sum(exps), __import__("math").prod(e+1 for e in exps))
         for name, exps in types if sum(exps) <= 6]
def rec(start, N, W):
    if N:
        if N <= 3:
            pair = (factorial(N), W)
            assert pair in {(1,2),(2,4),(6,8),(6,6)}
        elif N >= 4:
            assert factorial(N) > W
    if N >= 12:
        return
    for i in range(start, len(atoms)):
        _, n, w = atoms[i]
        if N+n <= 12:
            rec(i, N+n, W*w)
rec(0, 0, 1)

print("VERIFY_OK", checks, len(atoms))
