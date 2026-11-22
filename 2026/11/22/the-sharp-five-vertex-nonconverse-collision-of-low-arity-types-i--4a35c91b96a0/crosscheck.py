"""Independent finite-diagram counting for two five-vertex orientations."""
from itertools import combinations, product

N = 5
EDGES = list(combinations(range(N), 2))

def decode(code):
    output = {}
    for i, j in EDGES:
        digit = code % 3 - 1
        code //= 3
        output[i, j] = digit
        output[j, i] = -digit
    return output

def check(code):
    D = decode(code)
    profiles = []
    for p in product((-1, 0, 1), repeat=N):
        allowed = True
        for i, j in EDGES:
            z = D[i, j]
            if z != 0 and p[i] != 0 and p[j] != 0 and (p[i], p[j]) != (z, -z):
                allowed = False
                break
        if allowed:
            profiles.append(p)
    def compatible(p,q):
        return all(p[i] == 0 or q[i] == 0 or (p[i], q[i]) == (-1, 1) for i in range(N))
    q = len(profiles)
    b = sum(compatible(p, r) for p in profiles for r in profiles)
    # Exhaustively construct every admissible orientation of the three new vertices,
    # then enumerate the actual profiles of all three labelled new vertices.
    valid_internal = []
    for signs in product((-1, 0, 1), repeat=3):
        xy, xz, yz = signs
        if all(signs) and signs not in ((1, -1, 1), (-1, 1, -1)):
            continue
        valid_internal.append(signs)
    total = 0
    for xy, xz, yz in valid_internal:
        for p in profiles:
            for r in profiles:
                if xy == 1 and not compatible(p,r): continue
                if xy == -1 and not compatible(r,p): continue
                for s in profiles:
                    if xz == 1 and not compatible(p,s):continue
                    if xz == -1 and not compatible(s,p):continue
                    if yz == 1 and not compatible(r,s):continue
                    if yz == -1 and not compatible(s,r):continue
                    total += 1
    print(f"code={code} unary={q} oriented_pair={b} all_pair={q*q+2*b} triple={total}")
    return q,b,total

if __name__ == '__main__':
    assert check(3048)==(44,973,653452)
    assert check(3124)==(44,973,658282)
    print('INDEPENDENT_FINITE_EXTENSION_CHECK_OK')
