"""Reproducible finite-dimensional Euclidean ridge checks for parity halfcubes.
Public domain science only. Run: python halfcube_ridge_verify.py
"""
from itertools import product, combinations
from math import factorial, sqrt, comb, acos, pi
import numpy as np
from scipy.spatial import ConvexHull

def parity(n):
    return np.asarray([v for v in product((0,1), repeat=n) if sum(v)%2==0],float)

def facets(n):
    out=[]
    for i in range(n):
        for b in (0,1):
            normal=np.zeros(n)
            normal[i]=2*b-1
            out.append((('coordinate',i,b),normal, float(b), None))
    for v in product((0,1), repeat=n):
        if sum(v)%2 !=1: continue
        a=np.asarray(v,float)
        # hamming distance from v >=1, hence sum (2v_i-1)*x_i <= sum v_i-1
        normal=2*a-1
        out.append((('simplex',v),normal,float(sum(v)-1),None))
    return out

def affine_volume(points, d):
    base=points[0]
    u,s,vh=np.linalg.svd(points[1:]-base,full_matrices=False)
    rank=int(np.sum(s>1e-9))
    if rank!=d: return 0.0,rank
    if d==1:
        proj=(points-base)@vh[:1].T
        return np.ptp(proj[:,0]),rank
    proj=(points-base)@vh[:d].T
    hull=ConvexHull(proj)
    return hull.volume,rank

def run(n):
    V=parity(n); F=facets(n)
    assert abs(ConvexHull(V).volume-(1-2**(n-1)/factorial(n)))<1e-7
    assert len(F)==2*n+2**(n-1)
    def get_points(a):
        return V[np.abs(V@a[1]-a[2])<1e-9]
    S=0.0
    for f in F:
        pts=get_points(f)
        measure,rank=affine_volume(pts,n-1)
        assert rank==n-1
        if f[0][0]=='coordinate':
            expected=1-2**(n-2)/factorial(n-1)
        else:
            expected=sqrt(n)/factorial(n-1)
        assert abs(measure-expected)<1e-7,(n,f,measure,expected)
        S+=measure
    rhsS=2*n*(1-2**(n-2)/factorial(n-1))+2**(n-1)*sqrt(n)/factorial(n-1)
    assert abs(S-rhsS)<1e-7
    ridge_data={'CC':[0,0.],'CS':[0,0.], 'SS':[0,0.]}
    V2=0.0
    for a,b in combinations(F,2):
        pts=V[(np.abs(V@a[1]-a[2])<1e-9)&(np.abs(V@b[1]-b[2])<1e-9)]
        if len(pts)<n-1: continue
        val,rank=affine_volume(pts,n-2)
        if rank<n-2: continue
        t=('C' if a[0][0]=='coordinate' else 'S')+('C' if b[0][0]=='coordinate' else 'S')
        ridge_data[t][0]+=1
        ridge_data[t][1]+=val
        angle=acos(np.dot(a[1],b[1])/(np.linalg.norm(a[1])*np.linalg.norm(b[1])))
        V2+=angle*val/(2*pi)
        if t=='CC':
            assert abs(angle-pi/2)<1e-8
            assert abs(val-(1-2**(n-3)/factorial(n-2)))<1e-7
        elif t=='CS':
            assert abs(angle-acos(1/sqrt(n)))<1e-8
            assert abs(val-sqrt(n-1)/factorial(n-2))<1e-7
        else: raise AssertionError('Simplex-simplex ridge exists')
    expectedCC=0 if n==4 else 4*comb(n,2)
    expectedCS=n*2**(n-1)
    assert ridge_data['CC'][0]==expectedCC and ridge_data['CS'][0]==expectedCS and ridge_data['SS'][0]==0,(n,ridge_data)
    formula=(0 if n==4 else comb(n,2)*(1-2**(n-3)/factorial(n-2)))+(n*2**(n-1)*sqrt(n-1)/(2*pi*factorial(n-2)))*acos(1/sqrt(n))
    assert abs(V2-formula)<1e-7,(n,V2,formula)
    print('n=%d vertices=%d facets=%d CC=%d CS=%d SS=%d surface=%.12f V[n-2]=%.12f PASS'%(n,len(V),len(F),ridge_data['CC'][0],ridge_data['CS'][0],ridge_data['SS'][0],S,V2))

if __name__=='__main__':
    for n in range(4,8):run(n)
    print('HALFCUBE_STEINER_PASS')
