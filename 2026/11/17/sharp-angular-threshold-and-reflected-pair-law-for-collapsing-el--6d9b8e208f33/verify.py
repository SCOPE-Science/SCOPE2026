"""Independent numerical checks for the thin-ellipse angular threshold law.
Run: python verify.py. Uses only numpy and scipy.
Numerical tests corroborate the theorem but do not establish the infinite limit.
"""
import math
import numpy as np
from scipy.stats import qmc


def angular_event(theta, eps, beta):
    pts=np.stack([np.cos(theta),eps*np.sin(theta)],axis=-1)
    C=[]
    for i in range(3):
        u=pts[:,(i+1)%3,:]-pts[:,i,:]
        v=pts[:,(i+2)%3,:]-pts[:,i,:]
        dot=np.einsum('ij,ij->i',u,v)
        C.append(dot/(np.linalg.norm(u,axis=1)*np.linalg.norm(v,axis=1)))
    return np.min(C,axis=0)>math.cos(beta)


def importance_probability(eps,beta,power=19):
    # Every admissible configuration outside the union of three reflection bands
    # has two angles near an ellipse tip (probability O(eps^2)).
    q=math.tan((math.pi-beta)/2)
    H=2/q
    U=qmc.Sobol(3,scramble=True,seed=1729).random_base2(power)
    t=2*math.pi*U[:,0]
    h=H*(2*U[:,1]-1)
    other=2*math.pi*U[:,2]
    total=0
    for i,j,k in ((0,1,2),(0,2,1),(1,2,0)):
        thetas=np.empty((len(U),3))
        thetas[:,i]=t
        thetas[:,j]=(2*math.pi-t+eps*h)%(2*math.pi)
        thetas[:,k]=other
        angles_good=angular_event(thetas,eps,beta)
        # Tie-break to avoid double-counting band overlaps.
        sums=np.array([np.abs(thetas[:,0]+thetas[:,1]-2*math.pi),
                       np.abs(thetas[:,0]+thetas[:,2]-2*math.pi),
                       np.abs(thetas[:,1]+thetas[:,2]-2*math.pi)])
        ix={(0,1):0,(0,2):1,(1,2):2}[(i,j)]
        own=(sums[ix]==np.min(sums,axis=0))
        total+=int(np.count_nonzero(angles_good&own))/len(U)
    return eps*H/math.pi*total


def main():
    for deg in [110,120,140]:
        b=math.radians(deg)
        c=6*(-1/math.tan(b))/math.pi
        ratios=[]
        for eps in [0.025,0.008,0.002]:
            p=importance_probability(eps,b,power=18)
            ratios.append(p/eps)
        print('beta',deg,'limit',round(c,9),'estimates',list(map(lambda x:round(x,9),ratios)))
        assert abs(ratios[-1]-c)/c<0.05, (deg,c,ratios)
    # Exact reflection-chord direction identity for random angles.
    rng=np.random.default_rng(19)
    t=rng.uniform(0,2*math.pi,3000)
    s=rng.uniform(0,2*math.pi,3000)
    e=0.03
    dx=np.cos(s)-np.cos(t)
    dy=e*(np.sin(s)-np.sin(t))
    assert np.max(np.abs(dx*np.cos((t+s)/2) + (dy/e)*np.sin((t+s)/2)))<1e-12
    print('THIN_ELLIPSE_STEINER_ANGULAR_CHECKS_OK')


if __name__=='__main__':
    main()
