"""Finite enumerator for prefix-degree inverse submonoids of polycyclic monoids."""
from itertools import product
from collections import Counter
from fractions import Fraction

ZERO = None

def words(q, n):
    return list(product(range(q), repeat=n))

def elements(q, N):
    return [ZERO] + [(u, v) for n in range(N+1) for u in words(q,n) for v in words(q,n)]

def mul(x,y):
    if x is ZERO or y is ZERO:
        return ZERO
    u,v=x; s,t=y
    if s[:len(v)] == v:
        return (u+s[len(v):],t)
    if v[:len(s)] == s:
        return (u,t+v[len(s):])
    return ZERO

def level_pair_count(q,m,n):
    a,b=sorted((m,n))
    return q**(2*b)*(q**a-1)**2 + q**(2*b-a)

def lcp(u,v):
    k=0
    for a,b in zip(u,v):
        if a!=b:break
        k+=1
    return k

def centralizer(q,N,m,d):
    return 1 + sum((q**n-1)**2 + (n<=d) for n in range(m+1)) + sum(q**(2*n)-2*q**(2*n-m)+(1+(d==m))*q**(2*(n-m)) for n in range(m+1,N+1))

def profile(q,N):
    size=1+sum(q**(2*n) for n in range(N+1))
    commuting = 2*size-1 + sum(level_pair_count(q,m,n)*(2 if m!=n else 1) for m in range(N+1) for n in range(m,N+1))
    cx = Counter({size:1})
    for m in range(N+1):
        for d in range(m+1):
            mult = q**m if d==m else (q-1)*q**(2*m-d-1)
            cx[centralizer(q,N,m,d)] += mult
    assert sum(cx.values())==size
    assert sum(z*k for z,k in cx.items())==commuting
    return size, commuting, cx

def check(q,N):
    el=elements(q,N)
    size, expected, pred=profile(q,N)
    assert size==len(el)
    brute=Counter()
    pairs_by_level=Counter()
    for x in el:
        c=0
        for y in el:
            if mul(x,y)==mul(y,x):
                c+=1
                if x is not ZERO and y is not ZERO:
                    pairs_by_level[len(x[0]),len(y[0])] += 1
        brute[c]+=1
        if x is not ZERO:
            m=len(x[0]); d=lcp(*x)
            assert c==centralizer(q,N,m,d), (q,N,x,c,centralizer(q,N,m,d))
    assert brute == pred, (q,N, brute,pred)
    for (m,n),v in pairs_by_level.items():
        assert v==level_pair_count(q,m,n), (q,N,m,n,v,level_pair_count(q,m,n))
    assert sum(z*k for z,k in brute.items())==expected
    print('PASS q=%d N=%d size=%d commuting=%d centralizer_strata=%d min_c=%d max_c=%d' %(q,N,size,expected,len(pred),min(pred),max(pred)))

if __name__=='__main__':
    for q,N in ((2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2)):
        check(q,N)
    for q in (2,3,5):
        K=Fraction(2*(q-1)*(q+1)**3,q*(q**3-1))
        print('asymptotic q=%d constant=%s' % (q,K))
        for N in (5,10,20):
            size,commuting,_=profile(q,N)
            scaled=Fraction((size*size-commuting)*q**N,size*size)
            print('  N=%d scaled-noncommuting=%.10f'%(N,float(scaled)))
