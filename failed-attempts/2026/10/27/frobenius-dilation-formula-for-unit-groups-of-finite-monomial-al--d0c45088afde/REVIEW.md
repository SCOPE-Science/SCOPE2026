# Independent mathematical audit

## correctness

PASS

The finite standard-monomial set is an order ideal containing 0, and the nonconstant span is the nilpotent maximal ideal J. The constant section splits the units as k^× times 1+J. An element with p^r-th power 1 must have constant term 1 since gcd(p,q−1)=1. Frobenius acts by the coefficient-field automorphism and injective dilation on exponent vectors until a monomial vanishes, so the kernel on J has N−s_r free coefficients, giving q^(N−s_r). In the cyclic decomposition each C_(p^a) contributes min(a,r) to K_r; differencing twice gives the claimed multiplicities, which vanish eventually because only 0 survives all dilations. This includes r=0 and the case R=k. An independent GF(4) multiplication replay in branches/audit-replays/moments_and_units.py checked the complete order histogram for (x^3,y^2,x^2y), giving C_3 × C_2^4 × C_4^2 as predicted.

## originality

FAIL

The distinct Resultary Frobenius-shadow record covers the entire classification on precisely this quotient class. Its counts and this record's torsion formula determine each other, not merely a common example. There is no distinct theorem left in the frozen Finding under statement-level review. This is a coverage decision; it does not establish which derivation came first or whether one relied on the other.

## value

FAIL

Extracting abstract units from standard monomials is a useful computation, but the frozen claim presents no independently new classification beyond the matching Frobenius-shadow theorem. In isolation it is a direct monomial-basis instance of Frobenius kernel counting and standard finite abelian p-group reconstruction. It supplies no separate obstruction, family, or unit-group distinction not given by that classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
