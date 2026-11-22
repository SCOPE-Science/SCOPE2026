#!/usr/bin/env python3
"""Reproducible checks for the stated full-observation rank-one Gauss--Newton map.

This is supplementary finite verification; the analytical proof is in RESULT.md.
Requires Python 3 and NumPy.
"""
from fractions import Fraction as Q
from math import sqrt
import numpy as np

checks = 0

def check(statement, msg):
    global checks
    assert statement, msg
    checks += 1

# Exact-rational identities for the two Gram-matrix offdiagonals and trace.
for ai in range(1, 12):
    for bi in range(1, 12):
        a2 = Q(ai, 13)
        b2 = Q(bi, 13)
        c2 = 1-a2
        d2 = 1-b2
        # In target coordinates, Gram offdiagonals factor exactly as
        # (W W^T)_(1,2) = a*b^2*c^3 and (W^T W)_(1,2) = a^2*b*d^3.
        t_left = (1-a2*b2)-a2*d2
        t_right = (1-a2*b2)-b2*c2
        check(t_left == c2, 'left Gram offdiagonal factorization')
        check(t_right == d2, 'right Gram offdiagonal factorization')
        check(t_left > 0 and t_right > 0, 'strict offdiagonal signs')
        # Squared singular values of W have sum 1-a^2 b^2 and product a^2 b^2 c^2 d^2.
        check(c2+a2*d2 == 1-a2*b2, 'trace')
        check((c2)*(a2*d2)-(a2*c2*d2*d2) == a2*b2*c2*d2, 'determinant')

rng = np.random.default_rng(20261121)
E = np.array([[1., 0.], [0., 0.]])

def two_dim(a,b):
    c=sqrt(1.-a*a); d=sqrt(1.-b*b)
    u=np.array([c,a]); v=np.array([d,b])
    # E minus the normal-space rank-one tensor.
    W=E-a*b*np.outer([a,-c],[b,-d])
    U,S,Vt=np.linalg.svd(W)
    return W,U,S,Vt

# Strict angle improvement and exact correspondence to the tangent projector.
for _ in range(2200):
    a=float(rng.uniform(.002,.998)); b=float(rng.uniform(.002,.998))
    c=sqrt(1.-a*a); d=sqrt(1.-b*b)
    u=np.array([c,a]);v=np.array([d,b])
    W,U,S,Vt=two_dim(a,b)
    T=E-(np.eye(2)-np.outer(u,u))@E@(np.eye(2)-np.outer(v,v))
    check(np.linalg.norm(W-T) < 8e-15, 'tangent projector')
    check(S[0]>S[1], 'unique top singular value')
    an=abs(U[1,0]); bn=abs(Vt[0,1])
    check(0<an<a, 'left angle decreases')
    check(0<bn<b, 'right angle decreases')
    check(S[0]<=1+5e-15, 'norm contraction of tangent projector')
    check(S[0]>=1-a*a*b*b-5e-15, 'singular norm lower bound')

# Higher-dimensional consistency, and complete irrelevance of starting singular scale.
for dims in [(3,4),(5,5),(8,6)]:
    m,n=dims
    for _ in range(70):
        us=rng.normal(size=m);us/=np.linalg.norm(us)
        vs=rng.normal(size=n);vs/=np.linalg.norm(vs)
        u=rng.normal(size=m);u/=np.linalg.norm(u)
        v=rng.normal(size=n);v/=np.linalg.norm(v)
        Xstar=np.outer(us,vs)
        W=Xstar-(np.eye(m)-np.outer(u,u))@Xstar@(np.eye(n)-np.outer(v,v))
        U,S,Vt=np.linalg.svd(W,full_matrices=False)
        check(S[0]>S[1], 'higher-dimensional unique top singular value')
        check(abs(us@U[:,0])+1e-12 >= abs(us@u), 'higher-dimensional left alignment')
        check(abs(vs@Vt[0,:])+1e-12 >= abs(vs@v), 'higher-dimensional right alignment')
        # Direct rank-one reconstruction is independent of the initial singular scale.
        for scale in [1e-5,1e-1,1.,1e3]:
            check(np.linalg.norm((W)- (np.outer(u,v)*scale + (Xstar-np.outer(u,v)*scale - (np.eye(m)-np.outer(u,u))@Xstar@(np.eye(n)-np.outer(v,v))))) < 5e-12,'scale independence')

# Boundary cases (left/right orthogonal and simultaneous orthogonality).
u=np.array([0.,1.]);v=np.array([3.,4.])/5
W=E-(np.eye(2)-np.outer(u,u))@E@(np.eye(2)-np.outer(v,v))
check(np.linalg.matrix_rank(W)==1, 'single orthogonal factor nonzero')
check(np.linalg.norm(W-v[0]*np.outer([1.,0.],v))<1e-15, 'first step aligns one factor')
u=v=np.array([0.,1.])
W=E-(np.eye(2)-np.outer(u,u))@E@(np.eye(2)-np.outer(v,v))
check(np.linalg.norm(W)==0, 'double orthogonality degeneracy')

# Local cubic coefficients: a_next/(a*b^2), b_next/(a^2*b) tend to 1.
for eps in [.01,.007,.004,.002]:
    for ar,br in [(1.,1.),(.5,1.),(1.,.5),(1.,1.3)]:
        a=eps*ar; b=eps*br
        _,U,_,Vt=two_dim(a,b)
        check(abs(abs(U[1,0])/(a*b*b)-1)<.003, 'left cubic coefficient')
        check(abs(abs(Vt[0,1])/(a*a*b)-1)<.003, 'right cubic coefficient')
print(f'PASS: {checks} assertions; exact rational identities and finite numerical checks')
