"""Numerical diagnostics for catenary arc diameter and rare-chord asymptotics.
Python 3 standard library only. Numerical checks supplement the written proof.
"""
import math


def q(L, x):
    return (L + x)**2 + (math.cosh(L) - math.cosh(x))**2


def stationary(L, x):
    return (math.cosh(L) - math.cosh(x))*math.sinh(x) - (L + x)


def inner_max(L):
    C = math.cosh(L)
    if C <= 2.0:
        return None
    m = math.acosh(C/2)
    if stationary(L,m) <= 0:
        return None
    lo, hi = 0.0, m
    for _ in range(75):
        mid = (lo+hi)/2
        if stationary(L,mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2


def transition():
    lo,hi=2.10,2.30
    for _ in range(70):
        L=(lo+hi)/2
        x=inner_max(L)
        assert x is not None
        if q(L,x)>4*L*L: hi=L
        else: lo=L
    L=(lo+hi)/2
    return L,inner_max(L)


def data(L):
    x=inner_max(L)
    assert x is not None
    C=math.cosh(L)
    H=C-math.cosh(x)
    D=math.sqrt(q(L,x))
    a=(L+x+H*math.sinh(L))/D
    b=math.cosh(x)*(C-2*math.cosh(x))/(2*D)
    rho=lambda z: math.cosh(z)/(2*math.sinh(L))
    A=16*rho(L)*rho(x)/(3*a*math.sqrt(b))
    return x,D,a,b,A


def quad_probability_above(L, eps, n=320):
    x,D,a,b,A=data(L)
    vlim=1.5*math.sqrt(eps/b)
    ulim=1.5*eps/a
    du=ulim/n;dv=2*vlim/n
    total=0.0
    for i in range(n):
        u=(i+0.5)*du
        dens_u=math.cosh(L-u)/(2*math.sinh(L))
        for j in range(n):
            v=-vlim+(j+0.5)*dv
            if D-math.sqrt((L-u+x+v)**2+(math.cosh(L-u)-math.cosh(x+v))**2) <= eps:
                total+=dens_u*math.cosh(x+v)/(2*math.sinh(L))
    return 4*total*du*dv, A*eps**1.5


def quad_probability_below(L, eps, n=250):
    D=2*L;u_max=1.5*eps;du=u_max/n
    total=0.0
    for i in range(n):
        u=(i+0.5)*du
        for j in range(n):
            v=(j+0.5)*du
            if D-math.hypot(2*L-u-v,math.cosh(L-u)-math.cosh(L-v)) <= eps:
                total += math.cosh(L-u)*math.cosh(L-v)/(4*math.sinh(L)**2)
    return 2*total*du**2, (math.cosh(L)/(2*math.sinh(L)))**2 *eps**2


def main():
    tests=0
    Ls, xs=transition()
    assert abs(Ls-2.1950423222006785)<1e-12
    assert abs(xs-0.8587436952563898)<1e-12
    assert abs(q(Ls,xs)-4*Ls*Ls)<1e-11
    assert abs(stationary(Ls,xs))<1e-12
    tests+=4
    _,_,a,b,C=data(Ls)
    assert a>2 and b>0 and abs(C-0.2091371276994043)<1e-11
    tests+=3
    for L in [0.2,0.7,1.4,1.8,2.1,2.18,2.194,2.196,2.25,2.4,3,4]:
        x=inner_max(L)
        best=max(4*L*L, q(L,x) if x is not None else 0)
        gridbest=0
        for i in range(601):
            xx=-L+2*L*i/600
            for j in [int((xx+L)*600/(2*L)), 600]:
                pass
            gridbest=max(gridbest,q(L,xx))
        assert gridbest <=best+1e-9
        assert best-gridbest <0.04
        tests+=2
    for L in [1.8,2.05,2.18]:
        assert q(L,inner_max(L))<4*L*L if inner_max(L) is not None else True
        tests+=1
    for L in [2.21,2.4,3.0]:
        assert q(L,inner_max(L))>4*L*L
        tests+=1
    for L in [1.8,2.0]:
        for eps in [.01,.003]:
            actual,pred=quad_probability_below(L,eps)
            assert abs(actual/pred-1)<0.07,(L,eps,actual/pred)
            tests+=1
    for L in [2.3,2.5]:
        for eps in [.003,.001]:
            actual,pred=quad_probability_above(L,eps)
            assert abs(actual/pred-1)<0.12,(L,eps,actual/pred)
            tests+=1
    print('PASS:',tests,'diagnostic conditions; critical L=',format(Ls,'.15f'),
          'x=',format(xs,'.15f'),'C=',format(C,'.15f'))

if __name__=='__main__': main()
