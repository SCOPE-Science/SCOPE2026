#!/usr/bin/env python3
"""Verify that the preset-fallback witness G0 (120-vertex LPS quotient X^{5,q}, q != p)
does not exist, and enumerate actual p=5 window members. Stdlib only."""
import math

def order_psl(q):
    return q * (q * q - 1) // 2

def order_pgl(q):
    return q * (q * q - 1)

def primes_upto(n):
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            step = i
            start = i * i
            s[start:n + 1:step] = [False] * (((n - start) // step) + 1)
    return [i for i, v in enumerate(s) if v]

print("=== (1) Integer Diophantine check: q(q^2-1)/2 = 120 <=> q(q^2-1) = 240 ===")
f = lambda q: q * (q * q - 1)
for q in range(1, 10):
    print(f"  q={q}: q(q^2-1)={f(q)} {'< 240' if f(q) < 240 else ('= 240' if f(q) == 240 else '> 240')}")
print("  f strictly increasing for q>=1, f(6)=210 < 240 < 336=f(7): NO integer solution.")
assert all(f(q) != 240 for q in range(1, 200))

print("=== (2) Integer check: q(q^2-1) = 120 (bipartite/PGL order) ===")
for q in range(1, 9):
    print(f"  q={q}: q(q^2-1)={f(q)}")
print("  Unique positive integer solution: q=5 (f(4)=60 < 120 = f(5) < 210=f(6)).")
assert f(5) == 120 and all(f(q) != 120 for q in list(range(1, 5)) + list(range(6, 200)))

print("=== (3) Prime quotients q != p=5: no 120-vertex LPS quotient ===")
hit = []
for q in primes_upto(60):
    if q == 2 or q == 5:
        continue
    a, b = order_psl(q), order_pgl(q)
    flag = "  <-- HIT 120" if (a == 120 or b == 120) else ""
    if flag:
        hit.append(q)
    print(f"  q={q:3d}: PSL={a:6d} PGL={b:6d}{flag}")
assert hit == [], hit
print("  No prime q != 5 yields order 120. Only degenerate q == p == 5 gives PGL order 120.")

print("=== (4) Degeneracy of q == p == 5 ===")
print("  LPS generators have determinant p (=5); mod q=p they are singular,")
print("  hence not elements of PGL(2,5)/PSL(2,5). LPS requires q != p.")
print("  So X^{5,5} is undefined as a Cayley graph; no citable adjacency exists.")

print("=== (5) Actual p=5 window members with 120 <= n <= 520 (q prime, q != 5) ===")
members = []
for q in primes_upto(60):
    if q == 2 or q == 5:
        continue
    leg = pow(5, (q - 1) // 2, q)
    bip = (leg == q - 1)  # (5/q) = -1 -> bipartite PGL order
    n = order_pgl(q) if bip else order_psl(q)
    if 120 <= n <= 520:
        members.append((q, n, bip))
        print(f"  q={q}: n={n} ({'bipartite PGL' if bip else 'nonbipartite PSL'})")
print(f"  Window members: {members}. No 120-vertex member; 'smallest member with 120 vertices' is vacuous.")
assert not any(n == 120 for _, n, _ in members)

print("VERIFY_OK: fallback G0 (120-vertex LPS quotient X^{5,q0}, q0 != 5) does not exist.")
