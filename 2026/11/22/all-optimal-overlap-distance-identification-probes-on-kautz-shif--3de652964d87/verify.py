"""Independent finite checks for prefix-transversal overlap fingerprints."""
from itertools import product
from collections import deque

def words(q,n):
    return [a for a in product(range(q),repeat=n) if all(a[i]!=a[i+1] for i in range(n-1))]

def dist_bfs(vs,q):
    by={w:i for i,w in enumerate(vs)}
    D=[]
    for root in vs:
        dd={root:0}; que=deque([root])
        while que:
            u=que.popleft()
            for a in range(q):
                if a!=u[-1]:
                    w=u[1:]+(a,)
                    if w not in dd: dd[w]=dd[u]+1; que.append(w)
        assert len(dd)==len(vs)
        D.append([dd[w] for w in vs])
    return D

def overlap(u,v):
    n=len(u)
    if u==v: return 0
    return n-max([k for k in range(n) if u[-k:]==v[:k]] or [0])

def check(q,n,exhaustive=True):
    vs=words(q,n); N=len(vs); by={v:i for i,v in enumerate(vs)}
    classes={}
    for j,v in enumerate(vs): classes.setdefault(v[:-1],[]).append(j)
    cs=list(classes.values()); d=q-1
    assert all(len(c)==d for c in cs)
    D=dist_bfs(vs,q)
    for i,u in enumerate(vs):
        for j,v in enumerate(vs): assert D[i][j]==overlap(u,v),(q,n,u,v,D[i][j],overlap(u,v))
    for c in cs:
        for i in range(len(c)):
            for j in range(i):
                assert all(D[w][c[i]]==D[w][c[j]] for w in range(N) if w not in (c[i],c[j]))
    total=d**len(cs)
    if exhaustive:
        for omissions in product(*cs):
            omit=set(omissions); basis=[i for i in range(N) if i not in omit]
            fingerprint={tuple(D[s][v] for s in basis) for v in range(N)}
            assert len(fingerprint)==N,(q,n,omissions)
    print('BFS_AND_CLASSIFICATION_OK',q,n,'vertices',N,'classes',len(cs),'minimum',N-len(cs),'bases',total,'exhaustive',exhaustive)

if __name__=='__main__':
    for q,n,e in ((3,2,True),(3,3,True),(3,4,True),(4,2,True),(5,2,True),(4,3,False)):
        check(q,n,e)
    print('VERIFY_OK')
