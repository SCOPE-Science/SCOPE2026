"""Finite consistency checks for the random height-two poset type law.

This checks finite extension counting and annealed formulas. The all-n
concentration and critical-window limit are proved in RESULT.md, not by code.
"""
from itertools import product
from math import comb, log, exp, lgamma
from fractions import Fraction


def graph_counts(n, edges):
    # Number of ideal/filter one-types and genuinely two-sided types.
    # An ideal is (included minima, included maxima).
    ideals = 0
    mixed = 0
    for a in range(1 << n):
        for b in range(1 << n):
            if all(not (b >> j & 1) or not (edges >> (n*i+j) & 1) or (a >> i & 1)
                   for i in range(n) for j in range(n)):
                ideals += 1
    for a in range(1, 1 << n):
        for b in range(1, 1 << n):
            if all((edges >> (n*i+j)) & 1
                   for i in range(n) for j in range(n)
                   if (a >> i & 1) and (b >> j & 1)):
                mixed += 1
    return ideals, mixed, 2*ideals - 1 + mixed


def direct_type_count(n, edges):
    N = 2*n+1
    x = N-1
    orig = {(i, n+j) for i in range(n) for j in range(n)
            if (edges >> (n*i+j)) & 1}
    valid = 0
    for v in product((0,1,2), repeat=2*n):
        rel = [list(row) for row in [[False]*N for _ in range(N)]]
        for i,j in orig:
            rel[i][j] = True
        for i, s in enumerate(v):
            if s == 1: rel[i][x] = True
            if s == 2: rel[x][i] = True
        for k in range(N):
            for i in range(N):
                if rel[i][k]:
                    for j in range(N):
                        if rel[k][j]: rel[i][j] = True
        if any(rel[i][i] for i in range(N)): continue
        if any(rel[i][x] != (v[i] == 1) or rel[x][i] != (v[i] == 2)
               for i in range(2*n)):
            continue
        if any(rel[i][j] != ((i,j) in orig)
               for i in range(2*n) for j in range(2*n)):
            continue
        valid += 1
    return valid

for n in (1,2,3):
    tot_ideals = tot_mixed = 0
    for edges in range(1 << (n*n)):
        a,b,t = graph_counts(n,edges)
        tot_ideals += a
        tot_mixed += b
        if n <= 2 or edges in (0,1,3,(1 << (n*n))-1,0b101010101):
            assert t == direct_type_count(n,edges), (n,edges,t)
    avg_j = Fraction(tot_ideals, 1 << (n*n))
    avg_m = Fraction(tot_mixed, 1 << (n*n))
    expected_j = Fraction(2**(n+1)-1) + sum(
        (Fraction(comb(n,i)*comb(n,j),2**(i*j))
         for i in range(1,n+1) for j in range(1,n+1)), Fraction())
    expected_m = sum(
        (Fraction(comb(n,i)*comb(n,j),2**(i*j))
         for i in range(1,n+1) for j in range(1,n+1)), Fraction())
    assert avg_j == expected_j and avg_m == expected_m, (n,avg_j,avg_m)
    print('FINITE_OK',n,'graphs',1 << (n*n),'E_ideals',avg_j,'E_mixed',avg_m)


def expected_mixed_norm(n, t):
    q=(2*log(n)+t)/n
    assert 0<q<1
    p=1-q
    vals=[lgamma(n+1)-lgamma(i+1)-lgamma(n-i+1)
          +n*log((1+p**i)/2) for i in range(1,n+1)]
    z=max(vals)
    return exp(z)*sum(exp(v-z) for v in vals) - (1-2**(-n))

for t in (-1.,0.,1.):
    limit=2*(exp(exp(-t/2))-1)
    seq=[expected_mixed_norm(n,t) for n in (500,2000,8000)]
    assert abs(seq[-1]-limit) < abs(seq[0]-limit), (t,seq,limit)
    assert abs(seq[-1]-limit) < .1*(1+limit), (t,seq,limit)
    print('ASYMPTOTIC_OK',t,'finite',*[round(x,6) for x in seq],
          'limit',round(limit,6))
print('VERIFY_OK')
