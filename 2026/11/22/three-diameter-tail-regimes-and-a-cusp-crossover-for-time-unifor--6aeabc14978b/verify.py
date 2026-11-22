"""Deterministic checks for rolling-phase trochoid distance geometry.

Run with python3 verify.py; Python standard library only.
"""
import math
import random

P = math.pi


def gamma(beta, t):
    return (t - beta * math.sin(t), 1 - beta * math.cos(t))


def length(beta, t, u):
    x, y = gamma(beta, t)
    xx, yy = gamma(beta, u)
    return math.hypot(xx-x, yy-y)


def exact_diameter(beta):
    if beta <= 1:
        return 2 * P
    a = math.acos(1 / beta)
    return 2 * (P-a+math.sqrt(beta*beta-1))


def distance_end(beta, s, u):
    return length(beta, s, 2*P-u)


def asymptotic_fixed(beta, eps):
    if beta < 1:
        return eps**2/(4*P**2*(1-beta)**2)
    if beta == 1:
        return (6**(2/3)*math.gamma(4/3)**2/math.gamma(5/3))/(2*P**2)*eps**(2/3)
    q = math.sqrt(beta*beta-1)
    a = math.acos(1/beta)
    delta = 2*P-2*a
    return eps/(P*q)*math.sqrt(exact_diameter(beta)/delta)


def approximate_tail(beta, eps, n=520):
    if beta < 1:
        center, half = 0.0, 1.09*eps/(1-beta)
    elif beta == 1:
        center, half = 0.0, 1.12*(6*eps)**(1/3)
    else:
        center = math.acos(1/beta)
        half = 3.5*math.sqrt(eps/math.sqrt(beta*beta-1))
    lo = max(0., center-half)
    hi = min(P, center+half)
    step = (hi-lo)/n
    count = 0
    target = exact_diameter(beta)-eps
    for i in range(n):
        s = lo+(i+.5)*step
        for j in range(n):
            u = lo+(j+.5)*step
            if distance_end(beta, s, u)>target:
                count += 1
    return count*step*step/(2*P*P)


def moving_max(lam):
    return 4*math.sqrt(2)/3*max(lam, 0)**1.5


def moving_area(lam, eps=None, n=540):
    # Direct comparison of the cubic limit and the *actual* trochoid distance.
    upper = 6+3*math.sqrt(abs(lam))
    step = upper/n
    cnt = 0
    for i in range(n):
        x = (i+.5)*step
        for j in range(n):
            y = (j+.5)*step
            if eps is None:
                yes = (x*x*x+y*y*y)/6-lam*(x+y)<1-moving_max(lam)
            else:
                beta = 1+lam*eps**(2/3)
                yes = distance_end(beta, eps**(1/3)*x, eps**(1/3)*y) > exact_diameter(beta)-eps
            if yes:
                cnt += 1
    return cnt*step*step/(2*P*P)


def main():
    rng = random.Random(104729)
    checks = 0
    for beta in [0.1, 0.5, 0.999, 1.0, 1.001, 1.05, 1.3, 2, 4, 10]:
        D = exact_diameter(beta)
        for _ in range(200):
            t, u = sorted((rng.random()*2*P, rng.random()*2*P))
            m=(t+u)/2
            gap=u-t
            sq = gap**2+4*beta**2*math.sin(gap/2)**2-4*beta*gap*math.sin(gap/2)*math.cos(m)
            assert abs(length(beta,t,u)**2-sq)<5e-12*(1+D**2)
            assert length(beta,t,u)<=D+5e-12
            checks+=2
        if beta<=1:
            assert abs(length(beta,0,2*P)-D)<1e-12
        else:
            a=math.acos(1/beta)
            assert abs(length(beta,a,2*P-a)-D)<1e-12
        checks+=1
    # A finite mesh tests rare-event constants, with a deliberately loose finite-size tolerance.
    for beta, eps, tol in [(0.5,.008,.06), (1,.0005,.03), (2,.001,.03)]:
        approx=approximate_tail(beta,eps)
        pred=asymptotic_fixed(beta,eps)
        assert abs(approx/pred-1)<tol, (beta,approx,pred)
        checks+=1
    for lam in [-2,-.5,0,.5,2]:
        target=moving_area(lam)
        actual=moving_area(lam,eps=1e-4)
        assert target>0
        assert abs(actual/target-1)<.08, (lam,actual,target)
        checks+=2
    print('PASS', checks, 'deterministic checks')

if __name__=='__main__':
    main()
