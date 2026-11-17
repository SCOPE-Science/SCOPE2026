#!/usr/bin/env python3
"""Finite independent Euclidean convex-hull checks for uniform cyclic chainlink polytopes."""
import itertools
import math
import numpy as np
from scipy.spatial import ConvexHull


def analytic(s, A, t):
    ell = A*t
    delta = math.sqrt(A*A-2*ell*ell)
    lp, lm = (A+delta)/2, (A-delta)/2
    volume = lp**s + lm**s
    dl = s*ell/delta*(lm**(s-1)-lp**(s-1))
    dA = s/2*((1+A/delta)*lp**(s-1)+(1-A/delta)*lm**(s-1))
    surface = 2*dA+(2-math.sqrt(2))*dl
    return volume,surface


def hull_measure(s,A,t):
    inequalities=[]
    rhs=[]
    for j in range(s):
        r=np.zeros(s);r[j]=-1;inequalities.append(r);rhs.append(0.0)
        r=np.zeros(s);r[j]=1;inequalities.append(r);rhs.append(A)
        r=np.zeros(s);r[j]=1;r[(j+1)%s]=-1
        inequalities.append(r);rhs.append(A*(1-t))
    inequalities=np.asarray(inequalities)
    rhs=np.asarray(rhs)
    points=[]
    for I in itertools.combinations(range(3*s),s):
        B=inequalities[list(I)]
        if np.linalg.matrix_rank(B)<s:
            continue
        p=np.linalg.solve(B,rhs[list(I)])
        if np.max(inequalities@p-rhs)>1e-8:
            continue
        if not any(np.linalg.norm(p-q)<1e-8 for q in points):
            points.append(p)
    hull=ConvexHull(points)
    return hull.volume,hull.area,len(points)


def main():
    cases=[(s,1.,t) for s in (3,4)
           for t in (.1,.26,1.-1./math.sqrt(2),.37,.5)]
    cases.append((5,1.,.3))
    for s,A,t in cases:
        v,surf=analytic(s,A,t)
        hv,hs,nverts=hull_measure(s,A,t)
        assert abs(hv-v)<1e-7*max(1,v),(s,t,hv,v)
        assert abs(hs-surf)<1e-7*max(1,surf),(s,t,hs,surf)
        assert nverts>=s+1
    tstar=1-1/math.sqrt(2)
    for s in range(3,21):
        f,S=analytic(s,1.,tstar)
        Q=S/f**((s-1)/s)
        assert abs(Q-2*s*f**(1/s))<1e-8*s
        assert Q<2*s
        for t in (0.1,0.2,0.4):
            f,S=analytic(s,1.,t)
            step=1e-6
            fp=analytic(s,1.,t+step)[0]
            fm=analytic(s,1.,t-step)[0]
            d=(fp-fm)/(2*step)
            assert abs(S-(2*s*f+(2-math.sqrt(2)-2*t)*d))<1e-6*s
    nonuniform_check([3.,4.,5.],1.)
    nonuniform_check([2.5,3.2,4.5,5.3],.6)
    print('CHAINLINK_SHARP_ISOPERIMETRY_PASS hull_cases=11 nonuniform_cases=2 dimensions=3..5 derivative=3..20')



def nonuniform_check(a,ell):
    s=len(a)
    H=[]
    bounds=[]
    for j in range(s):
        r=np.zeros(s);r[j]=-1;H.append(r);bounds.append(0.)
        r=np.zeros(s);r[j]=1;H.append(r);bounds.append(a[j])
        r=np.zeros(s);r[j]=1;r[(j+1)%s]=-1
        H.append(r);bounds.append(a[j]-ell)
    H=np.asarray(H);bounds=np.asarray(bounds)
    points=[]
    for I in itertools.combinations(range(3*s),s):
        B=H[list(I)]
        if np.linalg.matrix_rank(B)<s:
            continue
        x=np.linalg.solve(B,bounds[list(I)])
        if max(H@x-bounds)>1e-8:
            continue
        if not any(np.linalg.norm(x-y)<1e-8 for y in points):
            points.append(x)
    hull=ConvexHull(points)
    def transfer_vol(aa,ll):
        M=np.eye(2)
        for val in aa:
            M=M@np.array([[val,-ll*ll/2],[1.,0.]])
        return np.trace(M)
    step=1e-5
    partial_sum=0.
    for j in range(s):
        up=list(a);dn=list(a)
        up[j]+=step;dn[j]-=step
        partial_sum+=(transfer_vol(up,ell)-transfer_vol(dn,ell))/(2*step)
    dell=(transfer_vol(a,ell+step)-transfer_vol(a,ell-step))/(2*step)
    surface=2*partial_sum+(2-math.sqrt(2))*dell
    assert abs(hull.volume-transfer_vol(a,ell))<1e-8
    assert abs(hull.area-surface)<1e-6

if __name__=='__main__':
    main()
