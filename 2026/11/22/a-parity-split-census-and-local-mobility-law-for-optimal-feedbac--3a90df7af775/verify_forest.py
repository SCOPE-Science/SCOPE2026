"""Independent exhaustive validation on the explicitly constructed circular ladder.
Run: python3 verify_forest.py
Uses only Python standard library; assertion failure exits nonzero.
"""
from itertools import combinations


def check(n):
    V=range(2*n)
    E=set()
    for i in range(n):
        for a,b in ((i,(i+1)%n),(n+i,n+(i+1)%n),(i,i+n)):
            E.add(tuple(sorted((a,b))))
    E=sorted(E)
    k=(n+2)//2
    full=[]; predicted=[]
    for comb in combinations(V,k):
        S=set(comb)
        roots=list(range(2*n))
        def root(x):
            while roots[x]!=x:
                roots[x]=roots[roots[x]];x=roots[x]
            return x
        forest=True
        for x,y in E:
            if x in S or y in S:continue
            a,b=root(x),root(y)
            if a==b:
                forest=False; break
            roots[a]=b
        if forest:full.append(tuple(comb))
        types=[(int(i in S)+int(n+i in S)) for i in range(n)]
        zeros=[i for i,t in enumerate(types) if t==0]
        cover=all(not(types[i]==0 and types[(i+1)%n]==0) for i in range(n))
        internal=sum(x in S and y in S for x,y in E)
        candidate=cover and (internal==0 if n%2 else internal<=1)
        if candidate:predicted.append(tuple(comb))
    assert set(full)==set(predicted),(n,len(full),len(predicted),len(set(full)^set(predicted)))
    expected=(n*(2**((n-1)//2))) if n%2 else (n*(3*(n//2)+2)*2**((n//2)-2))
    assert len(full)==expected,(n,len(full),expected)
    return n,k,len(full)

if __name__=='__main__':
    for n in range(3,13):print('forest_exact',*check(n))
    print('OK exact all size-k candidates, n=3,...,12')
