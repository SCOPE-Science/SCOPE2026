"""Reproducible exact arithmetic for a three-node entropy limiter example.

All quantities are Fractions; no floats, network access, or external packages.
"""
from fractions import Fraction as Q

def dot(w, a):
    return sum((wi*ai for wi, ai in zip(w, a)), Q(0))

def entropy(t):
    return t*t/Q(2) + t**4/Q(4)

def E(w, a):
    return dot(w, [entropy(t) for t in a])

def squared_distance(w, a, b):
    return dot(w, [(x-y)**2 for x,y in zip(a,b)])

def run():
    w=(Q(1,6),Q(4,6),Q(1,6))
    x=(Q(2,5),Q(1),Q(8,5))
    y=(Q(1,2),Q(1),Q(3,2))
    z=(Q(191,400),Q(2017,2000),Q(2977,2000))
    m=Q(1)
    theta=Q(5,6)
    B=Q(59,64)
    assert sum(w)==1 and all(v>0 for v in w)
    assert dot(w,x)==m and dot(w,y)==m and dot(w,z)==m
    assert y==tuple(m+theta*(v-m) for v in x)
    assert E(w,y)==B
    assert E(w,z)-E(w,y)==-Q(254723823,2560000000000)
    assert E(w,z)<B
    assert squared_distance(w,y,x)==Q(1,300)
    assert squared_distance(w,z,x)==Q(2497,800000)
    assert squared_distance(w,z,x)-squared_distance(w,y,x)==-Q(509,2400000)
    assert all(v>0 for v in x+y+z)
    # Convexity: eta''(t)=1+3*t**2>0, eta'''(1)=6>0.
    # The weighted-cubic witness on the zero-mean subspace is nonzero.
    u=(Q(4,6),-Q(1,6),Q(0))
    assert dot(w,u)==0
    assert dot(w,[q**3 for q in u])==Q(5,108)
    # The derivative test on the putative projection is nonstationary.
    # Under weighted inner product, projected gradient of E at y has
    # components eta'(y_i)-sum_j w_j eta'(y_j).
    yp=[v+v**3 for v in y]
    av=dot(w,yp)
    grad=[v-av for v in yp]
    delta=[v-m for v in y]
    assert delta[1]==0 and grad[1]!=0
    print('Exact rational witness PASS')
    print('budget',B,'candidate_entropy',E(w,z))
    print('radial_squared_correction',squared_distance(w,y,x))
    print('better_squared_correction',squared_distance(w,z,x))
    print('improvement',squared_distance(w,y,x)-squared_distance(w,z,x))

if __name__=='__main__':
    run()
