"""Standalone finite perturbation check of two planar periodic billiard rays.
Requires numpy; analytic statements and exact inequalities are in RESULT.md.
"""
import math
import numpy as np
D=1.0
R=0.1
BETA=1.1
O=np.array([[0.,0.,0.],[D,0,0],[D/2,D*math.sqrt(3)/2,0]])
C=O.mean(axis=0)
Q=np.array([o+R*(C-o)/np.linalg.norm(C-o) for o in O])
assert abs(np.linalg.norm(Q[0]-Q[1])-(1-math.sqrt(3)*R))<1.e-13
assert 1<BETA<2/math.sqrt(3)

def bounce(q,v,j):
    d=q-O[j]
    W=np.array([1.,1.,BETA*BETA])
    A=np.dot(W*v,v); B=2*np.dot(W*d,v); Cc=np.dot(W*d,d)-R*R
    discriminant=B*B-4*A*Cc
    assert discriminant>0, ('missed obstacle', j, discriminant)
    roots=[(-B-math.sqrt(discriminant))/(2*A),(-B+math.sqrt(discriminant))/(2*A)]
    t=min(t for t in roots if t>1.e-7)
    q1=q+t*v
    normal=W*(q1-O[j]);normal/=np.linalg.norm(normal)
    v1=v-2*np.dot(v,normal)*normal
    return q1,v1

def return_map(q,v,order):
    for j in order: q,v=bounce(q,v,j)
    return q,v

def check_orbit(qcycle):
    qbase=qcycle[0]
    vbase=(qcycle[1]-qcycle[0]);vbase/=np.linalg.norm(vbase)
    plane_n=(qbase-O[0])/R
    tangent=np.cross(np.array([0.,0.,1.]),plane_n)
    wave=np.cross(np.array([0.,0.,1.]),vbase)
    order=list(range(1,len(qcycle)))+[0]
    qfix,vfix=return_map(qbase,vbase,order)
    assert np.linalg.norm(qfix-qbase)<1.e-11
    assert np.linalg.norm(vfix-vbase)<1.e-11
    pair={}
    for label,t,w in [('planar',tangent,wave),('transverse',np.array([0.,0.,1.]),np.array([0.,0.,1.]))]:
        def perturbed(a,b):
            qq=qbase+a*t
            offset=qq-O[0]
            qq=O[0]+offset*R/math.sqrt(offset[0]**2+offset[1]**2+BETA**2*offset[2]**2)
            vv=vbase+b*w;vv/=np.linalg.norm(vv)
            qf,vf=return_map(qq,vv,order)
            return np.array([np.dot(qf-qbase,t),np.dot(vf-vbase,w)])
        h=2.e-7
        matrix=np.column_stack(((perturbed(h,0)-perturbed(-h,0))/(2*h),
                                (perturbed(0,h)-perturbed(0,-h))/(2*h)))
        values=np.linalg.eigvals(matrix)
        numerical=math.log(max(abs(values)))/len(qcycle)
        c=1.0 if len(qcycle)==2 else math.sqrt(3)/2
        L=1-2*R if len(qcycle)==2 else 1-math.sqrt(3)*R
        a=2*((BETA**2)*c if label=='transverse' else 1/c)/R
        predicted=math.acosh(1+a*L/2)
        assert abs(numerical-predicted)<3.e-6, (label,len(qcycle),numerical,predicted)
        pair[label]=predicted
    return pair

two=np.array([O[0]+R*(O[1]-O[0])/D,O[1]+R*(O[0]-O[1])/D])
pair2=check_orbit(two)
pair3=check_orbit(Q)
assert pair2['transverse']>pair2['planar']
assert pair3['transverse']<pair3['planar']
print('VERIFY_OK ray_cycles=2 normal_and_planar_blocks=4 geometric_return_checks=2 thresholds_exact=1 sample_beta=1.1')
