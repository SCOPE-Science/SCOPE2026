#!/usr/bin/env python3
"""Independent shortest-rule zero forcing enumeration for clique-expanded cycles."""
from math import comb
from collections import Counter

def adjm(n,m):
    out=[]
    for i in range(n):
        for a in range(m):
            q=(i*m+a)
            nb=set(i*m+b for b in range(m) if b!=a)
            for k in {(i-1)%n,(i+1)%n}:
                nb.update(k*m+b for b in range(m))
            out.append(sum(1<<j for j in nb))
    return out

def force(mask,adj):
    allmask=(1<<len(adj))-1
    blue=mask
    while True:
        if blue==allmask:return True
        growth=0
        for i,a in enumerate(adj):
            if blue>>i&1:
                w=a & (allmask^blue)
                if w and not (w&(w-1)):growth|=w
        if not growth:return False
        blue |=growth

def predicted(mask,n,m):
    full=[]
    for i in range(n):
        z=sum(not (mask>>(i*m+a)&1) for a in range(m))
        if z>1:return False
        if z==0:full.append(i)
    return any(min((j-i)%n,(i-j)%n)<=2 for z,i in enumerate(full) for j in full[z+1:])

def expected_poly(n,m):
    N=n*m; c=Counter()
    for k in range(n+1):c[n*(m-1)+k]+=comb(n,k)*m**(n-k)
    for k in range(n//3+1):
        independent = (n*comb(n-2*k,k)//(n-2*k)) if k else 1
        c[n*(m-1)+k]-=independent*m**(n-k)
    return {x:y for x,y in c.items() if y}

def test(n,m):
    A=adjm(n,m); d=Counter(); cnt=0; mincount=0
    for s in range(1<<(n*m)):
        got=force(s,A); exp=predicted(s,n,m)
        assert got==exp,(n,m,s,got,exp)
        if got:
            cnt+=1; d[s.bit_count()]+=1
            if s.bit_count()==n*(m-1)+2:
                mincount+=1
                for v in range(n*m):
                    if s>>v&1:assert not force(s^(1<<v),A)
    q=expected_poly(n,m)
    assert dict(d)==q,(n,m,d,q)
    edges=n*(n-1)//2 if n<=5 else 2*n
    assert mincount==edges*m**(n-2),(n,m,mincount,edges*m**(n-2))
    print(f'GRAPH_OK n={n} m={m} masks={1<<(n*m)} valid={cnt} min_count={mincount} all_coefficients=PASS',flush=True)
    return (1<<(n*m),cnt)

def published_boundary_witness():
    # Direct twelve-blue witness for C_5[K_3]; no citation inference from this finite check.
    n,m=5,3
    S=sum(1<<(i*m+a) for i in range(n) for a in range(m) if i in (0,1) or a>0)
    assert S.bit_count()==12 and force(S,adjm(n,m))
    assert not any(force(S^(1<<v),adjm(n,m)) for v in range(n*m) if S>>v&1)
    print('LITERATURE_BOUNDARY_OK C5[K3] blue=12 previous_reported=13')

def main():
    published_boundary_witness()
    profiles=[(3,2),(3,3),(3,4),(4,2),(4,3),(5,2),(5,3),(6,2),(7,2),(8,2)]
    states=good=0
    for n,m in profiles:
        a,b=test(n,m);states+=a;good+=b
    print(f'VERIFY_OK profiles={len(profiles)} candidate_sets={states} zero_forcing_sets={good} literal_rule=PASS all_polynomial_coefficients=PASS minimal_counts=PASS')
if __name__=='__main__':main()
