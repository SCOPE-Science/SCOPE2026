"""Numerical cross-check of the closed-form paired Gaussian ambiguity design law.

Uses only Python's standard library; the analytic proof is in RESULT.md.
"""
import math

PI = math.pi


def analytic_floor(s1, s2, radius, w1=1.0, w2=1.0):
    if not (s1 > 1 and s2 > 1 and radius > 0 and w1 > 0 and w2 > 0):
        raise ValueError('Outside theorem assumptions')
    c1 = PI * radius**2 * (s1 + 1/s1) / 4
    c2 = PI * radius**2 * (s2 + 1/s2) / 4
    d1 = PI * radius**2 * (s1 - 1/s1) / 4
    d2 = PI * radius**2 * (s2 - 1/s2) / 4
    raw = (math.log(w2*d2/(w1*d1)) + c1 - c2)/(d1+d2)
    x = min(1., max(-1., raw))
    return x, w1*math.exp(-c1+d1*x) + w2*math.exp(-c2-d2*x)


def floor_by_scan(s1, s2, radius, separation, w1=1., w2=1.):
    def val(phi):
        z1 = s1*math.cos(phi)**2 + math.sin(phi)**2/s1
        z2 = s2*math.cos(phi-separation)**2 + math.sin(phi-separation)**2/s2
        return w1*math.exp(-PI*radius**2*z1/2) + w2*math.exp(-PI*radius**2*z2/2)
    count=3000
    jj=min(range(count), key=lambda j:val(PI*j/count))
    left=(jj-1)*PI/count
    right=(jj+1)*PI/count
    # Golden-section refinement near the smallest sampled angle.
    ratio=(math.sqrt(5)-1)/2
    c=right-ratio*(right-left)
    d=left+ratio*(right-left)
    for _ in range(92):
        if val(c) < val(d):
            right=d;d=c;c=right-ratio*(right-left)
        else:
            left=c;c=d;d=left+ratio*(right-left)
    return val((left+right)/2)


def main():
    n=0
    for s1,s2,w1,w2 in [(4.,2.,1.,1.),(5.,1.6,1.,1.),(4.,2.,2.,1.),(1.7,4.,1.,3.)]:
        for radius in [.2,.5,1.3,2.]:
            x, opt=analytic_floor(s1,s2,radius,w1,w2)
            sample=floor_by_scan(s1,s2,radius,PI/2,w1,w2)
            assert abs(sample-opt) <= 2e-9*max(1.,opt),(s1,s2,radius,opt,sample)
            for delta in [.1,.4,1.,1.4]:
                value=floor_by_scan(s1,s2,radius,delta,w1,w2)
                assert value < opt-1e-12*max(1.,opt),(s1,s2,radius,delta,value,opt)
            n+=1
    s1=4.;s2=2.
    eta1=s1-1/s1;eta2=s2-1/s2
    rcrit2=2*math.log(eta1/eta2)/(PI*(s1-1/s2))
    xlim=(s1+1/s1-s2-1/s2)/(eta1+eta2)
    assert 0<xlim<1
    for factor,case in [(0.5,-1),(1.,-1),(1.4,0)]:
        r=math.sqrt(rcrit2)*factor
        x,_=analytic_floor(s1,s2,r)
        if factor<=1: assert abs(x+1)<1e-12
        else: assert -1<x<xlim
    print('GAUSSIAN_PAIR_DESIGN_PASS cases=%d nonorthogonal_checks=%d threshold_squared=%.12g' % (n,4*n,rcrit2))

if __name__=='__main__':
    main()
