"""Standalone symbolic and numerical checks for the three-variable Pearson map."""
import math
import random
import sympy as sp
r,s,q,e=sp.symbols('r s q e',real=True)
A=sp.Matrix([[1,r,r],[r,1,s],[r,s,1]])
H=sp.eye(3)-sp.ones(3)/3
B=A*H
D=2*r-1-s
K=sp.factor(B.row(1).dot(B.row(1)))
assert sp.simplify(4*(r*r-r*s-r+s*s-s+1)-(D*D+3*(1-s)**2))==0
assert sp.factor(B.row(0).dot(B.row(1))-(1-r)*D/3)==0
assert sp.factor(B.row(0).dot(B.row(0))-2*(1-r)**2/3)==0
assert sp.factor(K-2*(r*r-r*s-r+s*s-s+1)/3)==0
q2=D**2/(D**2+3*(1-s)**2)
c23=sp.factor(B.row(1).dot(B.row(2))/K)
assert sp.factor(c23-(2*q2-1))==0
assert sp.factor(sp.det(A)-(1-s)*(1+s-2*r*r))==0
f=q/sp.sqrt(4*q*q+6*q+3)
assert sp.simplify(sp.diff(f,q)-3*(q+1)/(4*q*q+6*q+3)**sp.Rational(3,2))==0
assert sp.simplify(4*q*q+6*q+3-1-2*(q+1)*(2*q+1))==0
series=sp.series(1+f.subs(q,-1+e),e,0,4)
assert sp.simplify(sp.limit((1+f.subs(q,-1+e))/e**2,e,0)-sp.Rational(3,2))==0
assert sp.simplify(sp.diff(f,q).subs(q,0)-1/sp.sqrt(3))==0
# Full row Pearson implementation, distinct from explicit scalar derivation.
def C(M):
    rows=[[float(x) for x in row] for row in M]
    z=[[x-sum(row)/3.0 for x in row] for row in rows]
    norms=[math.sqrt(sum(v*v for v in row)) for row in z]
    return [[sum(z[i][k]*z[j][k] for k in range(3))/(norms[i]*norms[j]) for j in range(3)] for i in range(3)]
def matrix(rr,ss):return [[1,rr,rr],[rr,1,ss],[rr,ss,1]]
def formula(rr,ss):
    D=2*rr-1-ss
    return D/math.sqrt(D**2+3*(1-ss)**2)
rng=random.Random(372025)
counts={'left':0,'right':0,'equal':0,'boundary':0}
for case in range(530):
    if case<500:
        ss=rng.uniform(-0.97,0.97)
        hi=math.sqrt((1+ss)/2)
        rr=rng.uniform(-hi,hi)
    elif case<515:
        rr=rng.uniform(-0.49,0.98);ss=rr
    else:
        ss=rng.uniform(-0.92,0.96);rr=math.sqrt((1+ss)/2)*(-1 if case%2 else 1)
    assert 1+ss-2*rr*rr >= -1e-12
    direct=C(matrix(rr,ss))
    t=formula(rr,ss)
    assert abs(direct[0][1]-t)<2e-12 and abs(direct[1][2]-(2*t*t-1))<2e-12
    if abs(rr-ss)<1e-12:
        assert abs(t+0.5)<2e-12
        counts['equal']+=1
    else:
        target=-1 if rr<ss else 0
        for j in range(700):
            t=t/math.sqrt(4*t*t+6*t+3)
        assert abs(t-target)<1e-10,(rr,ss,t,target)
        counts['left' if rr<ss else 'right']+=1
    if case>=515:counts['boundary']+=1
print('VERIFY_OK symbolic_identities=11 case_total=530 basin_counts=',counts,'local_superattraction=3/2','local_mixed_multiplier=1/sqrt(3)')
