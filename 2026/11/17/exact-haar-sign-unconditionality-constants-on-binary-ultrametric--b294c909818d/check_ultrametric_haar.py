"""Exact rational verification of Haar sign transforms in finite ultrametrics."""
from fractions import Fraction as Q
from itertools import product


def leaf_bits(i,d):
    return tuple((i>>(d-1-t))&1 for t in range(d))


def all_nodes(d):
    return [p for t in range(d) for p in product((0,1), repeat=t)]


def distance_depth(x,y,d):
    return next(i for i in range(d) if x[i]!=y[i])


def predicted(r):
    d=len(r)
    F=[Q(2*s,3)+Q(5,9)+Q(4,9)*Q(-1,2)**s for s in range(d)]
    vals=[]
    for k in range(d):
        v=sum((r[t-1] - (r[t] if t<d else 0))*F[t-k-1] for t in range(k+1,d+1))/r[k]
        vals.append(v)
    return max(vals),vals


def row_kernel(x,d,signs,nodes):
    out=[]
    for z in product((0,1),repeat=d):
        k=1
        for j,p in enumerate(nodes):
            t=len(p)
            if x[:t]==p and z[:t]==p:
                k+=signs[j]*(2**t)*(1 if x[t]==z[t] else -1)
        out.append(Q(k,2**d))
    return out


def tree_norm(masses,d,r):
    total=Q(0)
    for t in range(1,d+1):
        edge=Q(r[t-1]-(r[t] if t<d else 0),2)
        for p in product((0,1),repeat=t):
            a=sum(masses[j] for j,z in enumerate(product((0,1),repeat=d)) if z[:t]==p)
            total+=edge*abs(a)
    return total


def verify(r):
    d=len(r); nodes=all_nodes(d); xs=list(product((0,1), repeat=d))
    target,pairs_by_depth=predicted(r)
    maxv=Q(0); by_depth=[Q(0)]*d; count=0
    for sgn in product((-1,1),repeat=len(nodes)):
        rows=[row_kernel(x,d,sgn,nodes) for x in xs]
        for i,x in enumerate(xs):
            for j in range(i+1,len(xs)):
                k=distance_depth(x,xs[j],d)
                v=tree_norm([rows[i][h]-rows[j][h] for h in range(2**d)],d,r)/r[k]
                if v>by_depth[k]:by_depth[k]=v
                if v>maxv:maxv=v
                count+=1
    assert maxv==target,(r,maxv,target)
    assert by_depth==pairs_by_depth,(r,by_depth,pairs_by_depth)
    print('EXACT_ALL_TRANSFORMS_AND_PAIRS',d,count,'optimal',maxv,'per-depth',[str(z) for z in by_depth])


def verify_row_F():
    for d in range(1,9):
        opt=Q(2*d,3)+Q(5,9)+Q(4,9)*Q(-1,2)**d
        best=Q(0)
        for ep in product((-1,1),repeat=d):
            m=Q(1); mass=Q(0)
            for e in ep:
                mass+=abs(m-e)/2
                m=(m+e)/2
            score=mass+abs(m)
            best=max(score,best)
        assert best==opt,(d,best,opt)
    print('EXACT_SIGNED_HAAR_ROW_BELLMAN_PASSED depths=1..8')


if __name__=='__main__':
    verify_row_F()
    for r in [(Q(1),Q(1,2)),(Q(1),Q(2,3),Q(1,4)),(Q(1),Q(9,10),Q(1,10)),(Q(1),Q(1,2),Q(1,4))]:
        verify(r)
    print('ALL_EXACT_ULTRAMETRIC_HAAR_CHECKS_PASSED')
