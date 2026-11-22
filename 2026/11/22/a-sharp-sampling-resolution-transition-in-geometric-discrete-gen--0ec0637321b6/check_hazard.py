"""Diagnostics for the sampled geometric-maximum DGE hazard theorem.

Requires mpmath. Analytical proofs are in RESULT.md; finite checks are not proofs.
"""
from mpmath import mp
mp.dps = 70

def survival(n, alpha, p, theta):
    if n == 0:
        return mp.mpf(1)
    z = mp.power(p, n)
    h = -mp.expm1(alpha * mp.log1p(-z))
    return h / (theta + (1-theta)*h)

def hazard(j, alpha, p, theta):
    return 1-survival(j+1,alpha,p,theta)/survival(j,alpha,p,theta)

def discriminator(alpha,p,theta):
    a = -mp.expm1(alpha*mp.log1p(-p))
    b = -mp.expm1(alpha*mp.log1p(-p*p))
    return a*(a*(1+b)-2*b)-theta*b*(1-a)**2

def classify(alpha,p,theta):
    if alpha >= 1:
        return 'increasing'
    if theta >= 2*alpha/(1+alpha):
        return 'decreasing'
    d = discriminator(alpha,p,theta)
    if d>0: return 'increasing'
    if d==0: return 'flat_first_then_increasing'
    return 'bathtub'

def verify(alpha,p,theta,n=120):
    alpha,p,theta=map(mp.mpf,(alpha,p,theta))
    hs=[hazard(j,alpha,p,theta) for j in range(n+1)]
    diffs=[hs[j+1]-hs[j] for j in range(n)]
    signs=[1 if d>mp.mpf('1e-55') else -1 if d< -mp.mpf('1e-55') else 0 for d in diffs]
    nz=[v for v in signs if v]
    assert all(nz[i]<=nz[i+1] for i in range(len(nz)-1)), (alpha,p,theta,signs[:20])
    mode=classify(alpha,p,theta)
    if mode=='increasing': assert all(d>0 for d in diffs if abs(d)>mp.mpf('1e-55'))
    if mode=='decreasing': assert all(d<0 for d in diffs if abs(d)>mp.mpf('1e-55'))
    if mode=='bathtub': assert diffs[0]<0
    assert mp.sign(discriminator(alpha,p,theta)) == mp.sign(diffs[0]),(alpha,p,theta)
    return mode, hs[:4]

if __name__ == '__main__':
    cases=0
    for alpha in ['0.1','0.25','0.5','0.9','0.99','1','1.1','2','10']:
      for p in ['0.03','0.1','0.25','0.5','0.8','0.9','0.99']:
       for theta in ['0.01','0.1','0.3','0.6','0.9','0.99']:
        verify(alpha,p,theta,140)
        cases += 1
    a=mp.mpf('0.5'); t=mp.mpf('0.1')
    c1,h1=verify(a,mp.mpf('0.5'),t)
    c2,h2=verify(a,mp.mpf('0.9'),t)
    assert c1=='increasing' and c2=='bathtub'
    print('parameter grids checked:',cases)
    print('same (alpha, theta), p=1/2:',c1, 'first hazards:', [mp.nstr(x,15) for x in h1])
    print('same (alpha, theta), p=9/10:',c2,'first hazards:',[mp.nstr(x,15) for x in h2])
    # Exhaustive rational step identities of the survival-hazard algebra.
    from fractions import Fraction as F
    algebra_checks=0
    for a_num in range(1,17):
      for b_num in range(1,a_num+1):
       a0=F(a_num,20);b0=F(b_num,20)
       for num in range(1,20):
        th=F(num,20)
        s1=a0/(th+(1-th)*a0);s2=b0/(th+(1-th)*b0)
        d=(s1*s1-s2)/s1
        R=a0*(a0*(1+b0)-2*b0)-th*b0*(1-a0)**2
        assert (d>0)==(R>0) and (d<0)==(R<0)
        algebra_checks+=1
    root=mp.findroot(lambda z: discriminator(a,z,t),(mp.mpf('0.5'),mp.mpf('0.9')))
    print('illustrative unique p threshold:',mp.nstr(root,24))
    print('bracket checks:',mp.nstr(discriminator(a,mp.mpf('0.66973958596628'),t),15),mp.nstr(discriminator(a,mp.mpf('0.66973958596629'),t),15))
    print('exact rational sign identities checked:',algebra_checks)
    print('All diagnostics passed.')
