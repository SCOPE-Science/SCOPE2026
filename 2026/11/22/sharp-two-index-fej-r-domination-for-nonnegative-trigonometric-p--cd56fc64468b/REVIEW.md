# Scientific review

## Correctness — PASS

The exact positive definite Fejér Toeplitz Gram form and the explicit vector solving \(Bu=\mathbf1\) prove the sharp constant for every \(m\ge1\), \(n\ge0\); the nonnegative quadratic defect gives both inequality and equality rigidity. The root-location lemma follows from the reversed-coefficient pair and self-reciprocity, including special cases \(q=0\) and \(r=0\). A standalone finite exact-arithmetic script passed 44,893 supplementary checks. The proof does not infer infinite validity from sampling.

## Originality — PASS relative to checked evidence

MacDonald's Theorem 3 (arXiv:2611.05363, first submitted November 3, 2026) proves the sharp coefficient \(2\) only for matching Fejér and polynomial degrees; setting \(m=n\) recovers that result. The independently varying order \(m\), degree \(n\), explicit quotient-remainder formula, equality family, and root location are not covered by the material inspected. Semantic searches and accessible research-claim comparisons located related Fejér approximation, sparse coefficient extremals and other Toeplitz bounds, but no identical two-index pointwise theorem. A prior theorem with an equivalent inverse-Toeplitz evaluation constant could still exist outside indexed or accessible sources; independent literature review is necessary for publication-level priority claims.

## Value — PASS

The independent ratio between smoothing length and signal bandwidth is natural in finite Fourier reconstruction: knowing the bandwidth does not force the averaging order to match it. The theorem determines the exact sharp pointwise loss for all ratios and identifies unique equality polynomials, with a non-obvious all-unit-circle root property. The dependence on \(n=qm+r\) describes a complete sharp staircase rather than a routine reparameterization of the matched case.

## Limits and evidence

Proof, normalization, boundary cases and reproduction command are in RESULT.md and verification_check.py. The finite checker is supplementary only; neither an independent audit nor an exhaustive historical originality certificate has been performed.

Self-review: passed. Independent audit: not yet performed.
