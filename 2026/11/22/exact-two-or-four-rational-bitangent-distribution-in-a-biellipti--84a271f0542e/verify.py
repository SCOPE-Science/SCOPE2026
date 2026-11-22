#!/usr/bin/env python3
"""Independent modular checks for bitangents and exact parameter frequencies.
Run: python3 verify.py [--csv examples.csv]
Uses only Python's standard library. Finite checks supplement, not replace, the proof.
"""
from collections import Counter
import csv
import sys

def isprime(p):
    return p >= 2 and all(p%d for d in range(2,int(p**.5)+1))

def brute_lines(p,r):
    inv2=pow(2,-1,p)
    out=set()
    for a in range(p):
        for b in range(p):
            # x=ay+b; restricted quartic: y^4+a^3 y^3 +(3a^2b+r)y^2+3ab^2y+b^3+1.
            u=(a**3*inv2)%p
            v=((3*a*a*b+r-u*u)*inv2)%p
            if (2*u*v-3*a*b*b)%p == 0 and (v*v-b**3-1)%p == 0:
                out.add((a,b))
    return out

def tower_lines(p,r):
    c=((r*r-4)*pow(4,-1,p))%p
    lines={(0,b) for b in range(p) if pow(b,3,p)==c}
    roots=[z for z in range(1,p) if (3*pow(z,4,p)+4*r*pow(z,3,p)+6*z*z-1)%p==0]
    for z in roots:
        for s in range(1,p):
            if s*s%p!=z:continue
            w=(9*s-pow(s,-3,p))%p
            lines.update((a,(a*s)%p) for a in range(1,p) if pow(a,3,p)==w)
    return lines,roots

def verify_prime(p):
    distribution=Counter()
    for r in range(p):
        if (r*r-4)%p==0:continue
        got,zs=tower_lines(p,r)
        brute=brute_lines(p,r)
        assert got==brute,('bitangent lines',p,r,sorted(got^brute))
        distribution[len(got)+1]+=1  # z=0 at infinity
        if p%3==2:
            sqroots=[z for z in zs if pow(z,(p-1)//2,p)==1]
            assert len(sqroots) in (0,1),('square-root uniqueness',p,r,zs)
            assert len(got)+1 == 2+2*len(sqroots),('count',p,r)
    if p%3==2:
        assert distribution==Counter({2:(p+1)//2,4:(p-5)//2}),('frequency',p,distribution)
    return {'q':p,'r_smooth':p-2,'count_2':distribution[2],
            'count_4':distribution[4], 'other_counts':sum(v for k,v in distribution.items() if k not in (2,4))}

def main():
    primes=[p for p in range(5,102) if isprime(p)]
    rows=[verify_prime(p) for p in primes]
    # all 24 prime fields through 101, including q=1 mod 3 control cases
    assert len(rows)==24, len(rows)
    if '--csv' in sys.argv:
        path=sys.argv[sys.argv.index('--csv')+1]
        with open(path,'w',newline='',encoding='utf-8') as f:
            wr=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');wr.writeheader();wr.writerows(rows)
    print('PASS: 24 primes 5..101; line-square identity on all smooth parameters; exact 2/4 frequencies when p=2 modulo 3')
    for row in rows:
        if row['q'] in (5,11,17,23,29):print(row)
if __name__=='__main__':main()
