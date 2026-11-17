"""Finite numerical checks of a spherical great-circle small-perimeter law."""
import numpy as np
from scipy.integrate import quad
PI=np.pi

def integrand(a,b):
    theta=np.array([a,b,PI-a-b])/2
    if np.any(theta<=0): return 0.
    return float(np.prod(np.sin(theta)**2/np.cos(theta)))

def formula_constant():
    I=quad(lambda a:quad(lambda b:integrand(a,b),0.,PI-a,epsabs=1e-10)[0],0.,PI,epsabs=1e-10)[0]
    return I/(12*PI**2)

def true_perimeter(t,phi):
    n=np.stack([np.sqrt(1-t*t)*np.cos(phi),np.sqrt(1-t*t)*np.sin(phi),t],axis=-1)
    corners=[]
    for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]:
        v=np.cross(n[:,i,:],n[:,j,:])
        v/=np.linalg.norm(v,axis=1)[:,None]
        sg=np.where(np.sum(v*n[:,k,:],axis=1)>=0,1.,-1.)
        corners.append(v*sg[:,None])
    v=np.stack(corners,axis=1)
    edge=np.arccos(np.clip(np.sum(v*np.roll(v,-1,axis=1),axis=-1),-1,1))
    return edge.sum(axis=1)

def test():
    K=formula_constant()
    assert abs(K-0.0003096989395717297)<1e-11, K
    rg=np.random.default_rng(20261112)
    N=450000
    phi=rg.uniform(0,2*PI,(N,3))
    ordered=np.sort(phi,axis=1)
    gaps=np.stack([ordered[:,1]-ordered[:,0],ordered[:,2]-ordered[:,1],2*PI+ordered[:,0]-ordered[:,2]],axis=1)
    valid=np.max(gaps,axis=1)<PI
    assert abs(valid.mean()-0.25)<0.003
    angle=PI-gaps[valid]
    w=np.prod(np.sin(angle/2)**2/np.cos(angle/2),axis=1)
    Kmc=w.sum()/N/6
    assert abs(Kmc/K-1)<0.04,(K,Kmc)
    # The planar perimeter derivative identity, independently reconstructing vertices.
    for angle_one in angle[:50]:
        a,b,c=angle_one
        directions=np.array([0.,PI-c,PI-c+PI-a])
        normals=np.stack([np.cos(directions),np.sin(directions)],axis=-1)
        offsets=rg.uniform(.03,.5,3)
        vertices=np.stack([np.linalg.solve(normals[[i,j]],-offsets[[i,j]]) for i,j in [(0,1),(1,2),(2,0)]])
        P=np.linalg.norm(vertices-np.roll(vertices,-1,axis=0),axis=1).sum()
        coefficients=np.array([np.cos(angle_one[i]/2)/(np.sin(angle_one[(i+1)%3]/2)*np.sin(angle_one[(i+2)%3]/2)) for i in range(3)])
        assert abs(P-coefficients@offsets)<1e-9
    # Importance sample t_i independently in [0, eps]. On P<=eps all t_i must lie here.
    eps=.28
    t=rg.uniform(0,eps,(N,3));p=rg.uniform(0,2*PI,(N,3)); sp=np.sort(p,axis=1)
    gp=np.stack([sp[:,1]-sp[:,0],sp[:,2]-sp[:,1],2*PI+sp[:,0]-sp[:,2]],axis=1)
    yes=(gp.max(axis=1)<PI)&(true_perimeter(t,p)<=eps)
    observed=yes.mean();se=np.sqrt(K*(1-K)/N)
    assert abs(observed-K)<6*se,(K,observed,se)
    print('K_analytic',K,'K_angles_MC',Kmc,'K_spherical_importance',observed,'SE',se)
    print('GREAT_CIRCLE_SMALL_PERIMETER_CHECKS_OK')

if __name__=='__main__': test()
