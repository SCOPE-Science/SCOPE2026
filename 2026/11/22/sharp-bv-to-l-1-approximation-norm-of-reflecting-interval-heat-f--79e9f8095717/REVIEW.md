# Scientific review

## Correctness — PASS
The normalization is the generator \(\partial_x^2\) with Neumann boundary conditions on the open unit interval. Signed-jump representation reduces all real distributional BV inputs to jump profiles, and positive symmetric heat-kernel crossing identifies the exact profile. The diagonal cumulative-heat derivative equals the derivative of the two-periodized Gaussian, whose strict decrease is justified by Jacobi's positive triple product. This proves that the midpoint jump is the unique global maximizer and classifies all equality cases. Cosine eigenexpansion yields the exact constant, time monotonicity/concavity and both asymptotics. Numerical quadrature and signed-multijump checks provide reproducible sanity tests only, not the infinite proof.

## Originality — PASS, with residual historical risk
The closest accessible full texts are Angiuli–Miranda–Pallara–Paronetto (2008), on BV recovery under parabolic semigroups; Choulli–Kayser–Ouhabaz (2015), on Neumann heat-kernel bounds and analyticity; and Angeloni–Vinti (2016), on convolution-type approximation in variation. Their theorems do not state a sharp finite-time norm of \(I-H_t\) from \(BV/\mathbb R\) to \(L^1\), or unique centered-jump equality. Heat-content literature may already contain the centered spectral sum as a fixed-input special case; the additional assertion that *this input is uniquely worst among every BV function at all positive times* does not follow from knowing one fixed heat-content series. An accessible 2014 heat-content abstract was compared, but its full text was not verified, leaving a specific priority risk.

## Value — PASS
This determines the exact physical error incurred by smoothing any discontinuous one-dimensional signal under reflecting diffusion, for every positive time and without unspecified constants. The strict midpoint extremizer and concave time law quantify how boundary reflection changes the placement of worst-case discontinuities and how quickly error saturates; neither a short-time asymptotic alone nor mere variation contraction gives the same calibration.

## Reproducibility and limitations
The proof uses interior distributional variation, not endpoint variation. The checker tests cosine-kernel normalization, heat crossing, centered-jump equality, sample monotonicity, signed multijumps, time derivatives and endpoint scales; finite checks cannot establish the global maximizer. Equivalent results may exist in unindexed semigroup/heat-content literature. No external mathematical validation has been undertaken.

Self-review: passed. Independent audit: not yet performed.
