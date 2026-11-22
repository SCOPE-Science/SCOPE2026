"""Independent canonical-interval component and code-capacity verifier."""
from itertools import combinations,product
from collections import Counter,defaultdict

def run(q,m):
    # Encode a palindromic word by its left half, including center.
    vertices=list(product(range(q),repeat=m+1))
    E=set()
    for rad in range(1,m+1):
        for pair in combinations(range(q),2):
            a,b=pair
            p=tuple((a,b)[i%2] for i in range(rad+1))
            t=tuple((b,a)[i%2] for i in range(rad+1))
            for outside in product(range(q),repeat=m-rad):
                E.add(frozenset((outside+p,outside+t)))
    assert len(E)==q*(q**m-1)//2
    root={h:h for h in vertices}
    def find(v):
        if root[v]!=v:root[v]=find(root[v])
        return root[v]
    for e in E:
        x,y=tuple(e)
        rx,ry=find(x),find(y)
        assert rx!=ry, ('not forest',q,m)
        root[rx]=ry
    groups=defaultdict(set)
    for v in vertices:groups[find(v)].add(v)
    actual=Counter(len(g) for g in groups.values())
    want=Counter({1:q**m})
    for rad in range(1,m):want[2**rad]+=q*(q-1)//2*(q-2)*q**(m-rad-1)
    want[2**m]+=q*(q-1)//2
    assert actual==want,(q,m,actual,want)
    # Explicit optimal two-read code: retain center <= its neighbor.
    code={v for v in vertices if v[-1]<=v[-2]}
    assert len(code)==q**m*(q+1)//2
    assert all(not(e<=code) for e in E)
    # Disjoint forbidden pairs form a matching covering all vertices with unequal middle letters.
    matched=set()
    for v in vertices:
        if v[-1]!=v[-2] and v[-1]<v[-2]:
            w=v[:-2]+(v[-1],v[-2])
            assert frozenset((v,w)) in E
            assert v not in matched and w not in matched
            matched.update((v,w))
    assert len(matched)==q**m*(q-1)
    return q,m,len(vertices),len(E),dict(sorted(actual.items())),len(code)

if __name__=='__main__':
    for q,m in [(2,9),(3,6),(4,4),(5,3),(6,3),(7,2)]:
        print(run(q,m))
    print('PASS: canonical edge forest census, sharp matching bound and optimal codes')
