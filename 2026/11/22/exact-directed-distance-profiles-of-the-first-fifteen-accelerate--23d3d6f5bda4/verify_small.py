"""Independent tuple-state construction of the finite directed graph.
Compare integer graph metrics with the checked census file for levels through 9.
"""
from collections import deque

def build(level):
    vertices=[(0,), (1,)]
    P={(0,):(1,), (1,):(0,)}
    Q=P.copy()
    for n in range(2,level+1):
        newP,newQ={},{}
        for a in vertices:
            newP[(0,)+a]=(1,)+Q[a]
            newP[(1,)+a]=(0,)+P[a]
            newQ[(0,)+a]=(1,)+Q[Q[a]]
            newQ[(1,)+a]=(0,)+P[P[a]]
        P,Q=newP,newQ
        vertices=list(P)
    return P,Q

def summary(n):
    p,q=build(n)
    v=list(p)
    maxd=0;mind=1<<20;diam_pairs=0
    for s in v:
        dis={s:0};todo=deque([s]);far=0
        while todo:
            x=todo.popleft();d=dis[x];far=max(far,d)
            for y in (p[x],q[x]):
                if y not in dis:dis[y]=d+1;todo.append(y)
        assert len(dis)==len(v)
        if far>maxd:maxd=far;diam_pairs=sum(z==far for z in dis.values())
        elif far==maxd:diam_pairs+=sum(z==far for z in dis.values())
        mind=min(mind,far)
    return mind,maxd,diam_pairs

expected=[(1,1,2),(2,2,4),(3,3,16),(4,5,8),(6,7,16),(7,8,96),(9,10,32),(10,11,64),(11,13,16)]
for n in range(1,10):
    t=summary(n)
    assert t==expected[n-1],(n,t,expected[n-1])
    print(n,t)
print('Independent tuple-state verification PASS')
