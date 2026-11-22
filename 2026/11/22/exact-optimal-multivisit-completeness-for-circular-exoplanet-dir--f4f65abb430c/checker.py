"""Independent finite numerical diagnostics for the ideal circular-orbit visibility theorem.

Requires scipy; calculations are diagnostics and not a substitute for the proof.
"""
import math
import random
from scipy.integrate import quad

PI = math.pi


def closed_form(n, c):
    assert n >= 3 and 0 < c < 1
    a = math.sin(PI/(2*n))
    if c >= a:
        return 1.0
    u = math.cos(PI/(2*n))
    r = math.sqrt((a-c)*(a+c))
    return 1 - 2*n/PI*(math.atan(r/u)-c*math.atan(r/(c*u)))


def completeness(n, c, gaps):
    assert n >= 3 and len(gaps) == n and min(gaps) >= 0
    assert abs(sum(gaps)-PI) < 1e-10
    # The line-of-sight polar coordinate z is uniform on [0,1].
    def loss(z):
        s = math.sqrt(max(0., 1-z*z))
        ell = PI if s <= c else 2*math.asin(c/s)
        return sum(max(0.,g-ell) for g in gaps)/PI
    points = []
    for g in gaps:
        if 2*math.asin(c) < g < PI:
            s = c/math.sin(g/2)
            if s < 1:
                points.append(math.sqrt(max(0.,1-s*s)))
    return 1-quad(loss,0.,1.,epsabs=5e-11,epsrel=5e-11,points=points,limit=200)[0]


def run():
    checks=0
    rng=random.Random(19037)
    for n in (3,4,5,6,8):
        for c in (.07,.2,.36,.51,.63,.77,.89,.97):
            gaps=[PI/n]*n
            p=closed_form(n,c)
            numeric=completeness(n,c,gaps)
            assert abs(p-numeric)<2e-8, (n,c,p,numeric)
            checks+=1
            for j in range(12):
                samples=[rng.expovariate(1) for _ in range(n)]
                total=sum(samples)
                other=[PI*x/total for x in samples]
                v=completeness(n,c,other)
                assert v<=p+2e-9,(n,c,p,v,other)
                checks+=1
            a=math.sin(PI/(2*n))
            if c<a:
                perturb=0.02/n
                altered=gaps.copy()
                altered[0]+=perturb
                altered[1]-=perturb
                v=completeness(n,c,altered)
                assert v<p-1e-9,(n,c,p,v)
                checks+=1
            elif c>a:
                slack=2*math.asin(c)-PI/n
                eps=min(slack/4, PI/(8*n))
                changed=gaps.copy()
                changed[0]+=eps
                changed[1]-=eps
                assert abs(completeness(n,c,changed)-1)<2e-8
                checks+=1
    for n in (3,4,5,7,10):
        a=math.sin(PI/(2*n)); u=math.cos(PI/(2*n))
        coef=4*n*math.sqrt(2*u)/(3*PI*a*a)
        for delta in (1e-3,2e-4,3e-5):
            tau=u+delta
            if tau>=1:continue
            c=math.sqrt(1-tau*tau)
            ratio=(1-closed_form(n,c))/delta**1.5
            assert abs(ratio/coef-1)<.05,(n,delta,ratio,coef)
            checks+=1
    # A three-visit benchmark: the IWA is 80% of orbit radius.
    assert closed_form(3,.6)==1.0
    assert closed_form(3,.6)>closed_form(3,.45)
    print(f'PASS: {checks+2} numerical and asymptotic diagnostic assertions')


if __name__=='__main__':
    run()
