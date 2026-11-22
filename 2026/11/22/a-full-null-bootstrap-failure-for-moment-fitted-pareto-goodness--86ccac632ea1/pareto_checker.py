"""Independent arithmetic and reproducibility checks for the Pareto MoM-bootstrap collapse theorem."""
import math
from fractions import Fraction
import numpy as np

def ks_against_pareto(data, beta):
    xs=np.sort(np.asarray(data, dtype=np.float64)); n=len(xs)
    f=-np.expm1(-beta*np.log(xs))
    return float(max(np.max(np.arange(1,n+1)/n-f),np.max(f-np.arange(n)/n)))

def fitted_shape(data):
    mean=float(np.mean(data)); return mean/(mean-1)

def distance(beta):return (1-beta)*beta**(beta/(1-beta))
def cvm_slope(beta):return 1/3-2/(beta+2)+1/(2*beta+1)

def run():
    rng=np.random.default_rng(731992); checks=0
    for beta in [Fraction(1,4),Fraction(1,3),Fraction(1,2),Fraction(2,3),Fraction(3,4)]:
        b=float(beta)
        # Closed-form continuous optimization checked on a dense deterministic mesh.
        xstar=b**(-1/(1-b)); u=1/xstar
        assert abs((u**b-u)-distance(b))<2e-14;checks+=1
        grid=np.linspace(0,1,100001)
        assert abs(np.max(grid**b-grid)-distance(b))<1e-5;checks+=1
        assert cvm_slope(b)>0;checks+=1
    assert abs(distance(0.5)-0.25)<1e-14;checks+=1
    assert abs(cvm_slope(0.5)-Fraction(1,30))<1e-14;checks+=1
    for n in [2000,10000,40000]:
        beta=0.5
        x=np.exp(rng.exponential(1/beta,size=n))
        estimate=fitted_shape(x)
        D=ks_against_pareto(x,estimate)
        assert estimate>1 and abs(D-.25)<.14;checks+=1
        # A refitted bootstrap obeys the same convention as the source's resampling algorithm.
        ds=[]
        for _ in range(50):
            y=np.exp(rng.exponential(1/estimate,size=n))
            ds.append(ks_against_pareto(y,fitted_shape(y)))
        assert np.quantile(ds,.95)<D;checks+=1
        print(f'n={n} fitted_beta={estimate:.6f} KS={D:.6f} bootstrap_95={np.quantile(ds,.95):.6f}')
    print(f'CHECKS PASSED {checks}')
if __name__=='__main__':run()
