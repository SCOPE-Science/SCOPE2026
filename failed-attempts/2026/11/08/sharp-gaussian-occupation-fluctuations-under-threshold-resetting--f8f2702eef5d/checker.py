"""Standalone exact-moment and finite-difference checks for a killed natural-scale diffusion.
All numbers in the exact tests use rational arithmetic; no extra packages needed.
"""
from fractions import Fraction as F
from math import isclose

TESTS = 0

def check(test, msg):
    global TESTS
    TESTS += 1
    if not test:
        raise AssertionError(msg)


def add(*ps):
    d = {}
    for p in ps:
        for e,c in p.items(): d[e] = d.get(e,F(0))+c
    return {e:c for e,c in d.items() if c}


def mul(p,q):
    d={}
    for e,c in p.items():
        for f,b in q.items(): d[e+f]=d.get(e+f,F(0))+c*b
    return {e:c for e,c in d.items() if c}


def scale(p,c):return {e:x*c for e,x in p.items() if x*c}


def integral(p,a,b):return sum(c*(b**(e+1)-a**(e+1))/(e+1) for e,c in p.items())


def moment_integrals(alpha, rho):
    # Integer alpha and rational resetting site rho, with unit threshold.
    beta=alpha+2
    C=(alpha+1)*beta
    rho=F(rho)
    c=1-(1-rho)/(2*(1-rho**beta))
    Glo={0:(1-rho)/2, 1:(1-rho)/2}
    Ghi={0:(1+rho)/2, 1:-(1+rho)/2}
    def region(y_positive):
        h=F(1) if y_positive else F(0)
        a=(1-c) if y_positive else c
        sign = F(1) if y_positive else F((-1)**(beta-1))
        # u(y) and u'(y) on the selected half-line.
        u=add({0:(1-2*c)/(2*C), 1:F(1)/(2*C)},
              {beta: (-a if y_positive else c)*F((-1)**(beta if not y_positive else 0))/C})
        up=add({0:F(1)/(2*C)},{beta-1:-beta*a*sign/C})
        speed={alpha:F(1) if y_positive else F((-1)**alpha)}
        return h,u,up,speed
    e_tau=e_pos=e_z2_poisson=e_z2_energy=F(0)
    for a,b,g,positive in [(-F(1),F(0),Glo,False),
                           (F(0),rho,Glo,True),
                           (rho,F(1),Ghi,True)]:
        if a==b:continue
        h,u,up,speed=region(positive)
        e_tau+=integral(mul(g,speed),a,b)
        e_pos+=h*integral(mul(g,speed),a,b)
        e_z2_poisson +=2*(h-c)*integral(mul(mul(mul(g,speed),u),{0:F(1)}),a,b)
        e_z2_energy +=2*integral(mul(g,mul(up,up)),a,b)
    return c, e_tau, e_pos, e_z2_poisson, e_z2_energy


def fast_formula(alpha,L):
    return (F(3*(alpha+1), 4*(alpha+2)*(alpha+3)*(2*alpha+3)) if isinstance(alpha,int) else 3*(alpha+1)/(4*(alpha+2)*(alpha+3)*(2*alpha+3)))*L**(alpha+2)


def thomas(diag,lo,hi,rhs):
    n=len(rhs)
    a=diag[:];b=rhs[:]
    for k in range(1,n):
        q=lo[k-1]/a[k-1]
        a[k]-=q*hi[k-1]; b[k]-=q*b[k-1]
    x=[0.0]*n; x[-1]=b[-1]/a[-1]
    for k in range(n-2,-1,-1): x[k]=(b[k]-hi[k]*x[k+1])/a[k]
    return x


def finite_difference(alpha,N):
    # Continuous-time killed random walk with cell-averaged speed density.
    # Unit interval [-1,1], mesh h=1/N.  The scheme respects natural scale.
    h=1.0/N
    xs=[i*h for i in range(-N+1,N)]
    def cell_weight(x):
        a=abs(x)
        if a < h/2:
            return 2*(h/2)**(alpha+1)/((alpha+1)*h)
        return ((a+h/2)**(alpha+1)-(a-h/2)**(alpha+1))/((alpha+1)*h)
    w=[cell_weight(x) for x in xs]
    diag=[2.0/(ww*h*h) for ww in w]
    up=[-1.0/(ww*h*h) for ww in w[:-1]]
    lo=[-1.0/(ww*h*h) for ww in w[1:]]
    m=thomas(diag,lo,up,[1.0]*len(xs))
    hsol=thomas(diag,lo,up,[float(x>0) for x in xs])
    origin=N-1
    c=hsol[origin]/m[origin]
    u=thomas(diag,lo,up,[float(x>0)-c for x in xs])
    z2=thomas(diag,lo,up,[2*(float(x>0)-c)*u[i] for i,x in enumerate(xs)])
    return c, z2[origin]/m[origin],m[origin]


