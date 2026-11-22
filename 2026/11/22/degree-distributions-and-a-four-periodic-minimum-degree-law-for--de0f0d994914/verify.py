#!/usr/bin/env python3
"""Independent exact checks of degree spectra for binary words avoiding 111.
Requires only Python 3 standard library; outputs diagnostics, not a proof.
"""
from collections import Counter, defaultdict
from math import comb


def admissible(w):
    return all(w[i:i+3] != (1,1,1) for i in range(len(w)-2))


def brute_hist(n):
    ans = Counter()
    for num in range(1<<n):
        w = tuple((num>>(n-1-j))&1 for j in range(n))
        if not admissible(w):
            continue
        deg = sum(admissible(w[:i] + (1-w[i],) + w[i+1:]) for i in range(n))
        ans[deg]+=1
    return ans


def blocked(a,b,c,d,e):
    return int(c==0 and ((a==1 and b==1) or (b==1 and d==1) or (d==1 and e==1)))

STATES = tuple(v for num in range(16) if admissible(tuple((num>>(3-j))&1 for j in range(4))) for v in [tuple((num>>(3-j))&1 for j in range(4))])

def next_state(s,x):
    if s[2] and s[3] and x:
        return None
    return s[1:]+(x,)


def spectrum(n):
    """Returns exact degree histogram via boundary-padded width-five transfer."""
    if n<=1:
        return Counter({0:1}) if n==0 else Counter({1:2})
    q=defaultdict(Counter)
    for a in (0,1):
        for b in (0,1):
            q[(0,0,a,b)][0]+=1
    for _ in range(n-2):
        p=defaultdict(Counter)
        for s,cnts in q.items():
            for x in (0,1):
                v=next_state(s,x)
                if v is None:continue
                delta=blocked(*s,x)
                for k,count in cnts.items():p[v][k+delta]+=count
        q=p
    for _ in range(2):
        p=defaultdict(Counter)
        for s,cnts in q.items():
            v=next_state(s,0)
            delta=blocked(*s,0)
            for k,count in cnts.items():p[v][k+delta]+=count
        q=p
    out=Counter()
    for cnts in q.values():
        for deficit,count in cnts.items():out[n-deficit]+=count
    return out


def max_degree_count(n):
    if n<3:return 2**n
    return sum(comb(n-2*k+2,k) for k in range((n+2)//3+1) if n-2*k+2>=k)

def minimum(n):return (n+1)//2 + int(n%4==2)

def main():
    for n in range(0,18):
        h=brute_hist(n)
        assert h == spectrum(n), (n,h,spectrum(n))
    for n in range(1,85):
        h=spectrum(n)
        assert min(h)==minimum(n),(n,min(h),minimum(n))
        assert max(h)==n
        assert h[n]==max_degree_count(n),(n,h[n],max_degree_count(n))
        if n%4==0: assert h[minimum(n)]==1
        t=[1,2,4]
        while len(t)<=n:t.append(sum(t[-3:]))
        assert sum(h.values())==t[n],(n,sum(h.values()),t[n])
    print('PASS: full independent bit-flip comparison for all n=0..17;')
    print('PASS: transfer spectra n=1..84, Tribonacci vertex counts, sharp minimum,')
    print('      uniqueness at n divisible by four, and maximum-degree count formula.')
    for n in range(3,13):print('n=',n,'hist=',sorted(spectrum(n).items()))

if __name__=='__main__':main()
