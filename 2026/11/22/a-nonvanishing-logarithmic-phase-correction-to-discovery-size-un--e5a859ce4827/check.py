"""Independent arithmetic diagnostics for a first-detection model.

The stated infinite claims use analytic arguments, not these finite checks.
"""
import math


def first_failure_tail(ratio, amplitude, n):
    return math.exp(-amplitude * (ratio ** (n+1) - ratio) / (ratio - 1))


def expected_scaled(ratio, amplitude):
    # E[R^K] by the tail-sum identity. Terminate after rigorous
    # superexponential decay has made all subsequent terms negligible.
    c = amplitude * ratio / (ratio - 1.0)
    total = 0.0
    u = c
    rpow = 1.0
    for n in range(100000):
        term = rpow * math.exp(-u)
        total += term
        if u > 730.0:
            break
        rpow *= ratio
        u *= ratio
    else:
        raise AssertionError('tail did not converge')
    return amplitude * (1.0+(ratio-1.0)*math.exp(c)*total)


def f_periodic(ratio, theta):
    # Bilateral series with uniform rapidly decaying tails.
    s = 0.0
    for j in range(-800, 100):
        exponent=(j-theta)*math.log(ratio)
        if exponent < -740:
            continue
        if exponent > 710:
            continue
        u=math.exp(exponent)
        s+=u*math.exp(-u)
    return s


def expected_asymptotic(ratio, theta):
    return ((ratio-1)**2/ratio)*f_periodic(ratio,theta)


def check():
    checks=0
    for R in (1.4, 2.0, 4.0, 10.0):
        for a in (0.01, .1, .7):
            c=a*R/(R-1)
            p=1
            for n in range(1,21):
                if p == 0.0:
                    break
                # Independent product of round failure probabilities.
                p*=math.exp(-a*R**n)
                q=first_failure_tail(R,a,n)
                assert abs(p-q)<=2e-14
                checks+=1
            pK=0.0
            pmfExpected=0.0
            for n in range(1, 150):
                prev=first_failure_tail(R,a,n-1)
                next_=first_failure_tail(R,a,n)
                z=prev-next_
                pK+=z
                pmfExpected+=R**n*z
                if next_ == 0.0:
                    break
            assert abs(1-pK)<1e-13
            assert abs(a*pmfExpected-expected_scaled(R,a))<1e-8*max(1,expected_scaled(R,a))
            checks+=2
    for R in (1.4,2.0,4.0,10.0):
        for th in (0.0,.13,.25,.5,.77,.9):
            f=f_periodic(R,th)
            assert f>0
            assert abs(f-f_periodic(R,th+1))<5e-10
            checks+=2
            # Explicit tail bound of fixed-R asymptotic: absolute O(a).
            for m in (7,10,13):
                c=math.exp(-(m+th)*math.log(R))
                a=c*(R-1)/R
                target=expected_asymptotic(R,th)
                measured=expected_scaled(R,a)
                assert abs(measured-target)<=a*(1+3*R)*max(1,target)
                checks+=1
    for R in (2.0, 4.0, 10.0):
        vals=[f_periodic(R,k/3000) for k in range(3000)]
        mean=sum(vals)/3000
        assert abs(mean-1/math.log(R))<2e-7
        checks+=1
    assert f_periodic(10,0)> f_periodic(10,.5)+.07
    checks+=1
    print('checks_passed:',checks)
    for ph in (0,.5):
        print('R=10 theta=',ph,'limiting sigma*E[area]=',repr(expected_asymptotic(10,ph)))
    print('R=10 phase_average=',repr(8.1/math.log(10)))


if __name__=='__main__':
    check()
