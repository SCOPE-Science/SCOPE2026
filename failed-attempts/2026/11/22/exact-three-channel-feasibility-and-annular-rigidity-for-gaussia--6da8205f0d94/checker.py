"""Standalone numerical diagnostics for the sharp three-mode radial Gaussian localization body.
All integrations use exact exponential antiderivatives on piecewise-constant masks;
these diagnostics do not replace the universal analytic proof.
"""
import math
import random
import json

INF = float('inf')

def tail(k, x):
    if math.isinf(x):
        return 0.0
    e = math.exp(-x)
    return e * (1 if k == 0 else (x + 1 if k == 1 else (x*x + 2*x + 2)/2))

def moment(k, a, b):
    return tail(k,a) - tail(k,b)

def f(p, u):
    v = u-p
    return u*(1-math.log(u)) - (v*(1-math.log(v)) if v>0 else 0.0)

def params(p,q):
    lo,hi=p,1.0
    for _ in range(90):
        u=(lo+hi)*0.5
        if f(p,u)>q:lo=u
        else:hi=u
    u=(lo+hi)*0.5
    v=u-p
    return -math.log(u), (-math.log(v) if v>0 else INF)

def bounds(p,q):
    if p <= 0: return 0.0,0.0,(0.0,0.0),(0.0,0.0)
    if p >= 1: return 1.0,1.0,(0.0,INF),(0.0,INF)
    a,b=params(p,q)
    c,d=params(1-p,1-q)
    return moment(2,a,b), 1-moment(2,c,d), (a,b),(c,d)

def segment_integral(a,b,x,y):
    return (moment(2,x,y)*2-(a+b)*moment(1,x,y)+a*b*moment(0,x,y))/2

def test_mask(breaks, values):
    def hv(x):
        for j in range(len(values)):
            if breaks[j] <= x < breaks[j+1]:return values[j]
        return 0.0
    p=sum(values[j]*moment(0,breaks[j],breaks[j+1]) for j in range(len(values)))
    q=sum(values[j]*moment(1,breaks[j],breaks[j+1]) for j in range(len(values)))
    r=sum(values[j]*moment(2,breaks[j],breaks[j+1]) for j in range(len(values)))
    qlo=p+(1-p)*math.log1p(-p)
    qhi=p*(1-math.log(p))
    assert qlo-2e-11 <= q <= qhi+2e-11, (p,q,qlo,qhi)
    lo,hi,(a,b),(c,d)=bounds(p,q)
    assert lo-2e-11 <= r <= hi+2e-11, (p,q,r,lo,hi)
    gap1=gap2=0.0
    # At the sharp (p,q) boundary, one endpoint is infinite and the
    # quadratic gap polynomial is not a finite certificate.  The exact
    # stability identity is asserted only in the interior of the moment lens.
    if qlo+1e-10 < q < qhi-1e-10:
        xs=sorted(set(breaks + [a,b,c,d,INF]))
        for x,y in zip(xs[:-1],xs[1:]):
            if x==y:continue
            mid=x+1 if math.isinf(y) else (x+y)*.5
            h=hv(mid)
            hmin=1.0 if a<mid<b else 0.0
            hmax=0.0 if c<mid<d else 1.0
            gap1+=abs(h-hmin)*abs(segment_integral(a,b,x,y))
            gap2+=abs(h-hmax)*abs(segment_integral(c,d,x,y))
        assert abs((r-lo)-gap1)<3e-10,(p,q,r,lo,gap1)
        assert abs((hi-r)-gap2)<3e-10,(p,q,r,hi,gap2)
        return {'p':p,'q':q,'r':r,'min':lo,'max':hi,'lower_gap_error':abs((r-lo)-gap1),'upper_gap_error':abs((hi-r)-gap2),'interior':True}
    assert abs(hi-lo)<3e-10, (p,q,r,lo,hi)
    return {'p':p,'q':q,'r':r,'min':lo,'max':hi,'lower_gap_error':0.,'upper_gap_error':0.,'interior':False}

if __name__=='__main__':
    random.seed(20261120)
    diagnostics=[]
    for j in range(140):
        breaks=[k*0.3 for k in range(81)]
        values=[random.random() for _ in range(80)]
        diagnostics.append(test_mask(breaks,values))
    for a,b in [(0.0,0.8),(0.2,1.7),(0.9,3.5),(2.0,6.0)]:
        breaks=[0.0,a,b,INF] if a>0 else [0.0,b,INF]
        vals=[0.,1.,0.] if a>0 else [1.,0.]
        diagnostics.append(test_mask(breaks,vals))
    for a,b in [(0.4,1.7),(0.6,2.4),(1.0,3.0)]:
        diagnostics.append(test_mask([0.0,a,b,INF],[1.0,0.0,1.0]))
    lo,hi,ab,cd=bounds(0.5,0.5)
    assert abs(lo-0.2911583219888445)<3e-12 and abs(hi-0.7088416780111555)<3e-12
    assert abs(hi+lo-1)<1e-13
    print(json.dumps({'status':'PASS','piecewise_masks_tested':len(diagnostics),'interior_masks_with_both_gap_identities':sum(x['interior'] for x in diagnostics),'max_gap_identity_error':max(max(x['lower_gap_error'],x['upper_gap_error']) for x in diagnostics),'p_half_q_half':{'lower':lo,'upper':hi,'annulus_a':ab[0],'annulus_b':ab[1]},'note':'Finite checks complement, never establish, the universal theorem.'},sort_keys=True,indent=2))
