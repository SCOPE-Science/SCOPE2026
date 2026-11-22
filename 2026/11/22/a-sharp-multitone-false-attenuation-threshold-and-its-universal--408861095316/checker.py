"""Independent elementary checks for the quasiperiodic reach-monitoring theorem.

Python 3, standard library only.  Deterministic tests are supplementary to the proof.
"""
import math
import random

COUNT = 0

def check(test, message):
    global COUNT
    COUNT += 1
    if not test:
        raise AssertionError(message)


def coefficients(E, h, frequencies, amplitudes):
    return [b * math.hypot(math.cos(w*h)-E, math.sin(w*h))
            for w, b in zip(frequencies, amplitudes)]


def density_two(rho, E, c1, c2, intervals=16000):
    # Exact conditional angular fraction integrated by composite Simpson quadrature.
    assert intervals % 2 == 0
    threshold = (E-1)/rho
    def integrand(theta):
        z=(threshold-c1*math.cos(theta))/c2
        if z <= -1: return 1.0
        if z >= 1: return 0.0
        return math.acos(z)/math.pi
    dx=math.pi/intervals
    s=integrand(0)+integrand(math.pi)
    for k in range(1,intervals):
        s+=(4 if k%2 else 2)*integrand(k*dx)
    return s*dx/(3*math.pi)


def main():
    rng = random.Random(1729)
    for _ in range(750):
        E=1.0001+3*rng.random()
        h=20*rng.random()-10
        w=0.1+8*rng.random()
        b=0.01+rng.random()
        theta=rng.random()*2*math.pi
        lhs=b*(math.cos(theta+w*h)-E*math.cos(theta))
        R=b*math.hypot(math.cos(w*h)-E,math.sin(w*h))
        a=math.atan2(-math.sin(w*h),math.cos(w*h)-E)
        # cos(theta-alpha) = cos theta cos alpha + sin theta sin alpha
        # our lhs coefficient of sin theta is -sin(w h)
        rhs=R*math.cos(theta-a)
        check(abs(lhs-rhs)<3e-14*(1+b*E), 'phasor reduction')
        check(R>=b*(E-1)-1e-14, 'amplitude lower bound')

    E=1.1
    h=1.0
    w=[1.0,math.sqrt(2)]
    b=[0.3,0.3]
    c1,c2=coefficients(E,h,w,b)
    S=c1+c2
    critical=(E-1)/S
    check(0<critical<1/sum(b),'admissible threshold')
    check(abs(critical-0.14023482821655095)<2e-14,'printed threshold')
    V2=math.pi
    C=V2/(2*math.pi)**2 * (2*S/critical) /math.sqrt(c1*c2)
    check(abs(C-2.295690859483767)<2e-12,'printed onset coefficient')

    for rho in [0.1,critical,critical*1.001,critical*1.01,critical*1.1,0.25,0.5,1.0]:
        p=density_two(rho,E,c1,c2)
        check(0<=p<=1,'valid occupation density')
        if rho<=critical:
            check(p<1e-12,'no reversal at/below threshold')
        else:
            check(p>0,'positive reversal density above threshold')
    # Near-threshold linear onset, n=2; check quotient converges.
    err=[]
    for delta in [1e-2,1e-3,1e-4]:
        rho=critical+delta
        p=density_two(rho,E,c1,c2)
        ratio=p/delta
        err.append(abs(ratio/C-1))
        check(abs(ratio/C-1)<1.2e-1, 'two-mode onset accuracy')
    check(err[2]<err[1]<err[0],'two-mode convergence')

    # One-mode exact density and universal square-root onset.
    E=1.3
    w=2.3
    b=0.4
    h=1.4
    c=coefficients(E,h,[w],[b])[0]
    critical1=(E-1)/c
    check(0<critical1<1/b,'one-mode positivity interval')
    C1=math.sqrt(2/critical1)/math.pi
    for delta in [1e-3,1e-4,1e-5]:
        p=math.acos((E-1)/((critical1+delta)*c))/math.pi
        check(abs(p/(C1*math.sqrt(delta))-1)<1e-2,'one-mode onset')

    # Perfect time alignment suppresses false creation regardless of source phase.
    for E in [1.02,1.2,2.0]:
        c=coefficients(E,0.0,[1,math.sqrt(2)],[0.3,0.3]); crit=(E-1)/sum(c)
        check(abs(crit-1/0.6)<1e-12,'perfect clock alignment threshold')

    # Deterministic long-run single-flow empirical frequency for two irrationally
    # related frequencies, compared to independent-angle torus integration.
    E=1.1; rho=0.5; h=1
    c1,c2=coefficients(E,h,[1,math.sqrt(2)],[0.3,0.3])
    target=density_two(rho,E,c1,c2)
    count=0; N=160000
    for k in range(N):
        t=0.811271828*k
        up=1+rho*0.3*(math.cos(t)+math.cos(math.sqrt(2)*t))
        down=1+rho*0.3*(math.cos(t+h)+math.cos(math.sqrt(2)*(t+h)))
        count += (down>E*up)
    freq=count/N
    check(abs(freq-target)<0.01,'equidistribution numeric sanity')
    print('PASS',COUNT,'diagnostics')
    print('two-mode coefficients',format(c1,'.15g'),format(c2,'.15g'))
    print('two-mode critical rho',format((E-1)/(c1+c2),'.15g'))
    print('two-mode C',format(C,'.15g'))
    print('occupation density at rho=0.5',format(target,'.10g'),'sampled',format(freq,'.10g'))

if __name__ == '__main__':
    main()
