#!/usr/bin/env python3
"""Exact finite-characteristic checks for the bielliptic Picard Prym formulas.

The universal proof is algebraic and appears in RESULT.md. This program checks
its polynomial identities as formal polynomials modulo several primes and
computes direct point counts for small prime fields.
"""
from math import comb, factorial

PRIMES = [7, 13, 19, 31, 37, 43, 61, 67, 73]

def coeff(N, target, p):
    """Dictionary {(exponent_a, exponent_b): coefficient} of [z^target](z²+a*z+b)^N."""
    ans = {}
    for u in range(N + 1):
        v = target - 2*u
        w = N-u-v
        if v < 0 or w < 0:
            continue
        c = comb(N, u)*comb(N-u, v) % p
        if c:
            ans[(v,w)] = (ans.get((v,w), 0) + c) % p
    return {k:v for k,v in ans.items() if v}

def multiply(f,g,p):
    h={}
    for (v,w),c in f.items():
        for (V,W),d in g.items():
            key=(v+V,w+W)
            h[key]=(h.get(key,0)+c*d)%p
    return {k:v for k,v in h.items() if v}

def scale(f,c,p):
    return {k:c*v%p for k,v in f.items() if c*v%p}

def shift_b(f,m):
    return {(v,w+m):c for (v,w),c in f.items()}

def diff_power(m,p):
    return {(2*(m-j),j): comb(m,j)*pow(-4,j,p)%p for j in range(m+1)}

def evaluated(f,a,b,p):
    return sum(c*pow(a,v,p)*pow(b,w,p) for (v,w),c in f.items())%p

def roots_at_b_one(A,p):
    return [a for a in range(p) if evaluated(A,a,1,p)==0]

def degree_poly(A):
    return max((v for (v,w) in A),default=-1)

def eval_derivative(A,a,p):
    return sum(v*c*pow(a,v-1,p) for (v,w),c in A.items() if v>0)%p

def trim(v):
    while v and v[-1] == 0:
        v.pop()
    return v

def polynomial_gcd(f, g, p):
    f=trim(f[:]); g=trim(g[:])
    while g:
        while f and len(f)>=len(g):
            factor=f[-1]*pow(g[-1],-1,p)%p
            shift=len(f)-len(g)
            for j,c in enumerate(g):
                f[j+shift]=(f[j+shift]-factor*c)%p
            trim(f)
        f,g=g,f
    return f

def is_squarefree_over_algebraic_closure(A,p):
    d=degree_poly(A)
    f=[0]*(d+1)
    for (v,w),c in A.items():
        f[v]=(f[v]+c)%p  # b=1
    derivative=[i*f[i]%p for i in range(1,len(f))]
    return len(polynomial_gcd(f,derivative,p))==1

def point_count(a,b,p):
    cubes=[0]*p
    for y in range(p):
        cubes[y*y*y%p]+=1
    return 1+sum(cubes[(x**4+a*x*x+b)%p] for x in range(p))

def check():
    for p in PRIMES:
        m=(p-1)//6
        A=coeff(2*m,3*m,p)
        B=coeff(4*m,3*m,p)
        F=coeff(4*m,6*m,p)
        Dm=diff_power(m,p)
        ratio=comb(4*m,m)*pow(comb(2*m,m),-1,p)%p
        right_B=scale(shift_b(multiply(Dm,A,p),m),ratio,p)
        right_F=scale(Dm,comb(4*m,2*m),p)
        assert B==right_B,(p,'B identity')
        assert F==right_F,(p,'F identity')
        assert degree_poly(A)==m,(p,'degree')
        assert is_squarefree_over_algebraic_closure(A,p),(p,'geometric repeated root')
        assert A.get((m,0))==comb(2*m,m)%p
        assert evaluated(A,2,1,p)!=0 and evaluated(A,p-2,1,p)!=0
        assert all((a*a-4)%p!=0 and eval_derivative(A,a,p)!=0 for a in roots_at_b_one(A,p))
        # The direct trace test is over the prime field (coefficients lie in F_p).
        if p<=19:
            for a in range(p):
                for b in range(1,p):
                    if (a*a-4*b)%p==0:
                        continue
                    trace=(evaluated(A,a,b,p)+evaluated(B,a,b,p)+evaluated(F,a,b,p))%p
                    count=point_count(a,b,p)
                    assert (count-1+trace)%p==0,(p,a,b,'Cartier trace',count,trace)
        print('p=',p,'m=',m,'Hasse degree=',m,'F_p roots=',roots_at_b_one(A,p),
              'two formal identities AND squarefree gcd PASS')
    print('PICARD_PRYM_HASSE_ALL_TESTS_PASS')

if __name__=='__main__':
    check()
