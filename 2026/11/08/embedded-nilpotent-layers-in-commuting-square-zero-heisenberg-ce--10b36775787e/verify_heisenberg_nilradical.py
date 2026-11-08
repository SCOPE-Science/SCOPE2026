"""Independent monomial-equivalence calculation of Heisenberg centralizer slice.
Commutativity and square-zero equations impose monomial zero relations and
binomial swap relations. This computes graded quotient dimensions directly.
Uses Python 3 standard library only.
"""
from itertools import combinations
from math import comb

def compositions(n,k):
    if k==1:
        yield (n,); return
    for i in range(n+1):
        for rest in compositions(n-i,k-1): yield (i,)+rest

def dimension(m,d):
    mons=list(compositions(d,2*m))
    idx={a:i for i,a in enumerate(mons)}
    parent=list(range(len(mons)))
    killed=[False]*len(mons)
    def root(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    def union(x,y):
        x=root(x);y=root(y)
        if x!=y:
            parent[y]=x
            killed[x] |= killed[y]
    for a,x in enumerate(mons):
        # variable order: b_0,...,b_(m-1), c_0,...,c_(m-1)
        if any(x[i] and x[m+i] for i in range(m)): killed[a]=True
        for i,j in combinations(range(m),2):
            if x[i] and x[m+j]:
                y=list(x);y[i]-=1;y[m+j]-=1;y[j]+=1;y[m+i]+=1
                union(a,idx[tuple(y)])
    return len({root(i) for i in range(len(mons)) if not killed[root(i)]})

if __name__=='__main__':
    for m in range(1,6):
        seq=[]
        for d in range(m+3):
            got=dimension(m,d)
            want=(1 if d==0 else 2*comb(m+d-1,d))+(max(d-1,0)*comb(m,d) if 2<=d<=m else 0)
            assert got==want,(m,d,got,want)
            seq.append(got)
        length=sum((d-1)*comb(m,d) for d in range(2,m+1))
        assert length==(m-2)*2**(m-1)+1
        # Independently multiply the normal-form mixed classes to check all
        # nilradical powers, using disjoint support rather than the sum formula.
        basis={(frozenset(S),u) for d in range(2,m+1)
               for S in combinations(range(m),d) for u in range(1,d)}
        power=basis
        for exponent in range(1,m//2+2):
            if exponent>1:
                power={(S|T,u+v) for S,u in power for T,v in basis if S.isdisjoint(T)}
            expected=sum((d-2*exponent+1)*comb(m,d) for d in range(2*exponent,m+1))
            assert len(power)==expected,(m,exponent,len(power),expected)
        print(f'm={m} Hilbert coefficients degrees 0..{m+2}: {seq}; nilradical length {length}; nilpotence exponent {m//2+1} PASS')
    print('ALL_HEISENBERG_SCHEME_HILBERT_CHECKS_PASS')
