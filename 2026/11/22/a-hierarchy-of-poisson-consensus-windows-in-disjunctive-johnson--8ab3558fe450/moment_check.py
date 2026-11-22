"""Exact finite-n first two factorial moments for random shadow gaps.
Run: python moment_check.py. No simulation or third-party libraries.
"""
from math import comb, log, exp, factorial

def choose(n,k):
    return comb(n,k) if 0<=k<=n else 0

def union_forbidden(n,k,r,s):
    # Two candidate k-sets intersect in exactly s ground labels.
    # A selected k-set is forbidden if it overlaps either candidate in >=r labels.
    ans=0
    for common in range(s+1):
        for a in range(k-s+1):
            for b in range(k-s+1):
                rest=k-common-a-b
                if a+common >=r or b+common>=r:
                    ans+=choose(s,common)*choose(k-s,a)*choose(k-s,b)*choose(n-2*k+s,rest)
    return ans

def moments(n,k,r,c):
    size=comb(n,k); base=comb(n-r,k-r); b=comb(k,r)
    p=((k/b)*log(n)+c)/base
    d=union_forbidden(n,k,r,k)
    mean=size*(1-p)**d
    second=0.0
    for s in range(k):
        count=comb(k,s)*comb(n-k,k-s)
        second+=size*count*(1-p)**union_forbidden(n,k,r,s)
    limit=exp(-c*b)/factorial(k)
    return p,mean,second,limit

if __name__=='__main__':
    for k,r,c in [(4,2,-0.5),(5,2,-0.5),(5,3,-0.2)]:
        for n in [50,150,500,1500]:
            p,m,s,l=moments(n,k,r,c)
            assert p>0 and 0<=m and 0<=s
            print(f'k={k} r={r} n={n} p={p:.8g} E[Y]={m:.6g} E[(Y)_2]={s:.6g} limit_mean={l:.6g} limit_second={l*l:.6g}')
