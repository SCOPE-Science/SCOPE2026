"""Finite-step checks for time-dependent independent-reversal walks (Python stdlib)."""
from math import comb, gamma, sqrt, pi, log


def walk_moments(c, n):
    # M_j=E[X_n^j], A_j=E[X_n^j V_n], initial V_0 fair, X_0=0.
    M=[1.,0.,0.,0.,0.]; A=[0.]*5
    for k in range(1,n+1):
        g=1-2*c/(k+2*c)
        NN=[]; BB=[]
        for j in range(5):
            NN.append(sum(comb(j,i)*(M[j-i] if i%2==0 else g*A[j-i]) for i in range(j+1)))
            BB.append(sum(comb(j,i)*(g*A[j-i] if i%2==0 else M[j-i]) for i in range(j+1)))
        M,A=NN,BB
    return M


def limit_cov(c,s,t):
    assert 0<s<=t
    return s*s/(2*c+1)+s**(2*c+1)/(2*c+1)*(log(t/s) if c==.5 else (t**(1-2*c)-s**(1-2*c))/(1-2*c))


def finite_covariance(c,N,s,t):
    m=int(round(N*s)); n=int(round(N*t)); assert 0<m<=n
    a=0.; m2=0.
    for k in range(1,m+1):
        g=1-2*c/(k+2*c)
        m2 += 2*g*a+1
        a=g*a+1
    cross=m2; prod=1.
    for k in range(m+1,n+1):
        prod*=1-2*c/(k+2*c)
        cross += a*prod
    return cross/(N*N)


def simpson_integral(f,a,b,n=10000):
    assert n%2==0
    h=(b-a)/n
    return (f(a)+f(b)+4*sum(f(a+(2*i+1)*h) for i in range(n//2))+2*sum(f(a+2*i*h) for i in range(1,n//2)))*h/3


def main():
    passed=0
    for c in [.25,.5,1.,2.,4.]:
        n=60000; M=walk_moments(c,n)
        variance=1/(2*c+1)
        fourth=3/((2*c+1)*(2*c+3))
        assert abs(M[2]/n**2-variance)<.0001; passed+=1
        assert abs(M[4]/n**4-fourth)<.0001; passed+=1
        assert abs(M[1])<1e-8; passed+=1
        assert abs(M[3])<1e-7; passed+=1
        binder=1-(M[4]/n**4)/(3*(M[2]/n**2)**2)
        assert abs(binder-2/(2*c+3))<.0002; passed+=1
    for c in (.25,.5,1.,2.):
        for s,t in ((.3,.7),(.4,1.),(1.,3.)):
            assert abs(finite_covariance(c,50000,s,t)-limit_cov(c,s,t))<.0003
            passed+=1
        for s,t in ((1.,1.5),(.4,1.5),(2.,9.)):
            integrand=lambda v: v**(-2*c)
            numerical=s*s/(2*c+1)+s**(2*c+1)/(2*c+1)*simpson_integral(integrand,s,t)
            assert abs(numerical-limit_cov(c,s,t))<1e-9
            passed+=1
    for c in (.5,1.,2.,4.):
        C=gamma(c+.5)/(sqrt(pi)*gamma(c))
        integrand=lambda theta: C*2*pow(max(0.,__import__('math').cos(theta)),2*c-1)
        # z=sin(theta); integrate theta from 0 to pi/2, using symmetry.
        area=simpson_integral(integrand,0,pi/2)
        assert abs(area-1)<1e-8
        passed+=1
    print('PASS:',passed,'deterministic finite-step and integral checks')

if __name__=='__main__':
    main()
