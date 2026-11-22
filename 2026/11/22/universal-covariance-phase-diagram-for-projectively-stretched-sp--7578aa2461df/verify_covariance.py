"""Finite diagnostics for a two-block spherical-Dirichlet covariance theorem.

Requires mpmath 1.3 or later. The infinite-dimensional/all-parameter
claims follow from the analytical proof, not from the checks in this file.
"""
import mpmath as mp

mp.mp.dps = 45
HALF = mp.mpf('0.5')

def moment(a, t, r, s):
    """E[(B/(B+r*(1-B)))**s], B~Beta(a,t)."""
    norm = mp.beta(a, t)
    return mp.quad(
        lambda b: b**(a-1)*(1-b)**(t-1)*(b/(b+r*(1-b)))**s/norm,
        [0, HALF, 1],
    )

def criterion(a, t, r):
    e1 = moment(a, t, r, 1)
    eh = moment(a, t, r, HALF)
    return e1/(eh**2)

def boundary(a):
    return a*(mp.gamma(a)/mp.gamma(a+HALF))**2

def derivative_log_criterion(a,t,r):
    # Strictly positive by Holder/log-convexity, checked on sample inputs.
    m1 = moment(a,t,r,1)
    m2 = moment(a,t,r,2)
    mh = moment(a,t,r,HALF)
    m3h = moment(a,t,r,mp.mpf('1.5'))
    return (m2/m1-m3h/mh)/r

def root(a, t):
    k=boundary(a)
    l=mp.mpf(1);u=mp.mpf(2)
    while criterion(a,t,u)<k:
        u*=2
        if u>mp.mpf('1e8'): raise AssertionError('failed to bracket')
    for _ in range(65):
        mid=(l+u)/2
        if criterion(a,t,mid)<k: l=mid
        else: u=mid
    return (l+u)/2

def group_covariance(a,t,r,shape1,shape2):
    # Two distinct coordinates in the first block.
    e1=moment(a,t,r,1)
    eh=moment(a,t,r,HALF)
    ci=mp.gamma(shape1+HALF)/mp.gamma(shape1)
    cj=mp.gamma(shape2+HALF)/mp.gamma(shape2)
    return ci*cj*(e1/a-(mp.gamma(a)/mp.gamma(a+HALF)*eh)**2)

def cross_covariance(a,t,r,shape1,shape2):
    # Coordinates in opposite blocks. Beta-subvector means factor out.
    ca=(mp.gamma(shape1+HALF)/mp.gamma(shape1))*(mp.gamma(a)/mp.gamma(a+HALF))
    cb=(mp.gamma(shape2+HALF)/mp.gamma(shape2))*(mp.gamma(t)/mp.gamma(t+HALF))
    mixed=mp.quad(lambda b: b**(a-1)*(1-b)**(t-1)*
                  mp.sqrt(b*r*(1-b))/(b+r*(1-b))/mp.beta(a,t),
                  [0,HALF,1])
    first=moment(a,t,r,HALF)
    second=moment(t,a,1/r,HALF)
    return ca*cb*(mixed-first*second)

assertions=0
for A,T in ((1,1),(2,1),(1,2),(2,2),(3,1)):
    K=boundary(A)
    assert K>1; assertions+=1
    assert criterion(A,T,1)<K; assertions+=1
    R=root(A,T)
    assert R>1 and abs(criterion(A,T,R)-K)<mp.mpf('1e-18'); assertions+=1
    for q in (mp.mpf('.2'),mp.mpf('.5'),1,2,5,11,100):
        assert derivative_log_criterion(A,T,q)>0; assertions+=1
    for scale in (mp.mpf('.5'),mp.mpf('.8')):
        assert criterion(A,T,scale*R)<K; assertions+=1
    for scale in (mp.mpf('1.2'),mp.mpf('2')):
        assert criterion(A,T,scale*R)>K; assertions+=1
    print('shape sums',A,T,'upper crossing',mp.nstr(R,17))

# Concrete four-dimensional uniform-positive-sphere example:
# all alpha_i=1/2, two coordinates in each block.
A=T=mp.mpf(1)
upper=root(A,T)
lower=1/upper
assert mp.mpf('4.258065')<upper<mp.mpf('4.258067'); assertions+=1
assert mp.mpf('.234848')<lower<mp.mpf('.234849'); assertions+=1
for r in (mp.mpf('.1'),mp.mpf('.2'),mp.mpf('.5'),1,2,3,5,10):
    cI=group_covariance(A,T,r,HALF,HALF)
    cJ=group_covariance(T,A,1/r,HALF,HALF)
    cX=cross_covariance(A,T,r,HALF,HALF)
    assert (cI>0)==(r>upper); assertions+=1
    assert (cJ>0)==(r<lower); assertions+=1
    assert cX<0; assertions+=1
    print('scale',mp.nstr(r,5),'within-first',mp.nstr(cI,12),
          'within-second',mp.nstr(cJ,12),'cross',mp.nstr(cX,12))
print('PASS: ', assertions, 'deterministic high-precision numerical assertions')
