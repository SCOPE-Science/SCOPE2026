"""Reproduce exact degree-two normal-form identities and finite orbit diagnostics.
Standard-library Python 3 only; numerical samples do not prove infinite-time claims.
"""
from fractions import Fraction as F
from math import exp, log, log1p, expm1

ZERO = {}
def P(d):
    return {k: F(v) for k, v in d.items() if v}
def add(a, b):
    out = dict(a)
    for k, v in b.items():out[k] = out.get(k,F(0)) + v
    return P(out)
def sc(a,c):return P({k:c*v for k,v in a.items()})
def mul(a,b):
    out = {}
    for (i,j),x in a.items():
        for (k,l),y in b.items():
            if i+j+k+l>2:continue
            m=(i+k,j+l);out[m]=out.get(m,F(0))+x*y
    return P(out)

a=P({(1,0):1});b=P({(0,1):1})
def lin(z):
    u,v=z
    return (add(u,sc(v,F(-1,2))),add(sc(u,F(1,2)),sc(v,-1)))
def quad(z):
    u,v=z
    return (sc(mul(v,v),F(-1,8)),sc(mul(u,u),F(1,8)))

def test_exact():
    assert lin(lin((a,b)))==(sc(a,F(3,4)),sc(b,F(3,4)))
    computed=tuple(map(add,lin(quad((a,b))),quad(lin((a,b)))))
    target=(add(add(sc(mul(a,a),F(-3,32)),sc(mul(a,b),F(1,8))),sc(mul(b,b),F(-1,4))),
            add(sc(mul(a,b),F(-1,8)),sc(mul(b,b),F(-1,32))))
    assert computed == target
    B=tuple(sc(t,F(-16,3)) for t in computed)
    expected=(add(add(sc(mul(a,a),F(1,2)),sc(mul(a,b),F(-2,3))),sc(mul(b,b),F(4,3))),
              add(sc(mul(a,b),F(2,3)),sc(mul(b,b),F(1,6))))
    assert B==expected
    assert F(-1,8)/(F(1,2)*(F(1,2)-1))==F(1,2)
    return 4

def kap(s):
    if s>60:return s-log(2)+log1p(exp(-s))
    return log1p(expm1(s)/2)
def T(u,v):return abs(u-kap(v)), abs(v-kap(u))
def odds(x):return log(x/(1-x))

def test_orbits():
    pairs=[(.81,.66),(.50001,.500004),(.80001,.8),(.9,.50000001),
           (.500001,.50000001),(.999,.7),(.6,.59999999),(.5,.97)]
    examples=0
    for x,y in pairs:
        u,v=odds(max(x,y)),odds(min(x,y))
        entry=None
        series=[]
        for n in range(140):
            assert 0<=v<u
            if v<=kap(u) and entry is None:entry=n
            if entry is not None:assert v<=kap(u)+1e-14
            series.append((u,v))
            u,v=T(u,v)
        assert entry is not None
        for n in (entry+58, entry+70, entry+82):
            assert n+2<140
            u,v=series[n];u2,v2=series[n+2]
            assert abs(u2/u-F(3,4))<1e-4,(x,y,n,u2/u)
        examples+=1
    u=odds(.83)
    for n in range(70):
        nu=u-kap(u)
        if n==48:assert abs(nu/u-.5)<1e-6
        u=nu
    return examples

if __name__=='__main__':
    exact=test_exact()
    trajectories=test_orbits()
    print(f'VERIFY_OK exact_polynomial_identities={exact} offdiagonal_trajectories={trajectories} sampled_two_step_ratios=24 diagonal_check=1')
