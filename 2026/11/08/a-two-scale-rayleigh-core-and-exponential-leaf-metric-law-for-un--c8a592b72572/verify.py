"""Exact finite-graph metric identities and independent probabilistic sanity checks."""
from itertools import combinations
import random, math


def fw(a):
    d=[r[:] for r in a]
    for k in range(len(d)):
        for i in range(len(d)):
            for j in range(len(d)):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d


def instance(a,b,rng):
    weights=[[rng.randint(1,60) for j in range(b)] for i in range(a)]
    n=a+b
    big=10**8
    adj=[[0 if i==j else big for j in range(n)] for i in range(n)]
    for i in range(a):
        for j in range(b):
            adj[i][a+j]=adj[a+j][i]=weights[i][j]
    d=fw(adj)
    core=[[0 if i==k else min(weights[i][j]+weights[k][j] for j in range(b)) for k in range(a)] for i in range(a)]
    closure=fw(core)
    count=0
    for i in range(a):
        for k in range(a):
            assert d[i][k]==closure[i][k], ('core identity',a,b,i,k)
            count+=1
    diameter=max(max(r) for r in closure)
    for j in range(b):
        w=min(weights[i][j] for i in range(a))
        for i in range(a):
            assert w<=d[a+j][i]<=w+diameter, ('tag-core bounds',a,b,i,j)
            count+=1
        for h in range(j+1,b):
            wh=min(weights[i][h] for i in range(a))
            assert w+wh<=d[a+j][a+h]<=w+wh+diameter, ('tag-tag bounds',a,b,j,h)
            count+=1
    return count


def verify():
    rng=random.Random(20022019)
    cnt=0
    for a in range(2,6):
        for b in range(1,10):
            for trial in range(17):
                cnt+=instance(a,b,rng)
    # Exact one-pair survival for the two-hub model: P(sqrt(b)*M>t)=(e^-t/sqrt(b)*(1+t/sqrt(b)))^b
    for b in [16,64,256,1024,65536]:
        for t in [0.25,0.5,1.0,2.0,3.0]:
            v=math.exp(-t/math.sqrt(b))*(1+t/math.sqrt(b))
            exact=v**b
            target=math.exp(-t*t/2)
            assert abs(exact-target)<12/math.sqrt(b)
            cnt+=1
    # A share of candidate locations with two different light spokes is o(1)
    # A double-light-spoke minimum can use at most the three independent edge times.
    for b in [200,1000,5000,20000]:
        z=1.75/math.sqrt(b)
        one=1-math.exp(-z)*(1+z)
        assert 0<one<z*z/2 and b*one<1.75**2/2
        cnt+=1
    print('VERIFY_OK',cnt,'exact deterministic and formula assertions')

if __name__=='__main__':
    verify()
