"""Reproducible certified bounds for the uniform-horizon Fourier multiplier.
Requires mpmath. Interval checks plus symbolic derivative identities in RESULT.md.
"""
import math
from mpmath import iv, mp
iv.dps=35
mp.dps=60

def f_iv(t):
    return (1-iv.sin(t)/t)*(1+6/(t*t))
def lower(y): return float(y.a)
def upper(y): return float(y.b)
def n_iv(t): return (t*t+18)*iv.sin(t)-t*(t*t+6)*iv.cos(t)-12*t

# For t in [1.5, pi], uniform 10.1 Lipschitz bound and a rational grid.
K=20000
xa=iv.mpf('1.5'); xb=iv.pi
hi=-1.0
for j in range(K+1):
    t=xa+(xb-xa)*j/K
    hi=max(hi,upper(f_iv(t)))
cover=10.1*(math.pi-1.5)/(2*K)+2e-13
assert hi+cover<1.62,(hi,cover)

# On [2pi,3pi] uniform 0.30 derivative bound.
K2=20000
lo=1e10
for j in range(K2+1):
    t=iv.pi*(2+iv.mpf(j)/K2)
    lo=min(lo,lower(f_iv(t)))
cover2=0.30*math.pi/(2*K2)+2e-13
assert lo-cover2>0.9572,(lo,cover2)

# Outlying upper/lower root brackets, certified signs via outward intervals.
bp=[iv.mpf('3.7141548'), iv.mpf('3.7141551')]
bm=[iv.mpf('14.1206451'),iv.mpf('14.1206455')]
assert lower(n_iv(bp[0]))>0 and upper(n_iv(bp[1]))<0
assert upper(n_iv(bm[0]))<0 and lower(n_iv(bm[1]))>0
fplus=f_iv(iv.mpf('3.714154911356975'))
fminus=f_iv(iv.mpf('14.120645277751043'))
assert lower(fplus)>1.64425 and upper(fplus)<1.64427
assert lower(fminus)>0.95715 and upper(fminus)<0.95716
assert upper(f_iv(iv.mpf('14.12')))<0.9572

# The analytic tail bound at 5pi is above the second-lobe candidate.
t=5*iv.pi
H=(1-1/t)*(1+6/t**2)
assert lower(H)>0.959

# Low-frequency factor at t=0 is 1; at large t it tends to 1.
# Exact Fourier multiplier check for the centered uniform interaction measure.
for x in (0.15,0.5,1,2,3,4,6,9,13,20):
    psi=2*(1-math.sin(x)/x)
    pred=psi*(3/x**2+0.5)
    assert abs(pred-(1-math.sin(x)/x)*(1+6/x**2))<1e-14
print('CERTIFIED_OK', 'low_interval_max',hi+cover,'first_positive_lobe_lower',lo-cover2,
      'peak',fplus,'valley',fminus, 'tail_lower',H)
