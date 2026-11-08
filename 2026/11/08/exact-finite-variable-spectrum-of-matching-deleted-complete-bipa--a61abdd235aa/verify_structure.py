"""Independent finite checks of the intrinsic bipartition and forbidden matching.
The theory-count formula is checked by enumerating canonical clipped parameters.
This does not replace the unbounded-variable-width mathematical proof.
"""
from math import comb

def make_graph(a,b,t):
    n=a+b
    edge={(i,a+j) for i in range(a) for j in range(b) if not (i==j and i<t)}
    E=lambda x,y: (min(x,y),max(x,y)) in edge
    return n,E

models=0
pairs=0
for a in range(3,10):
    for b in range(a,10):
        for t in range(a+1):
            n,E=make_graph(a,b,t)
            def same(x,y):
                return x==y or any(E(x,z) and E(y,z) for z in range(n))
            def missing(x,y):
                return x!=y and not E(x,y) and not same(x,y)
            for x in range(n):
                for y in range(n):
                    pairs+=1
                    assert same(x,y) == ((x<a)==(y<a))
                    assert missing(x,y) == (t>0 and
                          ((x<t and y==a+x) or (y<t and x==a+y)))
            assert sum(any(missing(x,y) for y in range(n)) for x in range(a))==t
            assert sum(any(missing(x,y) for y in range(n)) for x in range(a,n))==t
            models+=1
print('structural_models=%d ordered_vertex_pairs=%d mismatches=0' % (models,pairs))

for k in range(3,9):
    seen=set()
    for t in range(0,k+1):
        for u in range(k+1):
            for v in range(u,k+1):
                if t==0:
                    if u<3 or v<3: continue
                    seen.add(('zero',u,v))
                elif t+u>=3 and t+v>=3:
                    seen.add(('positive',t,u,v))
    expected=(k**3+4*k*k-7*k-2)//2
    assert len(seen)==expected
    print('k=%d canonical_profiles=%d formula=%d' % (k,len(seen),expected))
print('STRUCTURAL AND THEORY-COUNT CHECKS PASSED')
