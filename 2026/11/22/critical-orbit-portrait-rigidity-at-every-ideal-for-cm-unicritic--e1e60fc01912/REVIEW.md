# Scientific review

## Correctness — PASS
Sano's complete published CM-PCF parameter list supplies a finite set of orbit shapes in each degree. The proof explicitly reconstructs each orbit and all pairwise differences. For degrees at least three every nonzero difference is an algebraic unit. In the quadratic cases the valuations of \(2\), \(4\), \(1\pm i\), \(2c\), and \(2c-1\) determine every local collision; the Chinese remainder theorem turns these local types into a complete classification of *whole* ideals. The standalone checker independently tests 1,078 local reductions, 484 composite reductions, and 9,438 finite-field specializations. The infinite conclusion rests on the proof, not the finite tests.

## Originality — PASS, with limitations
The closest primary paper, Sano, arXiv:2611.16354v1 (Theorem 1.1, Proposition 3.4, Corollary 5.4), classifies complex CM-PCF parameters and their characteristic-zero critical orbit types, not exact critical portraits over \(\mathcal O_{\mathbb Q(c)}/\mathfrak a\) for every ideal \(\mathfrak a\). Pink's characteristic-positive liftability theorem constructs possible lifts of marked quadratic dynamics, not the ring-level specialization of the fixed Gaussian parameters. Anderson–Manes–Tobin discuss a different reduction invariant of the polynomial map. Search comparisons against published mathematical research records for portrait stability, exact prime-power types, Gaussian critical orbits, and CM-PCF parameter reduction found no directly dominating result. The exact dyadic intermediate types \((1,1)\) and \((1,2)\) and the global composite-ideal classification are not asserted by those sources. This does not establish historical uniqueness; specialized unindexed results are a residual risk.

## Mathematical value — PASS
Specialization of a *marked* postcritical orbit is a natural arithmetic invariant distinct from ordinary good reduction of the map. The result gives a complete all-degree, all-ideal classification, showing robust stability even in the presence of ramification and inseparable reductions, with exactly enumerated sharp exceptions in degree two. The unexpected intermediate portraits over the second dyadic layer, together with the fact that mixed exceptional prime factors restore the generic portrait by the Chinese remainder theorem, supply structural boundary information, not a one-off finite table or isolated numerical improvement.

## Limits and closest literature
The result uses Sano's published characteristic-zero classification as an input. There is no uniform statement about base-field extensions, non-CM PCF parameters, or all starting points. Originality search is best-effort, not a proof of nonexistence of unindexed results. Independent mathematical audit has not been carried out.

Self-review: passed. Independent audit: not yet performed.
