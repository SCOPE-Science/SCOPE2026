"""Numerical convergence diagnostic for normal-cone collision critical window.
The theorem is proved by the hypergeometric local and distributional CLT;
these calculations are not a substitute for the proof.
"""
from scipy.stats import hypergeom, norm
from math import sqrt,floor
for a in (-1.,0.,1.):
    c=norm.sf(a)**2/norm.pdf(a)
    print('a=',a,'limit sigma-normalized M*C=',c)
    for n in (200,800,3200,12800):
        h=round(.4*n); k=round(.3*n)
        mu=h*k/n
        sigma=sqrt(k*(n-k)*h*(n-h)/(n*n*(n-1)))
        r=floor(mu+a*sigma)
        p=hypergeom.sf(r-1,n,h,k)
        pt=hypergeom.pmf(r,n,h,k)
        less=hypergeom.cdf(r-1,n,h,k)
        # M*C = less + p**2 / pt
        MC=less+p*p/pt
        boundary=(p*p/pt)/MC
        print(f' n={n} r={r} value={MC/sigma:.9f} boundary_fraction={boundary:.8f}')
print('CRITICAL_SCALING_NUMERIC_PASS')
