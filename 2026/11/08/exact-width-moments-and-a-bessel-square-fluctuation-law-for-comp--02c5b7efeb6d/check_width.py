"""Reproducible numerical checks for complete-bipartite symmetric-edge-polytope width laws."""
import numpy as np
from scipy.special import ndtr, ndtri, k1, gammaln
from numpy.polynomial.legendre import leggauss
from scipy.stats import norm


def gaussian_support(xs, ys):
    return np.maximum(np.max(xs, axis=-1)-np.min(ys,axis=-1),
                      np.max(ys,axis=-1)-np.min(xs,axis=-1))


def cdf_integral(p,q,t,n=150):
    nodes, weights = leggauss(n)
    v = (nodes[:,None]+1)/2
    z = (nodes[None,:]+1)/2
    vweights = weights[:,None]/2
    zweights = weights[None,:]/2
    w=v+(1-v)*z
    l=ndtri(v)
    u=ndtri(w)
    gap=np.maximum(ndtr(l+t)-ndtr(u-t),0.0)
    body = p*(p-1)*(1-v)*((1-v)*z)**(p-2)*gap**q
    return np.sum(vweights*zweights*body)


def limiting_cdf(y):
    y=np.asarray(y)
    a=np.exp(-y/2)
    return (2*a*k1(2*a))**2


def verify():
    rng=np.random.default_rng(20261102)
    # Exact geometric support and sampled normal CDF.
    for p,q in [(2,2),(2,3),(3,4)]:
        x=rng.normal(size=(120000,p))
        y=rng.normal(size=(120000,q))
        h=gaussian_support(x,y)
        # The support of all 2pq signed edge roots must equal the max-min identity.
        edge=np.max(np.abs(x[:,:,None]-y[:,None,:]),axis=(1,2))
        assert np.allclose(h,edge,rtol=0,atol=1.e-14)
        for t in (1.,2.,3.):
            empirical=np.mean(h<=t)
            analytic=cdf_integral(p,q,t)
            assert abs(empirical-analytic)<.014,(p,q,t,empirical,analytic)
    # Elementary gamma transform and the Bessel-square limit law.
    x=rng.exponential(size=(350000,4))
    z=np.minimum(x[:,0]*x[:,1],x[:,2]*x[:,3])
    val=-np.log(z)
    assert abs(np.mean(val)-(2*np.euler_gamma+1))<.016
    assert abs(np.var(val)-3)<.07
    for t in [0.2,0.5,0.9]:
        rhs=np.exp(3*gammaln(1+t)+gammaln(2+t)-gammaln(2+2*t))
        assert abs(np.mean(z**t)-rhs)<.012
    for cut in [-1.,0.,1.,2.,3.,5.]:
        assert abs(np.mean(val<=cut)-limiting_cdf(cut))<.009
    # Random intrinsic directions: centered Gaussians, radial normalization.
    for m in (256,2048):
        d=2*m-1
        a=norm.isf(1/m)
        outputs=[]
        for _ in range(28):
            g=rng.normal(size=(256,2*m))
            g-=g.mean(axis=1,keepdims=True)
            rad=np.linalg.norm(g,axis=1)
            h=gaussian_support(g[:,:m],g[:,m:])
            width=2*h/rad
            outputs.append(a*np.sqrt(d)*width/2-2*a*a)
        t=np.concatenate(outputs)
        for cut in [0.,2.,4.]:
            tol=.17 if m==256 else .125
            assert abs(np.mean(t<=cut)-limiting_cdf(cut))<tol,(m,cut,np.mean(t<=cut),limiting_cdf(cut))
    print('COMPLETE_BIPARTITE_SYMMETRIC_EDGE_WIDTH_CHECKS_PASSED')

if __name__=='__main__':
    verify()
