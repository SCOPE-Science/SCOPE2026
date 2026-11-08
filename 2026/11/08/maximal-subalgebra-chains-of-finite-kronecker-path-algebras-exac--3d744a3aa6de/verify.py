"""Direct finite-field subalgebra and saturated-chain enumeration.

Run: python verify.py
All arithmetic is over prime fields; the theorem is over all finite fields.
"""
from itertools import combinations, product
from collections import Counter


def qint(n, q):
    return (q**n - 1) // (q - 1)


def flag(n, q):
    z = 1
    for j in range(1, n + 1):
        z *= qint(j, q)
    return z


def predicted(m, q):
    h = 3
    for d in range(1, m + 1):
        h = q*h + 2*qint(d+1, q) + d+1
    return flag(m, q)*h


def all_rref(n, q):
    for k in range(n+1):
        for piv in combinations(range(n), k):
            choices = [(i,j) for i in range(k) for j in range(piv[i]+1,n) if j not in piv]
            for vals in product(range(q),repeat=len(choices)):
                R = [[0]*n for _ in range(k)]
                for i,p in enumerate(piv): R[i][p] = 1
                for (i,j), v in zip(choices, vals): R[i][j]=v
                yield tuple(map(tuple,R)),piv


def reduce_vec(x, b, piv, q):
    x=list(x)
    for row,p in zip(b,piv):
        s=x[p]
        if s: x=[(u-s*v)%q for u,v in zip(x,row)]
    return not any(x)


def mult(x,y,q):
    a,b,*v=x
    c,d,*w=y
    return tuple([a*c%q,b*d%q]+[(a*w0+d*v0)%q for v0,w0 in zip(v,w)])


def subalgebras(m,q):
    n=m+2
    ss=[]
    for b,piv in all_rref(n,q):
        if all(reduce_vec(mult(x,y,q),b,piv,q) for x in b for y in b):
            ss.append((b,piv))
    return ss


def stage_weights(m,q):
    w=[q**(m-j)*(2*qint(j+1,q)+j+1) for j in range(m+1)]
    return w


def test(m,q):
    ss=subalgebras(m,q)
    ss.sort(key=lambda t:len(t[0]))
    chains={}
    n=m+2
    for b,p in ss:
        if not b:
            chains[b]=1
            continue
        count=0
        for c,r in ss:
            if len(c)==len(b)-1 and all(reduce_vec(row,b,p,q) for row in c):
                count+=chains[c]
        chains[b]=count
    full=tuple(tuple(1 if j==i else 0 for j in range(n)) for i in range(n))
    actual=chains[full]
    expected=predicted(m,q)
    assert actual==expected,(m,q,actual,expected)
    assert sum(stage_weights(m,q))*flag(m,q)==actual
    print('CHAIN_OK',q,m,'subalgebras',len(ss),'chains',actual)

for q,m in [(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(5,1)]:
    test(m,q)
print('VERIFY_OK')
