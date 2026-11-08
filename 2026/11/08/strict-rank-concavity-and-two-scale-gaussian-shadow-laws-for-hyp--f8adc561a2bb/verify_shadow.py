"""Independent finite Gaussian k-set shadow validation.
Scientific verification, not an infinite proof.
"""
import itertools
import math
import numpy as np
from scipy.spatial import ConvexHull
from scipy.integrate import quad
from scipy.stats import beta, norm

def exact_mean(n,k):
    # Gaussian pair hyperplane probability, NOT the beta density expression.
    # T ~ N(0,1/2). Use integration over the tie projection.
    from scipy.special import ndtr
    def term(t):
        p=ndtr(-t)
        return (math.comb(n-2,k-1)*p**(k-1)*(1-p)**(n-k-1)
                * math.exp(-t*t)/math.sqrt(math.pi))
    return n*(n-1)*quad(term,-10,10,epsabs=2e-10)[0]

def random_count(pts,k):
    sums=np.array([pts[list(s)].sum(axis=0) for s in itertools.combinations(range(len(pts)),k)])
    return len(ConvexHull(sums).vertices)

def main():
    rng=np.random.default_rng(20261102)
    for n in [4,6,8]:
      for k in range(1,n):
        theo=exact_mean(n,k)
        samples=np.array([random_count(rng.standard_normal((n,2)),k) for _ in range(500)])
        se=samples.std(ddof=1)/math.sqrt(len(samples))
        assert abs(samples.mean()-theo) < 6*se+0.12, (n,k,samples.mean(),theo,se)
      seq=np.array([exact_mean(n,k) for k in range(1,n)])
      assert np.allclose(seq,seq[::-1],atol=1e-6)
      assert (np.diff(seq,2)<-1e-7).all(), (n,seq)
    for n in [20,80,250]:
      seq=np.array([exact_mean(n,k) for k in range(1,n)])
      assert np.all(np.diff(seq,2)<0), (n,seq)
    print('GAUSSIAN_HYPERSIMPLEX_SHADOW_FORMULA_AND_CONCAVITY_CHECKS_PASSED')

if __name__=='__main__': main()
