# Refutation of the stated twice-twisted (2,1)-annulus snake-graph F-polynomial conjunction

## Context

The admitted target fixes the unpunctured annulus C(2,1) (two marked points on the
outer boundary, one on the inner boundary) with a rank-3 triangulation
T0 = {a1, a2, a3} and principal coefficients. A five-flip loop L = (1,2,3,1,2),
described as effecting two Dehn twists, produces a bridging arc gamma. The target
conjunction claims jointly:

- (a) the snake graph G_gamma has 5 tiles with exactly 13 perfect matchings;
- (b) the F-polynomial is
  F_gamma(y) = (1+y1)(1+y1*y2)(1+y3) + y1*y2*y3*(2+y1+y3);
- (c) this polynomial is verified both by the matching sum and by Fomin–Zelevinsky
  mutation along L, with a stated theta wall factorization.

The submitted research returns a refutation of the exact stated conjunction, not a
repaired formula.

## Definitions

- Snake graph G_gamma: the tiled graph associated to gamma over T0.
- Perfect matching: a set of edges covering every vertex exactly once.
- F-polynomial via Musiker–Schiffler–Williams (MSW): for a plain arc on an
  unpunctured surface, F_gamma(y) = sum over perfect matchings P of y(P), where
  each y(P) is a monomial in coefficient variables y1, y2, y3.
- Key evaluation: setting y = (1,1,1) sends every monomial to 1, so
  F_gamma(1,1,1) equals the number of perfect matchings counted with multiplicity
  (i.e., the coefficient sum after collecting like terms).

## Result (headline)

The stated conjunction (a) and (b) is false. The claimed polynomial evaluates to
F_claim(1,1,1) = 12 with 9 distinct monomials, whereas any perfect-matching sum
over 13 matchings must evaluate to 13 at y = (1,1,1). Since 12 != 13, the claimed
13 matchings and the claimed polynomial cannot both hold.

## Proof / evidence

Lemma (matching-sum evaluation): by the MSW formula, before collecting like terms
there is one summand per matching; evaluation at (1,1,1) therefore counts
matchings. Collecting like terms preserves the sum, so F(1,1,1) equals the number
of matchings even when distinct matchings give the same monomial.

Exact expansion: write A = (1+y1)(1+y1*y2)(1+y3) and E = y1*y2*y3*(2+y1+y3).
First A = (1 + y1 + y1*y2 + y1^2*y2)(1+y3), giving eight distinct monomials each
with coefficient 1:
1, y1, y1*y2, y1^2*y2, y3, y1*y3, y1*y2*y3, y1^2*y2*y3.
Second E = 2*y1*y2*y3 + y1^2*y2*y3 + y1*y2*y3^2.
Adding, the only collisions are on y1*y2*y3 (1+2=3) and y1^2*y2*y3 (1+1=2).
Full ledger: 1:1, y3:1, y1:1, y1*y3:1, y1*y2:1, y1^2*y2:1, y1*y2*y3:3,
y1^2*y2*y3:2, y1*y2*y3^2:1. There are 9 distinct monomials; the coefficient sum
is 1+1+1+1+1+1+3+2+1 = 12. Hence F_claim(1,1,1) = 12.

Contradiction: the Lemma requires F(1,1,1) = 13 for 13 matchings. Since 12 != 13,
(a) and (b) are arithmetically incompatible. The argument uses only the two
numbers asserted by the target and is independent of exchange matrices,
triangulation labelling, or snake-graph shape.

Corroboration (non-load-bearing): FZ-mutation replay along L from standard cyclic
affine seeds keeps F-polynomials small and never produces the claimed 9-term
polynomial, consistent with clause (c) lacking support.

## Limitations

This is a refutation of the exact stated conjunction only. It does not compute the
true geometric snake graph of gamma, the correct matching count, the correct
F-polynomial, or any repaired wall factorization, and it does not diagnose which
of the two numbers (13 vs the polynomial) is wrong. No downstream theorem use is
claimed.

## Reproducibility

Stdlib-only script output/artifacts/verify_refutation.py expands the polynomial
exactly via exponent-tuple arithmetic, prints the 9-monomial ledger, checks the
coefficient sum equals 12 and differs from 13, and prints REFUTATION_OK.
Replay: python3 -I output/artifacts/verify_refutation.py.

## References

- Musiker–Schiffler, Cluster algebras of unpunctured surfaces and snake graphs
  (general perfect-matching expansion method).
- Musiker–Schiffler–Williams, Positivity for cluster algebras from surfaces;
  Canakci–Schiffler snake-graph calculus and loop-graph reformulations.
- Gross–Hacking–Keel–Kontsevich, Canonical bases for cluster algebras (theta
  existence framework, no instance formula for this loop).
