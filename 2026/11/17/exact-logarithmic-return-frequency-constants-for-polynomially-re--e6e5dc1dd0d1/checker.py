import math

def rho(p,e):
    if p==1: return e/(1+e)
    d=e**(p/(p-1))
    return d**(p-1)/(d**(p-1)+(1-d)**(p-1))

def frac(p,e,a):
    t=e**p-abs(1-a)**p
    if t<=0: return 0
    return t/(a**p+t)

cases=0
for p in (1,1.01,1.1,1.5,2,3,5):
 for e in (.03,.1,.2,.49,.6,.8):
    r=rho(p,e)
    if p>1:
      d=e**(p/(p-1)); c=1-d
    else:c=1
    for j in range(1001):
      a=1-e+2*e*j/1000
      assert frac(p,e,a)<=r+1e-11,(p,e,a,frac(p,e,a),r)
      cases+=1
    assert abs((1-c)**p +c**p*r/(1-r)-e**p)<1e-8, (p,e)
    for alpha in (.6,1.3,2):
      Q=math.exp(-math.log(r)/(alpha*p))
      # explicit q-step scaled error is below epsilon
      if Q<1e25:
        k=6
        ratios=[((Q**k*(k+1)**2)/(Q**(k+h)*(k+h+1)**2))**(alpha*p) for h in range(1,30)]
        err=(1-c)**p+c**p*sum(ratios)
        assert err <e**p,(p,e,alpha,err,e**p)
        cases+=1
    # compare exact p2
    if p==2:assert abs(r-e*e)<1e-14
    if p==1:assert abs(r-e/(1+e))<1e-14
print('checks_passed',cases)
print('samples',[(p,e,round(rho(p,e),8), round(p/math.log(1/rho(p,e)),8))for p in (1,2,3) for e in (.25,.5)])
