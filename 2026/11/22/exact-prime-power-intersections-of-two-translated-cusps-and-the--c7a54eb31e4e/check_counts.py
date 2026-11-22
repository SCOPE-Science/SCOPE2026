#!/usr/bin/env python3
"""Independent finite checks for common zeros of two translated cusp polynomials.

Run: python3 check_counts.py
Only Python's standard library is needed. Tests do not prove the infinite theorem.
"""
from math import prod


def isprime(n):
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def predicted(p,k):
    assert isprime(p) and k >= 1
    if p == 2:
        return 2 if k == 1 else 4 if k <= 5 else 2**(k//2)
    if p == 3:
        if k <= 3:
            return 3**(k-1)
        if k <= 6:
            return 3**(k-2)
        return 81 + 3**(k-max(3,(k-1)//2))
    split = pow(p-2,(p-1)//2,p) == 1
    return p**(k//2) + 2*int(split)


def count_via_original_equations(p,k):
    m = p**k
    c = 0
    if p == 2:
        if k == 1:
            return sum((x*x + y**3)%2==0 and ((x+1)**2+(y+1)**3)%2==0
                       for x in range(2) for y in range(2))
        for y in range(m):
            x0 = (-1 - 3*(y*(y+1)//2)) % (m//2)
            for x in (x0, x0+m//2):
                if (x*x+y*y*y)%m == 0 and ((x+1)**2+(y+1)**3)%m == 0:
                    c += 1
    else:
        inv2 = pow(2,-1,m)
        for y in range(m):
            x = (-(3*y*y+3*y+2)*inv2) % m
            if (x*x+y*y*y)%m == 0 and ((x+1)**2+(y+1)**3)%m == 0:
                c += 1
    return c


def direct_bruteforce(m):
    return sum((x*x+y**3)%m==0 and ((x+1)**2+(y+1)**3)%m==0
               for x in range(m) for y in range(m))


def factor(n):
    factors=[]
    p=2
    while p*p<=n:
        if n%p == 0:
            k=0
            while n%p==0:
                k+=1;n//=p
            factors.append((p,k))
        p+=1
    if n>1:factors.append((n,1))
    return factors


def main():
    cases=[]
    for p,max_k in [(2,16),(3,11),(5,7),(7,6),(11,4),(13,4),
                    (17,3),(19,3),(23,3),(29,3),(31,3),(37,2),(41,2),
                    (43,2),(47,2)]:
        for k in range(1,max_k+1):
            got=count_via_original_equations(p,k)
            expected=predicted(p,k)
            assert got == expected,(p,k,got,expected)
            cases.append((p,k,got))
    small=[p**k for p,k,_ in cases if p**k<=169]
    for m in small:
        assert direct_bruteforce(m)==prod(predicted(p,k) for p,k in factor(m)),m
    composites=[6,10,12,15,18,24,30,36,45,60,72,90,100,105,120,140,180,200,210]
    for m in composites:
        assert direct_bruteforce(m)==prod(predicted(p,k) for p,k in factor(m)),m
    print('PASS',len(cases),'prime-power cases via original polynomials; ',
          len(small),'direct square-enumeration prime-power checks; ',
          len(composites),'composite CRT checks')
    print('Samples',[(p,k,n) for p,k,n in cases if (p,k) in [(2,1),(2,5),(2,8),(3,3),(3,6),(3,7),(3,9),(5,4),(11,3)]])

if __name__=='__main__':main()
