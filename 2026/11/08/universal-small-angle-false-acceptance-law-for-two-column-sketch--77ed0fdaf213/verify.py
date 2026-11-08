"""Reproduce constants and numerical diagnostics of the two-column condition threshold law.

Requires Python 3, NumPy and SciPy.  Numerical experiments are illustrative,
not a substitute for the analytic small-angle proof.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.integrate import quad


def volume(k, threshold):
    assert k >= 2 and threshold > 1
    area = 2 * math.pi ** ((k-1) / 2) / math.gamma((k-1) / 2)
    low, high = 1 / threshold, threshold
    val, err = quad(lambda b: b ** (k-2) * math.sqrt(max(0.0, (high-b)*(b-low))),
                    low, high, epsabs=1e-12, epsrel=1e-12)
    return 2 * area * val


def gaussian_constant(k, threshold):
    return math.gamma(k)/((4*math.pi)**(k/2)*math.gamma(k/2))*volume(k, threshold)


def scaled_probability(k, threshold, theta, law='gaussian', n=240000, seed=123):
    """Importance sampler for Pr[kappa <= threshold]/theta**k.

    Draws Y normally and integrates over X=theta*z by uniform-ball importance
    sampling.  This does not generate rare X outcomes by rejection.
    """
    rng=np.random.default_rng(seed)
    Y=rng.standard_normal((n,k)); ny=np.linalg.norm(Y,axis=1)
    Z=rng.standard_normal((n,k)); Z/=np.linalg.norm(Z,axis=1)[:,None]
    Z *= (threshold*ny*rng.random(n)**(1/k))[:,None]
    W=np.cos(theta)*Z + np.sinc(theta/np.pi)*Y
    aa=np.sum(Z*Z,axis=1)
    bb=np.sum(W*W,axis=1)
    ab=np.sum(Z*W,axis=1)
    trace=aa+bb
    det=aa*bb-ab*ab
    q=threshold**2/(1+threshold**2)**2
    ok=(det>=q*trace*trace)
    norm=math.pi**(k/2)/math.gamma(k/2+1)*(threshold*ny)**k
    X=theta*Z
    if law=='gaussian':
        density=np.exp(-np.sum(X*X,axis=1)/2)/(2*math.pi)**(k/2)
        fzero=(2*math.pi)**(-k/2)
    elif law=='uniform4':
        density=np.prod(np.abs(X)<=2.0,axis=1)/(4.0**k)
        fzero=4.0**(-k)
    elif law=='laplace':
        density=np.exp(-np.sum(np.abs(X),axis=1))/(2.0**k)
        fzero=2.0**(-k)
    else:
        raise ValueError('law')
    samples=norm*density*ok
    expected=fzero*(2**(-k))*volume(k,threshold)*(2**(k/2))*math.gamma(k)/math.gamma(k/2)
    return samples.mean(),samples.std(ddof=1)/math.sqrt(n),expected


def run():
    K=Fraction(5,2)
    exact2=(K-1/K)**2/Fraction(8)
    exact3=(K-1/K)**2*(K+1/K)/Fraction(8)
    assert exact2==Fraction(441,800)
    assert exact3==Fraction(12789,8000)
    assert abs(gaussian_constant(2,float(K))-float(exact2))<2e-12
    assert abs(gaussian_constant(3,float(K))-float(exact3))<2e-12
    checks=4
    for k in range(2,7):
        for t in (1.2,2.5,5.0):
            V=volume(k,t)
            assert math.isfinite(V) and V>0
            checks+=1
    for k,law in ((2,'gaussian'),(3,'gaussian'),(2,'uniform4'),(2,'laplace')):
        estimate,se,limit=scaled_probability(k,2.5,0.018,law)
        print('k',k,law,'estimate p/theta^k=',round(estimate,8),
              'SE=',round(se,8),'theory=',round(limit,8))
        # Limited-angle bias is O(theta); generous tolerance for stochastic sampling.
        assert abs(estimate-limit)<7*se+0.035*limit
        checks+=1
    print('PASS',checks,'independent numerical and exact-rational checks')


if __name__=='__main__':
    run()
