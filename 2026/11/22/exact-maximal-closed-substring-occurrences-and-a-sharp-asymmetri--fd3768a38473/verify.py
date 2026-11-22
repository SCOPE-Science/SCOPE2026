"""Exact checks of the endpoint classification for five alternating binary runs.

Usage: python3 verify.py
No third-party packages or external files are needed.
The finite checks corroborate, but do not replace, the universal proof.
"""
from itertools import product
from functools import lru_cache
from random import Random

@lru_cache(None)
def is_closed(s):
    if len(s) == 1:
        return True
    for k in range(1, len(s)):
        if s[:k] != s[-k:]:
            continue
        # Count overlapping occurrences, not Python's nonoverlapping .count().
        if sum(s[i:i+k] == s[:k] for i in range(len(s)-k+1)) == 2:
            return True
    return False

def exhaustive_endpoints(s):
    n=len(s)
    return {(i,j+1) for i in range(n) for j in range(i,n)
            if is_closed(s[i:j+1])
            and (i==0 or not is_closed(s[i-1:j+1]))
            and (j==n-1 or not is_closed(s[i:j+2]))}

def run_endpoints(a,b,c,d,e):
    n=a+b+c+d+e
    r={(0,a),(a,a+b),(a+b,a+b+c),
       (a+b+c,a+b+c+d),(a+b+c+d,n)}
    for t in range(1,min(a,c)+1):
        if t!=c:
            r.add((a-t,a+b+t))
    for t in range(1,min(b,d)):
        r.add((a+b-t,a+b+c+t))
    for t in range(1,min(c,e)+1):
        if t!=c:
            r.add((a+b+c-t,a+b+c+d+t))
    if b!=d:
        r.add((a-min(a,c),a+b+c+min(b,d)))
        r.add((a+b-min(b,d),a+b+c+d+min(c,e)))
    else:
        r.add((a-min(a,c),a+b+c+d+min(c,e)))
    for t in range(c+1,min(a,e)+1):
        r.add((a-t,a+b+c+d+t))
    return r

def formula(a,b,c,d,e):
    return (5+min(a,c)+min(c,e)+min(b,d)
            -int(c<=a)-int(c<=e)+int(b!=d)
            +max(0,min(a,e)-c))

def word(t):
    a,b,c,d,e=t
    return '0'*a+'1'*b+'0'*c+'1'*d+'0'*e

def check(t):
    direct=exhaustive_endpoints(word(t))
    predicted=run_endpoints(*t)
    assert direct==predicted,(t,sorted(direct-predicted),sorted(predicted-direct))
    assert len(predicted)==formula(*t),(t,len(predicted),formula(*t))

if __name__=='__main__':
    count=0
    for t in product(range(1,7),repeat=5):
        check(t);count+=1
    print('PASS exhaustive parameter cubes:',count)
    rng=Random(260702838)
    for j in range(2000):
        check(tuple(rng.randrange(1,18) for _ in range(5)))
    print('PASS seeded larger-parameter comparisons: 2000')
    for n in range(5,43):
        values=[]
        for a in range(1,n-3):
            for b in range(1,n-a-2):
                for c in range(1,n-a-b-1):
                    for d in range(1,n-a-b-c):
                        e=n-a-b-c-d
                        values.append(formula(a,b,c,d,e))
        assert min(values)==6,(n,min(values))
        expected=6 if n==5 else 4+(2*n+1)//3
        assert max(values)==expected,(n,max(values),expected)
    print('PASS exact fixed-length extrema for all n = 5..42')
