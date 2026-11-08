"""Independent arithmetic/finite-section checks for the two-edge periodic-tail shift.
Standard library only. Finite sections corroborate; the analytic proof is infinite.
"""
from fractions import Fraction as Q
from math import sqrt


def check_exact(a,b,t2,u2,r,w2):
    a,b,t2,u2,r,w2=map(Q, (a,b,t2,u2,r,w2))
    c=a*b
    d=a*a+b*b
    d0=t2+u2
    c02=b*b*u2
    assert 0<r<1
    assert c+(d-d0)*r+(c-c02/c)*r*r==0
    assert w2 == (d+c*(r+1/r))/4
    assert w2>(a+b)**2/4
    assert (d+c*(r+1/r)-d0)==(c02/c)*r
    return 5


def jacobi_top(a,b,t,u,N,iterations=1500):
    # J = B B*, diagonal d0,d,...; off diag bu,ab,... .
    d0=t*t+u*u; d=a*a+b*b
    c0=b*u; c=a*b
    x=[1/sqrt(N)]*N
    for j in range(iterations):
        z=[0.]*N
        for i in range(N):
            z[i]=(d0 if i==0 else d)*x[i]
            if i>0:z[i]+=(c0 if i==1 else c)*x[i-1]
            if i+1<N:z[i]+=(c0 if i==0 else c)*x[i+1]
        norm=sqrt(sum(v*v for v in z))
        x=[v/norm for v in z]
    return (sum((d0 if i==0 else d)*x[i]*x[i] for i in range(N))
            +2*sum((c0 if i==0 else c)*x[i]*x[i+1] for i in range(N-1)))


def analytic_radius(a,b,t,u):
    c=a*b; c0=b*u; d=a*a+b*b; d0=t*t+u*u
    k=t*t+(1+b/a)*u*u-(a+b)**2
    if k<=0:return (a+b)/2
    def F(r):return c+(d-d0)*r+(c-c0*c0/c)*r*r
    lo=0.; hi=1.
    for _ in range(100):
        mid=(lo+hi)/2
        if F(mid)>0:lo=mid
        else:hi=mid
    r=(lo+hi)/2
    return sqrt(d+c*(r+1/r))/2


def main():
    count=0
    count+=check_exact(1,1,4,1,Q(1,3),Q(4,3))
    count+=check_exact(2,1,4,4,Q(2,3),Q(7,3))
    for a,b,t,u in [(1,1,1,1),(1,1,2,1),(1,1,sqrt(2),1),
                    (2,1,1,1),(2,1,3,1),(2,1,2,2),(.5,2,1,1),
                    (1,2,3,4),(1.5,2.5,3,2)]:
        R=analytic_radius(a,b,t,u)
        finite=sqrt(jacobi_top(a,b,t,u,320))/2
        assert finite<=R+1e-7, (a,b,t,u,R,finite)
        assert R-finite<0.02, (a,b,t,u,R,finite)
        count+=2
    a=2.;b=1.;u=1.
    crit=(a+b)**2-(1+b/a)*u*u
    coeff=a**3/(4*b*(a+b)*u**4)
    errors=[]
    for k in [0.01,0.002,0.0005]:
        actual=(analytic_radius(a,b,sqrt(crit+k),u)-(a+b)/2)/k**2
        assert abs(actual-coeff)<0.09,(actual,coeff)
        errors.append(abs(actual-coeff))
        count+=1
    assert errors[-1]<0.005 and all(errors[i+1]<errors[i] for i in range(len(errors)-1))
    count+=1
    print('TWO_EDGE_PERIODIC_TAIL_CHECK_OK',count,'assertion groups; exact identities and finite sections')

if __name__=='__main__':main()
