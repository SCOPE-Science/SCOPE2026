"""Independent numerical checks of circular Green-kernel quadrature design formulas.

All global optimization and equality statements are proved analytically in RESULT.md.
Requires Python 3 and NumPy; this finite checker is not an infinite certificate.
"""
import itertools
import math
import random
import numpy as np


def kernel(a, b, kappa, scale):
    d = (a-b) % 1.0
    return scale * (math.exp(-kappa*d)+math.exp(-kappa*(1.0-d))) / (-math.expm1(-kappa))


def bridge_cost(length, kappa, scale):
    return 2.0*scale/(kappa*kappa) * (kappa*length-2.0*math.tanh(kappa*length/2.0))


def cost_from_gaps(points, kappa, scale):
    xx = sorted(points)
    gaps = [xx[(j+1) % len(xx)]-xx[j] if j < len(xx)-1 else 1.0+xx[0]-xx[-1]
            for j in range(len(xx))]
    return sum(bridge_cost(a, kappa, scale) for a in gaps)


def cost_direct(points, kappa, scale):
    if not points:
        return 2.0*scale/kappa
    matrix = np.array([[kernel(a,b,kappa,scale) for b in points] for a in points])
    vector = np.full(len(points), 2.0*scale/kappa)
    return 2.0*scale/kappa - float(vector @ np.linalg.solve(matrix, vector))


def weights_direct(points, kappa, scale):
    matrix = np.array([[kernel(a,b,kappa,scale) for b in points] for a in points])
    return np.linalg.solve(matrix, np.full(len(points), 2.0*scale/kappa))


def weights_from_gaps(points, kappa):
    n=len(points)
    return np.array([(math.tanh(kappa*((points[i]-points[i-1]) % 1)/2)
                      +math.tanh(kappa*((points[(i+1)%n]-points[i]) % 1)/2))/kappa
                    for i in range(n)])


def q_data(n, probabilities):
    q = [0.0]*(n-1)
    p0=probabilities.get(0, 0.0)
    p1=sum(pr for mask,pr in probabilities.items() if mask.bit_count()==1)
    for k in range(1,n):
        q[k-1] = sum(pr for mask,pr in probabilities.items()
                     if mask & 1 and mask & (1 << k)
                     and all(not(mask & (1 << j)) for j in range(1,k)))
    return p0,p1,q


def analytic_expectation(gaps, probabilities, kappa, scale):
    n=len(gaps)
    p0,p1,qs=q_data(n,probabilities)
    total=p0*2*scale/kappa+p1*bridge_cost(1.0,kappa,scale)
    for k,qk in enumerate(qs,1):
        total+=qk*sum(bridge_cost(sum(gaps[(i+j)%n] for j in range(k)),kappa,scale) for i in range(n))
    return total


def brute_expectation(points, probabilities, kappa, scale):
    return sum(pr*cost_direct([x for j,x in enumerate(points) if mask&(1 << j)],kappa,scale)
               for mask,pr in probabilities.items())


def indexed_gap_points(gaps):
    return np.cumsum([0.0]+gaps[:-1]).tolist()


def iid_probabilities(n,p):
    return {mask:p**mask.bit_count()*(1-p)**(n-mask.bit_count()) for mask in range(1<<n)}


def alternate_probabilities():
    return {0b0101:0.5, 0b1010:0.5}


def expected_minimum(n,p,kappa,scale):
    if p==0.0:
        return 2*scale/kappa
    if p==1.0:
        return n*bridge_cost(1/n,kappa,scale)
    return ((1-p)**n*(2*scale/kappa)
            +n*p*(1-p)**(n-1)*bridge_cost(1,kappa,scale)
            +n*p*p*sum((1-p)**(k-1)*bridge_cost(k/n,kappa,scale) for k in range(1,n)))


def main():
    rng=random.Random(773)
    tests=0
    for n in (1,2,3,4,6,8):
        for kappa in (0.5,1.7,5.0,11.0):
            for j in range(20):
                points=sorted(rng.random() for _ in range(n))
                a=cost_direct(points,kappa,1.3)
                b=cost_from_gaps(points,kappa,1.3)
                assert abs(a-b)<2e-8, (n,kappa,a,b)
                if n>=2:
                    w=weights_direct(points,kappa,1.3)
                    wt=weights_from_gaps(points,kappa)
                    assert np.max(abs(w-wt))<1e-8, (n,kappa,w,wt)
                    assert min(w)>0
                tests+=1
    for n in (2,3,4,5,6):
        for p in (0.2,0.5,0.85,1.0):
            probs=iid_probabilities(n,p)
            for kappa in (0.5,2.,7.):
                for _ in range(3):
                    z=np.array([0.1+rng.random() for _ in range(n)])
                    gaps=(z/z.sum()).tolist()
                    points=indexed_gap_points(gaps)
                    brute=brute_expectation(points,probs,kappa,1.0)
                    formula=analytic_expectation(gaps,probs,kappa,1.0)
                    uniform=analytic_expectation([1/n]*n,probs,kappa,1.0)
                    exact=expected_minimum(n,p,kappa,1.0)
                    assert abs(brute-formula)<2e-8, (n,p,kappa,brute,formula)
                    assert abs(uniform-exact)<1e-10, (n,p,kappa,uniform,exact)
                    assert formula>=uniform-1e-11, (n,p,kappa)
                    tests+=1
    probs=alternate_probabilities()
    for kappa in (0.5,3.,10.):
        baseline=2*bridge_cost(0.5,kappa,1.0)
        for a in (0.01,0.1,0.2,0.249,0.35,0.48):
            gaps=[a,0.5-a,a,0.5-a]
            pts=indexed_gap_points(gaps)
            assert abs(brute_expectation(pts,probs,kappa,1.0)-baseline)<1e-9
            assert abs(analytic_expectation(gaps,probs,kappa,1.0)-baseline)<1e-9
            tests+=1
        for a in (0.1,0.2,0.3):
            gaps=[a,0.5-a+0.02,a,0.5-a-0.02]
            val=analytic_expectation(gaps,probs,kappa,1.0)
            assert val>baseline+1e-11
            tests+=1
    print('PASS',tests,'independent matrix/gap/weight/erasure/optimizer checks')


if __name__=='__main__':
    main()
