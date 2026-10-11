#!/usr/bin/env python3
import math

def closed(gamma0,Gamma):
    if gamma0<=Gamma/2:
        return 0.0
    k=math.sqrt(2*gamma0*Gamma-Gamma*Gamma)
    x=math.pi*Gamma/k
    return 1/math.expm1(x)

def b(t,gamma0,Gamma):
    if gamma0<=Gamma/2:
        k=math.sqrt(max(0.0,Gamma*Gamma-2*gamma0*Gamma))
        if k==0:
            return math.exp(-Gamma*t/2)*(1+Gamma*t/2)
        return math.exp(-Gamma*t/2)*(math.cosh(k*t/2)+(Gamma/k)*math.sinh(k*t/2))
    k=math.sqrt(2*gamma0*Gamma-Gamma*Gamma)
    return math.exp(-Gamma*t/2)*(math.cos(k*t/2)+(Gamma/k)*math.sin(k*t/2))

def bprime_formula(t,gamma0,Gamma):
    k=math.sqrt(2*gamma0*Gamma-Gamma*Gamma)
    return -(gamma0*Gamma/k)*math.exp(-Gamma*t/2)*math.sin(k*t/2)

def main():
    derivative_checks=0
    maxima_checks=0
    sum_checks=0
    for ratio in (0.55,0.7,1.0,2.0,5.0,10.0,25.0):
        Gamma=1.0
        gamma0=ratio*Gamma
        k=math.sqrt(2*gamma0*Gamma-Gamma*Gamma)
        h=1e-6
        for t in (0.3,1.1,2.4):
            num=(b(t+h,gamma0,Gamma)-b(t-h,gamma0,Gamma))/(2*h)
            ana=bprime_formula(t,gamma0,Gamma)
            assert abs(num-ana)<2e-8
            derivative_checks+=1

        q=math.exp(-math.pi*Gamma/k)
        for n in range(1,8):
            tn=2*math.pi*n/k
            assert abs(bprime_formula(tn,gamma0,Gamma))<2e-12
            assert abs(abs(b(tn,gamma0,Gamma))-q**n)<2e-12
            maxima_checks+=1

        s=sum(q**n for n in range(1,20000))
        assert abs(s-closed(gamma0,Gamma))<5e-13
        sum_checks+=1

    # Closed Markovian side.
    for ratio in (0.1,0.49,0.5):
        assert closed(ratio,1.0)==0.0

    # Threshold asymptotic.
    threshold_ratios=[]
    for eps in (0.04,0.01,0.004):
        r=(1+eps)/2
        N=closed(r,1.0)
        threshold_ratios.append(N/math.exp(-math.pi/math.sqrt(eps)))
    assert abs(threshold_ratios[-1]-1)<abs(threshold_ratios[0]-1)
    assert abs(threshold_ratios[-1]-1)<1e-12

    # Strong-coupling three-term expansion.
    strong_errors=[]
    for r in (50.0,200.0,800.0):
        s=math.sqrt(2*r-1)
        approx=s/math.pi-0.5+math.pi/(12*s)
        strong_errors.append(abs(closed(r,1.0)-approx))
    assert strong_errors[-1] < strong_errors[0]/20

    print("VERIFY_OK")
    print("derivative_checks =",derivative_checks)
    print("revival_maximum_checks =",maxima_checks)
    print("geometric_sum_checks =",sum_checks)
    print("threshold_normalized_ratio =",threshold_ratios[-1])
    print("strong_coupling_last_error =",strong_errors[-1])

if __name__=="__main__":
    main()
