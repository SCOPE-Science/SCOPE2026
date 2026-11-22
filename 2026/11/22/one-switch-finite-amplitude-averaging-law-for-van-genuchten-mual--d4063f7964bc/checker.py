"""Reproducible numerical diagnostics for two-saturation VGM averaging.

Numerical checks supplement, but do not replace, the sign-change proof.
Requires mpmath (https://mpmath.org/).
"""
import mpmath as mp

mp.mp.dps = 55
checks = 0

def ensure(b, tag):
    global checks
    checks += 1
    if not b:
        raise AssertionError(tag)

def conductivity(x, m, r):
    if x == 0:
        return mp.mpf(0)
    if x == 1:
        return mp.mpf(1)
    z = mp.power(x, 1/m)
    h = -mp.expm1(m*mp.log1p(-z))
    return mp.power(x, r-2/m)*h*h

def gap(s, h, m, r):
    return (conductivity(s-h,m,r)+conductivity(s+h,m,r))/2-conductivity(s,m,r)

# Fixed-parameter controls and high-precision benchmark.
m = mp.mpf('0.5'); r=mp.mpf('0.5')
h=mp.mpf('0.1')
left=gap(h,h,m,r); right=gap(1-h,h,m,r)
ensure(left<0 and right>0,'small contrast endpoints')
root=mp.findroot(lambda s:gap(s,h,m,r),(.29,.36))
ensure(abs(gap(root,h,m,r))<mp.mpf('1e-45'),'root residual')
ensure(abs(root-mp.mpf('0.320940259474397514314519456665'))<mp.mpf('1e-28'),'benchmark root')
ensure(gap(root-mp.mpf('.001'),h,m,r)<0<gap(root+mp.mpf('.001'),h,m,r),'switch direction')
h=mp.mpf('.4')
ensure(gap(h,h,m,r)>0 and gap(1-h,h,m,r)>0,'large contrast endpoints')
for j in range(101):
    s=h+(1-2*h)*j/100
    ensure(gap(s,h,m,r)>0,'large contrast all-positive grid')

# Broad deterministic grid, interior means and contrasts.
# Grid sampling is illustrative only; uniqueness is analytically proved.
for m0 in ('.16','.3','.5','.75','.9'):
  for r0 in ('.05','.2','.5','.85','.99','1','1.2'):
    m=mp.mpf(m0); r=mp.mpf(r0)
    for h0 in ('.02','.07','.14','.27','.4','.49'):
        h=mp.mpf(h0)
        vals=[gap(h+(1-2*h)*j/80,h,m,r) for j in range(81)]
        if r>=1:
            ensure(all(x>0 for x in vals),'convex regime')
        else:
            positive_seen=False
            for v in vals:
                if v>0:positive_seen=True
                if positive_seen:ensure(v>mp.mpf('-1e-40'),'forbidden positive-negative switch')
            if vals[0]>0:ensure(all(v>0 for v in vals),'positive left')
            if vals[-1]<0:ensure(all(v<0 for v in vals),'negative right')

# Evaluate the analytic power-series derivative sign at two dry/wet saturations.
for m0 in ('.2','.5','.8'):
  for r0 in ('.15','.5','.85','1','1.2'):
    m=mp.mpf(m0); r=mp.mpf(r0)
    def coeff(k):
        return (-1)**k * mp.binomial(m,k+1) # all k >=0 strictly positive
    def bracket(s,N=32):
        d=[]
        for j in range(N):
            d.append(sum(coeff(k)*coeff(j-k) for k in range(j+1)))
        return sum(d[j]*(r+j/m)*(r+j/m-1)*mp.power(s,j/m) for j in range(N))
    b=bracket(mp.mpf('.05'))
    if r<1: ensure(b<0,'dry concavity')
    else: ensure(b>0,'dry convexity')
    ensure(bracket(mp.mpf('.94'))>0,'wet convexity')

print('diagnostic assertions passed:',checks)
print('benchmark crossover:',mp.nstr(root,38))
print('for m=1/2, r=1/2, h=1/10: left/right',
      mp.nstr(left,30),mp.nstr(right,30))
