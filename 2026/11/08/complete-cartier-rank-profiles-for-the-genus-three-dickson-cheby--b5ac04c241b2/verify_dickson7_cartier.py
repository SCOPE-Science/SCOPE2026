#!/usr/bin/env python3
"""Exact independent Cartier-Manin and Kummer-quotient checks.

No third-party dependencies. Finite tests corroborate, but do not replace,
the proof for every characteristic.
"""

from math import isqrt

D = {1: -7, 3: 14, 5: -7, 7: 1}
PROFILE = {1: (3, 3, 3, 3), 3: (3, 2, 1, 0),
           5: (3, 2, 1, 0), 9: (3, 1, 0, 0),
           11: (3, 1, 0, 0), 13: (3, 0, 0, 0)}


def primes_upto(limit):
    for n in range(3, limit+1, 2):
        if all(n % d for d in range(3, isqrt(n)+1, 2)):
            yield n


def h_matrix(p):
    f = [0]*9
    for j, a in D.items():
        f[j] += 2*a
        f[j+1] += a
    f = [v % p for v in f]
    coeff = [1]
    for _ in range((p-1)//2):
        out = [0]*(len(coeff)+8)
        for i, v in enumerate(coeff):
            if v:
                for j, a in enumerate(f):
                    if a:
                        out[i+j] = (out[i+j]+v*a) % p
        coeff = out
    return [[coeff[p*i-j] if 0 <= p*i-j < len(coeff) else 0
             for j in range(1, 4)] for i in range(1, 4)]


def multiply(A, B, p):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) % p
             for j in range(3)] for i in range(3)]


def rank(A, p):
    M = [row[:] for row in A]
    r=0
    for c in range(3):
        piv=next((i for i in range(r,3) if M[i][c] % p),None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv=pow(M[r][c],-1,p)
        M[r]=[(x*inv) % p for x in M[r]]
        for i in range(3):
            if i != r and M[i][c]:
                x=M[i][c]
                M[i]=[(a-x*b) % p for a,b in zip(M[i],M[r])]
        r+=1
    return r


def quotient_identity():
    # Check (z+z^{-1})/Dickson recurrence as Laurent polynomials over Z.
    def add(A,B,sgn=1):
        C=A.copy()
        for k,v in B.items():
            C[k]=C.get(k,0)+sgn*v
        return {k:v for k,v in C.items() if v}
    x={1:1,-1:1}
    def mul(A,B):
        C={}
        for i,a in A.items():
            for j,b in B.items():
                C[i+j]=C.get(i+j,0)+a*b
        return {k:v for k,v in C.items() if v}
    d0={0:2};d1=x
    for _ in range(2,8):
        d0,d1=d1,add(mul(x,d1),d0,-1)
    assert d1 == {7:1,-7:1}
    # y^2=(z+1)^2*(z^14+1)/z^8 = (x+2)*(z^7+z^-7)
    lhs=mul(mul({0:1,1:1},{0:1,1:1}),{14:1,0:1})
    lhs={i-8:v for i,v in lhs.items()}
    rhs=mul(add(x,{0:2}),d1)
    assert lhs==rhs
    print('KUMMER_QUOTIENT_IDENTITY_OK')


def main():
    quotient_identity()
    count=0
    sample={}
    for p in primes_upto(173):
        if p==7:
            continue
        A=h_matrix(p)
        matrices=[[[int(i==j) for j in range(3)] for i in range(3)]]
        for _ in range(3):
            matrices.append(multiply(matrices[-1],A,p))
        ranks=tuple(rank(B,p) for B in matrices)
        assert ranks==PROFILE[p%14], (p,ranks,PROFILE[p%14],A)
        sample.setdefault(p%14,p)
        count+=1
    assert set(sample)==set(PROFILE)
    print('COMPLETE_PRIME_RESIDUE_PROFILES_OK',count,sample)
    print('CERTIFICATE_OK')


if __name__=='__main__':
    main()
