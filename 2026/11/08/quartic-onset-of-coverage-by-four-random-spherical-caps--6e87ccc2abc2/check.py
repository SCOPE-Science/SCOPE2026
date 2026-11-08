"""Reproducibility checks for the tetrahedral four-cap covering onset.

Run: python check.py   (NumPy and SciPy required).
Finite-dimensional checks corroborate, rather than prove, the asymptotic theorem.
"""
import math
import numpy as np
from scipy.stats import qmc

V=np.array([[1.,1.,1.],[1.,-1.,-1.],[-1.,1.,-1.],[-1.,-1.,1.]])/math.sqrt(3)
B=np.array([[1/math.sqrt(2),1/math.sqrt(6)],[-1/math.sqrt(2),1/math.sqrt(6)],[0,-2/math.sqrt(6)]])
W0=math.acos(1/3)


def centers(aa):
    u=np.einsum('...ij,kj->...ki',np.eye(3)+aa,V)
    return u/np.linalg.norm(u,axis=-1,keepdims=True)


def clearances(u):
    out=[]
    for k in range(4):
        inds=[j for j in range(4) if j!=k]
        x=u[...,inds,:]
        n=np.cross(x[...,1,:]-x[...,0,:],x[...,2,:]-x[...,0,:])
        # All four planes near the reference tetrahedron, using positive offsets.
        h=np.abs(np.sum(n*x[...,0,:],axis=-1))/np.linalg.norm(n,axis=-1)
        out.append(h)
    return np.stack(out,axis=-1)


def metric_jacobian():
    perturb=[]
    for a,b in [(1.,0.),(0.,1.)]:
        perturb.append(np.diag([a,b,-a-b]))
    for i,j in [(0,1),(0,2),(1,2)]:
        x=np.zeros((3,3));x[i,j]=x[j,i]=1.;perturb.append(x)
    tangents=[]
    for z in perturb:
        y=V@z.T
        y-=np.einsum('ij,ij->i',V,y)[:,None]*V
        tangents.append(y.ravel())
    for j in range(3):
        omega=np.zeros(3);omega[j]=1
        tangents.append(np.cross(np.broadcast_to(omega,V.shape),V).ravel())
    X=np.array(tangents)
    return math.sqrt(np.linalg.det(X@X.T))


def leading_five_volume(delta):
    return (19683*math.sqrt(3)*math.pi/512)*delta**4


def local_ratio(epsilon,seed=384719,power=17):
    delta=1/3-math.cos(W0+epsilon)
    radius=1.25*math.sqrt(4.5*delta)
    points=qmc.Sobol(d=5,scramble=True,seed=seed).random_base2(power)
    t=2*points-1
    diag=(t[:,:2]*radius)@B.T
    off=4*delta*t[:,2:]
    a=np.zeros((len(t),3,3))
    for k in range(3):a[:,k,k]=diag[:,k]
    for k,(i,j) in enumerate([(0,1),(0,2),(1,2)]):
        a[:,i,j]=a[:,j,i]=off[:,k]
    good=(clearances(centers(a)).min(axis=1)>=math.cos(W0+epsilon))
    box_volume=(2*radius)**2/math.sqrt(3)*(8*delta)**3
    return box_volume*good.mean()/leading_five_volume(delta)


def main():
    assert abs(metric_jacobian()-2048/243)<1e-11
    assert np.allclose(clearances(V),1/3,rtol=0,atol=1e-12)
    t=1e-5
    for i,(j,k) in enumerate([(0,1),(0,2),(1,2)]):
        a=np.zeros((3,3));a[j,k]=a[k,j]=t
        deriv=(clearances(centers(a))-clearances(V))/t
        signatures=[(1,-1,-1,1),(1,-1,1,-1),(1,1,-1,-1)]
        assert np.allclose(deriv,(8/27)*np.array(signatures[i]),atol=2e-4)
    for t in [0.01,0.002]:
        a=np.diag([t,-t,0.])
        hs=clearances(centers(a))
        # Q=2*t^2: prediction 1/3-4*t^2/9
        assert np.allclose(hs,1/3-4*t*t/9,atol=1e-6)
    ratios=[local_ratio(e) for e in [0.04,0.02,0.01,0.005]]
    print('local five-volume ratios',ratios)
    assert 1.04<ratios[0]<1.16
    assert 0.99<ratios[-1]<1.03
    assert abs(ratios[-1]-1)<abs(ratios[0]-1)
    # Exact conversion from delta to angular radius.
    assert abs((81*math.sqrt(3)/(4*math.pi))*math.sin(W0)**4-16*math.sqrt(3)/math.pi)<1e-13
    print('FOUR_RANDOM_CAPS_TETRAHEDRAL_QUARTIC_ONSET_OK')


if __name__=='__main__':main()
