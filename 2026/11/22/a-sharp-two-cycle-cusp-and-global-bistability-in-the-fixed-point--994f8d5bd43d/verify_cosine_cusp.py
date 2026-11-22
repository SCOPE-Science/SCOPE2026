"""Finite diagnostics for an exact cosine-map phase diagram.

The accompanying mathematical proof, not numerical sampling, establishes the
universal cycle counts and the long-time asymptotic law.
"""
from fractions import Fraction as Q
from math import cos, sin, tan, pi, sqrt


def check_exact_sign_bounds():
    # Certified elementary inequalities 3 < pi < 22/7 and
    # 1-t^2/2 <= cos(t) <= 1-t^2/2+t^4/24 for t in [0, pi/2].
    lower_cos_pi_over_ten = 1-Q(11,35)**2/2
    lower_angle = Q(49,100)*3*lower_cos_pi_over_ten
    assert lower_angle > Q(139,100)
    theta = Q(139,100)
    cos_upper = 1-theta**2/2+theta**4/24
    assert Q(49,100)*cos_upper < Q(1,10)
    upper_angle = Q(77,100)
    assert Q(49,100)*(1-upper_angle**2/2) > Q(1,3)


def bisect(fun, lo, hi, count=90):
    fl, fr = fun(lo), fun(hi)
    assert fl * fr < 0, (lo, hi, fl, fr)
    for _ in range(count):
        mid = (lo+hi)/2
        fm = fun(mid)
        if fm*fl <= 0: hi=mid; fr=fm
        else: lo=mid; fl=fm
    return (lo+hi)/2


def test():
    check_exact_sign_bounds()
    a,b,c = Q(51,100), Q(1,2), Q(49,100)
    a,b,c = float(a),float(b),float(c)
    A=pi/2; q=(1-a)/(1-b); r=c/b; p=A*q
    C=lambda u: cos(p*cos(A*u))
    Cp=lambda u: A*p*sin(A*u)*sin(p*cos(A*u))
    G=lambda u: r*C(u)
    fun=lambda u:G(u)-u
    # Full original map and one complete left-to-right-to-left return.
    F=lambda x: 1-(1-a)*cos(pi*x/(2*b)) if x<=b else c*cos(pi*(x-1)/(2*(1-b)))
    for j in range(201):
        u=j/200
        assert abs(F(F(b*u))/b-G(u))<3e-14
    roots=[bisect(fun,*bounds) for bounds in [(0,.2),(.2,2/3),(2/3,1)]]
    multipliers=[r*Cp(u) for u in roots]
    assert 0<multipliers[0]<1<multipliers[1]
    assert 0<multipliers[2]<1
    for u in [i/1000 for i in range(1001) if abs(i/1000-roots[1])>0.001]:
        z=u
        for _ in range(350):z=G(z)
        target=roots[0] if u<roots[1] else roots[2]
        assert abs(z-target)<2e-10
    s_star=bisect(lambda s:s*tan(s)-1,0.5,1.2)
    q_star=1/(A*sin(s_star));u_star=s_star/A
    h=lambda u:q_star*cos(A*u)
    assert abs(h(u_star)-u_star)<2e-14
    assert abs(-q_star*A*sin(A*u_star)+1)<2e-14
    K=A*A*(1/3+s_star*s_star/2)
    for d in [0.005,-0.005,0.001,-0.001]:
        cubic=(h(h(u_star+d))-(u_star+d))/(d**3)
        assert abs(cubic+K)<0.03
    for u0 in [0.1,0.95]:
        u=u0
        for _ in range(100000):u=h(h(u))
        observed=sqrt(100000)*(u-u_star)
        target=(1 if u0>u_star else -1)/sqrt(2*K)
        assert abs(observed-target)<0.03, (observed,target)
    print('PASS: exact rational bounds, 3 two-cycles, multiplier signs, global basin samples, cusp cubic and critical clock')
    print('benchmark left u and multipliers:',[(round(u,11),round(z,8)) for u,z in zip(roots,multipliers)])
    print('critical q, u, K:',q_star,u_star,K)

if __name__ == '__main__':test()
