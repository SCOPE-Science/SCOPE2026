"""Numerical cross-checks for sharp planar Minkowski inverse stability.

Analytic proof is in RESULT.md; samples here do not certify universal claims.
"""
import math

pi = math.pi

def G(t):
    x = abs((t + pi) % (2*pi) - pi)
    return -math.cos(x)/(4*pi) + (.5 - x/(2*pi))*math.sin(x)

def angular_dist(x,y):
    d = abs((x-y+pi)%(2*pi)-pi)
    return d

def nearly(x,y,tol=2e-12):
    assert abs(x-y)<=tol*max(1.,abs(x),abs(y)), (x,y)

assert abs(G(0)+1/(4*pi))<1e-12
nearly(G(pi),1/(4*pi))
nearly(G(pi/2),1/4)
for eps in [.4, .1, .04, .02, .004, .0008, .0001]:
    c=math.cos(eps);a=1-c
    weights=[(.25,eps),(.25,-eps),(a/4,pi/2),(a/4,-pi/2),(c/2,pi)]
    nearly(sum(w for w,_ in weights),1)
    nearly(sum(w*math.cos(t) for w,t in weights),0)
    nearly(sum(w*math.sin(t) for w,t in weights),0)
    # Difference at angle zero between convolutions of the two balanced measures.
    delta=2*pi*(sum(w*G(t) for w,t in weights)-.5*G(0)-.5*G(pi))
    expected=(pi-eps)*math.sin(eps)/2+pi*(1-c)/4
    nearly(delta,expected)
    transport=eps/2+pi*a/4
    assert delta<=pi*transport+1e-12
    print('epsilon',eps,'support_difference',delta,'transport_cost_upper',transport,'ratio_lower',delta/transport)
assert abs(((pi-1e-4)*math.sin(1e-4)/2+pi*(1-math.cos(1e-4))/4)/
           (1e-4/2+pi*(1-math.cos(1e-4))/4)-pi)<.001

# An independent finite-grid check of strict short-arc kernel contraction.
for i in range(101):
    x=-pi+2*pi*i/101
    for j in range(i):
        y=-pi+2*pi*j/101
        d=angular_dist(x,y)
        assert abs(G(x)-G(y))<d/2+1e-12
print('PASS: exact-formula comparisons and 5050 pairwise kernel checks')
