#!/usr/bin/env python3
"""Exact coefficient checks for period-two parallel chip-firing on split graphs."""
import json
from math import comb


def add_uniform_factor(p, length):
    if length == 0:
        return []
    q = []
    running = 0
    for j in range(len(p) + length - 1):
        if j < len(p):
            running += p[j]
        if j >= length:
            running -= p[j - length]
        q.append(running)
    return q


def polynomial(a, b):
    d = a+b-1
    H = {}
    for k in range(a+1):
        for l in range(b+1):
            sizes = ((a+b-k-l, k), (k+l, a-k), (a-k, l), (k, b-l))
            if any(length == 0 and exponent > 0 for length, exponent in sizes):
                continue
            minimum = k*d + (a-k)*(d-k-l) + l*a + (b-l)*(a-k)
            p = [comb(a,k)*comb(b,l)]
            for length, exponent in sizes:
                for _ in range(exponent):
                    p = add_uniform_factor(p, length)
            for offset, c in enumerate(p):
                H[minimum+offset] = H.get(minimum+offset,0)+c
    return {k:v for k,v in H.items() if v}


def predicted_min(a,b):
    if b >= a:
        return a*(a+b-1)
    return a*(a+2*b-1) - ((a+b)**2//4)


def endpoint(a,b):
    if b >= a:
        return 2
    t = (a+b)//2
    if (a+b)%2 == 0:
        return 2*comb(a,t)
    return 2*(comb(a,t)+comb(a,t+1))


def total_closed(a,b):
    result=0
    for k in range(a+1):
        for l in range(b+1):
            sizes=((a+b-k-l,k),(k+l,a-k),(a-k,l),(k,b-l))
            if any(length==0 and exponent>0 for length, exponent in sizes):
                continue
            term=comb(a,k)*comb(b,l)
            for length,exponent in sizes: term*=length**exponent
            result+=term
    return result


def main():
    tests = 0
    for a in range(2,13):
        for b in range(1,13):
            H=polynomial(a,b)
            m=predicted_min(a,b)
            symmetry=2*a*(a-1)+4*a*b-a-b
            assert set(H) == set(range(m,symmetry-m+1)), (a,b,'support')
            assert H[m]==H[symmetry-m]==endpoint(a,b), (a,b,'endpoint')
            assert all(H[t]==H[symmetry-t] for t in H), (a,b,'palindrome')
            assert sum(H.values())==total_closed(a,b), (a,b,'total')
            assert all(c%2==0 for c in H.values()), (a,b,'orbit parity')
            tests+=1
    samples={f'{a},{b}': {'total':sum((p:=polynomial(a,b)).values()),
                             'minimum':min(p),'maximum':max(p),
                             'endpoint_coefficient':p[min(p)]}
             for a,b in [(2,1),(3,1),(3,2),(3,3),(4,2),(4,4),(5,2)]}
    print(json.dumps({'status':'PASS','tested_parameter_pairs':tests,
                      'parameter_domain':'2<=a<=12,1<=b<=12',
                      'checks':['coefficientwise mass reflection','contiguous support',
                                'sharp minimum and endpoint coefficients',
                                'total-count specialization','even coefficients'],
                      'samples':samples},sort_keys=True))


if __name__=='__main__':main()
