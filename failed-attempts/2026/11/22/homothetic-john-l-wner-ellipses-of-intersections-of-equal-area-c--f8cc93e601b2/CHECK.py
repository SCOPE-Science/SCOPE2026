"""Numerical corroboration of an exact planar convex-geometric theorem.

Requires numpy. The analytic proof, not finite tests, establishes the theorem.
"""
import math
import numpy as np


def pos_matrix(rng):
    X=rng.normal(size=(2,2)); return X.T@X+np.eye(2)*0.2


def run():
    rng=np.random.default_rng(341983)
    angles=np.linspace(0,2*math.pi,8001)
    u=np.column_stack((np.cos(angles),np.sin(angles)))
    cases=[]
    for _ in range(180):
        a,b=pos_matrix(rng),pos_matrix(rng)
        b*=math.sqrt(np.linalg.det(a)/np.linalg.det(b))
        cases.append((a,b))
    for t in (1.,1.001,1.5,2.,10.,1e3):
        cases.append((np.diag([t,1/t]),np.diag([1/t,t])))
    cases.append((np.eye(2),np.eye(2)))
    for a,b in cases:
        m=(a+b)/2; d=(a-b)/2
        w,v=np.linalg.eigh(m)
        srt=(v*np.sqrt(w))@v.T
        inv=(v*(1/np.sqrt(w)))@v.T
        c=inv@d@inv
        s=math.sqrt(max(0,1-np.linalg.det(a)/np.linalg.det(m)))
        val=np.linalg.eigvalsh(c)
        assert np.allclose(np.sort(val),[-s,s],rtol=1e-8,atol=1e-9)
        assert abs(np.trace(c))<1e-8
        mismatch=max(0,float(np.trace(np.linalg.solve(a,b))-2))
        assert math.isclose(s,math.sqrt(mismatch/(4+mismatch)),rel_tol=1e-8,abs_tol=1e-8)
        dr=(1/np.sqrt(np.maximum(np.einsum('ij,jk,ik->i',u,np.eye(2)+c,u),np.einsum('ij,jk,ik->i',u,np.eye(2)-c,u))))
        assert dr.max()<=1+1e-8
        assert dr.min()>=1/math.sqrt(1+s)-1e-8
        r=1/math.sqrt(1+s)
        assert math.isclose((math.pi/math.sqrt(np.linalg.det(m)))/(math.pi*r*r/math.sqrt(np.linalg.det(m))),1+s,rel_tol=1e-10)
        # Independently test the exact four contacts in the normalized eigenbasis.
        z,V=np.linalg.eigh(c)
        for axis in (V[:,0],V[:,1]):
            point=r*axis
            assert abs(max(point@(np.eye(2)+c)@point,point@(np.eye(2)-c)@point)-1)<1e-8
        for choice in (-1,1):
            point=(V[:,0]+choice*V[:,1])/math.sqrt(2)
            assert abs(point@(np.eye(2)+c)@point-1)<1e-8
            assert abs(point@(np.eye(2)-c)@point-1)<1e-8
        area_k=.5*np.trapz(dr**2,angles)
        assert math.pi/(1+s)-1e-5<=area_k<=math.pi+1e-5
        assert np.allclose(srt@inv,np.eye(2),atol=1e-9)
    print('EQUAL_AREA_ELLIPSE_EXTREMAL_PAIR_CHECKS_OK',len(cases))


if __name__=='__main__': run()
