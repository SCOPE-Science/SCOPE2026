# Scientific review

## Correctness

**PASS.** The assertion is a universal existence theorem for one lattice per window, not a full frame-set classification. Jacobi's product makes the theta logarithmic derivative positive and strictly decreasing; Poisson summation and the large-parameter expansion provide the two endpoint limits. At reciprocal lattice density two, the bounded alternating pre-Gramian vector vanishes on odd rows by reflection and on even rows by the exact theta equation. The published \(M^1\) pre-Gramian criterion transfers this concrete kernel to failure of the Gabor frame inequality. Explicit differentiation verifies the log-concavity threshold, and theta asymptotics verify the scale laws. The bundled checker passed 276 finite consistency assertions; these are supplementary to the infinite analytical proof.

## Originality

**PASS, relative to the primary material inspected; subject to independent publication-priority checking.** Lemvig (arXiv:2611.05337) gives sufficient frame conditions away from the relevant rational degree-two case, not an all-window negative existence theorem on that case. Horst–Lemvig–Videbæk (arXiv:2311.01547, Corollary 4.3(a)(i)) give the conditional even-window Zak-zero obstruction, but not its existence and unique aspect for every positive quadratic-Gaussian generator. Ulanovskii–Zlotnikov (arXiv:2606.31450) prove the reverse quantifier pattern—fixed lattice, selected polynomial—and at a different general density boundary. The first-Hermite mixture and positive Gaussian-scale mixture cases have different polynomial degree or complete-monotonicity structure and do not imply the present theorem. An older equivalent calculation might exist in Zak/theta literature; none was established by the comparison undertaken.

## Value

**PASS.** The result supplies an explicit natural counterexample family to the tempting inference that strict positivity, symmetry, localization, or even strong log-concavity assures stability on every integer-oversampled rectangular Gabor lattice. The aspect is a unique computable solution of a dimensionless monotone equation with sharp limiting laws, and the entire strongly log-concave subfamily is included. This directly elucidates a degree-two rational-density gap left by the recent general sufficient conditions.

## Boundaries and risks

The theorem is restricted to a particular explicit alternating null vector; other nonframe aspects may exist and are neither excluded nor classified. The numerical checker samples finitely many parameters, so it is not evidence of universal completeness. Full publication-priority auditing of older Zak-transform, theta, and Hermite-combination sources remains open.

Self-review: passed. Independent audit: not yet performed.
