#!/usr/bin/env python3
"""Independent exact enumeration of the cubic scroll torus evaluation code.
No external packages; prime fields and small extension fields are supported.
"""
from collections import Counter
from itertools import product
from math import comb

FIELDS={4:(2,[1,1,1]),5:(5,None),7:(7,None),8:(2,[1,1,0,1]),9:(3,[1,0,1])}

def finite_field(q):
    p,poly=FIELDS[q]
    degree=1 if poly is None else len(poly)-1
    def digits(k):
        ds=[]
        for _ in range(degree):
            ds.append(k%p); k//=p
        return ds
    def code(ds):return sum(v*(p**i) for i,v in enumerate(ds))
    ds=[digits(i) for i in range(q)]
    add=[[code([(x+y)%p for x,y in zip(ds[i],ds[j])]) for j in range(q)] for i in range(q)]
    mul=[]
    for a in range(q):
        row=[]
        for b in range(q):
            if degree==1:
                row.append((a*b)%p);continue
            v=[0]*(2*degree-1)
            for i,ai in enumerate(ds[a]):
                for j,bj in enumerate(ds[b]):v[i+j]=(v[i+j]+ai*bj)%p
            for i in range(len(v)-1,degree-1,-1):
                carry=v[i]
                for j in range(degree):v[i-degree+j]=(v[i-degree+j]-carry*poly[j])%p
            row.append(code(v[:degree]))
        mul.append(row)
    for a in range(1,q):
        assert len({mul[a][b] for b in range(q)})==q
    return add,mul

def formula(q):
    t=q-1;n=t*t
    u0=t*(t*t+t+6)//2
    u1=3*t*t
    u2=t*t*(t-1)//2
    v0=u0
    v1=3*t*(t-1)
    v2=t*(t-1)*(t-2)//2
    W=Counter({0:1})
    def term(w,a):W[w]+=a
    # B=0
    term(n,u0);term(n-t,u1);term(n-2*t,u2)
    # B(x) has no nonzero root: B constant or scalar x
    term(n,2*t);term(n-t,2*t*u0);term(n-t+1,2*t*u1);term(n-t+2,2*t*u2)
    # B(x) has one root x0 in the torus
    term(n-t,t*t)
    term(n-2*t+1,t*t*3*t)
    term(n-2*t+2,t*t*t*(t-1))
    term(n-t+1,t*t*v0);term(n-t+2,t*t*v1);term(n-t+3,t*t*v2)
    assert sum(W.values())==q**5,(q,sum(W.values()),q**5)
    return +W

def brute(q):
    add,mul=finite_field(q)
    t=q-1;n=t*t
    zero=0
    # Cache A_i(x), B_j(x) for direct independent evaluation.
    nonzero=range(1,q)
    x2={x:mul[x][x] for x in nonzero}
    Avalues={a:tuple(add[add[a[0]][mul[a[1]][x]]][mul[a[2]][x2[x]]] for x in nonzero) for a in product(range(q),repeat=3)}
    Bvalues={b:tuple(add[b[0]][mul[b[1]][x]] for x in nonzero) for b in product(range(q),repeat=2)}
    W=Counter()
    for avec,avals in Avalues.items():
        for bvec,bvals in Bvalues.items():
            zeros=0
            for ai,bi in zip(avals,bvals):
                for y in nonzero:
                    if add[ai][mul[bi][y]]==0:zeros+=1
            W[n-zeros]+=1
    assert sum(W.values())==q**5
    return +W

if __name__=='__main__':
    for q in [4,5,7,8,9]:
        a=formula(q); b=brute(q)
        assert a==b, f'FAIL q={q}: {dict(a-b)} {dict(b-a)}'
        t=q-1
        nonzero=[w for w,v in a.items() if w and v]
        print('q=',q,'length=',t*t,'dimension=5','minimum=',min(nonzero),'spectrum=',sorted(a.items()))
        assert min(nonzero)==t*(t-2)
        assert a[t*(t-2)]==t*t*(t-1)//2
        assert a[t*(t-2)+1]==3*t**3
        print('EXACT_MATCH',q,'COUNT',q**5)
    print('ALL_CHECKS_PASSED')
