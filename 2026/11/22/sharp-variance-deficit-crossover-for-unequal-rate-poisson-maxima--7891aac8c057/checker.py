"""Independent finite-mass checks for a Poisson-maximum dispersion theorem.

The mathematical arguments are analytic; this script verifies the formulas
numerically with explicit unallocated probability mass reported.
"""
from itertools import product
from math import exp, pi


def poisson_mass(lam, kmax):
    assert lam > 0
    p = [exp(-lam)]
    for k in range(kmax):
        p.append(p[-1] * lam / (k + 1))
    return p


def cdf_moments(rates, kmax):
    pmfs = [poisson_mass(rate, kmax) for rate in rates]
    cdfs = []
    for p in pmfs:
        C, acc = [], 0.0
        for v in p:
            acc += v
            C.append(acc)
        cdfs.append(C)
    prev = 0.0
    mean = sq = unique_mean = 0.0
    for k in range(kmax + 1):
        val = 1.0
        for F in cdfs:
            val *= F[k]
        atom = val - prev
        mean += k * atom
        sq += k*k*atom
        prev = val
        if k:
            for i in range(len(rates)):
                other_below = 1.0
                for j in range(len(rates)):
                    if i != j:
                        other_below *= cdfs[j][k-1]
                unique_mean += k * pmfs[i][k] * other_below
    var = sq - mean*mean
    tie_mean = mean - unique_mean
    residual_cov_via_size_bias = unique_mean-var
    return (mean, var, tie_mean, residual_cov_via_size_bias, 1-prev)


def direct_enumeration(rates, kmax):
    pmfs = [poisson_mass(rate, kmax) for rate in rates]
    vals = [0.0]*6
    for counts in product(range(kmax+1), repeat=len(rates)):
        mass = 1.0
        for i, k in enumerate(counts):
            mass *= pmfs[i][k]
        maximum = max(counts)
        residual = sum(counts)-maximum
        vals[0] += mass
        vals[1] += mass*maximum
        vals[2] += mass*maximum**2
        vals[3] += mass*residual
        vals[4] += mass*maximum*residual
        vals[5] += mass*maximum*(counts.count(maximum)>=2)
    total, mean, second, er, emr, emtie = vals
    var = second/total-(mean/total)**2
    cov = emr/total-mean*er/total**2
    return mean/total,var,emtie/total,cov,1-total


def audit():
    for rates,kmax in [((0.3,0.6),26),((1.0,2.0),35),((0.5,1.0,1.3),27)]:
        one=cdf_moments(rates,kmax)
        two=direct_enumeration(rates,kmax)
        assert max(one[-1],two[-1])<1e-11
        assert max(abs(one[j]-two[j]) for j in range(4))<2e-9
        mean,var,tie,cov,_=two
        assert abs((mean-var)-(tie+cov))<2e-9
        assert mean>var and tie>0 and cov>=-1e-10
        print('direct',rates,'mean=',round(mean,9),'var=',round(var,9),'tie=',round(tie,9),'cov=',round(cov,9))
    for rates in [(1,2),(2,2),(2,2,1)]:
        for t in [10,50,200]:
            mean,var,tie,cov,tail=cdf_moments([t*x for x in rates], max(100,int(8*t*max(rates)+50)))
            assert tail<1e-10
            assert abs((mean-var)-(tie+cov))<1e-7*max(1,mean)
            print('scaled',rates,'t=',t,'fano=',round(var/mean,9),'deficit=',round(mean-var,8))
    for rates in [(1,2),(2,2,1)]:
        predicted = 2*sum(rates[i]*rates[j] for i in range(len(rates)) for j in range(i+1,len(rates)))
        for t in (0.003,0.001):
            mu, var, _, _, residual = cdf_moments([t*x for x in rates],80)
            observed = (mu-var)/(t*t)
            assert residual < 1e-12
            assert abs(observed-predicted)/predicted < .03
            print('sparse',rates,'t=',t,'coefficient=',round(observed,7),'limit=',predicted)
    print('two-top Gaussian Fano limit',round(1-1/pi,9))
    print('All checks passed; numerical truncations are not proofs.')

if __name__=='__main__':
    audit()
