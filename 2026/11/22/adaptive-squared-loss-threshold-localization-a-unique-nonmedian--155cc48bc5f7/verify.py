"""Numerical checks for two noisy threshold queries under squared loss.

All finite checks supplement the analytic proof in RESULT.md.
Standard library only; Python 3.10+.
"""
import math
from fractions import Fraction


def polynomial(e, d):
    return (8*d**3*e**3 + 8*d**3*e**2 - 12*d**2*e**3
            +4*d*e**3 - 2*d*e**2 + 4*d*e - 4*d - e**2 + e)


def opt_d(e):
    assert 0 < e < 1
    left, right = 0.0, 0.5
    for _ in range(90):
        mid = (left+right)/2
        if polynomial(e, mid) > 0:
            left = mid
        else:
            right = mid
    return (left+right)/2


def moments(pieces, threshold, e):
    """Posterior prior pieces (a,b,density), then noisy sign query."""
    probs=[]; nums=[]
    for y in [-1, 1]:
        total=moment=0.0
        for a,b,w in pieces:
            for c,d in zip(sorted({a,b,max(a,min(b,threshold))})[:-1],
                           sorted({a,b,max(a,min(b,threshold))})[1:]):
                if d==c: continue
                sign=1 if (c+d)/2>threshold else -1
                factor=(1+y*e*sign)/2
                total+=w*factor*(d-c)
                moment+=w*factor*(d*d-c*c)/2
        probs.append(total);nums.append(moment)
    prior_mean=sum((b*b-a*a)*w/2 for a,b,w in pieces)
    return sum(v*v/p for p,v in zip(probs,nums) if p>0)-prior_mean*prior_mean


def after_plus(e):
    return [(0.0,.5,1-e),(.5,1.0,1+e)]


def Iplus_formula(e,d):
    q=(1+e)*(.5-d)
    cov=(1+e)*(.5-d)*(.5-.25*e-(.5-d)/2)
    # cov = E[X 1_{X>u}] - E[X]P(X>u)
    return 4*e*e*cov*cov/(1-e*e*(2*q-1)**2)


def adapt_info(e,d):
    return e*e/16 + Iplus_formula(e,d)


def parallel_info(t,u,e):
    cuts=sorted({0.0,float(t),float(u),1.0})
    response_info=0.
    for y in [-1,1]:
        for z in [-1,1]:
            prob=num=0.
            for a,b in zip(cuts[:-1],cuts[1:]):
                m=(a+b)/2
                s1=1 if m>t else -1
                s2=1 if m>u else -1
                factor=(1+y*e*s1)*(1+z*e*s2)/4
                prob+=factor*(b-a)
                num+=factor*(b*b-a*a)/2
            if prob>0: response_info+=num*num/prob
    return response_info-.25


def run_checks():
    count=0
    for en, dn in [(Fraction(1,3),Fraction(1,7)),(Fraction(2,5),Fraction(1,9)),
                   (Fraction(7,10),Fraction(1,6))]:
        e=float(en); d=float(dn)
        assert abs(moments(after_plus(e),.5+d,e)-Iplus_formula(e,d))<1e-15
        count+=1
    for e in [.005,.02,.1,.2,.4,.6,.8,.95,.999]:
        d=opt_d(e)
        assert abs(polynomial(e,d))<5e-12
        assert 0<d<e/(2*(1+e))
        assert abs(adapt_info(e,d)-parallel_info(.5,.5,e))>1e-14
        for i in range(301):
            u=i/300
            v=moments(after_plus(e),u,e)
            assert v<=Iplus_formula(e,d)+2e-13, (e,u,v,d)
            count+=1
        for i in range(100):
            dd=(i+.25)/200
            assert Iplus_formula(e,dd)>moments(after_plus(e),.5-dd,e)
            count+=1
    for e in [.02,.1,.2,.4,.7,.95]:
        for j in range(21):
            t=(j+.5)/44
            u=1-t
            theory=2*e*e*t*t*(1-t)**2/(1-e*e+4*e*e*t)
            assert abs(theory-parallel_info(t,u,e))<2e-14
            count+=1
    for e in [0.001, 0.002, 0.004, 0.008, 0.016]:
        d=opt_d(e)
        assert abs(d-(e/4-e**3/8)) < 2*e**4
        first_approx=e*e/8-3*e**4/32+e**5/32
        assert abs(adapt_info(e,d)-first_approx)<e**6
        count+=1
    print(f"PASS: {count} checks: posterior moments, second-stage global grid, mirror dominance,")
    print("exact parallel mirrored risk, polynomial root, posterior-median gap and weak-channel series.")
    for e in [0.1,0.5,0.9]:
        d=opt_d(e)
        print(f"contrast={e:.1f} optimal halfshift={d:.12f} posterior median halfshift={e/(2*(1+e)):.12f}")

if __name__=='__main__':run_checks()
