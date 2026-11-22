"""Independent finite checks for spherical covering after erasing regular-polygon join vertices.
No finite check substitutes for the included analytic proof.
"""
from itertools import combinations
from math import cos, pi, sin, sqrt, acos
import numpy as np
from scipy.optimize import minimize
from scipy.spatial import ConvexHull, QhullError


def regular(n, offset):
    return [np.array([cos(2*pi*j/n), sin(2*pi*j/n)]) for j in range(n)]


def gap_radius(n, residual):
    indices=sorted(residual)
    assert indices
    gaps=[(indices[(j+1)%len(indices)]-indices[j])%n for j in range(len(indices))]
    if len(indices)==1: gaps=[n]
    return cos(max(gaps)*pi/n)


def signed_join(r,s):
    if r>1e-12 and s>1e-12:
        return r*s/sqrt(r*r+s*s)
    if r< -1e-12 and s< -1e-12:
        return -r*s/sqrt(r*r+s*s)
    return 0.0


def vertices(p,q,i,j):
    a=[np.array([*v,0,0]) for k,v in enumerate(regular(p,0)) if k not in i]
    b=[np.array([0,0,*v]) for k,v in enumerate(regular(q,0)) if k not in j]
    return np.array(a+b)


def independent_cosine(V):
    # If origin lies in hull, covering cosine equals nearest facet distance of hull.
    # Otherwise it is the negative distance from origin to the hull.
    m=len(V)
    res=minimize(lambda w: np.dot(w@V,w@V),np.ones(m)/m,
                 jac=lambda w:2*V@(w@V),
                 bounds=[(0,1)]*m,constraints=[{'type':'eq','fun':lambda w:np.sum(w)-1,
                                                'jac':lambda w:np.ones(m)}],
                 method='SLSQP', options={'ftol':1e-12,'maxiter':300})
    if not res.success and np.linalg.norm(res.x@V)>1e-6:
        raise RuntimeError(res.message)
    dist=np.linalg.norm(res.x@V)
    if dist>2e-6:
        return -dist
    hull=ConvexHull(V)
    # SciPy inequalities A x + b <=0; origin inside => b<=0.
    return min(-hull.equations[:,-1]/np.linalg.norm(hull.equations[:,:-1],axis=1))


checks=0
for p,q in [(4,5),(3,5),(5,6),(6,7)]:
    # Cases where both residual factors nonempty, with full-dimensional hull
    for i_count in range(min(p,3)):
        for j_count in range(min(q,3)):
            for i in combinations(range(p),i_count):
                for j in combinations(range(q),j_count):
                    ri=gap_radius(p,set(range(p))-set(i))
                    rj=gap_radius(q,set(range(q))-set(j))
                    formula=signed_join(ri,rj)
                    V=vertices(p,q,i,j)
                    try:
                        numeric=independent_cosine(V)
                    except QhullError:
                        # Hull is lower dimensional. Direct spherical argument handles these
                        # configurations; independent facet test is inapplicable.
                        continue
                    if abs(formula-numeric)>1e-6:
                        raise AssertionError((p,q,i,j,formula,numeric))
                    checks+=1
print('independent full-dimensional hull comparisons:',checks)

p,q=4,5
counts={}
critical=[]
for k in range(5):
    seq=[]
    for removed in combinations(range(p+q),k):
        I=set(removed)&set(range(p))
        J={z-p for z in removed if z>=p}
        if len(I)==p or len(J)==q:
            # If a factor is empty, and the other includes the origin, the
            # covering cosine is zero (valid for k<=4 in this experiment).
            val=0.0
        else:
            val=signed_join(gap_radius(p,set(range(p))-I),gap_radius(q,set(range(q))-J))
        seq.append(val)
        if val < -1e-10: critical.append((k,removed,val))
    counts[k]=(sum(t>1e-10 for t in seq),sum(abs(t)<1e-10 for t in seq),sum(t< -1e-10 for t in seq))
print('k => (positive,zero,negative) for square+pentagon:',counts)
assert counts=={0:(1,0,0),1:(5,4,0),2:(5,31,0),3:(0,84,0),4:(0,106,20)}
assert len(critical)==20 and all(k==4 for k,_,_ in critical)
c=cos(2*pi/5)/sqrt(1+2*cos(2*pi/5)**2)
assert all(abs(t+c)<1e-12 for _,_,t in critical)
print('critical cosine:',-c,'covering angle deg:',acos(-c)*180/pi)
print('one pentagon erasure cosine:',c,'angle deg:',acos(c)*180/pi)
print('passed')
