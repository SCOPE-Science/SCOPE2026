#!/usr/bin/env python3
"""Direct enumeration checks for prescribed multiplication fibers in POI_n."""
from itertools import combinations
from math import comb
from collections import Counter,defaultdict

def maps(n):
    out=[]
    universe=tuple(range(1,n+1))
    for r in range(n+1):
        for A in combinations(universe,r):
            for B in combinations(universe,r):
                out.append((A,B))
    return out

def multiply(f,g):
    A,B=f;C,D=g
    d=dict(zip(C,D))
    src=tuple(a for a,b in zip(A,B) if b in d)
    dst=tuple(d[b] for b in B if b in d)
    return src,dst

def fiber_formula(n,r,s,A,D):
    t=len(A)
    if len(D)!=t or t>min(r,s) or r+s-t>n: return 0
    outerA=(0,)+A+(n+1,)
    outerD=(0,)+D+(n+1,)
    ag=[outerA[i+1]-outerA[i]-1 for i in range(t+1)]
    dg=[outerD[i+1]-outerD[i]-1 for i in range(t+1)]
    total=0
    for I in combinations(range(1,n+1),t):
        outerI=(0,)+I+(n+1,)
        ig=[outerI[i+1]-outerI[i]-1 for i in range(t+1)]
        dp={(0,0):1}
        for aa,dd,ii in zip(ag,dg,ig):
            nd=defaultdict(int)
            for (x,y),v in dp.items():
                for j in range(min(aa,ii,r-t-x)+1):
                    for k in range(min(dd,ii-j,s-t-y)+1):
                        nd[x+j,y+k] += v*comb(aa,j)*comb(dd,k)*comb(ii,j)*comb(ii-j,k)
            dp=nd
        total+=dp.get((r-t,s-t),0)
    return total

def top_fiber(n,dom,img):
    if len(dom)!=n-2 or len(img)!=n-2: return 0
    holes=tuple(x for x in range(1,n+1) if x not in dom)
    holes2=tuple(x for x in range(1,n+1) if x not in img)
    u,v=holes;z,w=holes2
    return 4+sum(p==q for p in (u,v-1) for q in (z,w-1))

def run(n):
    mm=maps(n); count=Counter(); rank_pair=Counter();
    for f in mm:
        for g in mm:
            target=multiply(f,g)
            count[(len(f[0]),len(g[0]),target)]+=1
            rank_pair[(len(f[0]),len(g[0]),len(target[0]))]+=1
    tested=0
    for (r,s,(A,D)),counted in count.items():
        calc=fiber_formula(n,r,s,A,D)
        assert counted==calc,(n,r,s,A,D,counted,calc)
        tested+=1
    # A zero factor count also matters for targets impossible by rank.
    for r in range(n+1):
        for s in range(n+1):
            for t in range(n+1):
                if (r,s,t) not in rank_pair: assert t>min(r,s) or r+s-t>n
    if n>=2:
        for A in combinations(range(1,n+1),n-2):
            for D in combinations(range(1,n+1),n-2):
                assert count[(n-1,n-1,(A,D))]==top_fiber(n,A,D)
        for A in combinations(range(1,n+1),n-1):
            for D in combinations(range(1,n+1),n-1):
                assert count[(n-1,n-1,(A,D))]==n
        assert sum(v for (r,s,T),v in count.items() if r==n-1 and s==n-1)==n**4
    print(f'n={n}: {len(mm)} maps, {len(mm)**2} products, {tested} nonzero rank-conditioned fibers; all identities verified')

if __name__=='__main__':
    for n in range(1,5): run(n)

def corank_one_spectrum(n):
    if n<2:return
    ground=tuple(range(1,n+1))
    F=[(tuple(i for i in ground if i!=a),tuple(i for i in ground if i!=b)) for a in ground for b in ground]
    empirical=Counter(multiply(f,g) for f in F for g in F)
    spec=Counter()
    for A in combinations(ground,n-2):
        for D in combinations(ground,n-2):
            got=empirical.get((A,D),0)
            expect=top_fiber(n,A,D)
            assert got==expect,(n,A,D,got,expect)
            spec[got]+=1
    for A in combinations(ground,n-1):
        for D in combinations(ground,n-1):
            assert empirical[(A,D)]==n
    N=n-1
    predicted={4:N*(N-1)*(N*N-N+2)//4,5:N*(N-1)*(N-2),6:5*N*(N-1)//2,8:N}
    assert all(spec[k]==v for k,v in predicted.items()),(n,spec,predicted)
    assert sum(spec.values())==comb(n,2)**2
    assert sum(k*v for k,v in spec.items())==n**4-n**3
    print(f'corank-one n={n}: nonzero spectrum {dict(sorted(spec.items()))}; all counts verified')

if __name__=='__main__':
    for n in range(2,13):corank_one_spectrum(n)
