"""Exact rational checks of projection-reflector identities and sharp planar examples.
Only Python standard library is required. Universal-time/uniform claims
follow from the mathematical proof, not finite checks.
"""
from fractions import Fraction as Q


def transpose(A):
    return [list(r) for r in zip(*A)]


def add(A, B):
    return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]


def sub(A, B):
    return [[x-y for x,y in zip(a,b)] for a,b in zip(A,B)]


def mul(A, B):
    bt=transpose(B)
    return [[sum((x*y for x,y in zip(a,b)),Q(0)) for b in bt] for a in A]


def scale(A, s):
    return [[s*x for x in a] for a in A]


def eye(n):
    return [[Q(int(i==j)) for j in range(n)] for i in range(n)]


def proj_from_vectors(vs):
    n=len(vs[0]); z=[[Q(0) for _ in range(n)] for _ in range(n)]
    for v in vs:
        assert sum(x*x for x in v)==1
        for i in range(n):
            for j in range(n): z[i][j]+=v[i]*v[j]
    return z


def check(P0,P,expected_cos):
    n=len(P0); I=eye(n)
    assert mul(P,P)==P and mul(P0,P0)==P0
    J0=sub(I,scale(P0,2)); J=sub(I,scale(P,2))
    B=mul(J,J0); sym=scale(add(B,transpose(B)),Q(1,2))
    Delta=sub(P,P0)
    assert sym==sub(I,scale(mul(Delta,Delta),2))
    if n==2:
        assert sym==scale(I,expected_cos)
        # -beta*mu*B generates a uniform radial e^{-beta*mu*expected_cos*t}.
        assert B[0][0]==expected_cos and B[1][1]==expected_cos
        assert B[0][1]==-B[1][0]
    return sym


U=proj_from_vectors([[Q(1),Q(0)]])
checks=0
for a,b in [(Q(1),Q(0)),(Q(4,5),Q(3,5))]:
    # only rational orthonormal vectors are used
    if a*a+b*b!=1: continue
    V=proj_from_vectors([[a,b]])
    C=2*a*a-1
    assert check(U,V,C)==scale(eye(2),C)
    checks+=1
# Exact threshold: 45-degree rotation represented by rational projector entries.
Vmid=[[Q(1,2),Q(1,2)],[Q(1,2),Q(1,2)]]
Bmid=mul(sub(eye(2),scale(Vmid,2)),sub(eye(2),scale(U,2)))
assert Bmid==[[Q(0),Q(-1)],[Q(1),Q(0)]]
assert check(U,Vmid,Q(0))==[[Q(0),Q(0)],[Q(0),Q(0)]]
checks+=1
# Above threshold, the reflector product has strictly negative symmetric part.
Vbad=proj_from_vectors([[Q(3,5),Q(4,5)]])
assert check(U,Vbad,Q(-7,25))==scale(eye(2),Q(-7,25))
checks+=1
# Two negative directions and one positive direction; one principal angle rotates.
U3=proj_from_vectors([[Q(1),Q(0),Q(0)],[Q(0),Q(1),Q(0)]])
V3=proj_from_vectors([[Q(1),Q(0),Q(0)],[Q(0),Q(4,5),Q(3,5)]])
assert check(U3,V3,None)==[[Q(1),Q(0),Q(0)],
                                 [Q(0),Q(7,25),Q(0)],
                                 [Q(0),Q(0),Q(7,25)]]
# Precise identity tested independently above; rank and projector tests are exact.
checks+=1
print('VERIFY_OK exact_rational_projector_identities=',checks,
      'critical_center=1 supercritical_growth=7/25')
print('FINITE_CHECK_ONLY: global convergence and universal sharpness are analytic.')
