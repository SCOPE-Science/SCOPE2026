"""Reproducible numerical checks for the anchored small-parallelogram law."""
import numpy as np
from scipy.integrate import quad
from scipy.special import roots_legendre

SEED=20261112
rng=np.random.default_rng(SEED)
def rho(theta,a):return 1+a*np.cos(theta)
def a_of(a):return np.pi*(1+a*a/2)
def predicted(a):return 8-4*a*a/(1+a*a/2)

def sample(a,n):
    # Rejection sampling of polar angles with density proportional to rho(theta)^2;
    # independently sample radius with conditional density 2r/rho(theta)^2.
    result=np.empty((n,2),dtype=float)
    done=0
    while done<n:
        k=min(max((n-done)*2,10000),3000000)
        angles=2*np.pi*rng.random(k)
        acc=rng.random(k)<((1+a*np.cos(angles))/(1+a))**2
        tt=angles[acc][:n-done]
        m=len(tt)
        rr=(1+a*np.cos(tt))*np.sqrt(rng.random(m))
        result[done:done+m,0]=rr*np.cos(tt)
        result[done:done+m,1]=rr*np.sin(tt)
        done+=m
    return result

for a in [0.,0.4]:
    area=a_of(a)
    D=(sample(a,1700000)); E=sample(a,1700000)
    v=np.abs(D[:,0]*E[:,1]-D[:,1]*E[:,0])/area
    theta=np.linspace(0,2*np.pi,20001,endpoint=False)
    defect=((rho(theta,a)-rho(theta+np.pi,a))**2).mean()*2*np.pi/area
    assert abs(predicted(a)-(8-defect))<2e-8
    if a>0:
        mask=v<0.005
        raw=(D[mask,0]*E[mask,0]+D[mask,1]*E[mask,1])
        same=(raw>0)
        branch_expected=0.5+a*a/4
        assert abs(same.mean()-branch_expected)<0.018,(same.mean(),branch_expected)
        q=(v[mask]/0.005)
        assert abs(q.mean()-0.5)<0.025
        theta_same=np.arctan2(D[mask,1][same],D[mask,0][same])
        mean_cos=np.cos(theta_same).mean()
        assert abs(mean_cos-2*a/(2+a*a))<0.028,(mean_cos,2*a/(2+a*a))
        print(f'conditional branch+={same.mean():.5f} expected={branch_expected:.5f} q_mean={q.mean():.5f} theta_cos+={mean_cos:.5f}')
    for eps in [0.01,0.005,0.0025]:
        p=np.mean(v<eps)
        se=np.sqrt(p*(1-p)/len(v))/eps
        val=p/eps
        print(f'a={a:.2f} eps={eps:.4f} empirical_slope={val:.5f} se={se:.5f} limit={predicted(a):.6f}')
        assert abs(val-predicted(a))<0.3, (a,eps,val)

# Exact disk law for raw determinant H=|det(X,Y)| (disk radius one),
# checked by independent quadrature and analytic moments.
for s in [0.05,0.25,0.75,0.99]:
    f=(8/np.pi)*(np.sqrt(1-s*s)-s*np.arccos(s))
    fq=(8/np.pi)*quad(lambda r:np.sqrt(1-(s/r)**2),s,1,epsabs=2e-10)[0]
    assert abs(f-fq)<1e-8,(s,f,fq)
    print('disk_pdf',s,f)
assert abs(quad(lambda s:(8/np.pi)*(np.sqrt(1-s*s)-s*np.arccos(s)),0,1)[0]-1)<1e-10
assert abs(quad(lambda s:s*(8/np.pi)*(np.sqrt(1-s*s)-s*np.arccos(s)),0,1)[0]-8/(9*np.pi))<1e-10
print('ANCHORED_DETERMINANT_CHECKS_OK')
