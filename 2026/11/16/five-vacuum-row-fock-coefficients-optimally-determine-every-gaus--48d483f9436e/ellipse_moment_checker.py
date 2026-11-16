"""Numerical checks of minimal Gaussian harmonic moment tomography for ellipses.

Requires numpy and scipy. Independent analytical arguments are necessary for the
all-ellipse assertion; numerical checks illustrate the formulas only.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import minimize

nr, na = 76, 256
tr, tw = leggauss(nr)
r = (tr+1)/2
rw = tw/2
angle = (2*np.pi/na)*np.arange(na)
angles = np.stack((np.cos(angle), np.sin(angle)), axis=1)

def calc(theta, need_F=False, need_H=False):
    s, bx, by, u, v=theta
    A=np.array([[.5-u,-v],[-v,.5+u]])
    if np.linalg.eigvalsh(A)[0]<=0: raise ValueError('shape not positive definite')
    b=np.array([bx,by]); cen=np.linalg.solve(A,b)/2
    R2=s+cen@A@cen
    if R2<=0:
        if need_H: raise ValueError('empty ellipse')
        return (np.zeros(5),0.) if need_F else np.zeros(5)
    val, U=np.linalg.eigh(A)
    S=(U/np.sqrt(val))@U.T*np.sqrt(R2)
    detS=np.linalg.det(S)
    unit=angles[:,None,:]*r[None,:,None]
    xy=cen+np.einsum('ij,abj->abi',S,unit)
    x,y=xy[:,:,0],xy[:,:,1]
    basis=np.stack((np.ones_like(x),x,y,x*x-y*y,2*x*y),axis=-1)
    wt=np.exp(-x*x-y*y)/np.pi *detS*r[None,:]*rw[None,:]*2*np.pi/na
    moments=np.einsum('abc,ab->c',basis,wt)
    if need_F:
        F=float(np.sum(wt*R2*(1-r[None,:]**2)))
    if need_H:
        xyb=cen+angles@S.T
        xb,yb=xyb[:,0],xyb[:,1]
        pb=np.stack((np.ones(na),xb,yb,xb*xb-yb*yb,2*xb*yb),axis=1)
        wb=np.exp(-xb*xb-yb*yb)/np.pi
        H=np.einsum('ai,aj,a->ij',pb,pb,wb)*np.linalg.det(A)**(-.5)*np.pi/na
        return moments,H
    if need_F: return moments,F
    return moments

inputs=[np.array([.8,.21,-.14,.08,.06]),np.array([.48,-.18,.13,-.11,.035]),np.array([1.1,.3,.26,.14,-.035])]
for th in inputs:
    m,H=calc(th,need_H=True)
    eigen=np.linalg.eigvalsh(H)
    assert eigen[0]>1e-6, eigen
    jac=np.column_stack([(calc(th+1e-5*np.eye(5)[j])-calc(th-1e-5*np.eye(5)[j]))/(2e-5) for j in range(5)])
    assert np.max(np.abs(H-jac))<3e-7, (H,jac)
    s,bx,by,u,v=th
    A=np.array([[.5-u,-v],[-v,.5+u]]);cen=np.linalg.solve(A,np.array([bx,by]))/2
    R2=s+cen@A@cen
    bound=R2**6/(64*np.linalg.det(A)**6.5)*np.exp(-5*(np.linalg.norm(cen)+np.sqrt(R2/np.min(np.linalg.eigvalsh(A))))**2)
    assert np.linalg.det(H)>=bound*(1-1e-8)
    def obj(t):
        if .25-t[3]**2-t[4]**2<=0: return 1e12
        mt,F=calc(t,need_F=True)
        return F-t@m
    def grad(t): return calc(t)-m
    res=minimize(obj,np.array([.7,0.,0.,0.,0.]),jac=grad,method='SLSQP',constraints=[{'type':'ineq','fun':lambda t:.245-t[3]**2-t[4]**2}],options={'maxiter':130,'ftol':1e-13})
    assert res.success and np.linalg.norm(res.x-th)<3e-4,(res.message,res.x,th)
    print('PASS theta=',th,'min_eig=',float(eigen[0]),'Jac_err=',float(np.max(np.abs(H-jac))),'recovery=',float(np.linalg.norm(res.x-th)))
print('GAUSSIAN_ELLIPSE_FIVE_MOMENT_TOMOGRAPHY_PASS cases=3')
