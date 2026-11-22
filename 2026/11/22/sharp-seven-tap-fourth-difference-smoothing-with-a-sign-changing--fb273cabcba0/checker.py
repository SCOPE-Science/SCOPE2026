"""Exact rational enclosure for seven-tap fourth-difference minimax theorem.

Requires standard-library Python 3.10+. Run `python checker.py`.
All inequality tests use Fraction; decimal output is presentation only.
"""
from decimal import Decimal, getcontext
from fractions import Fraction as F

getcontext().prec = 45

# Rational approximations are *not* asserted to be exact solutions.
r, t, s = (F(v) for v in (
    '0.232153505742839771',
    '0.599390549762174356',
    '0.889568489524926657',
))
a, b, c = (F(v) for v in (
    '-4.733331041291834190',
    '6.952079757871099737',
    '-3.231435284320775249',
))
xs = [r, t, s, F(1)]
eps = [F(1), F(-1), F(1), F(-1)]
assert 0 < r < t < s < 1


def q(y):
    return y*y + a*y**3 + b*y**4 + c*y**5


def derivative(y):
    return 2*y + 3*a*y*y + 4*b*y**3 + 5*c*y**4


def cubic(y):
    return 2 + 3*a*y + 4*b*y*y + 5*c*y**3


# Dual inequality for all y² + A y³ + B y⁴ + C y⁵.
lam = []
for i, x in enumerate(xs):
    denominator = x**3
    for j, y in enumerate(xs):
        if j != i:
            denominator *= x-y
    lam.append(F(1)/denominator)
assert all((lam[i] < 0) if i % 2 == 0 else (lam[i] > 0) for i in range(4))
assert all(sum(w*x**p for w, x in zip(lam, xs)) == 0 for p in (3,4,5))
assert sum(w*x*x for w,x in zip(lam,xs)) == -F(1)/(r*t*s)
mu = [abs(v) for v in lam]
LOWER = abs(sum(w*x*x for w,x in zip(lam,xs)))/sum(mu)

# Rigorously isolate all three positive stationary roots of the rational q.
B = F(2) + 6*abs(a) + 12*abs(b) + 20*abs(c)
UPPER = abs(q(F(1)))
root_brackets = []
for root_approx in (r,t,s):
    scale = 10**12
    lo = F((root_approx.numerator*scale)//root_approx.denominator,scale)
    hi = lo + F(1,scale)
    assert cubic(lo)*cubic(hi) < 0
    root_brackets.append((lo,hi))
    mid = (lo+hi)/2
    radius = (hi-lo)/2
    # |q''| <= B on [0,1], exact Taylor bound at unknown critical point.
    at_stationary = abs(q(mid)) + abs(derivative(mid))*radius + B*radius*radius/2
    UPPER = max(UPPER,at_stationary)
assert LOWER < UPPER
assert F(2029850838641552,10**16) < 16*UPPER < F(203,1000)
assert F(2029850838641552,10**16) < 16*LOWER

# Since the true minimizer has norm <= UPPER, four-node dual equality
# forces its coefficients to be extremely close to the rational test q.
slacks=[UPPER-e*q(x) for x,e in zip(xs,eps)]
assert all(delta>=0 for delta in slacks)
node_errors=[]
for i in range(4):
    lower_signed = -sum(mu[j]*slacks[j] for j in range(4) if j!=i)/mu[i]
    node_errors.append(max(abs(lower_signed),slacks[i]))

# Recover the coefficient differences via degree-2 Lagrange interpolation
# of (q_star-q)/y³, at the first three rational nodes.
coef_errors=[F(0)]*3
for i,x in enumerate(xs[:3]):
    others=[xx for j,xx in enumerate(xs[:3]) if j!=i]
    den=(x-others[0])*(x-others[1])
    basis=[others[0]*others[1]/den,-(others[0]+others[1])/den,F(1)/den]
    for j in range(3):
        coef_errors[j]+=abs(basis[j])*node_errors[i]/x**3
assert max(coef_errors)<F(1,10**12)

# Fourier coefficients for P(cos theta)=1+a*y+b*y²+c*y³,
# y=(1-cos theta)/2, and P=sum u(j)e^(ij theta).
u0=F(1)+a/2+3*b/8+5*c/16
u1=-a/4-b/4-15*c/64
u2=b/16+3*c/32
u3=-c/64
u=[u0,u1,u2,u3]
u_err=[coef_errors[0]/2+3*coef_errors[1]/8+5*coef_errors[2]/16,
       coef_errors[0]/4+coef_errors[1]/4+15*coef_errors[2]/64,
       coef_errors[1]/16+3*coef_errors[2]/32,
       coef_errors[2]/64]
assert all(ui>err for ui,err in zip(u,u_err))
assert u0+2*(u1+u2+u3)==1

# P_star(t)<0, although u_star(j)>0 at every tap, so positive-kernel
# and positive-Fourier restrictions have genuinely different optima.
P_t=F(1)+a*t+b*t*t+c*t**3
P_t_err=coef_errors[0]*t+coef_errors[1]*t*t+coef_errors[2]*t**3
assert P_t+P_t_err<0

# In the strictly Fourier-nonnegative class Theorem 1.4 of
# Gaitan--Garzon--Madrid gives 64/25 tan²(pi/10)
# = 64/25 (1-2/sqrt(5)) > 1/4. Prove the inequality rationally:
# 1-2/sqrt(5)>25/256 iff 4/5 < (231/256)^2.
assert F(4,5) < F(231,256)**2
assert 16*UPPER < F(1,4)

print('EXACT RATIONAL CERTIFICATE: PASS')
print('C in (', Decimal((16*LOWER).numerator)/Decimal((16*LOWER).denominator), ',',
      Decimal((16*UPPER).numerator)/Decimal((16*UPPER).denominator), ')')
print('All optimal seven-tap coefficients u(0),u(1),u(2),u(3) are strictly positive.')
print('The unique optimal Fourier symbol is negative at an interior angle.')
print('All computations use exact rational arithmetic; uniqueness/existence is analytic.')
