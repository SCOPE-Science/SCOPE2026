#!/usr/bin/env python3
"""Exact-rational checks for affine branch geometry and the neutral transfer law."""
from fractions import Fraction as Q

n = 0
for eps in [Q(1,128), Q(1,64), Q(1,32), Q(1,16)]:
    s=1+2*eps
    c=Q(1,2)-eps
    e=1-2*eps
    d=Q(1,2)+eps+4*eps**2
    a=1/(2*s)
    assert c < Q(1,2) < d < e < 1
    def T(x): return 2*x if x<=Q(1,2) else 1-s*(x-Q(1,2))
    def R(t): return 1-2*s*t if t<=a else s*s*(t-a)
    assert T(c)==e and T(Q(1,2))==1 and T(d)>=e
    assert T(e)==d and T(1)==c
    for i in range(1025):
        t=Q(i,1024)
        x=c+2*eps*s*t
        result=(T(T(x))-c)/(2*eps*s)
        assert result==R(t), (eps,t,result,R(t))
        assert 0<=result<=1
        n+=1
    m=s*(s-Q(1,2))
    assert a<=Q(1,2) and m<=Q(45,64)
    assert s*s*(m-a)<a
    n+=1
# Limiting two-cell transfer equations and normalization.
A=Q(4,3); B=Q(2,3)
assert A/2+B==A and A/2==B
assert (A+B)/2==1
mean=A*Q(1,8)+B*Q(3,8)
assert mean==Q(5,12)
assert 2*mean==Q(5,6)
print('PASS',n,'exact conjugacy and branch samples; stationary density and moment identities')
