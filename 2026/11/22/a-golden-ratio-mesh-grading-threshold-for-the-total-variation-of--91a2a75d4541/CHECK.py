"""Independent numerical checks for natural-cubic step data on geometric grids.

Run: python CHECK.py.  This code is supplementary to the analytical proof.
No third-party dependencies are needed.
"""
from math import sqrt, isclose


def parameters(R):
    s = sqrt(R*R + R + 1)
    a = 1/(1+R+s)
    q = R*a*a
    beta = R*R*a
    return a,q,beta


def kernel_F(k):
    assert 0 <= k < 1
    t = (3-sqrt(3*(1-k+k*k)))/(3*(1+k))
    return t*(1-t)*(2-t-k*(1+t))/3


def exact_variation(R,N):
    a,q,beta = parameters(R)
    return 1+6*sum(beta**i*(1-q**(N-i))/(1-q**N)*
        kernel_F(a*(1-q**(N-i-1))/(1-q**(N-i)))
        for i in range(1,N))


def direct_natural_second_derivatives(R,N):
    h = [R**i for i in range(N)]
    y = [0.] + [1.]*N
    if N == 1: return [0.,0.]
    n = N-1
    diag = [2*(h[i]+h[i+1]) for i in range(n)]
    upper = [h[i+1] for i in range(n-1)]
    lower = [h[i+1] for i in range(n-1)]
    rhs = [6*((y[i+2]-y[i+1])/h[i+1]-(y[i+1]-y[i])/h[i]) for i in range(n)]
    for i in range(1,n):
        t=lower[i-1]/diag[i-1]
        diag[i]-=t*upper[i-1]
        rhs[i]-=t*rhs[i-1]
    u=[0.]*n
    u[-1]=rhs[-1]/diag[-1]
    for i in range(n-2,-1,-1):
        u[i]=(rhs[i]-upper[i]*u[i+1])/diag[i]
    return [0.]+u+[0.]


def cubic_value(t,dy,h,ML,MR,y0):
    return y0+dy*t+(h*h/6)*(ML*(-2*t+3*t*t-t*t*t)+MR*(t*t*t-t))


def direct_variation(R,N):
    h=[R**i for i in range(N)]
    y=[0.]+[1.]*N
    M=direct_natural_second_derivatives(R,N)
    out=0.
    for i in range(N):
        dy=y[i+1]-y[i]; A=h[i]*h[i]/6
        aa=3*A*(M[i+1]-M[i])
        bb=6*A*M[i]
        cc=dy-A*(2*M[i]+M[i+1])
        roots=[]
        if abs(aa)>1e-12*max(1.,abs(bb),abs(cc)):
            disc=bb*bb-4*aa*cc
            if disc>0:
                roots=[(-bb+sqrt(disc))/(2*aa),(-bb-sqrt(disc))/(2*aa)]
        elif bb != 0:
            roots=[-cc/bb]
        ts=sorted([0.,1.]+[t for t in roots if 0<t<1])
        z=[cubic_value(t,dy,h[i],M[i],M[i+1],y[i]) for t in ts]
        out+=sum(abs(z[j+1]-z[j]) for j in range(len(z)-1))
    return out,M


def infinite_subcritical(R):
    a,q,beta=parameters(R)
    assert beta<1
    return 1+6*beta*kernel_F(a)/(1-beta)


def supercritical_constant(R,terms=400):
    a,q,beta=parameters(R)
    assert beta>1
    return 6*sum(beta**(-j)*(1-q**j)*kernel_F(a*(1-q**(j-1))/(1-q**j))
                 for j in range(1,terms+1))


def check():
    for R in (.4,1.,1.6,2.,(3+sqrt(5))/2,3.,4.,6.):
        a,q,beta=parameters(R)
        for N in range(2,17):
            predicted=exact_variation(R,N)
            observed,M=direct_variation(R,N)
            assert isclose(predicted,observed,rel_tol=2e-8,abs_tol=2e-8), (R,N,predicted,observed)
            expected=[0.]+[6*(-a)**i*(1-q**(N-i))/(1-q**N) for i in range(1,N)]+[0.]
            assert all(isclose(u,v,rel_tol=2e-7,abs_tol=2e-9) for u,v in zip(M,expected)), (R,N,M,expected)
    print('INDEPENDENT_TRIDIAGONAL_AND_CUBIC_EXTREMA_CHECK_PASS')
    for R in (.5,1.,2.):
        target=infinite_subcritical(R)
        assert abs(exact_variation(R,600)-target)<1e-8
    print('SUBCRITICAL_CLOSED_LIMIT_CHECK_PASS')
    R=(3+sqrt(5))/2
    a,q,beta=parameters(R)
    slope=6*kernel_F(a)
    assert abs(beta-1)<1e-14
    assert abs(exact_variation(R,900)/900-slope)<.002
    print('GOLDEN_RATIO_CRITICAL_LINEAR_SLOPE_CHECK_PASS')
    for R in (3.,4.,6.):
        a,q,beta=parameters(R)
        target=supercritical_constant(R)
        N=150
        assert abs(exact_variation(R,N)/beta**N-target)<1e-7, (R,N,target)
    print('SUPERCRITICAL_EXPONENTIAL_CONSTANT_CHECK_PASS')
    print('ALL_GEOMETRIC_NATURAL_SPLINE_VARIATION_CHECKS_PASS')


if __name__=='__main__':
    check()
