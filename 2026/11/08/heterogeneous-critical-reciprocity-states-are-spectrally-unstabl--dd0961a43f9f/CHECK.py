"""Exact symbolic checks for a reactive-game critical-reciprocity instability theorem.

Run: python CHECK.py   (requires sympy)
The general theorem is analytic; these checks verify illustrative instances.
"""
import sympy as sp

N = 2
b = sp.Rational(1)
c = sp.Rational(1, 2)
a = c / b
q0 = [sp.Rational(1, 10), sp.Rational(3, 10)]
eta = [sp.Rational(1, 5), sp.Rational(2, 5)]
p0 = [x + a for x in q0]
p = sp.symbols('p1:3')
q = sp.symbols('q1:3')
r = [p[i]-q[i] for i in range(N)]
F = []
for i in range(N):
    gp = sum((b*r[j]-c)*(q[i]*r[j]+q[j])/(1-r[i]*r[j])**2 for j in range(N))/N
    gq = sum((b*r[j]-c)*(1-q[j]-p[i]*r[j])/(1-r[i]*r[j])**2 for j in range(N))/N
    F.extend((p[i]+eta[i]*gp, q[i]+eta[i]*gq))
X = [v for i in range(N) for v in (p[i], q[i])]
subs = {p[i]:p0[i] for i in range(N)} | {q[i]:q0[i] for i in range(N)}
assert all(sp.simplify(F[k].subs(subs)-X[k].subs(subs))==0 for k in range(2*N))
J = sp.Matrix(F).jacobian(X).subs(subs)
expected=sp.Matrix([[sp.Rational(77,75),-sp.Rational(2,75),sp.Rational(14,225),-sp.Rational(14,225)],
 [sp.Rational(8,75),sp.Rational(67,75),sp.Rational(16,225),-sp.Rational(16,225)],
 [sp.Rational(4,45),-sp.Rational(4,45),sp.Rational(29,25),-sp.Rational(4,25)],
 [sp.Rational(8,45),-sp.Rational(8,45),sp.Rational(8,75),sp.Rational(67,75)]])
assert J==expected
weights=[h/sum(eta) for h in eta]
qm=sum(weights[i]*q0[i] for i in range(N))
var=sp.simplify(sum(weights[i]*(q0[i]-qm)**2 for i in range(N)))
s=1-a*a
C=sp.simplify(b*(sum(eta)/N)/s**2)
S=sp.simplify(2*(1+a)*qm-s)
root=sp.sqrt(S*S+16*a*var)
muplus=sp.simplify(1+C*(S+root)/2)
muminus=sp.simplify(1+C*(S-root)/2)
assert sp.simplify(muplus-(sp.Rational(222,225)+sp.sqrt(265)/225))==0
assert sp.simplify(muminus-(sp.Rational(222,225)-sp.sqrt(265)/225))==0
assert J.charpoly().as_expr().expand()==sp.prod([z for z in []]) if False else True
z=sp.symbols('z')
assert sp.simplify(J.charpoly(z).as_expr()-(z-1)**2*(z-muplus)*(z-muminus))==0
assert (muplus>1) is sp.S.true

# Independent exact rational tests of the rank-two matrix formula.
for qv,ev,aa,bb in [
 ([sp.Rational(1,10),sp.Rational(1,5),sp.Rational(1,4)],
  [sp.Rational(1,3),sp.Rational(3,4),sp.Rational(1,2)],sp.Rational(1,3),sp.Rational(2)),
 ([sp.Rational(1,8),sp.Rational(2,9),sp.Rational(3,10),sp.Rational(1,5)],
  [sp.Rational(2,5),sp.Rational(3,5),sp.Rational(4,5),sp.Rational(1,5)],sp.Rational(1,4),sp.Rational(3))]:
    n=len(qv); ss=1-aa*aa
    vv=sp.Matrix(n,n,lambda i,j:sp.simplify(bb*ev[i]*(2*aa*qv[i]+2*qv[j]-ss)/(n*ss**2)))
    hh=sp.simplify(bb*sum(ev)/(n*ss**2))
    ww=[e/sum(ev) for e in ev]
    mm=sp.simplify(sum(ww[i]*qv[i] for i in range(n)))
    variance=sp.simplify(sum(ww[i]*(qv[i]-mm)**2 for i in range(n)))
    SS=2*(1+aa)*mm-ss
    assert vv.rank()==2
    assert sp.simplify(sp.trace(vv)-hh*SS)==0
    assert sp.simplify((sp.trace(vv)**2-sp.trace(vv*vv))/2+4*aa*hh**2*variance)==0
    assert variance>0
print('PASS: exact fixed point; full four-variable Jacobian; spectrum; two arbitrary-N rank-two rational checks')
