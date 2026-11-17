"""Reproduce exact algebraic identities and diagnostic blow-up profiles for the group-defence population flow.

All infinite-time conclusions require the accompanying mathematical proof;
finite integrations below are diagnostics only.
"""
from fractions import Fraction as Q
from math import exp
from scipy.integrate import solve_ivp


def ratio_g_over_q(x, M, C, D, E, A, p):
    g = D - E/(x+A)
    q = M*x/(x**p+C)
    return g/q


def verify_exact_parameter_cases():
    checks = 0
    for p in (1,2,3):
        for i in range(1,11):
            R=Q(i+1,4);K=Q(i+3,2);M=Q(i+2,3)
            C=Q(i+1,5);D=Q(i+4,3);A=Q(i+1,2)
            x=Q(i+2,7)
            B=max(x,K)
            q=M*x/(x**p+C)
            Ystar=2*R*(B**p+C)/M
            for state in ("critical","subcritical","supercritical"):
                E=D*A*({"critical": Q(1),"subcritical":Q(3,2),"supercritical":Q(1,2)}[state])
                g=D-E/(x+A)
                gp=max(g,Q(0))
                # H'(x,y) with h'=2g_+/q, y=Ystar+1.
                y=Ystar+1
                dx=R*x*(1-x/K)-q*y
                dH=g*y+2*gp*dx/q
                assert dx <= -q*y/2
                assert dH <= 0
                if state == 'critical':
                    assert ratio_g_over_q(x,M,C,D,E,A,p) == D*(x**p+C)/(M*(x+A))
                if state == 'supercritical':
                    assert g >= D-E/A > 0
                checks += 1
    return checks


def integrate_from_reciprocal_predator(M, end_u=32):
    # The inverse predator density z=e^{-u} is the independent scale;
    # this avoids direct integration near the Riccati singularity.
    R=K=A=C=D=1.0;E=0.5;p=2
    g0=D-E/A
    nu=M/(C*g0)
    x0=0.3
    def rhs(u,v):
        x,t=v;z=exp(-u)
        g=D-E/(x+A)
        dx=z*R*x*(1-x/K)/g-M*x/(g*(x**p+C))
        dt=z/g
        return dx,dt
    sol=solve_ivp(rhs,(0,end_u),(x0,0.0),method='DOP853',rtol=1e-12,atol=[1e-30,1e-14],dense_output=True)
    assert sol.success
    vals=[]
    for u in ((18,24,30) if nu<1 else (16,20,24) if nu==1 else (10,14,18)):
        x,t=sol.sol(u);z=exp(-u)
        scaled=x/z**nu
        # Physical-time derivative, y=1/z
        xd=R*x*(1-x/K)-M*x/((x**p+C)*z)
        vals.append((u,scaled,xd,t))
    a,b,c=[v[1] for v in vals]
    assert abs(c-b)/max(abs(c),1e-20)<0.001
    assert abs(b-a)/max(abs(b),1e-20)<0.01
    if nu<1:
        assert abs(vals[2][2])>abs(vals[1][2])*1.2
    if nu==1:
        assert abs(vals[2][2]/vals[1][2]-1)<0.01
    if nu>1:
        assert abs(vals[2][2])<abs(vals[1][2])/1.2
    return nu, vals

if __name__=='__main__':
    print('Exact-rational Lyapunov and coefficient cases:',verify_exact_parameter_cases())
    for M in (0.25,0.5,1.0):
        print('regime and profile:',integrate_from_reciprocal_predator(M))
    print('PASS: identities and finite diagnostics')
