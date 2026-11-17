"""Direct numerical verification of polytope volumes and each ridge area.
Requires NumPy and SciPy; independently projects every ridge vertex hull.
"""
from itertools import product, combinations
from math import factorial, sqrt
import numpy as np
from scipy.spatial import ConvexHull

def check(ms):
    r=len(ms);n=sum(ms)
    blocks=[];s=0
    for m in ms:blocks.append(tuple(range(s,s+m)));s+=m
    vertices=[np.zeros(n)]
    for b in blocks:
        for nonempty in range(1,1<<len(b)):
            x=np.zeros(n)
            for j,k in enumerate(b):
                if (nonempty>>j)&1:x[k]=1
            vertices.append(x)
    V=np.array(vertices)
    actual_vol=ConvexHull(V).volume
    theory_vol=np.prod([factorial(m) for m in ms])/factorial(n)
    assert abs(actual_vol/theory_vol-1)<1e-7,(ms,actual_vol,theory_vol)
    normals=[];rhs=[];tags=[]
    for k in range(n):
        v=np.zeros(n);v[k]=-1
        normals.append(v);rhs.append(0);tags.append(('L',k))
    for choices in product(*blocks):
        v=np.zeros(n);v[list(choices)]=1
        normals.append(v);rhs.append(1);tags.append(('U',choices))
    sums={'LL':0,'LU':0,'UU':0}; checked=0
    for i,j in combinations(range(len(normals)),2):
        face=V[(V@normals[i]==rhs[i]) & (V@normals[j]==rhs[j])]
        if len(face)<n-1:continue
        centered=face[1:]-face[0]
        _,svals,B=np.linalg.svd(centered,full_matrices=False)
        if sum(svals>1e-8)!=n-2:continue
        proj=(face-face[0])@B[:n-2].T
        area=ConvexHull(proj).volume
        t1,t2=tags[i],tags[j]
        typ=''.join(sorted([t1[0],t2[0]]))
        if typ=='LL':
            a,b=t1[1],t2[1]
            ba=next(k for k,Bb in enumerate(blocks) if a in Bb)
            bb=next(k for k,Bb in enumerate(blocks) if b in Bb)
            tms=ms[:]
            tms[ba]-=1;tms[bb]-=1
            predicted=np.prod([factorial(m) for m in tms])/factorial(n-2)
        elif typ=='LU':
            L=t1 if t1[0]=='L' else t2
            q=next(k for k,Bb in enumerate(blocks) if L[1] in Bb)
            tms=[m-1 for m in ms]
            tms[q]-=1
            predicted=sqrt(r)*np.prod([factorial(m) for m in tms])/factorial(n-2)
        else:
            U1=t1[1];U2=t2[1]
            q=next(k for k in range(r) if U1[k]!=U2[k])
            tms=[m-1 for m in ms]
            tms[q]-=1
            predicted=sqrt(2*r-1)*np.prod([factorial(m) for m in tms])/factorial(n-2)
        if not abs(area-predicted)<1e-7*predicted:
            raise AssertionError((ms,t1,t2,area,predicted))
        sums[typ]+=area;checked+=1
    scale=n*(n-1)*theory_vol
    goal={'LL':r*r/2,'LU':r*sqrt(r),'UU':r*sqrt(2*r-1)/2}
    for typ in sums:
        assert abs(sums[typ]/scale-goal[typ])<1e-7,(ms,typ,sums[typ]/scale,goal[typ])
    return checked,sums

if __name__=='__main__':
    prof=[(2,2),(2,3),(2,2,2),(2,3,2),(3,3)]
    n=0
    for ms in prof:
        checked,sums=check(list(ms));n+=checked
        print(ms,checked,{k:round(v,8) for k,v in sums.items()})
    print('LAYERED_CHAIN_METRIC_PASS',len(prof),n)
