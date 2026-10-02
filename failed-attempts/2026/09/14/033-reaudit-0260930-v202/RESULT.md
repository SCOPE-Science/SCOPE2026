# Cyclotomic p-adic Heegner nonvanishing for 37a1 over Q(sqrt(-11)) at p = 5

## Context

Let E/Q be the elliptic curve 37a1,
\[
E:y^2+y=x^3-x,
\]
and let K=Q(sqrt(-11)). The primes 37 and 5 split in K, and E has good
ordinary reduction at p=5. The goal is to verify a concrete rank-one
cyclotomic p-adic Gross-Zagier nonvanishing statement for the Heegner class
attached to K.

## Definitions and verified inputs

- `E=ellinit([0,0,1,-1,0])`, conductor 37.
- The quadratic twist by -11 has minimal model
  `ellinit([0,0,1,-121,-333])`, conductor 4477=11^2*37.
- PARI gives `a_5(E)=-2`, and `#E(F_5)=8`, so p=5 is ordinary.
- Kronecker symbols and ideal factorization give
  `(-11/5)=(-11/37)=1`, hence 5 and 37 split in K.
- E has multiplicative reduction at 37; for 37a1 it is **nonsplit**.
  This sign is irrelevant to the good-ordinary calculation at p=5.
- The archived rank computations give rank E(Q)=1 and rank E^(-11)(Q)=0,
  hence rank E(K)=1 by the quadratic-twist rank decomposition.

## Result

For the cyclotomic ordinary normalization used by the archived PARI
computations:

1. The 5-adic cyclotomic regulator of E/Q is nonzero. On the rational point
   (0,0),
   \[
   R_5((0,0))=
   5+5^2+5^3+3\cdot5^6+4\cdot5^7+5^9+5^{10}+O(5^{11}),
   \]
   so its 5-adic valuation is exactly 1.

2. The ordinary cyclotomic p-adic L-function of E has a simple zero at the
   central point to the computed precision: its first derivative begins
   \[
   2\cdot5+2\cdot5^2+2\cdot5^4+\cdots,
   \]
   again of valuation 1. The -11 twist has rank zero and its archived
   p-adic BSD value is a 5-adic unit.

3. Because p=5 splits in K, the cyclotomic Rankin/base-change p-adic
   L-function factors, up to the standard nonzero local normalization, into
   the E and E^(-11) ordinary factors. Consequently its central value
   vanishes and its cyclotomic derivative is nonzero.

4. By the ordinary split p-adic Gross-Zagier formula, the cyclotomic p-adic
   height of the Heegner class of discriminant -11 is nonzero. Equivalently
   for this specialization, the cyclotomic Rankin p-adic L-function has
   order exactly one at the central character.

This is a concrete nonvanishing/simple-zero verification. It is not a proof
of every assertion of the p-adic Birch-Swinnerton-Dyer conjecture.

## Proof / evidence

The exact and p-adic numerical inputs are archived in
`artifacts/pari_results.json`, with the command list in
`artifacts/reproducibility.json`. The regulator is stable through precisions
6, 8, and 10:
```
5 + 5^2 + 5^3 + 3*5^6 + O(5^7)
5 + 5^2 + 5^3 + 3*5^6 + 4*5^7 + O(5^9)
5 + 5^2 + 5^3 + 3*5^6 + 4*5^7 + 5^9 + 5^10 + O(5^11).
```
The leading coefficient is a 5-adic unit, so the regulator cannot vanish.

The archived p-adic L derivative has leading term `2*5`, while the twist
rank-zero p-adic BSD output is `1+O(5^8)`. The nonzero derivative of the
product therefore follows from the ordinary split factorization. The
p-adic Gross-Zagier theorem then transfers this nonvanishing to the
cyclotomic height of the Heegner class over K.

The coordinate returned by PARI's `ellheegner(E)` is **not** used to identify
the discriminant -11 Heegner point. In particular, the previous version's
identification of `[0,0]` with that Heegner class was unsupported; Sage's
Heegner-point interface treats the discriminant as explicit data and gives
separate examples already at discriminant -7 for 37a1.

## Originality context

The 5-adic regulator of 37a1 at p=5 is already a documented example in Sage
and in published Iwasawa-theoretic literature. The value here is therefore
the explicit K=Q(sqrt(-11)) Rankin/Heegner specialization and consistency
check, not novelty of the regulator computation or of the p-adic
Gross-Zagier theorem.

## Limitations

The p-adic numbers rely on PARI/GP's p-adic-height and p-adic-L
implementations with tracked precision; those libraries are not formally
verified here. The factorization is used with its standard ordinary local
normalization, whose omitted factor is nonzero. No explicit affine
coordinates are claimed for the discriminant -11 Heegner point. The result
establishes nonvanishing and a simple zero, not the full p-adic BSD formula.

## Reproducibility

Use PARI/GP 2.17.2 commands listed in
`artifacts/reproducibility.json`; verbatim archived values are in
`artifacts/pari_results.json`.

## References

- D. Disegni, p-adic Gross-Zagier formulae, arXiv:1510.02114.
- D. Disegni, universal p-adic Gross-Zagier formula, arXiv:2001.00045.
- SageMath elliptic-curve documentation for p-adic regulators and Heegner
  points.
- PARI/GP documentation for `ellpadicheight`, `ellpadicregulator`,
  `ellpadicL`, `ellpadicbsd`, and `ellheegner`.
