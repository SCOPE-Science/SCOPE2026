"""Standalone checks of one-probe functional Nystrom trace ordering."""
from fractions import Fraction
from math import gamma, pi, sqrt
import numpy as np


def scalar_trace(values, weights, q, f):
    a = np.asarray(values, dtype=float)
    w = np.asarray(weights, dtype=float)
    b = f(a)
    p = 2*q - 1
    da = np.dot(w, a**p)
    db = np.dot(w, b**p)
    left = float(f(np.array([np.dot(w, a**(p+1))/da]))[0]) if da > 0 else 0.
    right = float(np.dot(w, b**(p+1))/db) if db > 0 else 0.
    return left, right


def dense_trace(a, g, q, f):
    aa, uu = np.linalg.eigh(a)
    aa = np.maximum(aa, 0.)
    af = (uu*f(aa))@uu.T
    def nystrom(B):
        z = g.copy()
        for _ in range(q):
            z = B@z
        base = g.copy()
        for _ in range(2*q-1):
            base = B@base
        den = float(g.T@base)
        return np.outer(z,z)/den if den > 1e-13 else np.zeros_like(B)
    nf = nystrom(a)
    fn = float(np.sum(f(np.maximum(np.linalg.eigvalsh(nf),0.))))
    df = float(np.trace(nystrom(af)))
    return fn, df


def exact_fraction_checks():
    count = 0
    specs = [(Fraction(1,3), Fraction(3,4), Fraction(2), Fraction(5)),
             (Fraction(1,11), Fraction(1), Fraction(4), Fraction(9)),
             (Fraction(2,5), Fraction(3,2), Fraction(2), Fraction(7))]
    for spec in specs:
        for q in (1,2,3):
            p = 2*q-1
            a=list(spec)
            w=[Fraction(2),Fraction(5),Fraction(1),Fraction(7)]
            def v(b):
                return sum(wi*bi**(p+1) for wi,bi in zip(w,b))/sum(wi*bi**p for wi,bi in zip(w,b))
            Ra=v(a)
            fc=lambda x:x/(1+x)
            fx=[fc(x) for x in a]
            assert fc(Ra)>=v(fx)
            fd=lambda x:x*x
            dx=[fd(x) for x in a]
            assert fd(Ra)<=v(dx)
            count+=2
    return count


def check():
    n_exact=exact_fraction_checks()
    rng=np.random.default_rng(25115)
    n_random=0
    n_dense=0
    for n in (2,3,5,7):
        for q in (1,2,3):
            for _ in range(150):
                vals=np.exp(rng.uniform(-2,2,size=n))
                if n > 2 and rng.random() < .3:
                    vals[0]=0.0
                weights=rng.uniform(.1,2.,size=n)
                for f,sgn in ((np.sqrt,1),(np.log1p,1),(lambda x:x/(1+x),1),
                              (lambda x:x*x,-1),(lambda x:x*x*x,-1)):
                    L,R=scalar_trace(vals,weights,q,f)
                    assert sgn*(L-R) >= -1e-10*(1+abs(L)+abs(R))
                    assert L <= sum(f(vals))+1e-9
                    assert R <= sum(f(vals))+1e-9
                    n_random+=1
                if n<=5:
                    T=rng.normal(size=(n,n))
                    U,_=np.linalg.qr(T)
                    A=(U*vals)@U.T
                    g=U@(np.sqrt(weights))
                    for f in (np.sqrt,lambda x:x*x):
                        L,R=scalar_trace(vals,weights,q,f)
                        x,y=dense_trace(A,g,q,f)
                        assert np.allclose((x,y),(L,R),rtol=5e-7,atol=2e-7)
                        n_dense+=1
    from scipy.integrate import quad
    n_integrals=0
    for alpha in (.5,2.):
        C=2*gamma(alpha+.5)/(sqrt(pi)*gamma(alpha))
        for e in (1e-3,1e-5):
            integrand=lambda v: (1-((v*v+e)/(v*v+1))**alpha)/(1+e*v*v)
            value=(2*sqrt(e)/pi)*quad(integrand,0,np.inf,epsabs=1e-12)[0]
            assert abs(value/(C*sqrt(e))-1)<.05
            n_integrals+=1
    print('PASS exact_fraction_checks',n_exact)
    print('PASS pointwise_spectral_checks',n_random)
    print('PASS dense_reconstruction_checks',n_dense)
    print('PASS asymptotic_integral_checks',n_integrals)
    print('PASS total',n_exact+n_random+n_dense+n_integrals)

if __name__=='__main__':
    check()
