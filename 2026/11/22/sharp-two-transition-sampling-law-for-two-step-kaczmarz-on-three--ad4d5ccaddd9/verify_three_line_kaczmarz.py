"""Standalone computational checks for the three-line two-step Kaczmarz theorem.
Runs exact-arithmetic contraction identities and a finite directional LP sanity check.
The analytic proof, not the finite checks, establishes the universal claim.
"""
from fractions import Fraction as F
from math import sqrt,cos,sin,pi
from itertools import product
import numpy as np
from scipy.optimize import linprog


def exact_R(u):
    u=F(u);q=min(u,(2*u-1)**2)
    if u < F(1,2):return q*u*(1-u)/(u+q*(1-2*u))
    return u*q

def first_prob(u):
    u=F(u);q=min(u,(2*u-1)**2)
    if u < F(1,2):return q*(1-2*u)/(u+q*(1-2*u))
    return F(0)

def matrices(u):
    u=float(u);c=sqrt(u);s=sqrt(1-u)
    rows=np.array([[1.,0.],[c,s],[c,-s]])
    P=np.eye(2)[None,:,:]-rows[:,:,None]*rows[:,None,:]
    return rows,P

def optimum_joint(u):
    u=F(u);p0=first_prob(u);p1=(1-p0)/2
    joint=np.zeros((3,3))
    joint[0,1]=float(p0)/2;joint[0,2]=float(p0)/2
    j=0 if u<F(1,4) else 2
    joint[1,j]=float(p1)
    j=0 if u<F(1,4) else 1
    joint[2,j]=float(p1)
    return joint

def covariance(P,joint):
    out=np.zeros((2,2))
    for i,j in product(range(3),repeat=2):
        E=P[j]@P[i];out+=joint[i,j]*(E.T@E)
    return out

EXACT=[F(1,64),F(1,16),F(1,4),F(3,8),F(7,16),F(1,2),F(9,16),F(3,4),F(15,16)]
checks=0
for u in EXACT:
    rows,P=matrices(u);joint=optimum_joint(u)
    assert abs(joint.sum()-1)<1e-12 and (joint>=0).all()
    M=covariance(P,joint)
    assert abs(np.linalg.eigvalsh(M)[-1]-float(exact_R(u)))<1e-12
    checks+=1
    # Separate finite-angle linear program: one inequality per direction.
    phis=np.arange(0,360)*pi/360
    vs=np.column_stack([np.cos(phis),np.sin(phis)])
    gains=np.empty((len(phis),9))
    for i,j in product(range(3),repeat=2):
        gains[:,3*i+j]=np.sum((vs@(P[j]@P[i]).T)**2,axis=1)
    A=np.column_stack([gains,-np.ones(len(phis))])
    lp=linprog([0.]*9+[1.],A_ub=A,b_ub=np.zeros(len(phis)),A_eq=np.array([[1.]*9+[0.]]),b_eq=[1.],bounds=[(0.,1.)]*9+[(0.,1.)],method='highs')
    assert lp.success,lp.message
    assert abs(lp.x[-1]-float(exact_R(u))) < 3e-5,(u,lp.x[-1],exact_R(u))
    checks+=1

# Analytic Rademacher-style exact coordinate expressions on a tight-frame case.
assert exact_R(F(1,4))==F(1,8);checks+=1
assert exact_R(F(3,4))==F(3,16);checks+=1
# IID uniform policy via direct nine ordered projections, not a re-expression of optimal sampler.
for u,target in [(F(1,4),F(1,4)),(F(3,4),F(11,18))]:
    P=matrices(u)[1];M=covariance(P,np.full((3,3),1/9))
    assert abs(np.linalg.eigvalsh(M)[-1]-float(target))<1e-12;checks+=1
print(f'PASS {checks} standalone exact/numeric checks; finite directional LP grid has 360 test angles')
