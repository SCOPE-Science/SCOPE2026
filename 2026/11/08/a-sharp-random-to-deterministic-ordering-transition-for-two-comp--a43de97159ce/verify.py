"""Exact-rational reproducibility checks for a two-component proximal reshuffling model.

Only Python standard library is needed. The universal result is established by
algebra in RESULT.md; these checks catch normalization/order transcription errors.
"""
from fractions import Fraction as F
import itertools

checks = 0

def check(ok, context):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(context)

def moments(a,b,ua,ub,h,p):
    a,b,ua,ub,h,p=map(F,(a,b,ua,ub,h,p))
    ra=1/(1+h*a); rb=1/(1+h*b)
    r=ra*rb
    ca=(1-ra)*ua+ra*(1-rb)*ub # a is last
    cb=(1-rb)*ub+rb*(1-ra)*ua # b is last
    delta=ca-cb
    ec=p*ca+(1-p)*cb
    m=ec/(1-r)
    ec2=p*ca*ca+(1-p)*cb*cb
    second=(2*r*m*ec+ec2)/(1-r*r)
    var=second-m*m
    star=(a*ua+b*ub)/(a+b)
    risk=var+(m-star)**2
    p0=a/(a+b)
    predicted=delta**2*((p-p0)**2/(1-r)**2 + p*(1-p)/(1-r*r))
    p_unc=F(1,2)+(1+r)*(a-b)/(4*r*(a+b))
    p_opt=min(F(1),max(F(0),p_unc))
    return locals()

for a in range(2,9):
  for b in range(1,a):
    for h in (F(1,20), F(1,4),F(1,2),F(1),F(2),F(5)):
      for ua,ub in ((1,-1),(2,0),(-3,4)):
        for p in (F(0),F(1,5),F(1,2),F(4,5),F(1)):
          d=moments(a,b,ua,ub,h,p)
          check(d['risk']==d['predicted'], ('risk',a,b,h,ua,ub,p))
          check(d['var']==d['delta']**2*p*(1-p)/(1-d['r']**2),('var',a,b,h,ua,ub,p))
          check(d['ca']-d['cb']==(1-d['ra'])*(1-d['rb'])*(ua-ub),('difference',a,b,h))
          check(F(0)<d['r']<F(1),('contraction',a,b,h))
          check(F(0)<=d['p_opt']<=1,('probability',a,b,h))
        d0=moments(a,b,ua,ub,h,F(a,a+b))
        check(d0['m']==d0['star'],('unbiased',a,b,h,ua,ub))
        q=d0['p_opt']
        r_opt=moments(a,b,ua,ub,h,q)['risk']
        for p in (F(0),F(1,2),F(1),d0['p0']):
            check(r_opt<=moments(a,b,ua,ub,h,p)['risk'],('minimum',a,b,h,p))
        # derivative-based exact minimizer: compare displacement against curvature.
        r=d0['r']; delta=d0['delta']; p0=d0['p0']
        curvature=2*delta**2/(1-r)**2-2*delta**2/(1-r*r)
        check(curvature>0,('strict_convexity',a,b,h))

for a,b,h in ((3,1,F(1,4)),(3,1,F(1)),(5,2,F(2,5))):
 d=moments(a,b,1,-1,h,F(1,2));print('a,b,h=',a,b,h,'r=',d['r'],'p0=',d['p0'],'p*=',d['p_opt'])
 for p in (F(1,2),d['p0'],d['p_opt'],F(1)):
  print('   p=',p,'mean=',moments(a,b,1,-1,h,p)['m'],'risk=',moments(a,b,1,-1,h,p)['risk'])

print('PASS exact-rational assertions:',checks)
