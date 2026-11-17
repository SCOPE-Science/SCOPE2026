"""Numerical diagnostics for a continued-fraction ordinal-entropy law.

Finite computations illustrate the statements; the infinite assertions rely on
non-asymptotic entropy bounds proved in RESULT.md.
Run: python verify.py
Requires: mpmath
"""
import math
from mpmath import mp

mp.dps = 90

def cf_irrational(a, tail):
    x = tail
    for v in reversed(a[1:]):
        x = 1 / (mp.mpf(v) + x)
    return x + a[0]

def denominators(terms):
    prevprev, prev = 1, 0
    out = []
    for a in terms:
        q = a * prev + prevprev
        out.append(q)
        prevprev, prev = prev, q
    return out

def phase_gaps(alpha, n):
    xs = sorted(mp.frac(j * alpha) for j in range(n))
    return [xs[j+1]-xs[j] for j in range(n-1)] + [1+xs[0]-xs[-1]]

def entropy(gaps):
    return -sum(x * mp.log(x) for x in gaps)

def ordinal_signature(alpha, x, n):
    points = [mp.frac(x+j*alpha) for j in range(n)]
    return tuple(sorted(range(n), key=lambda j: points[j]))

def check_distinct(alpha):
    for n in range(2, 12):
        cuts = sorted(mp.frac(-j*alpha) for j in range(n))
        labels=set()
        for j in range(n):
            x = (cuts[j]+cuts[j+1])/2 if j<n-1 else mp.frac((cuts[-1]+cuts[0]+1)/2)
            labels.add(ordinal_signature(alpha, x, n))
        assert len(labels)==n, (n,len(labels))
    return 10

def trial(name, alpha, q, Q, n):
    gaps=phase_gaps(alpha,n)
    H=entropy(gaps)
    assert abs(sum(gaps)-1)<mp.mpf('1e-80')
    if n>=q:
        assert H >= mp.log(mp.mpf(q)/3) - mp.mpf('1e-65')
        assert max(gaps)<=mp.mpf(3)/q+mp.mpf('1e-65')
    if n<=Q//4:
        eps=mp.mpf(2)*n/Q
        h=lambda x: -x*mp.log(x)-(1-x)*mp.log(1-x)
        upper=mp.log(q)+h(eps)+eps*mp.log(n)
        assert H<=upper+mp.mpf('1e-65'), (name,n,H,upper)
    return float(H),float(H/mp.log(n))

golden=(mp.sqrt(5)-1)/2
custom=cf_irrational([0,2,2,2,2000], golden)
# q_3=12 and q_4=24005 for the custom continued fraction.
assert denominators([0,2,2,2,2000])==[1,2,5,12,24005]
counts=check_distinct(golden)+check_distinct(custom)
for n in (16,64,125,512,1024,2048):
    H, ratio=trial('custom',custom,12,24005,n)
    print('custom',n,round(H,8),round(ratio,7))
for n in (15,55,144,610):
    H=float(entropy(phase_gaps(golden,n)))
    ratio=float(H/mp.log(n))
    print('golden',n,round(H,8),round(ratio,7))
print('VERIFY_OK: ordinal cells',counts,'custom fraction denominator 24005, finite entropy bounds and normalized ratios')
