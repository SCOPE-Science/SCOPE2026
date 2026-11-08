"""Exact algebraic checks for stationary moment identification in a 1D finite-tumble harmonic particle.

Requires Python 3 and SymPy. Executing this file prints the count of independently
checked algebraic and rational identities; the theorem itself is proved in RESULT.md.
"""
from fractions import Fraction
import sympy as S

checks = 0

def ensure(condition, description):
    global checks
    assert bool(condition), description
    checks += 1


a, c, s, x, y = S.symbols('a c s x y', positive=True)
mu2 = c / ((a+c)*(a+1))
mu4 = 3*c*(c+2) / ((a+c)*(a+1)*(a+3)*(a+c+2))
mu6 = 15*c*(c+2)*(c+4) / ((a+c)*(a+1)*(a+3)*(a+5)*(a+c+2)*(a+c+4))
Q = S.factor(mu4/(3*mu2))
R = S.factor(mu6/(5*mu4))
ensure(S.simplify(Q-(c+2)/((a+3)*(a+c+2)))==0, 'fourth ratio')
ensure(S.simplify(R-(c+4)/((a+5)*(a+c+4)))==0, 'sixth ratio')

# Independently assemble the three-state generator and solve stationarity
# recursively for raw conditional position moments.
for av in (S.Rational(1,4),S.Rational(3,4),S.Rational(1),S.Rational(2),S.Rational(7,3),S.Rational(5)):
    for cv in (S.Rational(1,3),S.Rational(2,3),S.Rational(3,2),S.Rational(4),S.Rational(11,2)):
        G = S.Matrix([[-av,av,0],[cv/2,-cv,cv/2],[0,av,-av]])
        p = S.Matrix([cv/(2*(av+cv)), av/(av+cv), cv/(2*(av+cv))])
        diag = S.diag(1,0,-1)
        for n in range(1,7):
            p = (n*S.eye(3)-G.T).inv()*n*diag*p
            if n in (2,4,6):
                observed=S.factor(sum(p))
                predicted={2:mu2,4:mu4,6:mu6}[n].subs({a:av,c:cv})
                ensure(S.factor(observed-predicted)==0, f'generator n={n}, a={av}, c={cv}')

cs = a*s*(a+1)/(1-s*(a+1))
qs=S.factor(Q.subs(c,cs))
rs=S.factor(R.subs(c,cs))
ensure(S.simplify(qs-(2+s*(a+1)*(a-2))/((a+3)*(a+2-2*s*(a+1))))==0,'q at fixed variance')
ensure(S.simplify(rs-(4+s*(a+1)*(a-4))/((a+5)*(a+4-4*s*(a+1))))==0,'r at fixed variance')
N=(5*s**2-3*s)*a**2+(10*s**2-12*s+2)*a+5*(1-s)**2
ensure(S.simplify(S.diff(qs,a)+2*N/((a+3)**2*(a+2-2*s*(a+1))**2))==0,'fold derivative')
A=1/s-1
ensure(S.simplify(qs.subs(a,0)-S.Rational(1,3))==0,'left limit')
ensure(S.simplify(S.limit(qs,a,A,dir='-')-s/(1+2*s))==0,'right limit')
ensure(S.simplify(N.subs(a,0)-5*(1-s)**2)==0,'derivative left sign')
ensure(S.simplify(N.subs(a,A)+(1-s)**2/s)==0,'derivative right sign')

# Verify symmetric cross-difference equations. They imply an inadmissible
# boundary value if both fourth and sixth normalized ratios agree.
qn=(5*s*s-3*s)*x*y+(5*s*s-6*s+1)*(x+y)+5*(s-1)**2
rn=(9*s*s-3*s)*x*y+(9*s*s-10*s+1)*(x+y)+9*(s-1)**2
ensure(S.simplify((qs.subs(a,x)-qs.subs(a,y))/(x-y)+2*qn/((x+3)*(y+3)*(2*s*x+2*s-x-2)*(2*s*y+2*s-y-2)))==0,'q cross difference')
ensure(S.simplify((rs.subs(a,x)-rs.subs(a,y))/(x-y)+4*rn/((x+5)*(y+5)*(4*s*x+4*s-x-4)*(4*s*y+4*s-y-4)))==0,'r cross difference')
U,V=S.symbols('U V')
sol=S.solve([qn.subs({x*y:U,x+y:V}),rn.subs({x*y:U,x+y:V})],[U,V])
# SymPy cannot substitute product+sum simultaneously in all forms reliably;
# reconstruct the linear equations in these symmetric variables explicitly.
Eq1=(5*s*s-3*s)*U+(5*s*s-6*s+1)*V+5*(s-1)**2
Eq2=(9*s*s-3*s)*U+(9*s*s-10*s+1)*V+9*(s-1)**2
sol=S.solve([Eq1,Eq2],(U,V))
ensure(S.simplify(sol[U]-A**2/2)==0,'product of hypothetical two rates')
ensure(S.simplify(sol[V]-3*A/2)==0,'sum of hypothetical two rates')
ensure(S.factor(S.Symbol('z')**2-sol[V]*S.Symbol('z')+sol[U]- (S.Symbol('z')-A)*(S.Symbol('z')-A/2))==0,'roots include excluded boundary')

# Exact finite-rate double point: variance and fourth moment agree while
# sixth moments disagree.
sample=[(S.Rational(3,4),S.Rational(21,4)),(S.Rational(11,15),S.Rational(143,30))]
vals=[tuple(S.factor(f.subs({a:av,c:cv})) for f in (mu2,mu4,mu6)) for av,cv in sample]
ensure(vals[0][0]==vals[1][0]==S.Rational(1,2),'witness second moments')
ensure(vals[0][1]==vals[1][1]==S.Rational(29,80),'witness fourth moments')
ensure(vals[0][2]==S.Rational(1073,3680),'witness sixth moment first')
ensure(vals[1][2]==S.Rational(7627,26144),'witness sixth moment second')
ensure(vals[0][2]!=vals[1][2],'sixth moment disambiguates')

# Confirm a unique stationary fold numerically at multiple arbitrary variances;
# this is diagnostic only, not the infinite-parametric proof.
for sv in (S.Rational(1,50),S.Rational(1,5),S.Rational(1,2),S.Rational(9,10)):
    upper=float(A.subs(s,sv))
    roots=S.nroots(N.subs(s,sv))
    valid=[float(S.re(z)) for z in roots if abs(float(S.im(z)))<1e-12 and 0<float(S.re(z))<upper]
    ensure(len(valid)==1,f'fold count s={sv}')
    z=valid[0]
    ensure(float(qs.subs({s:sv,a:z})) < float(qs.subs({s:sv,a:upper*0.999999})), 'fold strict min')

print(f'{checks} exact/rational/numeric diagnostics passed')
print('fold witness (m2,m4,m6):', vals)
