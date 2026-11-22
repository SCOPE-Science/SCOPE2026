"""Standalone finite tests of rotation ordinal gap entropy and continued-fraction cluster inequalities.
Only verifies finite examples; the infinite theorem is analytic.
Run: python check.py (requires mpmath).
"""
from mpmath import mp
from math import log, floor
mp.dps = 85


def cf_alpha(digits):
    # Infinite irrational tail sqrt(2); all digits listed are the true initial digits.
    tail = mp.sqrt(2)
    for a in reversed(digits):
        tail = a + 1 / tail
    return 1 / tail


def conv(digits):
    p0,p1,q0,q1=0,1,1,0
    ans=[]
    for a in [0]+digits:
        p=a*p1+p0; q=a*q1+q0
        ans.append((p,q));p0,p1,q0,q1=p1,p,q1,q
    return ans


def gap_data(alpha,n):
    v=sorted(mp.frac(j*alpha) for j in range(n))
    gaps=[v[i+1]-v[i] for i in range(n-1)]+[1+v[0]-v[-1]]
    assert abs(mp.fsum(gaps)-1)<mp.mpf('1e-60')
    return gaps


def h(gaps):return float(-mp.fsum(g*mp.log(g) for g in gaps if g>0))

def hb(x):
    x=float(x)
    return -x*log(x)-(1-x)*log(1-x) if 0<x<1 else 0

# Check ordinal gap correspondence directly by sampling inside every gap for small orders.
alpha=cf_alpha([2,1,3,4])
pattern_checks=0
for n in range(2,13):
    cuts=sorted(mp.frac(-j*alpha) for j in range(n))
    pats=[]
    for i in range(n):
        lo=cuts[i];hi=cuts[(i+1)%n]+(1 if i==n-1 else 0)
        x=mp.frac((lo+hi)/2)
        orb=[mp.frac(x+j*alpha) for j in range(n)]
        pats.append(tuple(sorted(range(n),key=lambda j:orb[j])))
    assert len(set(pats))==n
    pattern_checks+=n
print('Distinct ordinal-gap patterns:',pattern_checks)

cases=[([2,1,1,1,1,1,1],6),([1,2,100],3),([1,2,1000],3),([1,2,10000],3),([2,5,73],3)]
count=0
for digits,_ in cases:
    alpha=cf_alpha(digits)
    cs=conv(digits)
    p,q=cs[-2]; P,Q=cs[-1]; a=digits[-1]
    assert a>=16 or digits[0]==2
    if a>=16:
        b=max(2,floor(a/log(a)))
        N=b*q
        gaps=gap_data(alpha,N)
        ent=h(gaps)
        delta=log(N)-ent
        d=abs(q*alpha-p)
        eps=float(q*(b-1)*d)
        bound=log(b)-hb(eps)-eps*log(b-1)
        assert eps<=1/log(a)+1e-15
        assert delta+1e-11 >= bound
        assert max(gaps)<mp.mpf(3)/q
        assert N < Q
        # Every short gap is the convergent return and the remaining q are between clusters.
        short=sum(1 for g in gaps if abs(g-d)<mp.mpf('1e-50'))
        assert short==q*(b-1),(digits,short,q*(b-1))
        assert delta<=log(3*Q/q)+1e-12
        count+=1
        print('a=',a,'q=',q,'b=',b,'N=',N,'defect=',round(delta,6),'cluster_lower=',round(bound,6),'short_gaps=',short)
# Bounded-type alpha: n gaps, finite entropy bound for diverse n.
alpha=(mp.sqrt(5)-1)/2
for N in range(2,701):
    assert log(N)-h(gap_data(alpha,N))<=log(6)+1e-11
    count+=1
print('Finite entropy bounds checked:',count, '; all passed')
