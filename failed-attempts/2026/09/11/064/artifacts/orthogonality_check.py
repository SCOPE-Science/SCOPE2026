"""Orthogonality of primitive characters mod prime q (all nonprincipal are primitive).
O(n) = sum^* chi(n) = q-2 if n==1 mod q; -1 if (n,q)=1 and n!=1; 0 if q|n.
Uses primitive root enumeration; stdlib only.
"""
import cmath, math


def orth(q, n):
    if n % q == 0:
        return 0j
    # find primitive root
    for g in range(2, q):
        if sorted(pow(g, k, q) for k in range(q - 1)) == list(range(1, q)):
            break
    dlog = {pow(g, k, q): k for k in range(q - 1)}
    # nonprincipal chars j=1..q-2 (j=0 mod q-1 is principal; there are q-2 of them)
    return sum(cmath.exp(2j * math.pi * j * dlog[n % q] / (q - 1)) for j in range(1, q - 1))


for q in (5, 7, 11):
    ok = True
    for n in range(1, 3 * q + 2):
        s = orth(q, n)
        r = round(s.real)
        exp = (q - 2) if n % q == 1 else (0 if n % q == 0 else -1)
        if r != exp or abs(s.imag) > 1e-9:
            ok = False
            print(f"FAIL q={q} n={n}: got {s}, expected {exp}")
    print(f"q={q}: {'ORTHOGONALITY_OK' if ok else 'MISMATCH'}")
