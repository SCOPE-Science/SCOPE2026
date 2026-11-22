#!/usr/bin/env python3
"""Exact rational checks for sharp BV box-average hat approximation bounds.

The finite checks support, but do not replace, the universal jump-decomposition proof.
Only Python standard-library modules are required.
"""
from fractions import Fraction as F
from random import Random


def c1(a):
    return max(F(1,2), F(1)-F(3,4)/a)


def cinf(a):
    if a <= F(2,3):
        return F(1)-a/2
    return F(1,2)+(F(2)-a)**2/(16*a)


def w(k,t,a):
    v=(F(k)+a/2-t)/a
    return min(F(1),max(F(0),v))


def linear_interp(x,jumps,a):
    k=x.numerator//x.denominator
    u=x-F(k)
    return sum(c*((F(1)-u)*w(k,t,a)+u*w(k+1,t,a)) for t,c in jumps)


def exact_error(jumps,a):
    xs=sorted({F(k) for k in range(-6,7)} | {t for t,c in jumps})
    if not all(F(-3) <= t <= F(3) for t,c in jumps):
        raise ValueError('finite test range')
    integral=F(0); sup=F(0)
    for x,y in zip(xs[:-1],xs[1:]):
        mid=(x+y)/2
        fv=sum(c for t,c in jumps if t <= mid)
        e0=fv-linear_interp(x,jumps,a)
        e1=fv-linear_interp(y,jumps,a)
        sup=max(sup,abs(e0),abs(e1))
        if e0*e1 >= 0:
            integral+=(y-x)*(abs(e0)+abs(e1))/2
        else:
            integral+=(y-x)*(e0*e0+e1*e1)/(2*(abs(e0)+abs(e1)))
    return integral,sup


def e1_jump_formula(t,a):
    W=max(F(0),F(1,2)-t/a)
    Z=min(F(1),F(1,2)+(F(1)-t)/a)
    return (-2*W*t*t+4*W*t+2*Z*t*t-2*Z-2*t+3)/2


def run():
    r=Random(170241)
    samples=0
    for d in range(1,33):
        for numerator in range(1,2*d+1):
            a=F(numerator,d)
            assert 0<a<=2
            ts={F(0),F(1,2),F(1),a/2,min(a/2,F(1,2))}
            tstar=(F(2)-a)/4
            if 0<=tstar<=F(1,2):ts.add(tstar)
            if a>=1:ts.add(F(1)-a/2)
            ts|={F(j,64) for j in range(33)}
            for t in ts:
                if not F(0)<=t<=F(1,2):continue
                ee,ss=exact_error([(t,F(1))],a)
                assert ee == e1_jump_formula(t,a), ('step L1 identity',a,t,ee)
                assert ee <= c1(a), ('L1 sharp bound',a,t,ee,c1(a))
                assert ss <= cinf(a), ('Linf sharp bound',a,t,ss,cinf(a))
                samples+=1
            # Attaining phases for both norms, including transitions.
            e1_t=F(0) if a<=F(3,2) else F(1,2)
            ee,_=exact_error([(e1_t,F(1))],a)
            assert ee==c1(a),('L1 witness',a,e1_t,ee,c1(a))
            einf_t = a/2 if a<=F(2,3) else (F(2)-a)/4
            _,ss=exact_error([(einf_t,F(1))],a)
            assert ss==cinf(a),('Linf witness',a,einf_t,ss,cinf(a))
    print('EXACT_PHASE_AND_WITNESS_CHECKS_PASS',samples)
    assert c1(F(3,2))==F(1,2) and cinf(F(3,2))==F(49,96)
    print('UNIQUE_L1_PRESERVING_LINFINITY_OPTIMUM_PASS alpha=3/2 c1=1/2 cinf=49/96')
    for k in range(2500):
        a=F(r.randrange(1,65),32)
        n=r.randrange(1,9)
        ts=r.sample([F(v,32) for v in range(-40,41)], n)
        jumps=sorted((t,F(r.randrange(-9,10),r.randrange(1,10))) for t in ts)
        tv=sum(abs(c) for t,c in jumps)
        ee,ss=exact_error(jumps,a)
        assert ee<=tv*c1(a),('random L1',a,jumps,ee,tv*c1(a))
        assert ss<=tv*cinf(a),('random Linf',a,jumps,ss,tv*cinf(a))
        node_tv=sum(abs(linear_interp(F(j+1),jumps,a)-linear_interp(F(j),jumps,a)) for j in range(-6,6))
        assert node_tv<=tv,('variation diminishing',a,jumps,node_tv,tv)
    print('EXACT_SIGNED_MULTI_JUMP_AND_TV_DIMINISHING_CHECKS_PASS 2500')
    print('ALL_BV_BOX_AVERAGING_CHECKS_PASS')


if __name__=='__main__':
    run()
