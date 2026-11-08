#!/usr/bin/env python3
"""Exact checks of fixed-weight Fibonacci residue asymptotics; stdlib only."""
from fractions import Fraction
from itertools import combinations
from math import factorial, comb

def fib_mod(m):
    a, b = 0, 1
    vals = []
    while True:
        vals.append(a)
        a, b = b, (a+b) % m
        if a == 0 and b == 1:
            return vals

def convolution(a, b, m):
    out = [0]*m
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[(i+j)%m] += x*y
    return out

def constants(k,m,r):
    vals = fib_mod(m)
    T = len(vals)
    single = [0]*m
    same = [0]*m
    near = [0]*m
    for j in range(T):
        x = vals[j]
        single[x] += 1
        same[(2*x)%m] += 1
        near[(x+vals[(j+1)%T])%m] += 1
    base = [0]*m
    base[0] = 1
    for _ in range(k-2):
        base = convolution(base, single, m)
    e = convolution(base,same,m)[r]
    a = convolution(base,near,m)[r]
    full = convolution(convolution(base,single,m),single,m)[r]
    return T, Fraction(full,T**k), Fraction(e+2*a,2*T**(k-1))

def independent_count(k,m,r,L):
    vals = fib_mod(m)
    T = len(vals)
    dp0 = [[0]*m for _ in range(k+1)]
    dp1 = [[0]*m for _ in range(k+1)]
    dp0[0][0] = 1
    for j in range(2,L+2):
        f = vals[j%T]
        nxt0 = [[dp0[w][a]+dp1[w][a] for a in range(m)] for w in range(k+1)]
        nxt1 = [[0]*m for _ in range(k+1)]
        for w in range(1,k+1):
            for a in range(m):
                nxt1[w][(a+f)%m] += dp0[w-1][a]
        dp0,dp1 = nxt0,nxt1
    counts = [dp0[k][r]+dp1[k][r] for r in range(m)]
    return counts[r], counts

def direct_count(k,m,L):
    vals = fib_mod(m)
    T = len(vals)
    out=[0]*m
    for inds in combinations(range(2,L+2),k):
        if any(y==x+1 for x,y in zip(inds,inds[1:])):
            continue
        residue=sum(vals[j%T] for j in inds)%m
        out[residue]+=1
    return out

def run():
    tested = 0
    row_checks = 0
    rational_checks = 0
    selected = [(2,2),(3,3),(4,4),(5,5),(3,7),(4,6),(5,8)]
    expected = {
        2:(Fraction(5,9),Fraction(5,6)),
        3:(Fraction(85,256),Fraction(33,64)),
        4:(Fraction(7,27),Fraction(7,18)),
        5:(Fraction(1,5),Fraction(3,10)),
    }
    for k,m in selected:
        T,_,_ = constants(k,m,0)
        for r in range(m):
            t,p,h=constants(k,m,r)
            assert t==T and p>=0 and h>=0
            rational_checks+=1
            if m==k and r==0:
                assert (p,h)==expected[k], (k,p,h)
                assert p>0
            for times in (3,5,9):
                L=T*times
                val, allcounts = independent_count(k,m,r,L)
                assert sum(allcounts)==comb(L-k+1,k)
                lead=Fraction(L**k,factorial(k))*p
                second=Fraction(L**(k-1),factorial(k-2))*h
                # The exact theorem implies the normalized remainder is bounded.
                # This is only a finite-range diagnostic, not a proof of the big-O.
                remainder=(val-lead+second)/L**(k-2)
                assert abs(remainder) < 100000, (k,m,r,L,remainder)
                row_checks+=1
                if m==k and k==2 and r==0:
                    a=L//3
                    assert val == (5*a*a-5*a+2)//2
                tested+=1
        for L in (k+1,k+4,min(17,max(k+5,2*k+1))):
            if L<k: continue
            _, counts=independent_count(k,m,0,L)
            if L<=19:
                assert counts == direct_count(k,m,L),(k,m,L)
                tested+=1
    print(f'VERIFY_OK parameter_pairs={len(selected)} rational_residue_constants={rational_checks} asymptotic_finite_checks={row_checks} independent_subset_checks=21 exact_integer_and_rational=yes')
if __name__ == '__main__':
    run()
