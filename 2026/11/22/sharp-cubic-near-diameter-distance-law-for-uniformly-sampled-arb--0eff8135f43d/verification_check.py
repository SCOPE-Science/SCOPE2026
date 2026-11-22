"""Independent numerical checks for an arbelos near-diameter asymptotic.
Only the Python standard library is needed. Run: python verification_check.py.
Numerical tests supplement the analytic proof; they do not establish an asymptotic theorem.
"""
import math


def coefficient(alpha):
    assert 0 < alpha < 1
    beta = 1-alpha
    ca = beta/(2*alpha)
    cb = alpha/(2*beta)
    ia = 2/math.sqrt(ca)*math.atan(2*math.sqrt(ca))
    ib = 2/math.sqrt(cb)*math.atan(2*math.sqrt(cb))
    iab = math.sqrt(8*alpha*beta)*(math.atan(math.sqrt(2*alpha**3/beta)) + math.atan(math.sqrt(2*beta**3/alpha)))
    return (4-ia-ib+iab)/(6*math.pi**2*alpha**2*beta**2)


def composite_simpson(f, N=20000):
    assert N % 2 == 0
    h=1/N
    s=f(0)+f(1)
    for i in range(1,N):
        s+=(4 if i%2 else 2)*f(i*h)
    return s*h/3


def coefficient_integral(alpha):
    beta=1-alpha
    ca=beta/(2*alpha); cb=alpha/(2*beta)
    j=composite_simpson(lambda p: 4-1/(.25+ca*p*p)-1/(.25+cb*(1-p)**2)+1/(.25+ca*p*p+cb*(1-p)**2)) /12
    return 2*j/(math.pi**2*alpha**2*beta**2)


def radical_inverse(k,b):
    out=0.; x=1/b
    while k:
        k,r=divmod(k,b)
        out+=r*x
        x/=b
    return out


def finite_epsilon_quadrature(alpha, epsilon, N=100000):
    beta=1-alpha
    total=0.
    for j in range(1,N+1):
        # Endpoints restricted to x<=2*epsilon from the left/right tips;
        # this includes the complete rare event for sufficiently small epsilon.
        u=2*radical_inverse(j,2)
        v=2*radical_inverse(j,3)
        lo1=math.sqrt(max(0,2*alpha*u-epsilon*u*u))
        hi1=math.sqrt(max(0,2*u-epsilon*u*u))
        lo2=math.sqrt(max(0,2*beta*v-epsilon*v*v))
        hi2=math.sqrt(max(0,2*v-epsilon*v*v))
        y=lo1+(hi1-lo1)*radical_inverse(j,5)
        z=lo2+(hi2-lo2)*radical_inverse(j,7)
        dsq=(2-epsilon*(u+v))**2+epsilon*(y-z)**2
        if dsq>(2-epsilon)**2:
            total+=(hi1-lo1)*(hi2-lo2)
    return (8/(math.pi**2*alpha**2*beta**2))*total/N


def main():
    cases=[.1,.2,.3,.5,.7,.9]
    for a in cases:
        closed=coefficient(a)
        numeric=coefficient_integral(a)
        assert abs(closed-numeric)<1e-9,(a,closed,numeric)
        assert abs(closed-coefficient(1-a))<1e-10
        assert closed>0
    sym=8/(3*math.pi**2)*(4+math.sqrt(2)*math.pi-6*math.sqrt(2)*math.atan(math.sqrt(2)))
    assert abs(coefficient(.5)-sym)<1e-11
    for a in [.001,.0001,.00001]:
        assert abs(a*coefficient(a)-4/(9*math.pi**2)) < .004
    for a in [.2,.5]:
        for e in [.05,.015]:
            val=finite_epsilon_quadrature(a,e)
            target=coefficient(a)
            print('shape',a,'epsilon',e,'rescaled probability',val,'coefficient',target)
            assert abs(val-target) < .015,(a,e,val,target)
    print('ARBELOS_CHORD_CHECKS_OK')

if __name__=='__main__': main()
