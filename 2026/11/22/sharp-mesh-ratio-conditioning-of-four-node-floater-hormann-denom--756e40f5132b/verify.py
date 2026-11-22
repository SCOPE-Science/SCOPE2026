"""Independent exact and floating-point checks for the four-node d=1 FH denominator theorem.

Run: python verify.py. Pure Python standard library.
These finite tests supplement the analytic proof; they do not certify its universal quantifiers.
"""
from fractions import Fraction as F
from math import sqrt, isclose


def direct(a,b,c,x):
    knots=(F(0),a,a+b,a+b+c)
    terms=[F((-1)**i,1)/((x-knots[i])*(x-knots[i+1])) for i in range(3)]
    return sum(map(abs,terms))/abs(sum(terms))


def formula(a,b,c,cell,q):
    C=(a+b)*(b+c)
    if cell=='left': L=a
    elif cell=='right': L=c
    else: raise ValueError(cell)
    assert 0 < q < L
    return 1+2*q*(L-q)/(q*q+b*q+C)


def q_star(L,b,C):
    L,b,C=map(float,(L,b,C))
    # Positive root of (L+b)q^2 + 2Cq - LC = 0.
    return L*C/(sqrt(C*C+L*(L+b)*C)+C)


def envelope(mu):
    s=sqrt(2*float(mu)+4)
    return (s-1)**2/(2*s-3)


def exact_piece_checks(a,b,c):
    result=0
    for j in range(1,100):
        t=F(j,100)
        q=a*t
        assert direct(a,b,c,a-q)==formula(a,b,c,'left',q)
        q=c*t
        assert direct(a,b,c,a+b+q)==formula(a,b,c,'right',q)
        assert direct(a,b,c,a+b*t)==1
        result+=3
    return result


def numeric_optim_checks(a,b,c):
    C=(a+b)*(b+c)
    mu=max(a,b,c)/min(a,b,c)
    winners=[]
    for cell,L in [('left',a),('right',c)]:
        q=q_star(L,b,C)
        assert 0<q<float(L)
        val=float(formula(a,b,c,cell,F.from_float(q)))
        # All exact grid points bounded by analytic stationary maximum and universal envelope.
        for j in range(1,200):
            v=float(formula(a,b,c,cell,L*F(j,200)))
            assert v<=val+1e-12
            assert v<=envelope(mu)+1e-12
        winners.append(val)
    if a>c: assert winners[0]>winners[1]
    if a<c: assert winners[0]<winners[1]
    if a==c: assert isclose(winners[0],winners[1],rel_tol=1e-12)
    return 400


samples=[(F(1),F(1),F(1)),(F(100),F(1),F(1)),(F(1),F(1),F(100)),
         (F(1),F(100),F(1)),(F(5),F(2),F(3)),(F(3),F(2),F(5)),
         (F(1,7),F(1,11),F(2,3)),(F(1,31),F(1,31),F(1)),
         (F(11),F(7),F(5)),(F(10),F(10),F(1))]
checks=0
for a,b,c in samples:
    checks+=exact_piece_checks(a,b,c)
    checks+=numeric_optim_checks(a,b,c)

for mu in [F(1),F(2),F(3),F(17),F(100),F(10**5)]:
    for a,b,c in ((mu,F(1),F(1)),(F(1),F(1),mu)):
        L=max(a,c)
        C=(a+b)*(b+c)
        q=q_star(L,b,C)
        cell='left' if a>c or (a==c and b==c) else 'right'
        got=float(formula(a,b,c,cell,F.from_float(q)))
        assert isclose(got,envelope(mu),rel_tol=1e-12)
        checks+=1

for mu in [10**3,10**5,10**7]:
    assert abs(envelope(mu)/sqrt(mu)-1/sqrt(2)) < 1/sqrt(mu)
    checks+=1

# Fewer than four interpolation sites: all the d=1 window terms have common sign.
for a,b in ((F(1),F(1)),(F(1),F(11)),(F(3),F(1,9))):
    for j in range(1,100):
        for x in (a*F(j,100),a+b*F(j,100)):
            nodes=(F(0),a,a+b)
            t0=F(1)/((x-nodes[0])*(x-nodes[1]))
            t1=-F(1)/((x-nodes[1])*(x-nodes[2]))
            assert abs(t0)+abs(t1)==abs(t0+t1)
            checks+=1
print(f'PASS: {checks} exact identities / finite-grid / asymptotic checks')
