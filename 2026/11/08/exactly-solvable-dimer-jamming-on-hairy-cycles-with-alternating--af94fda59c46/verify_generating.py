"""Independent exact-series verification for dimer jamming on a cycle with one leaf at every core vertex."""
from fractions import Fraction
from math import factorial

# Series coefficients of N(z) = (1-z)^2 F(z), computed from the standalone
# differential equation, not from the closed expected-coverage recurrence.
a = [Fraction(0), Fraction(1), Fraction(-1,3)]
for k in range(3, 130):
    a.append(a[-1] * Fraction(-2, 2*k-1))

def f_via_series(m):
    return sum(((m-k+1)*a[k] for k in range(1,m+1)), Fraction(0))

def f_via_first_edge(m):
    f = [Fraction(0)]
    for j in range(1,m+1):
        f.append(1 + Fraction(4*sum(f[:j-1])+2*f[-1], 2*j-1))
    return f[m]

for m in range(0, 110):
    assert f_via_series(m) == f_via_first_edge(m), m

# S_n = 1 + (F_{n-1} + F_{n-2})/2 is an exact rational number.
# Define rho via convergent sum N(1)=sum a[k] and show the exact
# error interval by alternation of decreasing terms, without floating-point.
for n in range(3, 95):
    sun = 1 + (f_via_series(n-1) + f_via_series(n-2))/2
    # Truncated series for the difference S_n-n*rho; bound remaining
    # using alternating-series theorem. The k=n leading term has weight 1/2.
    tail = [(Fraction(2*k-2*n+1, 2)*a[k]) for k in range(n, 130)]
    assert all(abs(tail[j+1]) < abs(tail[j]) for j in range(len(tail)-1))
    # Sum with enough terms to bound sign exactly, using sum of first 2/3 terms.
    assert 0 < (-1)**(n-1)*sum(tail[:3]) < abs(tail[0])
    # Finite partial sums of N(1), N'(1) yield an exact identity;
    # the infinite derivative identity N'(1)=1-N(1)/2 removes offset.
    approx_rho = sum(a[1:130], Fraction(0))
    approx_derivative = sum((k*a[k] for k in range(1,130)),Fraction(0))
    truncated_tail = sum((Fraction(2*k-2*n+1, 2)*a[k] for k in range(n,130)), Fraction(0))
    assert sun-n*approx_rho == 1-approx_rho/2-approx_derivative+truncated_tail

# ODE coefficient recurrence: for N(z)=sum a[k] z^k,
# N'(z) = z/2 + ... is checked directly via z-series ODE for F.
for m in range(1,125):
    lhs=(2*m-1)*f_via_series(m)
    rhs=2*m-1+4*sum((f_via_series(j) for j in range(m-1)),Fraction(0))+2*f_via_series(m-1)
    assert lhs==rhs

print('PASS exact generating-function coefficients through degree 125, 110 recurrence comparisons, 92 strict alternating finite-size checks')
try:
    import mpmath as mp
    mp.mp.dps=65
    rho=mp.mpf('0.5')+ mp.sqrt(mp.pi)*mp.exp(-1)*mp.erfi(1)/4
    assert abs(rho-mp.mpf('0.7690397534563842095680')) < mp.mpf('2e-22')
    print('rho =',mp.nstr(rho,50))
except ImportError:
    print('mpmath unavailable: exact rational tests unaffected')
