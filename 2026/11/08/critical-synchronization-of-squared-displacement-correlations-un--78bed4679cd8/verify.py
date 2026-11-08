"""Exact symbolic verification for independent-coordinate resetting with a common fluctuating diffusivity.

Requires Python 3 and SymPy. No simulation or floating-point inference is used.
"""
import sympy as sp

alpha, beta, lam, tau = sp.symbols('alpha beta Lambda tau', positive=True)
x, y, omega = sp.symbols('x y omega', real=True)

def generator(p):
    return sp.expand(
        lam**2 * sp.diff(p, omega, 2)
        + omega**2 * (sp.diff(p, x, 2) + sp.diff(p, y, 2))
        + alpha*(p.subs(x, 0) - p)
        + alpha*(p.subs(y, 0) - p)
        + beta*(p.subs(omega, 0) - p)
    )

# Stationary moment closure, independently generated from the polynomial generator.
labels = [sp.Integer(1), omega**2, omega**4, x**2, x**2*omega**2,
          x**4, x**2*y**2]
unknowns = sp.symbols('m0 m1 m2 m3 m4 m5 m6')
formal = dict(zip(labels, unknowns))

def expectation(poly):
    poly = sp.Poly(sp.expand(poly), x, y, omega)
    result = 0
    for (px,py,pw), coefficient in poly.terms():
        mon = x**px * y**py * omega**pw
        if mon not in formal:
            # Exchangeability gives E[y^2 omega^2] = E[x^2 omega^2].
            if mon == y**2*omega**2:
                mon = x**2*omega**2
            else:
                raise AssertionError('Missing moment: '+str(mon))
        result += coefficient*formal[mon]
    return sp.expand(result)

equations = [unknowns[0]-1]
for p in labels[1:]:
    equations.append(expectation(generator(p)))
sol = sp.solve(equations, unknowns, dict=True)
assert len(sol)==1
sol = sol[0]
mY=sol[unknowns[1]]
mY2=sol[unknowns[2]]
mX=sol[unknowns[3]]
mXY=sol[unknowns[4]]
mX4=sol[unknowns[5]]
mX2Y2=sol[unknowns[6]]

assert sp.simplify(mY-2*lam**2/beta)==0
assert sp.simplify(mY2-24*lam**4/beta**2)==0
assert sp.simplify(mX-4*lam**2/(alpha*beta))==0
assert sp.simplify(mXY-8*lam**4*(6*alpha+beta)/(alpha*beta**2*(alpha+beta)))==0
assert sp.simplify(mX4-96*lam**4*(6*alpha+beta)/(alpha**2*beta**2*(alpha+beta)))==0
assert sp.simplify(mX2Y2-16*lam**4*(6*alpha+beta)/(alpha**2*beta**2*(alpha+beta)))==0

var=sp.factor(mX4-mX**2)
cross=sp.factor(mX2Y2-mX**2)
mixed=sp.factor(mXY-mX*mY)
K=80*lam**4/(alpha**2*beta**2*(alpha+beta))
assert sp.simplify(var-K*(7*alpha+beta))==0
assert sp.simplify(cross-K*alpha)==0
assert sp.simplify(2*mixed-K*alpha**2)==0

# Conditional moment semigroup: L(x^2-mX)=-alpha(x^2-mX)+2(omega^2-mY),
# L(omega^2-mY)=-beta(omega^2-mY).
assert sp.simplify(generator(x**2)-(-alpha*x**2+2*omega**2))==0
assert sp.simplify(generator(omega**2)-(-beta*omega**2+2*lam**2))==0
H=(sp.exp((alpha-beta)*tau)-1)/(alpha-beta)
Cauto=sp.simplify(sp.exp(-alpha*tau)*(var+2*mixed*H))
Ccross=sp.simplify(sp.exp(-alpha*tau)*(cross+2*mixed*H))
assert sp.simplify(Cauto-K*sp.exp(-alpha*tau)*(7*alpha+beta+alpha**2*H))==0
assert sp.simplify(Ccross-K*sp.exp(-alpha*tau)*(alpha+alpha**2*H))==0
R=(alpha+alpha**2*H)/(7*alpha+beta+alpha**2*H)
assert sp.simplify(R-Ccross/Cauto)==0
u=sp.symbols('u', nonnegative=True)
assert sp.simplify(sp.diff((alpha+alpha**2*u)/(7*alpha+beta+alpha**2*u),u)-alpha**2*(6*alpha+beta)/(7*alpha+beta+alpha**2*u)**2)==0
Rcritical=sp.simplify(sp.limit(R,beta,alpha))
assert sp.simplify(Rcritical-(1+alpha*tau)/(8+alpha*tau))==0
Rsmall=sp.factor(sp.limit(R.subs(beta,2*alpha),tau,sp.oo))
Rlarge=sp.factor(sp.limit(R.subs(alpha,2*beta),tau,sp.oo))
assert Rsmall==sp.Rational(1,5)
assert Rlarge==1
Rinfty=alpha*beta/(beta**2+6*alpha*beta-6*alpha**2)
assert sp.simplify(R.subs({alpha:sp.Integer(1),beta:sp.Integer(2)})-Rinfty.subs({alpha:sp.Integer(1),beta:sp.Integer(2)})).limit(tau,sp.oo)==0

# Exact all-d radial average fluctuation formula.
d=sp.symbols('d',integer=True,positive=True)
normalized_relative=sp.factor((var+(d-1)*cross)/(d*mX**2))
assert sp.simplify(normalized_relative-5*alpha/(alpha+beta)-5*(6*alpha+beta)/(d*(alpha+beta)))==0

print('PASS: generator closure, six stationary moments, two lag covariances,')
print('      critical and off-critical limits, monotonicity and dimensional law')
print('Critical ratio:',Rcritical)
print('High-dimensional relative variance:',sp.limit(normalized_relative,d,sp.oo))
