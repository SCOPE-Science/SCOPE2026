#!/usr/bin/env python3
"""Exact rational certificate for two trace-distance revivals.
Python 3 standard library only.  No floating point is used in assertions.
"""
from fractions import Fraction as Q

N = 80
# a=i/(1/3+i)=(9+3i)/10.  z_t=-(1/3+i)t.
A_RE, A_IM = Q(9,10), Q(3,10)

def certified_square(t):
    t = Q(t)
    zr, zi = -t / 3, -t
    pr, pi = Q(1), Q(0)
    sr, si = pr, pi
    for n in range(N):
        ar, ai = n + A_RE, A_IM
        br, bi = ar*zr-ai*zi, ar*zi+ai*zr
        newr = (pr*br-pi*bi)/((n+1)**2)
        newi = (pr*bi+pi*br)/((n+1)**2)
        pr, pi = newr, newi
        sr, si = sr+pr, si+pi
    # For all four t<=16, |z_t|<17 and |a|<1. Thus
    # |T_(n+1)|/|T_n| <= 17/(n+1), for every n>=80.
    # Tail n>=81 bounded by |T_80| * (17/81)/(1-17/82).
    epsilon = (abs(pr)+abs(pi)) * Q(17,81) / (1-Q(17,82))
    sq = sr*sr+si*si
    delta = 2*(abs(sr)+abs(si))*epsilon+epsilon*epsilon
    return sq-delta, sq+delta

bounds={
    Q(15,2):('below',Q(19,500)),
    Q(10):('above',Q(111,1000)),
    Q(14):('below',Q(7,200)),
    Q(16):('above',Q(9,200)),
}
for t,(kind,d) in bounds.items():
    lo,hi=certified_square(t)
    assert lo>=0, (t,'nonpositive certified lower bound')
    if kind=='below':
        assert hi < d*d, (t,'upper square inequality failed')
    else:
        assert lo > d*d, (t,'lower square inequality failed')
    print('t=',str(t), 'certified squared trace distance in',
          '[%.13g, %.13g]'%(float(lo),float(hi)),
          'and',kind, str(d))
print('PASS: two separated positive-variation intervals,')
print('BLP lower bound > (111/1000-19/500)+(9/200-7/200) = 83/1000.')
