# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified structural ledger for the southeast-polar quarter-plane walk S3

## Model
S3 = {(-1,-1), (0,1), (1,0), (1,-1)} (SW, N, E, SE), walks confined to x >= 0, y >= 0
starting at (0,0). Drift vector (1,-1): southeast polar, nonsingular.
Step polynomial: S(x,y) = 1/(xy) + y + x + x/y.
Kernel: K(x,y;t) = xy - t(1 + x y^2 + x^2 y + x^2).

## Certified results
**Theorem 1 (infinite group word).** Let Phi(x,y) = (1/(x(y+1)), y) and
Psi(x,y) = (x, (x^2+1)/(xy)), and Theta = Psi o Phi. Then Theta has infinite order,
hence G(S3) is infinite.
**Theorem 2 (genus one).** For every t in (0,1/4) the kernel curve K=0 is smooth of
genus one (both x- and y-discriminants have distinct roots).
**Theorem 3 (exact growth bounds).** Excursion exponential rate rho_exc < 3.61 and
total-walk rate rho_tot < 3.8285, by exact rational evaluation.

## Proof of Theorem 1
Phi, Psi are involutions: 1/((1/(x(y+1)))(y+1)) = x and
(x^2+1)/(x((x^2+1)/(xy))) = y identically. A fixed point of Theta satisfies
x^2(y+1) = 1 and y^2 = (x^2+1)/x, whence with y = (1-x^2)/x^2, x is a positive root of
f(x) = x^5 - x^4 + x^3 + 2x^2 - 1.
f(0.634) = -0.000382... < 0 < 0.003152... = f(0.635), so a root x0 in (0.634, 0.635)
exists. f'(x) = x(5x^3-4x^2+3x+4); the cubic factor has derivative 15x^2-8x+3 with
discriminant 64-180 = -116 < 0, hence is strictly increasing with value 4 at 0, so
f' > 0 on (0,inf) and the root is unique. The Jacobian of Theta at (x0,y0) is
J = [[-1, -X/(y0+1)], [(dX/dx)(1-1/X^2)/y0, (dX/dy)(1-1/X^2)/y0 - Y/y0]]
with X = x0; substituting the fixed-point relations gives det J = 1 and
tr J = x0^3 - 2 (both verified as rational-function identities: tr-(x^3-2) and det-1
have numerators divisible by f, checked symbolically). Hence tr in
(0.634^3-2, 0.635^3-2) subset (-1.7452,-1.7439) strictly inside (-2,2):
eigenvalues are non-real complex conjugates of modulus 1 (det = 1). So Theta is
conjugate to an irrational or rational rotation; finite order k forces tr = 2cos(2pi j/k)
with [Q(tr):Q] = phi(m)/2 for m the order. Resultant Res_z(f(z), w-(z^3-2)) equals
T(w) = w^5+18w^4+120w^3+367w^2+527w+289 (verified: T(x^3-2) reduced mod f gives zero
remainder). T is irreducible over Q: mod 5 it has no linear factor (5 evaluations) and
is not divisible by any of the 10 irreducible monic quadratics over F5 (trial division),
and degree 5 leaves no other factorisation type. Thus [Q(tau):Q] = 5, so phi(m)/2 = 5,
i.e. m in {11, 22}, whose trace minimal polynomial is
M11(w) = w^5+w^4-4w^3-3w^2+3w+1. But Res(T,M11) = 3056498369 != 0 (exact Sylvester
determinant over Q), so tau is not 2cos(2pi/11) or 2cos(pi/11)-type; no finite m works.
Hence Theta has infinite order. Replay: verify_group.py (GROUP_WORD_OK),
verify_tracepoly.py (TRACEPOLY_OK).

## Proof of Theorem 2
As polynomial in y, K has coefficients a2 = -tx, a1 = x-tx^2, a0 = -tx^2-t, so
D(x) = a1^2-4a2a0 = t^2x^4+(-4t^2-2t)x^3+x^2-4t^2x = xC(x) with
C(x) = t^2x^3+(-4t^2-2t)x^2+x-4t^2. For cubic ax^3+bx^2+cx+d the discriminant formula
gives disc(C) = -16t^3h(t) with h(t) = 91t^5+96t^4+30t^3-t^2-t-1; this is verified as a
coefficient-list polynomial identity over Q[t] in verify_genus.py. On (0,1/4),
h < 0: split into [0,1/16],[1/16,1/8],[1/8,3/16],[3/16,1/4] and bound
h <= 91u^5+96u^4+30u^3-l^2-l-1 < 0 with values -0.991,-0.982,-0.803,-0.290.
Thus disc(C) > 0 on (0,1/4): three distinct real roots; C(0) = -4t^2 < 0 rules out root
at 0, so D has distinct roots {0} union three nonzero. In x, K has
disc_y E(y) = t^2y^4-2ty^3+y^2-4t^2y-4t^2 with disc(E) = -256t^7h(t) > 0 likewise
(same h). Both projections are separable; the biquadratic kernel is smooth of genus one.

## Proof of Theorem 3
For excursions, e_n x^0y^0 <= [total S-weight sum] gives e_n <= S(x,y)^n for all x,y>0.
At (0.634,1.487): S = 1700772859/471379000 = 3.60807939... < 3.61 exactly.
For totals, every confined endpoint (X,Y) with x,y >= 1 has x^Xy^Y >= 1, so
q_n <= S(x,y)^n there. At (1,1.4142): S = 135354041/35355000 = 3.82842712... < 3.8285
exactly (compare 1+2sqrt(2) = 3.82842712...). Hence rho_exc < 3.61 < rho_tot < 3.8285
is consistent with, but does not prove, the heuristic fits rho_tot ~ 3.8277.

## What is NOT claimed
No irrational excursion/total exponent and no Q(1,1;t) non-D-finiteness is proved here.
Least-squares fits (rho ~ 3.8266-3.8285, alpha ~ -1.26 to -1.59 depending on the
1/sqrt(n) vs 1/n correction) and box-truncation eigenvalues (1.40,2.23,2.69,2.95,3.12,3.23
for B = 1..6) are documented heuristics/bounds only. The polar transfer from excursion
asymptotics to total-walk singularity is left open.

## Replay
stdlib-only Python 3: python3 output/artifacts/verify_group.py (-> GROUP_WORD_OK),
python3 output/artifacts/verify_tracepoly.py (-> TRACEPOLY_OK),
python3 output/artifacts/verify_genus.py (-> GENUS_OK),
python3 output/artifacts/verify_bounds.py (-> BOUNDS_OK). Each runs in seconds.