def trapezoid_integral(f,a,b,n=10000):
    if a==b:return 0.0
    h=(b-a)/n
    # Composite midpoint gives good convergence away from integrable cusps.
    return h*sum(f(a+(k+.5)*h) for k in range(n))


def noninteger_checks(alpha,rho):
    beta=alpha+2; C=(alpha+1)*beta
    c=1-(1-rho)/(2*(1-rho**beta))
    def g(y):
        return ((1+min(rho,y))*(1-max(rho,y)))/2
    def u(y):
        p=abs(y)**beta
        return ((1-2*c)/2+y/2-(1-c)*p if y>=0 else
                (1-2*c)/2+y/2+c*p)/C
    def up(y):
        a=1-c if y>0 else c
        return (0.5-beta*a*abs(y)**(beta-1))/C
    def w(y):return abs(y)**alpha
    parts=[(-1.,0.),(0.,rho),(rho,1.)]
    et=sum(trapezoid_integral(lambda y:g(y)*w(y),a,b) for a,b in parts)
    ep=sum(trapezoid_integral(lambda y:g(y)*w(y),a,b) for a,b in parts[1:])
    v1=2*sum(trapezoid_integral(lambda y:g(y)*up(y)**2,a,b) for a,b in parts)
    v2=2*sum(trapezoid_integral(lambda y:g(y)*w(y)*((1 if y>0 else 0)-c)*u(y),a,b) for a,b in parts)
    check(abs(et-(1-rho**beta)/C)<1e-6,('noninteger T',alpha,rho,et))
    check(abs(ep-c*et)<1e-6,('noninteger occupation',alpha,rho,ep))
    check(abs(v1-v2)<1e-6,('noninteger energy',alpha,rho,v1,v2))
    if rho==0:
        check(abs(v1/et-float(fast_formula(alpha,1)))<1e-6,
              ('noninteger closed coefficient',alpha,rho,v1/et))


def main():
    for alpha in range(7):
        for rho in [F(0), F(1,7),F(1,4),F(1,3), F(1,2),F(3,4),F(7,8)]:
            c,t,h,z2,energy=moment_integrals(alpha,rho)
            beta=alpha+2;C=(alpha+1)*beta
            check(t==(1-rho**beta)/C, ('mean',alpha,rho,t))
            check(h==c*t,('occupancy',alpha,rho))
            check(z2==energy, ('energy',alpha,rho,z2,energy))
            check(z2>0,('positive',alpha,rho))
            if rho==0:
                check(c==F(1,2),('symmetry',alpha))
                check(z2/t==fast_formula(alpha,F(1)),('closed form',alpha,z2/t,fast_formula(alpha,F(1))))
                R=F(3*(alpha+1)*(alpha+2),2*(alpha+3)*(2*alpha+3))
                poisson=F(1,2*(alpha+2)**2)
                check(z2/t==R*poisson,('matched poisson',alpha))
                check(F(0)<R<F(3,4),('ratio bound',alpha))
    for alpha in (0.25,0.5,1.5,2.7):
        for rho in (0.,0.2,0.6):noninteger_checks(alpha,rho)
    for alpha in (0,1,2,3):
        for N in (40,120,280):
            c,v,t=finite_difference(alpha,N)
            exact=float(fast_formula(alpha,F(1)))
            # Half-space observable at a single grid point has a small discretization effect.
            tol=0.08 if N==40 else 0.03 if N==120 else 0.015
            check(abs(v-exact) < tol*exact,('FD variance',alpha,N,v,exact))
            check(abs(c-.5)<(0.6/N),('FD occupation',alpha,N,c))
            check(abs(t-F(1,(alpha+1)*(alpha+2)))<0.02,('FD mean',alpha,N,t))
    print('PASS:',TESTS,'exact rational / independent finite-difference assertions')
    for alpha in (0,1,2,4,10):
        print('alpha',alpha,'sigma_thr(L=1)',float(fast_formula(alpha,F(1))),
              'equal-rate ratio',float(F(3*(alpha+1)*(alpha+2),2*(alpha+3)*(2*alpha+3))))

if __name__=='__main__':main()
