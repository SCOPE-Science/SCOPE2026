"""Standalone arithmetic checks for a logit eco-evolutionary Hopf coefficient.

Requires Python 3.11+ standard library. The infinite-dimensional scientific claim
is established analytically in RESULT.md; checks here test the exact identities
and the concrete nondegenerate parameter witness.
"""
from fractions import Fraction as F
from decimal import Decimal as D, localcontext


def exact_sign_identity(theta, s, R, T, P):
    a=s-R+P-T; b=R-s; c=-(P+s)
    x=1/(1+theta); q=a*x+c; z=1-2*x
    DD=R+T+theta*(P+s)
    assert q==-DD/(1+theta)
    C1=2+z*a/q
    C2=-2*q+z*a
    assert C1==(1+theta)*(R+T+P+s)/DD
    assert C2==((3-theta)*(R+T)+(3*theta-1)*(P+s))/(1+theta)
    assert C1>0
    if theta>=F(1,3): assert C2>0


for t in [F(1,9),F(1,4),F(1,3),F(1,2),F(4,5),F(9,10)]:
    for s,R,T,P in [(F(-1),F(2),F(1),F(40)),(F(-1),F(3),F(2),F(1)),(F(-2),F(3),F(1,2),F(4))]:
        exact_sign_identity(t,s,R,T,P)

with localcontext() as ctx:
    ctx.prec=70
    theta=D(1)/D(4)
    x=D(4)/D(5);h=D(4)/D(25);z=D(-3)/D(5)
    a=D(36);b=D(3);c=D(-39);d=D(-1)
    L=D(4).ln()
    BETA=(D(85)+D(48)*L)/D(108)
    N=(D(595)-D(204)*L)/(D(51)*(D(85)+D(48)*L))
    P=D(675)/(D(85)+D(48)*L)
    Q=a*x+c
    assert Q==-D(51)/D(5)
    assert D(0)<N<D(1) and BETA>(D(5)*L)/D(7)
    assert abs(BETA*h*P-D(1))<D('1e-65')
    assert abs((b*x+c*N+a*x*N+d)-L/BETA)<D('1e-65')
    C1=D(70)/D(17);C2=-D(6)/D(5)
    ES=D(140)*P/(D(51)*N*(D(1)-N))
    assert D(315)<ES<D(316)
    lam2=BETA*BETA*h*z
    lam3=BETA**3*h*(D(1)-D(6)*x+D(6)*x*x)
    for eps,required in [(D(100),-1),(D(400),1)]:
        A=-BETA*h*Q
        B=eps*(D(1)+theta)*N*(D(1)-N)
        Fxx=lam2*P*P
        Fxn=lam2*P*Q+BETA*h*a
        Fnn=lam2*Q*Q
        Fxxx=lam3*P**3
        Fxnn=lam3*P*Q*Q+D(2)*lam2*a*Q
        full=Fxxx+(B/A)*Fxnn+(Fxn/A)*(Fxx+(B/A)*Fnn)
        reduced=-BETA*(P*C1+B*C2)
        assert abs(full-reduced)<D('1e-58'),(full,reduced)
        ell=full/D(16)
        assert (ell>0)-(ell<0)==required
        print('epsilon=',eps,'ell=',format(ell,'.18f'))
    print('beta_H=',format(BETA,'.18f'))
    print('N_H=',format(N,'.18f'))
    print('epsilon_star=',format(ES,'.18f'))
    print('VERIFY_OK')
