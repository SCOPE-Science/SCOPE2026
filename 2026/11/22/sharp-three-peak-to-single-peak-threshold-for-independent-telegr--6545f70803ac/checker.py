"""Finite reproducibility checks for the shape theorem for two independent telegraph-filter stationary coordinates.
No numerical calculation substitutes for the analytical convexity and asymptotic proofs.
"""
from fractions import Fraction
from math import gamma, sqrt, pi, log


def hyp2f1(a, b, c, q):
    assert 0 <= q < 1
    term = total = 1.0
    for n in range(1, 20000):
        term *= ((a+n-1)*(b+n-1))/((c+n-1)*n)*q
        total += term
        if abs(term) < 3e-16 * abs(total):
            break
    else:
        raise RuntimeError('hypergeometric series did not converge at requested point')
    return total


def log_density(alpha, s):
    assert alpha > 0 and 0 < s < 2
    t = 1-s/2; b = 1+s/2
    h = hyp2f1(1-alpha, .5, alpha+.5, (t/b)**2)
    C = gamma(alpha+.5)/(sqrt(pi)*gamma(alpha))
    beta_half = sqrt(pi)*gamma(alpha)/gamma(alpha+.5)
    return 2*log(C)+log(beta_half)+(2*alpha-1)*log(t)+(2*alpha-2)*log(b)+log(h)


def log_derivative(alpha, s):
    t = 1-s/2; b = 1+s/2
    q = (t/b)**2
    h = hyp2f1(1-alpha, .5, alpha+.5, q)
    hp = (1-alpha)*.5/(alpha+.5)*hyp2f1(2-alpha, 1.5, alpha+1.5, q)
    return -(2*alpha-1)/(2*t)+(2*alpha-2)/(2*b)-(1/t+1/b)*q*hp/h


def valley(alpha):
    lo=0.05; hi=2-1e-10
    assert log_derivative(alpha,lo)<0 and log_derivative(alpha,hi)>0
    for _ in range(80):
        md=(lo+hi)/2
        if log_derivative(alpha,md)>0:hi=md
        else:lo=md
    return (lo+hi)/2


def main():
    count = 0
    for num in (-9,-7,-5,-3,-1,0,1,3,5,7,9):
        u=Fraction(num,10); A=1-u*u; D=1+u*u
        for j in range(1,40):
            s=Fraction(j,20)
            B=A+D*s+A*s*s/4
            Bp=D+A*s/2
            discr=B*A/2-Bp*Bp
            assert discr<0
            count+=1
    for a in (.1,.25,.4,.49,.5):
        for j in range(3,87):
            s=j/50
            h=.0005
            second=log_density(a,s+h)+log_density(a,s-h)-2*log_density(a,s)
            assert second>1e-9, (a,s,second)
            count+=1
    for a in (.5,.65,.9,1.):
        for j in range(3,97):
            s=j/50
            assert log_derivative(a,s)<0, (a,s)
            count+=1
    for j in range(3,98):
        s=j/50
        assert abs(log_density(1,s)-log((2-s)/4))<5e-13
        count+=1
    for a in (.1,.25,.4,.49,.495,.499):
        v=valley(a)
        assert 0<v<2
        assert log_derivative(a,max(.05,v-.002))<0
        assert log_derivative(a,min(2-1e-9,v+.002))>0
        count+=3
    for a in (.49,.495,.499):
        ratio=(2-valley(a))/(1-2*a)
        assert abs(ratio-4)<12*(1-2*a)**.5, (a,ratio)
        count+=1
    print(f'PASS: {count} exact-rational, numerical-shape, and boundary checks; infinite conclusions are analytical.')


if __name__ == '__main__':
    main()
