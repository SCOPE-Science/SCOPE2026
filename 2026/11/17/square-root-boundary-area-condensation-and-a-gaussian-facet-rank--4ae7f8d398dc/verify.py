"""Independent finite Euclidean checks for cube + crosspolytope polar geometry."""
import itertools, math
import numpy as np
from scipy.spatial import ConvexHull
from scipy.special import gammaln, logsumexp

def exact_formula(d):
    k=np.arange(1,d+1)
    shell=np.array([2**d*math.comb(d,int(j))*math.sqrt(j)/math.factorial(int(j)-1) for j in k],float)
    volume=sum(2**d * math.comb(d,j)/math.factorial(j) for j in range(d+1))
    return shell,volume

def hull_test(d):
    verts=[]
    for s in itertools.product((-1,1),repeat=d):
        for j in range(d):
            v=np.array(s,float);v[j]*=2;verts.append(v)
    hull=ConvexHull(np.array(verts),qhull_options='Qx')
    shells={j:0.0 for j in range(1,d+1)}
    norms={}
    # Triangular decomposition of d-1 faces by qhull; simplex area by Gram determinant
    for simp,eq in zip(hull.simplices,hull.equations):
        points=hull.points[simp]
        edge=points[1:]-points[0]
        gram=edge@edge.T
        area=math.sqrt(max(0,float(np.linalg.det(gram))))/math.factorial(d-1)
        unit=eq[:d]/np.linalg.norm(eq[:d]);
        support=int(np.sum(np.abs(unit)>1e-7))
        assert np.allclose(np.abs(unit[np.abs(unit)>1e-7]),1/math.sqrt(support),atol=1e-7)
        shells[support]+=area
    predicted,v=exact_formula(d)
    for j,x in shells.items(): assert math.isclose(x,predicted[j-1],rel_tol=1e-8,abs_tol=1e-8),(d,j,x,predicted[j-1])
    assert math.isclose(hull.volume,v,rel_tol=1e-8,abs_tol=1e-8),(d,hull.volume,v)
    print('exact hull',d,'facets-triangulated',len(hull.simplices),'volume',hull.volume,'area',hull.area)

def asymptotic(d):
    k=np.arange(1,d+1,dtype=float)
    loga = gammaln(d+1)-gammaln(k+1)-gammaln(d-k+1)+0.5*np.log(k)-gammaln(k)
    logv = gammaln(d+1)-gammaln(np.arange(d+1)+1)-gammaln(d-np.arange(d+1)+1)-gammaln(np.arange(d+1)+1)
    p=np.exp(loga-logsumexp(loga));
    S_V=math.exp(logsumexp(loga)-logsumexp(logv))
    y=(k-np.sqrt(d))/d**0.25
    mean=np.dot(p,y);var=np.dot(p,(y-mean)**2)
    mass=np.sum(p[np.abs(y)<2])
    print('asymptotic',d,'mode',int(k[np.argmax(p)]),'mean_scaled',round(mean,5),'var_scaled',round(var,5),'|y|<2 mass',round(mass,5),'S/V/d^.75',round(S_V/d**0.75,5))

if __name__=='__main__':
    for d in range(2,6):hull_test(d)
    for d in [100,1000,10000]:asymptotic(d)
    print('CUBE_DIAMOND_SURFACE_PASS')
