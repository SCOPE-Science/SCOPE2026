"""Exact interval certificate for the first nonoptimal greedy latitude ordering.

Runs without third-party modules. Every interval is an outward-rounded rational
multiple of 10**(-25); trigonometric enclosures use Machin's formula and Taylor
remainder bounds. No floating-point operations enter the certificate.
"""
from fractions import Fraction as F
from math import factorial
from functools import lru_cache

Q = 10**25


def ceil_div(a, b):
    return -((-a)//b)


class I:
    __slots__ = ('lo', 'hi')
    def __init__(self, lo, hi=None):
        self.lo = lo
        self.hi = lo if hi is None else hi
        assert self.lo <= self.hi
    @staticmethod
    def frac(q):
        return I((q.numerator*Q)//q.denominator,
                 ceil_div(q.numerator*Q, q.denominator))
    def __add__(a,b): return I(a.lo+b.lo, a.hi+b.hi)
    def __sub__(a,b): return I(a.lo-b.hi, a.hi-b.lo)
    def __mul__(a,b):
        vals=[u*v for u in (a.lo,a.hi) for v in (b.lo,b.hi)]
        return I(min(vals)//Q,ceil_div(max(vals),Q))
    def __truediv__(a,b):
        assert b.lo*b.hi>0
        vals=[(u*Q,v) for u in (a.lo,a.hi) for v in (b.lo,b.hi)]
        return I(min(x//y for x,y in vals),max(ceil_div(x,y) for x,y in vals))
    def __pow__(a,n):
        assert isinstance(n,int) and n>=0
        v=I(Q)
        for _ in range(n):v=v*a
        return v
    def abs(a):
        if a.lo>=0:return a
        if a.hi<=0:return I(-a.hi,-a.lo)
        return I(0,max(-a.lo,a.hi))


def atan_interval(inv, terms):
    # Alternating arctan(x) for 0<x<=1, error bounded by next term.
    s=sum((F(1 if k%2==0 else -1,(2*k+1)*inv**(2*k+1))
          for k in range(terms)), F(0))
    e=F(1,(2*terms+1)*inv**(2*terms+1))
    return (s,s+e) if terms%2==0 else (s-e,s)


a1,b1=atan_interval(5,44)
a2,b2=atan_interval(239,14)
PI_LO,PI_HI=16*a1-4*b2,16*b1-4*a2
assert F(3)<PI_LO<PI_HI<F(22,7)


def trig_enclosure(L,t,sine):
    a=F(2*t+1,2*L-1)
    left,right=a*PI_LO,a*PI_HI
    z=(left+right)/2
    half=(right-left)/2
    # Taylor polynomial, with Lagrange-remainder error bounded by |z|^(degree+1)/(degree+1)!
    if sine:
        val=sum((F((-1)**j, factorial(2*j+1))*z**(2*j+1)
                 for j in range(32)),F(0))
        err=F(22,7)**65/factorial(65) + half
    else:
        val=sum((F((-1)**j, factorial(2*j))*z**(2*j)
                 for j in range(32)),F(0))
        err=F(22,7)**64/factorial(64) + half
    return I(((val-err).numerator*Q)//(val-err).denominator,
             ceil_div((val+err).numerator*Q,(val+err).denominator))


GREEDY={
  3:(1,0),4:(1,2,0),5:(2,1,3,0),6:(2,3,1,4,0),
  7:(3,2,4,1,5,0),8:(3,4,2,5,1,6,0),
  9:(4,3,5,2,6,1,7,0),10:(4,5,3,6,2,7,1,8,0),
  11:(5,4,7,3,6,2,8,1,9,0),
  12:(5,7,4,6,2,9,3,8,1,10,0),
}
BETTER12=(4,5,6,8,3,7,2,9,1,10,0)


def evaluate(L):
    n=L-1
    x=[trig_enclosure(L,t,False) for t in range(n)]
    y=[trig_enclosure(L,t,True) for t in range(n)]
    assert all(a.lo>0 for a in y)

    # Cache all three-node interpolation ratios and sine-power weights.
    # This avoids repeating interval divisions in each subset certificate.
    dif=[[x[k]-x[j] for j in range(n)] for k in range(n)]
    rat=[[[None if j==s or j==k or s==k else dif[k][j]/dif[s][j]
           for j in range(n)] for s in range(n)] for k in range(n)]
    powers=[[[None if k==s else (y[k]/y[s])**m for m in range(L)]
             for s in range(n)] for k in range(n)]

    @lru_cache(None)
    def amp(mask):
        selected=[j for j in range(n) if mask>>j&1]
        remaining=[j for j in range(n) if not(mask>>j&1)]
        if not remaining:return I(0)
        m=L-len(selected)
        results=[]
        for k in remaining:
            summ=I(0)
            for s in selected:
                term=powers[k][s][m]
                for j in selected:
                    if j!=s:
                        term=term*rat[k][s][j]
                summ=summ+term.abs()
            results.append(summ)
        return I(max(a.lo for a in results),max(a.hi for a in results))

    def masks(path):
        out=[];mask=0
        assert sorted(path)==list(range(n))
        for s in path:
            mask |= 1<<s
            out.append(mask)
        return out

    def attain(path):
        ms=masks(path)
        vals=[amp(k) for k in ms]
        idx=max(range(n),key=lambda j:vals[j].hi)
        ref=vals[idx]
        # Path's worst cost is the reference mask, strictly bigger than all other values.
        assert all(v.hi < ref.lo for j,v in enumerate(vals) if j!=idx)
        return ms[idx],ref

    greedy=GREEDY[L]
    # Verify the precise deterministic greedy selection rule, including its
    # first choice (highest sin co-latitude), with strict comparisons.
    assert all(y[greedy[0]].lo > y[j].hi for j in range(n) if j!=greedy[0])
    mask=1<<greedy[0]
    for chosen in greedy[1:]:
        winning=amp(mask|(1<<chosen))
        for other in range(n):
            if not(mask>>other&1) and other!=chosen:
                assert winning.hi < amp(mask|(1<<other)).lo, ('greedy tie',L,chosen,other)
        mask|=1<<chosen
    gm,gv=attain(greedy)
    opt_path=BETTER12 if L==12 else greedy
    om,ov=attain(opt_path)

    # Exact cutset proof: remove all masks with amplitude >= proposed optimum.
    # For every other mask comparison to this optimum is certified strict.
    allowed={0}
    count_low=count_high=0
    for mask in range(1,1<<n):
        a=amp(mask)
        if mask==om:
            count_high+=1
            continue
        if a.hi<ov.lo:
            count_low+=1
        else:
            assert a.lo>ov.hi, ('unresolved interval comparison',L,mask)
            count_high+=1
            continue
        if any((mask^(1<<j)) in allowed for j in range(n) if mask>>j&1):
            allowed.add(mask)
    assert (1<<n)-1 not in allowed, ('counterpath',L)
    if L<12:
        assert gm==om and gm==masks(greedy)[[amp(k).hi for k in masks(greedy)].index(max(amp(k).hi for k in masks(greedy)))]
    else:
        assert ov.hi < gv.lo
    fmt=lambda v: ('%.12f'% (v.lo/Q),'%.12f'%(v.hi/Q))
    print('L',L,'greedy',greedy,'Gmask',gm,'G',fmt(gv),
          'opt',opt_path,'Omask',om,'O',fmt(ov),
          'below',count_low,'at-or-above',count_high,
          'good-reachable',len(allowed),flush=True)

if __name__=='__main__':
    for L in range(3,13): evaluate(L)
    print('CERTIFIED: first greedy failure occurs at band-limit 12')
