"""Standalone finite geometric checks for hypersimplex ridge-curvature formulas.
Requires Python 3, NumPy and SciPy. No literature data or network required.
"""
import itertools
import math
import numpy as np
from scipy.spatial import ConvexHull


def eulerian_row(order):
    a=[1]
    for m in range(2,order+1):
        a=[(j+1)*(a[j] if j<len(a) else 0)+(m-j)*(a[j-1] if j else 0) for j in range(m)]
    return a


def eulerian(order,idx):
    if idx<0 or idx>=order:return 0
    return eulerian_row(order)[idx]


def sliced_volume(points):
    center=points[0]
    w=points-center
    _,sing,vt=np.linalg.svd(w,full_matrices=False)
    dim=int(np.sum(sing>1e-8))
    p=w@vt[:dim].T
    if dim==0:return 0,0.0
    if dim==1:return 1,float(p.max()-p.min())
    return dim,float(ConvexHull(p).volume)


checks=0
for n in range(4,10):
    norm=np.eye(n)-np.ones((n,n))/n
    for k in range(2,n-1):
        verts=np.array([[int(j in subset) for j in range(n)]
                       for subset in itertools.combinations(range(n),k)],float)
        if len(verts)<n:continue
        dim0,_=sliced_volume(verts)
        assert dim0==n-1,(n,k,dim0)
        alpha=math.acos(-1/(n-1))
        beta=math.acos(1/(n-1))
        num={"same":0,"mixed":0}
        totals={"same":0.,"mixed":0.}
        for i,j in itertools.combinations(range(n),2):
            for s,t in itertools.product((0,1),repeat=2):
                pts=verts[(verts[:,i]==s)&(verts[:,j]==t)]
                if len(pts)<2:continue
                dim,actual=sliced_volume(pts)
                if dim!=n-3:continue
                u=(1 if s else -1)*norm[i]
                v=(1 if t else -1)*norm[j]
                geom_angle=math.acos(np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v)))
                cat='same' if s==t else 'mixed'
                expected_angle=alpha if cat=='same' else beta
                assert abs(geom_angle-expected_angle)<2e-8
                shift=s+t
                expected_vol=math.sqrt(n-2)*eulerian(n-3,k-shift-1)/math.factorial(n-3)
                assert math.isclose(actual,expected_vol,rel_tol=2e-8,abs_tol=2e-8),(n,k,s,t,actual,expected_vol)
                num[cat]+=1
                totals[cat]+=actual*geom_angle/(2*math.pi)
                checks+=1
        M=eulerian(n-3,k-2)
        S=eulerian(n-3,k-1)+eulerian(n-3,k-3)
        h=math.sqrt(n-2)*math.comb(n,2)/(2*math.pi*math.factorial(n-3))
        assert math.isclose(totals['same'],h*S*alpha,rel_tol=1e-8,abs_tol=1e-8)
        assert math.isclose(totals['mixed'],h*2*M*beta,rel_tol=1e-8,abs_tol=1e-8)
        assert num['same']==math.comb(n,2)*(int(k<=n-3)+int(k>=3))
        assert num['mixed']==n*(n-1)
print('RIDGE_VOLUME_NORMAL_GEOMETRY_PASS cases=',checks,'n=4..9')

for n in (80,160,320,640):
    a=eulerian_row(n-3)
    sigma=math.sqrt((n-2)/12)
    vals=[]
    for z in (0,0.5,1.0,1.5):
        k=round(n/2+z*sigma)
        j=k-2
        s=(a[j-1] if j>0 else 0)+(a[j+1] if j+1<len(a) else 0)
        R=math.acos(-1/(n-1))/math.acos(1/(n-1)) * (s/(2*a[j]))
        zz=(k-n/2)/sigma
        predicted=6*(zz*zz-1)+4/math.pi
        vals.append(abs(n*(R-1)-predicted))
    assert max(vals)<1,(n,vals)
    print('CRITICAL_WINDOW n=',n,'max_unscaled_residual=',round(max(vals),5))
print('HYPERSIMPLEX_CURVATURE_PASS')
