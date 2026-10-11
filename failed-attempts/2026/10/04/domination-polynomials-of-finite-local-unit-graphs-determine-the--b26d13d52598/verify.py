#!/usr/bin/env python3
from math import comb, gcd
from itertools import combinations

def model_graph(q, s, char2):
    V = [(a, j) for a in range(q) for j in range(s)]
    adj = {v: set() for v in V}
    for i, u in enumerate(V):
        for v in V[i+1:]:
            a, b = u[0], v[0]
            edge = (a != b) if char2 else ((a + b) % q != 0)
            if edge:
                adj[u].add(v)
                adj[v].add(u)
    return V, adj

def brute_polynomials(q, s, char2):
    V, adj = model_graph(q, s, char2)
    n = len(V)
    D = [0] * (n + 1)
    T = [0] * (n + 1)
    for mask in range(1 << n):
        S = {V[i] for i in range(n) if (mask >> i) & 1}
        if all(v in S or any(u in S for u in adj[v]) for v in V):
            D[len(S)] += 1
        if all(any(u in S for u in adj[v]) for v in V):
            T[len(S)] += 1
    return D, T

def formula_polynomials(q, s, char2):
    N = q * s
    D = [comb(N, k) for k in range(N + 1)]
    for k in range(s + 1):
        D[k] -= q * comb(s, k)
    D[0] += q - 1
    D[s] += q if char2 else 1

    B = [comb(N, k) for k in range(N + 1)]
    for k in range(s + 1):
        B[k] -= q * comb(s, k)
    B[0] += q - 1

    if char2:
        T = B
    else:
        T = B[:]
        r = (q - 1) // 2
        # subtract r*(A^2-(A-sx)^2), A=(1+x)^s-1
        for k in range(1, s + 1):
            T[k + 1] -= r * 2 * s * comb(s, k)
        T[2] += r * s * s
    return D, T

def recover_from_D(D):
    N = len(D) - 1
    if D[1] > 0:
        # Field case: s=1. Singleton coefficient is q in characteristic 2,
        # and 1 in odd characteristic.
        return N, 1, (D[1] == N)
    bad = [k for k in range(1, N) if D[k] != comb(N, k)]
    assert bad
    h = max(bad)
    delta = D[h] - comb(N, h)
    if delta == -N:
        s = h + 1
        char2 = True
    else:
        s = h
        char2 = False
    assert N % s == 0
    return N // s, s, char2

def brute_Zn(n):
    V = list(range(n))
    units = {a for a in V if gcd(a, n) == 1}
    adj = {v: set() for v in V}
    for i, a in enumerate(V):
        for b in V[i+1:]:
            if (a + b) % n in units:
                adj[a].add(b); adj[b].add(a)
    D = [0]*(n+1); T=[0]*(n+1)
    for mask in range(1<<n):
        S = {V[i] for i in range(n) if (mask>>i)&1}
        if all(v in S or any(u in S for u in adj[v]) for v in V):
            D[len(S)] += 1
        if all(any(u in S for u in adj[v]) for v in V):
            T[len(S)] += 1
    return D,T

cases = [
    (2, 2, True),   # Z/4Z residue model
    (2, 4, True),   # Z/8Z residue model
    (4, 1, True),   # F_4
    (4, 4, True),   # F_4[x]/(x^2) residue model
    (3, 1, False),  # F_3
    (3, 3, False),  # Z/9Z residue model
    (5, 1, False),  # F_5
]
for q,s,c2 in cases:
    if q*s <= 16:
        b = brute_polynomials(q,s,c2)
        f = formula_polynomials(q,s,c2)
        assert b == f, (q,s,c2,b,f)
        assert recover_from_D(f[0]) == (q,s,c2)

# Independently verify actual modular-ring graphs for Z/4Z, Z/8Z, Z/9Z.
for n,q,s,c2 in [(4,2,2,True),(8,2,4,True),(9,3,3,False)]:
    assert brute_Zn(n) == formula_polynomials(q,s,c2)

print("VERIFY_OK")
print("model_cases=7")
print("actual_modular_rings=Z4,Z8,Z9")
print("largest_exhaustive_graph_order=16")
print("reconstruction_from_domination_polynomial=verified")
