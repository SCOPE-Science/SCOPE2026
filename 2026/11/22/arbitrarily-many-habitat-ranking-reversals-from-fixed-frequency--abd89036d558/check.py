"""Independent arithmetic checks for a two-habitat Markov-modulated movement theorem.

Requires Python 3 and sympy. The theorem's all-parameter assertion follows
from the proof in RESULT.md; these finite tests are supplementary only.
"""
from fractions import Fraction
import random
import sympy as S

s=S.symbols('s', positive=True)
checks=0

def chk(condition, message):
    global checks
    checks += 1
    if not bool(condition):
        raise AssertionError(message)

def stationary_probability(r, b, strength):
    """Exact stationary mass of habitat A for complete-graph switching."""
    m=len(r)
    Q=S.ones(m,m)-m*S.eye(m)
    # Behavior i moves A->B at r_i/2-b_i, B->A at r_i/2+b_i.
    rates_u=[r[i]/2-b[i] for i in range(m)]
    rates_v=[r[i]/2+b[i] for i in range(m)]
    chk(all(z>0 for z in rates_u+rates_v),'strictly positive movements')
    T=S.diag(*r)-strength*Q.T
    x=T.inv()*S.Matrix([rates_v[i]/m for i in range(m)])
    return S.factor(sum(x))

# Hand-checkable sharp three-mode instance.
r=[S.Integer(1), S.Integer(2), S.Integer(4)]
b=[S.Rational(13,32),-S.Rational(105,128),S.Rational(7,16)]
formula=S.Rational(1,2)+9*(s-1)*(s-4)/(128*(21*s*s+28*s+8))
for strength in [S.Rational(1,10), S.Rational(1,2),S.Integer(1),
                 S.Rational(3,2),S.Integer(2),S.Integer(3),
                 S.Integer(4),S.Integer(5),S.Integer(10),S.Integer(100)]:
    chk(S.simplify(stationary_probability(r,b,strength)-formula.subs(s,strength))==0,
        'exact 6-state equilibrium check')
for strength,expect in [(S.Rational(1,2),1),(S.Integer(2),-1),(S.Integer(5),1)]:
    value=S.sign(formula.subs(s,strength)-S.Rational(1,2))
    chk(value==expect,'three phases')
chk(S.factor(formula-S.Rational(1,2)).as_numer_denom()[0].subs(s,1)==0,'root one')
chk(S.factor(formula-S.Rational(1,2)).as_numer_denom()[0].subs(s,4)==0,'root four')
chk(sum([b[i]/r[i] for i in range(3)])/3==S.Rational(9,256),'slow switching limit')
chk(sum(b)/sum(r)==S.Rational(3,896),'fast switching limit')

# Arbitrary specified positive crossover points: verify interpolation identity,
# strict positive rates, and sign at all prescribed roots for m=2..8.
for m in range(2,9):
    r=[S.Integer(i) for i in range(1,m+1)]
    t=[S.Rational(2*j+1,j+2) for j in range(1,m)]
    chk(len(set(t))==m-1,'distinct root design')
    P=S.prod(s-tj for tj in t)
    base=[S.factor(P.subs(s,-ri/m)/S.prod(r[k]-ri for k in range(m) if k!=i))
          for i,ri in enumerate(r)]
    # Choose an exact scaling ensuring all directional movement rates positive.
    eps=min(S.Rational(1,1),*[ri/(4*abs(z)) for ri,z in zip(r,base) if z!=0])
    b=[eps*z for z in base]
    chk(all(abs(bi)<ri/2 for bi,ri in zip(b,r)),'positive directional rates')
    N=S.factor(sum(b[i]*S.prod(r[k]+m*s for k in range(m) if k!=i)
                   for i in range(m)))
    chk(S.expand(N-eps*P)==0,'polynomial interpolation')
    for tj in t:
        chk(N.subs(s,tj)==0,'exact prescribed crossover')

# Generic irreducible Markov behavior generator: check adjugate degree bound.
rng=random.Random(18407)
for m in range(2,6):
    for trial in range(5):
        Q=S.zeros(m)
        for i in range(m):
            for j in range(m):
                if i!=j:
                    Q[i,j]=rng.randint(1,6)
            Q[i,i]=-sum(Q[i,j] for j in range(m) if j!=i)
        rv=[S.Integer(rng.randint(1,9)) for i in range(m)]
        M=S.diag(*rv)-s*Q.T
        den=S.Poly(M.det(),s)
        chk(den.degree()<=m-1,'denominator degree at most m-1')
        # Numerator from Cramer's rule for a generic fixed input vector.
        w=S.Matrix([S.Integer(rng.randint(-3,3)) for i in range(m)])
        # Cramer's numerator equals sum of determinants with replaced columns.
        numer=S.Integer(0)
        for j in range(m):
            X=M.copy()
            X[:,j]=w
            numer += X.det()
        poly=S.Poly(S.expand(numer),s)
        chk(poly.degree()<=m-1,'numerator degree at most m-1')
print('PASS:',checks,'supplementary exact-arithmetic assertions')
