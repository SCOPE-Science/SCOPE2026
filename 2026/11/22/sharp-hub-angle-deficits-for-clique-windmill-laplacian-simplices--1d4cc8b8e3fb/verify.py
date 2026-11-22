"""Exact score identities and independent finite-sample checks for clique-windmill Laplacian simplices."""
import math
import numpy as np
from scipy.special import ndtr


def laplacian(r,m):
    d=r*m
    a=np.zeros((d+1,d+1),dtype=int)
    a[0,1:]=1;a[1:,0]=1
    for b in range(m):
        ids=range(1+b*r,1+(b+1)*r)
        for i in ids:
            for j in ids:
                if i!=j:a[i,j]=1
    return np.diag(a.sum(axis=1))-a


def centered_peak(z,r,m):
    arr=z.reshape(m,r)
    raw=(r+1)*arr-arr.sum(axis=1,keepdims=True)
    mu=z.mean()
    return raw.max()-mu


def conditional_prob(z,r,m):
    peak=centered_peak(z,r,m)
    d=m*r
    return float(ndtr(-peak/((d+1)*math.sqrt(1+1/d))))


def test_exact_geometry():
    rng=np.random.default_rng(20261115)
    c=0
    for r in range(1,6):
        for m in range(1,9):
            L=laplacian(r,m)
            n=1+r*m
            assert np.array_equal(L,L.T)
            assert np.array_equal(L.sum(axis=0),np.zeros(n,dtype=int))
            assert np.linalg.matrix_rank(L)==n-1
            for _ in range(12):
                g=rng.normal(size=n)
                scores=L@g
                z=g[1:]
                raw=((r+1)*z.reshape(m,r)-z.reshape(m,r).sum(axis=1,keepdims=True)).ravel()
                assert np.allclose(scores[1:],raw-g[0],atol=1e-10)
                assert abs(scores[0]-(n-1)*g[0]+z.sum())<1e-10
                hub=(scores[0]>scores[1:].max())
                derived=(n*(g[0]-z.mean())>centered_peak(z,r,m))
                assert hub==derived
                c+=1
            # Validate exact variance by explicit coefficients on the Gaussian g.
            per=L[1]
            assert int(per@per)==r*r+r-1+1 # residual -g0 contributes 1
    return c


def trial(r,m,B,seed):
    rng=np.random.default_rng(seed)
    vals=[]
    remain=B
    while remain:
        t=min(512,remain)
        z=rng.standard_normal((t,m,r))
        raw=(r+1)*z-z.sum(axis=2,keepdims=True)
        peak=raw.max(axis=(1,2))-z.mean(axis=(1,2))
        pv=ndtr(-peak/((m*r+1)*math.sqrt(1+1/(m*r))))
        vals.append(pv)
        remain-=t
    ps=np.concatenate(vals)
    p=float(ps.mean())
    err=float(ps.std(ddof=1)/math.sqrt(B))
    return p,err


def test_conditional():
    for r,m in ((1,8),(2,8),(3,5)):
        rng=np.random.default_rng(40102+r*100+m)
        B=160000
        z=rng.standard_normal((B,m,r))
        g0=rng.standard_normal(B)
        raw=(r+1)*z-z.sum(axis=2,keepdims=True)
        peak=raw.max(axis=(1,2))-z.mean(axis=(1,2))
        cond=ndtr(-peak/((m*r+1)*math.sqrt(1+1/(m*r))))
        from_sample=((g0-z.mean(axis=(1,2)))*(m*r+1)>peak)
        discrepancy=abs(cond.mean()-from_sample.mean())
        bound=6*math.sqrt(.25/B)+.001
        assert discrepancy<bound,(r,m,discrepancy,bound)
    return 3


def main():
    count=test_exact_geometry()
    indep=test_conditional()
    print('Exact Gaussian score identities checked:',count,'small-case random Gaussian vectors')
    print('Hub conditional expectation separately checked:',indep,'cases')
    print('r m p_estimate normalized_deficit expected_limit max_6se')
    for r in (1,2,3):
        for m in (32,128,512,2048):
            p,e=trial(r,m,15000,20261115+100*r+m)
            val=(.5-p)*(m*r+1)/math.sqrt(math.log(m))
            lim=math.sqrt(r*r+r-1)/math.sqrt(math.pi)
            print(r,m,f'{p:.9f}',f'{val:.6f}',f'{lim:.6f}',f'{6*e*(m*r+1)/math.sqrt(math.log(m)):.6f}')
            assert p < .5
    print('WINDMILL_LAPLACIAN_CONE_EXACT_PASS')

if __name__=='__main__':main()
