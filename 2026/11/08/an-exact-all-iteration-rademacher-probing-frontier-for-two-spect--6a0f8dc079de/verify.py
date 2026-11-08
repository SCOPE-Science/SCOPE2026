"""Standalone reproducibility checks for the two-eigenvalue Landweber probe law.

The infinite-time and distributional statements are proved algebraically in RESULT.md;
finite tests here are diagnostic only. Dependencies: Python >=3.9, numpy.
"""
from math import comb
import numpy as np


def weights(lam_lo, lam_hi, omega, k):
    return np.array([(1-(1-omega*lam_lo)**k)**2/lam_lo,
                     (1-(1-omega*lam_hi)**k)**2/lam_hi])


def all_time_formula(kappa, p, projection_error):
    return abs(projection_error)*(kappa-1)*max(
        1/(1+p*(kappa-1)), 1/(kappa-p*(kappa-1)))


def test_random_projectors():
    rng = np.random.default_rng(17331)
    runs = 0
    for d in [3, 5, 8]:
        for rank in [1, d-1]:
            for rep in range(25):
                q,_ = np.linalg.qr(rng.standard_normal((d,d)))
                U=q[:,:rank]
                P=U@U.T
                lp=float(rng.uniform(.05,.6))
                kappa=float(rng.uniform(1.05,40))
                lh=kappa*lp
                omega=float(rng.uniform(.05,1.0))/lh
                sigma=float(rng.uniform(.5,2))
                N=30
                W=rng.choice([-1.,1.],(N,d))
                Phat=np.mean(W*(W@P.T),axis=0)
                for k in [1,2,3,5,11,25,100,800]:
                    qlo,qhi=weights(lp,lh,omega,k)
                    Gamma=sigma**2*(qhi*P+qlo*(np.eye(d)-P))
                    g=np.diag(Gamma)
                    gh=np.mean(W*(W@Gamma.T),axis=0)
                    observed=(gh-g)/g
                    t=qhi/qlo
                    predicted=(Phat-np.diag(P))*(t-1)/(1+np.diag(P)*(t-1))
                    assert np.allclose(observed,predicted,rtol=5e-9,atol=5e-12)
                    bounds=np.array([all_time_formula(kappa,p,e) for p,e in zip(np.diag(P),Phat-np.diag(P))])
                    assert np.all(abs(observed)<=bounds+3e-11)
                    runs+=1
                lim=(Phat-np.diag(P))*(1/kappa-1)/(1+np.diag(P)*(1/kappa-1))
                first=(Phat-np.diag(P))*(kappa-1)/(1+np.diag(P)*(kappa-1))
                true_bound=np.maximum(np.abs(first),np.abs(lim))
                assert np.allclose(true_bound,bounds,atol=2e-12)
    return runs


def test_rank_one_exact_law():
    from itertools import product
    testcases=0
    for d in [3,4,5]:
        P=np.ones((d,d))/d
        p=1/d
        for N in [1,2]:
            if d*N>12:
                continue
            values={}
            for bits in product([-1.,1.],repeat=d*N):
                W=np.array(bits).reshape(N,d)
                shat=np.mean(W*(W@P.T),axis=0)[0]
                S=round(N*d*(shat-p))
                values[S]=values.get(S,0)+1
            M=N*(d-1)
            assert sum(values.values())==2**(d*N)
            for h in range(M+1):
                s=2*h-M
                assert values.get(s,0)==comb(M,h)*2**N
            testcases+=1
    return testcases


def test_boundaries():
    for kappa in [1.001,2,10,300]:
        vals=[]
        for p in [.12,.49,.5,.51,.88]:
            first=(kappa-1)/(1+p*(kappa-1))
            end=(kappa-1)/(kappa-p*(kappa-1))
            vals.append((p,first,end))
            if p<.5:
                assert first>end
            elif p>.5:
                assert end>first
            else:
                assert abs(end-first)<1e-10
    return len(vals)*4

if __name__=='__main__':
    a=test_random_projectors()
    b=test_rank_one_exact_law()
    c=test_boundaries()
    print(f'VERIFY_OK; {a} dense-operator comparisons; {b} exact exhaustive binomial cases; {c} endpoint checks')
