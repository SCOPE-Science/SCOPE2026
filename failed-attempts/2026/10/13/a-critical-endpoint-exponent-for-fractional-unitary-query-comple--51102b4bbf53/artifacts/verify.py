#!/usr/bin/env python3
import math
def lower_ratio(alpha,c,eps):
    t=c*eps**alpha
    return math.log(math.sin(math.pi*t)/(4*eps))/math.log(1/eps)
for alpha in (0.25,0.5,0.75):
    vals=[lower_ratio(alpha,1.3,10.0**(-k)) for k in (6,12,24)]
    assert abs(vals[-1]-(1-alpha))<0.08
for alpha in (1.25,1.5,2.0):
    eps=1e-12; t=1.7*eps**alpha
    assert 2*math.pi*t<eps
for delta in (0.1,0.5,0.9):
    for t in (1e-4,1e-3,1e-2):
        L=t*(2*math.pi-delta)
        assert 4*math.sin(L/4)<=L+1e-15
        assert L<2*math.pi*t
print("VERIFY_OK")
