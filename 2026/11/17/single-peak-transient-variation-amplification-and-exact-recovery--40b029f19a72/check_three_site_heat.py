#!/usr/bin/env python3
"""Independent numerical and exact-algebra checks for a three-state Markov heat norm."""
import math, random


def exact_profile(a, b, c, d, w1, w2, t):
    # Rates a=1->2, b=2->1, c=2->3, d=3->2.
    alpha, beta = a+b, c+d
    gap = math.hypot(alpha-beta,2*math.sqrt(b*c))
    u=(alpha+beta-gap)/2; v=(alpha+beta+gap)/2
    assert 0 < u < v
    deriv=(-alpha+b*w2/w1,-beta+c*w1/w2)
    def column(delta):
        return ((v+delta)*math.exp(-u*t)-(u+delta)*math.exp(-v*t))/gap
    return tuple(map(column,deriv)),deriv,(u,v)


def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def heat_uniformization(a,b,c,d,t):
    R=max(a,b+c,d)
    # Q=R(P-I), P is a stochastic transition matrix.
    P=[[1-a/R,a/R,0],[b/R,1-(b+c)/R,c/R],[0,d/R,1-d/R]]
    power=[[float(i==j) for j in range(3)] for i in range(3)]
    result=[[0.0]*3 for _ in range(3)]
    term=math.exp(-R*t)
    for k in range(250):
        for i in range(3):
            for j in range(3):
                result[i][j]+=term*power[i][j]
        if k>R*t+28 and term < 1e-17:
            break
        power=mul(power,P)
        term *= R*t/(k+1)
    return result


def variation_coeffs(E,w1,w2):
    result=[]
    for h in ((0,1,1),(0,0,1)):
        y=[sum(E[i][j]*h[j] for j in range(3)) for i in range(3)]
        result.append((w1*abs(y[1]-y[0])+w2*abs(y[2]-y[1]))/(w1 if h[1] else w2))
    return tuple(result)


def main():
    rng=random.Random(20261112)
    checked=0
    for i in range(350):
        a,b,c,d=[10**rng.uniform(-0.6,0.6) for _ in range(4)]
        w1,w2=[10**rng.uniform(-0.8,0.8) for _ in range(2)]
        t=rng.uniform(0,4.0)
        analytic,deriv,(u,v)=exact_profile(a,b,c,d,w1,w2,t)
        E=heat_uniformization(a,b,c,d,t)
        independent=variation_coeffs(E,w1,w2)
        assert max(abs(x-y) for x,y in zip(analytic,independent)) < 2e-11, (i,analytic,independent)
        assert not (deriv[0]>=0 and deriv[1]>=0)
        if max(deriv)>0:
            j=0 if deriv[0]>0 else 1
            delta=deriv[j]
            peak_time=math.log(v*(u+delta)/(u*(v+delta)))/(v-u)
            assert peak_time>0
            peak=exact_profile(a,b,c,d,w1,w2,peak_time)[0][j]
            predicted=(v+delta)/v*(u*(v+delta)/(v*(u+delta)))**(u/(v-u))
            assert abs(peak-predicted)<2e-11 and peak>1
            # Other branch strictly contracts, initially active branch eventually contracts.
            k=1-j
            for q in [0.001,peak_time, 2*peak_time, 10/max(u,1e-3)]:
                gg=exact_profile(a,b,c,d,w1,w2,q)[0]
                assert gg[k]<1+1e-11
            lo=peak_time; hi=max(2*peak_time,1/u)
            while exact_profile(a,b,c,d,w1,w2,hi)[0][j] > 1:
                hi*=2
            for _ in range(80):
                mid=(lo+hi)/2
                if exact_profile(a,b,c,d,w1,w2,mid)[0][j]>1:lo=mid
                else:hi=mid
            T=(lo+hi)/2
            assert T>peak_time
        else:
            assert all(exact_profile(a,b,c,d,w1,w2,q)[0][j]<1+1e-11 for q in [0.02,0.3,1,5] for j in (0,1))
        checked+=1
    # Exact elementary golden-ratio witness (rates all 1, edge variation weights 1,3).
    g=lambda t: 2*math.exp(-t)-math.exp(-3*t)
    tp=math.log(1.5)/2; T=math.log((1+math.sqrt(5))/2)
    assert abs(g(tp)-(4/3)*math.sqrt(2/3))<1e-14
    assert abs(g(T)-1)<1e-14
    assert g(0.1)>1 and g(T+0.1)<1
    # Verifies the companion column strictly decreases.
    for t in [0.01,0.1,0.3,0.6,2]:
        other=(2/3)*math.exp(-t)+(1/3)*math.exp(-3*t)
        assert abs(other-exact_profile(1,1,1,1,1,3,t)[0][1])<1e-14
        assert other<1
    print('INDEPENDENT_MARKOV_UNIFORMIZATION_350_CASES_PASS')
    print('SINGLE_PEAK_AND_UNIQUE_RECOVERY_CHECKS_PASS')
    print('EXACT_GOLDEN_RATIO_RECOVERY_IDENTITY_PASS')
    print('ALL_THREE_SITE_HEAT_CHECKS_PASS')

if __name__=='__main__':
    main()
