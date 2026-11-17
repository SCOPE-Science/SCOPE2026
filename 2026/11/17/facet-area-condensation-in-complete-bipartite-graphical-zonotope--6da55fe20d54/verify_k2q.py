"""Direct finite geometric checks for Euclidean facets of K_{2,q} graphical zonotopes."""
import math
import itertools
import numpy as np
from scipy.spatial import ConvexHull


def all_vertices(q):
    n=q+2
    edges=[(h,j) for h in (0,1) for j in range(2,n)]
    seen=set()
    for perm in itertools.permutations(range(n)):
        rank=[0]*n
        for i,u in enumerate(perm):rank[u]=i
        x=[0]*n
        for u,v in edges:
            # centered [0,e_u-e_v] segment
            if rank[u]>rank[v]:
                x[u]+=1;x[v]-=1
            else:
                x[u]-=1;x[v]+=1
        seen.add(tuple(x))
    # vertices of centered original zonotope are 1/2 of sign vectors
    return np.array(list(seen),dtype=float)/2


def predicted_facets(q):
    n=q+2
    output=[]
    for mask in range(1,(1<<n)-1):
        S={i for i in range(n) if mask&(1<<i)}
        T=set(range(n))-S
        if len(S)==1 and next(iter(S))>=2 or len(T)==1 and next(iter(T))>=2:
            area=(q-1)*2**(q-2)*math.sqrt(q+1)
            typ='leaf'
        elif len(S)==1 and next(iter(S))<2 or len(T)==1 and next(iter(T))<2:
            area=math.sqrt(q+1)
            typ='hub'
        elif len(S.intersection({0,1}))==1 and len(T.intersection({0,1}))==1:
            b=len(S.intersection(set(range(2,n))))
            if not (1<=b<=q-1): continue
            area=math.sqrt((b+1)*(q-b+1))
            typ='mixed'
        else:
            continue
        output.append((S,area,typ))
    return output


def check(q):
    n=q+2
    V=all_vertices(q)
    # zero-sum orthonormal basis
    U=np.linalg.svd(np.eye(n)-np.ones((n,n))/n)[0][:,:n-1]
    X=V@U
    outer=ConvexHull(X)
    facets=predicted_facets(q)
    assert len(facets)==2*q+2**(q+1)
    total=0.0
    groups={'leaf':[],'hub':[],'mixed':[]}
    for S,pred,typ in facets:
        v=np.array([int(i in S)-len(S)/n for i in range(n)])
        heights=V@v
        onface=V[np.abs(heights-np.max(heights))<1e-9]
        center=onface.mean(axis=0)
        directions=np.linalg.svd(onface-center)[2][:n-2].T
        c=(onface-center)@directions
        area=ConvexHull(c).volume if n-2>=2 else float(np.ptp(c[:,0]))
        assert abs(area-pred)<1e-7, (q,S,area,pred)
        total+=area
        groups[typ].append(area)
    formula=2*q*(q-1)*2**(q-2)*math.sqrt(q+1)+2*sum(math.comb(q,b)*math.sqrt((b+1)*(q-b+1)) for b in range(q+1))
    assert abs(total-formula)<1e-6
    assert abs(outer.area-formula)<1e-6
    expected_vol=math.sqrt(q+2)*q*2**(q-1)
    assert abs(outer.volume-expected_vol)<1e-6
    print(f'q={q} dimension={n-1} vertices={len(V)} facets={len(facets)} leaf={len(groups["leaf"])} hub={len(groups["hub"])} mixed={len(groups["mixed"])} A={total:.9f} volume={outer.volume:.9f}: PASS')

def asymptotic_check(q):
    # Stable probabilities for B ~ Binomial(q,1/2).
    from scipy.stats import binom
    b=np.arange(q+1)
    Ef=float(np.dot(binom.pmf(b,q,0.5),np.sqrt((b+1)*(q-b+1))))
    ratio=4*Ef/(q*(q-1)*math.sqrt(q+1))
    loss=ratio/(1+ratio)
    scaled=(q**1.5)*loss
    assert abs(scaled-2)<10/math.sqrt(q), (q,scaled)
    assert abs(Ef-(q/2+0.75)) < 1/q, (q,Ef)
    print(f'q={q} binomial_mean={Ef:.9f} scaled_nonleaf_fraction={scaled:.9f}: PASS')

if __name__=='__main__':
    for q in (2,3,4):check(q)
    for q in (100,1000,3000):asymptotic_check(q)
    print('ALL_K2Q_FACET_GEOMETRY_AND_ASYMPTOTICS_PASS')
