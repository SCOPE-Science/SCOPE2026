"""Exact-algebra and finite-orbit diagnostics for a discrete plankton map.

Requires only Python 3 standard library. The analytical theorem is proved in RESULT.md;
no finite computation is used as an infinite-time certificate.
"""
from fractions import Fraction as Q
from math import sqrt, log


def convolution(x, y, degree):
    return [sum(x[j] * y[k-j] for j in range(k+1)) for k in range(degree+1)]


def inverse(p, degree):
    assert p[0] != 0
    result = [1/p[0]] + [Q(0)] * degree
    for k in range(1, degree+1):
        result[k] = -sum(p[j]*result[k-j] for j in range(1,k+1))/p[0]
    return result


def analytic_coefficients(c, theta):
    degree = 5
    a = 1/(1+c)
    b = c*a**3
    v = [Q(0), Q(1), Q(0), Q(0), Q(0), Q(0)]
    w = [Q(0), a, b, Q(0), Q(0), Q(0)]
    one_minus_w = [Q(1)] + [-q for q in w[1:]]
    den = [1+c] + [-c*q for q in w[1:]]
    inv = inverse(den, degree)
    w2 = convolution(w,w,degree)
    w_next = [x+y for x,y in zip(w2, convolution(convolution(one_minus_w,v,degree),inv,degree))]
    vp = convolution(v,convolution(w2,inv,degree),degree)
    v_next = [v[k]-theta*c*vp[k] for k in range(degree+1)]
    K = theta*c*a**3
    L = 3*theta*c**2*a**5
    assert w_next[1] == a and w_next[2] == b
    assert v_next[:5] == [Q(0),Q(1),Q(0),-K,-L]
    assert -(L/(2*K*K)) == -3*(1+c)/(2*theta)
    assert a*(-L/(2*K*K)) + b/(2*K) == -1/theta
    return K,L


def rational_step(u,v,c,theta):
    r = c*theta
    beta = theta*(1+c)**2
    up = u*(2-u) - u*v/(1+c*u)
    vp = v*(1-r+beta*u/(1+c*u)-theta*u)
    return up,vp


def diagnostic(c,theta,u,v,N):
    c,theta,u,v = map(float,(c,theta,u,v))
    K=theta*c/(1+c)**3
    A=1/sqrt(2*K)
    B=-3*(1+c)/(2*theta)
    C=A/(1+c)
    for n in range(1,N+1):
        u,v=(u*(2-u)-u*v/(1+c*u),
             v*(1-theta*c*(1-u)**2/(1+c*u)))
        assert 0<u<=1 and v>0
        if n in {100000,1000000,N}:
            print('c,theta,n:',c,theta,n,
                  'sqrt(n)*v:',round(sqrt(n)*v,9),
                  'limit:',round(A,9),
                  'n*(v-A/sqrt(n)):',round(n*(v-A/sqrt(n)),9),
                  'limit:',round(B,9),
                  'n*(u-1+C/sqrt(n)):',round(n*(u-1+C/sqrt(n)),9),
                  'limit:',round(1/theta,9))


def main():
    cases=[(Q(1,4),Q(4,5),Q(4,5),Q(3,25)),
           (Q(1,2),Q(1,2),Q(13,20),Q(1,25)),
           (Q(1,10),Q(2),Q(13,10),Q(9,100))]
    for c,theta,u,v in cases:
        assert c>0 and c<=Q(1,2) and theta*c<1
        assert 0<u<2 and 0<v<(2-u)*(1+c*u)
        K,L=analytic_coefficients(c,theta)
        up,vp=rational_step(u,v,c,theta)
        w=1-u
        assert 1-up == w*w + (1-w)*v/(1+c-c*w)
        assert vp == v*(1-theta*c*w*w/(1+c-c*w))
        assert 0<up<=1 and vp>0
        assert vp<(2-up)*(1+c*up)
        print('Exact rational checks passed:',c,theta,'K',K,'L',L)
    # The neutral first predator step at exactly u=1 is admissible; strict decay starts next step.
    cc,tt=Q(1,4),Q(4,5)
    u1,v1=rational_step(Q(1),Q(1,2),cc,tt)
    assert v1==Q(1,2) and Q(0)<u1<Q(1)
    u2,v2=rational_step(u1,v1,cc,tt)
    assert Q(0)<u2<Q(1) and Q(0)<v2<v1
    diagnostic(*cases[0],N=2500000)
    diagnostic(*cases[1],N=1000000)
    diagnostic(*cases[2],N=1000000)
    print('All exact algebra tests passed; finite diagnostics completed.')

if __name__=='__main__':
    main()
