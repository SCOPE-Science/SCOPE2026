#!/usr/bin/env python3
"""Finite sanity checks for the stated predator-prey recurrence; not a proof."""
import math
for r, alpha, gamma in ((0.5,0.4,0.6),(0.5,0.6,0.6),(1.2,0.7,0.7)):
    x,y=1.0,0.2
    logy=math.log(y)
    values=[]
    for n in range(1,200001):
        f=r*x*math.exp(1-x)
        p=alpha*x*y/(1+x)
        m=1-gamma+alpha*x/(1+x)
        assert 0<m<1 and 0<=p<f+x and x>0
        xnew=x+f-p
        ynew=y*m
        assert xnew>0 and 0<=ynew<=y
        logy+=math.log(m)
        x,y=xnew,ynew
        if n in (10000,50000,200000):
            residual=x-math.log(n)-math.log(math.log(n))-math.log(r*math.e)
            scaled=logy/n if alpha<gamma else logy*math.log(n)/n
            values.append((n,residual,scaled))
    assert all(abs(z[1])<0.3 for z in values)
    assert values[-1][1]<values[0][1]
    assert values[-1][2]<0
    target=math.log(1-gamma+alpha) if alpha<gamma else -gamma
    assert abs(values[-1][2]-target)<0.25
    print('CASE',r,alpha,gamma,'target',round(target,8),'last',values[-1])
print('VERIFY_OK positive_three_cases=3 finite_horizons_per_case=3 analytic_limits_not_certified=1')
