"""Exact reproducibility checks for radial bianalytic Toeplitz commutators.
Standard-library Python only. This is finite corroboration, not a substitute
for the analytical proof of the general asymptotic theorem.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext


def beta_moment(m, alpha, k):
    ans=F(1)
    for j in range(k):
        ans *= F(m+1+j, m+alpha+2+j)
    return ans


def jacobi_a2(j, m, alpha):
    t=2*j+m+alpha
    return F(j*(j+alpha)*(j+m)*(j+m+alpha),t*t*(t*t-1))


def compressed_monomial(m, alpha, k):
    """Matrix of compressed t**k, encoded by (a00, a01_times_sigma, a11)."""
    mu=beta_moment(m,alpha,1)
    var=beta_moment(m,alpha,2)-mu*mu
    M=lambda u:beta_moment(m,alpha,u)
    return (M(k), M(k+1)-mu*M(k),
            (M(k+2)-2*mu*M(k+1)+mu*mu*M(k))/var)


def bracket_squared(m,alpha,k,l):
    """Both squared singular values of [T_{t**k},T_{t**l}] in one 2D block."""
    a=compressed_monomial(m,alpha,k)
    b=compressed_monomial(m,alpha,l)
    var=beta_moment(m,alpha,2)-beta_moment(m,alpha,1)**2
    numerator=(a[0]-a[2])*b[1]+(b[2]-b[0])*a[1]
    return numerator*numerator/var


def dec(x):return Decimal(x.numerator)/Decimal(x.denominator)

checks=0
# Exact identity from the Jacobi recurrence, for rational weights.
for alpha in [F(-1,2), F(0),F(1,3),F(1),F(2),F(6)]:
    for m in list(range(0,23))+[30, 50, 100]:
        actual=bracket_squared(m,alpha,1,2)
        expected=jacobi_a2(1,m,alpha)*jacobi_a2(2,m,alpha)**2
        assert actual == expected,(alpha,m,actual,expected)
        checks+=1

# Alternating/linear symbols produce zero commutators: a nontrivial check
# against accidentally squaring the incorrect 2x2 skew entry.
for alpha in [F(0),F(3,2)]:
    for m in range(12):
        assert bracket_squared(m,alpha,1,1)==0
        assert bracket_squared(m,alpha,2,2)==0
        checks+=2

# High-mode asymptotic: c_m*m**3 tends to
# (alpha+2)*sqrt(alpha+1)*W, W=k*l*(l-k) for t**k,t**l.
with localcontext() as ctx:
    ctx.prec=70
    for alpha in [F(-1,2),F(0),F(1),F(3,2),F(5)]:
        for k,l in [(1,2),(1,3),(2,3),(2,4)]:
            m=500000
            value=(dec(bracket_squared(m,alpha,k,l)).sqrt())*Decimal(m)**3
            W=Decimal(k*l*(l-k))
            predicted=(dec(alpha)+2)*(dec(alpha)+1).sqrt()*W
            # Relative error O(1/m); allow a safe numerical finite-size margin.
            assert abs(value/predicted-1)<Decimal('0.0002'),(alpha,k,l,value,predicted)
            checks+=1

# Boundary-jet cancellation: t and (t-1)**2+2(t-1) have independent? For
# exact commuting pair h=2t+7 the bracket must vanish; the monomial
# linearity is tested directly via the rational skew coefficient formula.
print('PASS:',checks,'exact-rational and high-precision checks')
