"""Exact-rational checks for the periodically switched threshold map.

Finite checks are diagnostics, not a substitute for the analytic proof.
"""
from fractions import Fraction as Q
from math import log


def test(a, b):
    a, b = Q(a), Q(b)
    assert a != b and b*(a-1)>2 and a*(b-1)>2
    lam = a*b
    T = (b+1)/(lam-1)
    assert 0 < T < min(Q(1), b-1)
    # Ordered branches and their constants: F(x)=lam*x+constant.
    constants = (b+1, b-1, 1-b, -b-1)
    def inverse(i,y):
        return (y-constants[i])/lam
    intervals = [(inverse(i,-T),inverse(i,T)) for i in range(4)]
    bounds = [(-T,-1/a),(-1/a,Q(0)),(Q(0),1/a),(1/a,T)]
    for (lo,hi),(blo,bhi) in zip(intervals,bounds):
        assert blo <= lo < hi <= bhi
        if blo == -T: assert lo == -T
        if bhi == T: assert hi == T
        assert lam*(hi-lo)==2*T
        assert lam*lo+constants[intervals.index((lo,hi))]==-T
        assert lam*hi+constants[intervals.index((lo,hi))]==T
    for i in range(3):
        assert intervals[i][1] < intervals[i+1][0]
    assert intervals[0][0]==-T and intervals[-1][1]==T
    # Exact total interval length for every finite cylinder level.
    level = [(-T,T)]
    for n in range(1,5):
        level = [(inverse(i,lo),inverse(i,hi)) for lo,hi in level for i in range(4)]
        assert len(level)==4**n
        assert sum((hi-lo for lo,hi in level),Q(0))==(2*T)*((Q(4)/lam)**n)
    # Cross-check true recurrence for interior inverse midpoints.
    def g(x):
        return 1 if x>=0 else -1
    for i,(lo,hi) in enumerate(intervals):
        x=(lo+hi)/2
        y=a*x-g(x)
        z=b*y-g(y)
        assert z==0
        assert z==lam*x+constants[i]
    print('PASS', 'a=',a,'b=',b,'lambda=',lam,'T=',T,
          'dimension≈',round(log(4)/log(float(lam)),10),
          'two-step survival fraction=',Q(4)/lam)

for a,b in [('5/2','23/10'),('3','4'),('7/2','5/2')]:
    test(a,b)
print('PASS: exact rational branch, cylinder and finite-level escape checks')
