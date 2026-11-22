# Scientific review: two-site bound-state inverse fibers

## Correctness — PASS

The Birman–Schwinger matrix at the upper free-band edge gives a necessary-and-sufficient strict condition for two simple eigenvalues above the band. Direct solution of the free tail yields the cubic; Vieta's identities give the exact quadratic reconstruction. The positivity and location of both unobserved roots are proved by the inequality for \(Q_{r,s}(1)\). The double-root fold and square-root branch separations are exact algebraic identities. Supplemental exact symbolic and numerical checks are reproducible using `check.py`. No finite experiment is claimed to prove the global theorem.

## Originality — PASS, with historical-priority risk

The nearest general source is Webb–Olver, arXiv:1702.03095, Sections 4.2–4.3 and Theorem 4.22, which computes the spectrum from all Jacobi coefficients using polynomial roots. Iantchenko–Korotyaev, arXiv:1004.2664, Theorem 1.3 and Section 3.3, instead reconstructs a Jacobi perturbation from full Jost data including resonances. Neither inspected theorem states the two-bound-energy-only exact two-to-one fiber, its fold, or the quantitative parameter splitting. The two papers' broader direct machinery can derive the starting cubic, but their full-data inversion does not imply unique recovery from the reduced data. A specialized prior treatment of the identical minimal two-defect fiber could still subsume the result, and independent priority assessment is warranted.

## Mathematical value — PASS

Bound-state-only recovery is an identifiable partial-data inverse-spectral question: two spectral outliers appear to match the two unknown positive onsite coefficients, yet the complete exact inverse problem generically has two answers. The result proves the precise ambiguity and its merger mechanism, rather than just exhibiting an isolated counterexample. The exact square-root separation is useful for understanding instability of inverse reconstruction from limited spectral observation. No claim is made about inverse recovery from stronger spectral measures or scattering observations.

## Limits

Positivity, unit hopping, Dirichlet half-line boundary and two bound states are essential to the stated classification. The zero- and one-bound-state regimes, other perturbation signs and higher-rank inverse fibers are outside scope. Tests complement, not replace, the proof. Historical overlap risk remains despite inspected primary work and semantic claim searches.

Self-review: passed. Independent audit: not yet performed.
