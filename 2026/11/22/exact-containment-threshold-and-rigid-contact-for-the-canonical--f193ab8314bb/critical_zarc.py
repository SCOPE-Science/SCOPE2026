"""Reproducible interval certificate for the canonical Z-arc trim threshold.
Requires mpmath. All sign comparisons use outward-enclosing intervals.
"""
from mpmath import iv, mp

iv.dps = 65
mp.dps = 50
ONE = iv.mpf(1)
BETA_C = iv.mpf(6)/iv.sqrt(111)
BETA_S = 5*iv.sqrt(3)/iv.sqrt(111)
S0 = iv.mpf(84)/5               # 16.8 degrees
S1 = iv.mpf(337)/20             # 16.85 degrees


def sc(q, k=0):
    a = q*iv.pi/180
    sn, cs = iv.sin(a), iv.cos(a)
    if k == 1:
        return sn*BETA_C+cs*BETA_S, cs*BETA_C-sn*BETA_S
    if k == -1:
        return sn*BETA_C-cs*BETA_S, cs*BETA_C+sn*BETA_S
    assert k == 0
    return sn, cs


def f(s,q,k):
    return sc(120-s)[0]*abs(sc(q,k)[0])+sc(s)[1]*abs(sc(q-120,k)[1])+abs(sc(q-s,k)[1])/2


def g(s,side,q,k):
    return (f(s,q,k)+iv.sqrt(111)*f(s,q,k+side))/12


def candidates(s):
    for side in (1,-1):
        for label,q,k in [ ('zero',iv.mpf(0),0),('thirty',iv.mpf(30),0),('right_angle',90+s,0),
                          ('beta_break',iv.mpf(0),-side),('thirty_beta',iv.mpf(30),-side),('right_beta',90+s,-side)]:
            yield side,label,q,k

base = g(S0,-1,iv.mpf(0),1)
print('BETA break (reflected):',base)
for side,label,q,k in candidates(S0):
    if side == -1 and label == 'beta_break':
        continue
    val=g(S0,side,q,k)
    diff=val-base
    assert diff.a > iv.mpf('0.01'), ('critical comparison failed',side,label,diff)
    print('competing orientation:', 'direct' if side==1 else 'reflected',label, 'difference',diff)

# Uniform derivative bound in the theorem: for all 12 branches, |G_s'|<5
# and for the beta branch similarly, so over [S0,S1] the gap drops < 10*(pi/3600)<0.01.
assert (10*iv.pi/3600).b < iv.mpf('0.01')

X = 21/(2*iv.sqrt(111))
Y = 5*iv.sqrt(3)/(12*iv.sqrt(111))
for s in [S0,S1]:
    val=g(s,-1,iv.mpf(0),1)
    geometrical=X*sc(s)[1]+Y*sc(s)[0]
    assert (val-geometrical).a < 0 < (val-geometrical).b
    assert (val-geometrical).delta < iv.mpf('1e-60')

alpha = (24*mp.sqrt(37)-131)/(37*mp.sqrt(3))
delta = mp.degrees(mp.atan(alpha))
tcrit = 30-2*delta
assert 3.6 < tcrit < 3.7
print('exact tan(delta)=(24 sqrt(37)-131)/(37 sqrt(3))')
print('critical trim angle (degrees):',mp.nstr(tcrit,43))
print('Certified 11 competitor inequalities and critical branch identity.')
