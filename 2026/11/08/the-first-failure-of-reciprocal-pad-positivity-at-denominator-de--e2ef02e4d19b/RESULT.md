# The first failure of reciprocal Padé positivity at denominator degree five

## Finding

For every nonnegative integer \(k\), let \(q_{k,5}\) be the normalized denominator of the \([k/5]\) Padé approximant to the exponential function,
\[
q_{k,5}(z)=\sum_{j=0}^{5}(-1)^j\binom5j\frac{(k+5-j)!}{(k+5)!}z^j,
\qquad
\frac1{q_{k,5}(z)}=\sum_{n=0}^{\infty}c_n(k,5)z^n.
\]
Then
\[
\boxed{c_n(k,5)>0\quad\text{for every }0\le k\le65\text{ and every }n\ge0.}
\]
In contrast, \(c_{38}(66,5)<0\). Consequently, **\(k=66\) is the least numerator degree admitting any negative reciprocal coefficient** when the denominator degree is five. The sign at \((66,38)\) was previously exhibited by Scardino; the new assertion is the complete all-coefficient positivity certificate for the preceding 66 numerator degrees, making that witness globally least in numerator degree.

## Assumptions and scope

Integers \(0\le k\le65\) and arbitrary integers \(n\ge0\) are covered; the comparison at \(k=66\) concerns \(n=38\). The polynomials have real rational coefficients and constant term one. No statement is made for denominator degrees other than five or for all numerator degrees greater than 66. The application is to reciprocal-denominator positivity in Padé-based numerical evaluation of matrix exponentials, not a claim about failure of any matrix-exponential algorithm.

## Proof

Define \(D_k=\prod_{s=1}^{5}(k+s)\) and \(P_k=D_kq_{k,5}\). The integer polynomial is
\[
P_k(z)=\sum_{j=0}^{5}(-1)^j\binom5j
\left(\prod_{s=1}^{5-j}(k+s)\right)z^j.
\]
For each of the 66 integers \(k\), the accompanying `root_centers.json` contains five complex rational centers, with real and imaginary parts integral multiples of \(10^{-9}\). All five associated closed disks of radius \(\varepsilon=10^{-6}\) are disjoint. For each center \(a\), write the exact Taylor expansion \(P_k(a+w)=\sum_{h=0}^5t_hw^h\). The standalone rational checker proves, for all 330 disks,
\[
|t_0|+\sum_{h=2}^{5}|t_h|\varepsilon^h
<|t_1|\varepsilon.
\]
The absolute values in this test are enclosed by rational square-root bounds, rather than evaluated with floating-point arithmetic. Rouché's theorem gives precisely one simple root in each disk, hence these are all five roots. The first center is positive real. Its disk is conjugation-invariant and contains exactly one root, so that root \(\rho>0\) is real. The same Taylor certificate establishes \(P'_k(\rho)<0\). Rational modulus enclosures show that every other root \(\zeta_j\), \(1\le j\le4\), has \(|\zeta_j|>\rho\).

Partial fractions now give
\[
c_n(k,5)=\sum_{j=0}^4 A_j\zeta_j^{-n},\qquad
A_j=-\frac{D_k}{\zeta_jP'_k(\zeta_j)},\qquad \zeta_0=\rho,\quad A_0>0.
\]
For each root disk the checker obtains exact rational bounds \(L_j\le|\zeta_j|\le U_j\) and \(\alpha_j\le|A_j|\le\beta_j\) from the Taylor derivative remainder and the modulus enclosures. For the real root the positive residue satisfies \(A_0\ge\alpha_0\). In all 66 cases the following inequalities hold *exactly*:
\[
U_0<L_j\quad(1\le j\le4),\qquad
\sum_{j=1}^{4}\beta_j\left(\frac{U_0}{L_j}\right)^{300}
<\frac{17}{50}\alpha_0<\alpha_0.
\]
Therefore for every \(n\ge300\),
\[
\rho^n c_n(k,5)
\ge A_0-\sum_{j=1}^{4}|A_j|\left(\frac{\rho}{|\zeta_j|}\right)^n>0.
\]
For the remaining \(0\le n<300\), the exact rational recurrence
\[
c_0(k,5)=1,\qquad
c_n(k,5)=-\sum_{j=1}^{\min(5,n)}\frac{[z^j]P_k(z)}{D_k}c_{n-j}(k,5)
\]
is evaluated with exact fractions for all \(k=0,\ldots,65\); all 19,734 nonconstant signs are strictly positive. The same recurrence confirms \(c_{38}(66,5)<0\), completing the least-numerator-degree assertion.

## Verification

Run `python3 verify.py` with `root_centers.json` in the same directory. Python 3 standard library suffices. The checker reads the 66-by-five exact rational centers, checks pairwise disk disjointness, proves 330 Rouché inequalities, validates root and residue bounds, proves 66 uniform tails from degree 300 onward, evaluates 19,734 exact rational finite signs, and independently tests the negative coefficient at \((66,38)\). It prints `VERIFY_OK` only if all assertions pass. Root centers may have been obtained numerically, but they serve *only* as exact rational candidate certificates; the verifier uses no numerical root solver or floating-point test. The infinite range follows analytically from partial fractions plus the certified strict tail bound, not from finite sampling.

## Relationship to prior work

Fasi and Higham introduced the reciprocal-denominator positivity conjecture in their matrix-exponential error analysis. Scardino's October 2026 paper established full positivity at \(k=0\), conditional eventual positivity through dominant-root geometry, and the explicit negative coefficient \(c_{38}(66,5)\). This result does not re-claim that witness. It closes the previously unstated gap \(1\le k\le65\) for denominator degree five *uniformly over every coefficient index*, thus identifies the first numerator degree at which positivity can fail. The all-index proof needs rigorous pole localization and an exact tail certificate in addition to finite recurrence checks.

## Limitations

This is a 66-parameter exact certificate and not a symbolic formula covering arbitrary numerator degree. The threshold is in \(k\) only, not a classification of all negative coefficients after \(k=66\). The primary application is a conditional positivity property in numerical matrix-exponential analysis, not an algorithmic complexity or accuracy theorem. Independent mathematical validation has not been performed.

## References

1. F. Scardino, *On a positivity conjecture of Fasi and Higham for Padé approximants to the matrix exponential*, arXiv:2610.39051v1, first publicly posted 2026-10-28, especially Sections 2 and 8. https://arxiv.org/html/2610.39051v1
2. M. Fasi and N. J. Higham, *An Arbitrary Precision Scaling and Squaring Algorithm for the Matrix Exponential*, SIAM Journal on Matrix Analysis and Applications 40 (2019), 1233–1256, especially Conjecture 3.2. https://doi.org/10.1137/18M1228876
