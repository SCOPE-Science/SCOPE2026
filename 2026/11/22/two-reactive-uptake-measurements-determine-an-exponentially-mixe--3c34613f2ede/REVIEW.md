# Scientific review

## Correctness — PASS

The forward map follows by solving the exponentially attenuated half-line reaction–diffusion boundary equation using decaying \(K_1\) Bessel solutions. The global inverse rests on a proved strict geometric-concavity statement for \(K_0/K_1\): an explicit Riccati derivative reduces its sign to \(H>0\), and the derivative at every hypothetical zero is strictly negative while both endpoint signs are positive. Consequently the two-rate ratio is an onto, strictly decreasing bijection of the positive mixing variable onto the claimed open ratio interval. The reconstruction formulas verify existence and uniqueness; an arbitrary positive mixing variable produces a continuum from one uptake. The numeric checker passed 18,012 finite assertions but is not an infinite proof. A remaining physical risk is that experimentally modifying reaction may alter transport too.

## Originality — PASS on inspected evidence

The central primary predecessor is Monofy et al. (2024), DOI 10.1029/2024AV001373, whose full open paper supplies the *forward* Bessel flux and focuses on inferring reaction rates from independently estimated transport parameters. This does not imply the *inverse* from two independently known reaction rates, the strict feasible data window, or minimum observation count without the additional monotonic-ratio argument. Bottacin-Busolin (2019), DOI 10.1029/2019WR025697, studies conservative breakthrough-curve equifinality under uncertain stream geometry. Segura (2021), DOI 10.1007/s00025-021-01531-1, provides prior general Riccati/Bessel-ratio theory and could yield parts of the auxiliary monotonicity. Kaltenbacher–Rundell (2021), arXiv:2101.06656, uses time-dependent richer inverse data. Relevant published research records searched by statement and parameter implication returned no covering theorem. Historical priority is provisional: an uninspected older Bessel-admittance inverse could subsume the result, and the ESSOAr preprint was not independently inspected beyond metadata (the same paper's OA journal text was inspected).

## Value — PASS

The main environmental model independently regresses the reference mixing parameters and infers the reaction constants. When instead two reaction rates are controlled or known, the theorem supplies a minimal, global, experimentally interpretable alternative: exactly two corrected scalar uptake readings and an if-and-only-if model-consistency test. The admissible interval is sharp, not a numerically chosen slice, and the nonidentifiability from one reading distinguishes necessary data from redundant replication. It establishes a benchmark rather than field-validated precision.

## Scientific limitations

Exact homogeneity across interventions, positive known transfer and porosity, infinite bed depth, no noise and no extra reactions are necessary for the stated theorem. Historical novelty is not independently certified.

Self-review: passed. Independent audit: not yet performed.
