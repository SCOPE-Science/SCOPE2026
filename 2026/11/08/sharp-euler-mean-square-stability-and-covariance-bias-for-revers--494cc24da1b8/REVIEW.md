# Scientific review

## Correctness — PASS

The theorem follows from the explicitly normalized Itô Euler step, the symmetric nonnegative \(2\times2\) diagonal second-moment transfer matrix and an independent off-diagonal multiplier dominated by its Perron root. The determinant of \(I-T\) factors as \(h^2\Delta(h)\), giving the unique sharp boundary; a strictly positive forcing vector excludes finite-second-moment invariant measures on and beyond that boundary. The inverse transfer yields the two covariance entries, and the exact \(h^2\)-positive one-step defect at target covariance proves strict stationary inflation. The singular-parameter limits are controlled by explicit radicals. Symbolic algebra and packaged exact-rational identities were checked; tests are corroboration, not the basis of the infinite assertions.

## Originality — PASS, with residual historical risk

The 2026 motivating work analyzes the continuous-time spectral gap and performs small-step Euler experiments, but does not give this explicit two-state discrete threshold or the stationary numerical covariance. The 2019 original perturbation work also treats continuous-time invariance and simulation rather than the all-parameter discrete threshold. Buckwar–Sickenberger's scalar test has decoupled noise matrices, not the coupled skew multiplicative operator. Generic system-SDE criteria in Buckwar–Kelly's 2010 work may anticipate the method: its publisher abstract was available, but its full text was not, leaving nonzero priority uncertainty. Published-research comparisons considered the source, aliases, model parameters, stronger generalized mean-square criteria, and accessible earlier claims; none identified a directly covering formula or equivalent same-model claim. Lack of a search hit is not proof of novelty.

## Value — PASS

The model is the exact two-dimensional Gaussian benchmark used to motivate the new reversible Stratonovich sampling algorithm. The result answers a practical missing question: how small a numerical step must be to ensure a long-run finite-variance Monte Carlo estimator. The sharp fourth-power amplitude penalty quantifies the cost of pushing the continuous-time acceleration, and the strict covariance inflation shows why finite-time stabilization alone is not exact sampling. It is a complete natural-parameter classification rather than an arbitrary finite experiment. It does not generalize without further analysis to nonlinear targets or other integrators.

## Closest literature and scientific limits

Sources: Louis–Pavliotis–Vilmart, arXiv:2610.03191 (2026); Abdulle–Pavliotis–Vilmart, arXiv:1903.03024 (2019); Buckwar–Sickenberger, arXiv:0912.1968 (2009/2011); Buckwar–Kelly, DOI:10.1137/090771843 (2010). The finite-step result depends on the Itô conversion and independent normal increments, not on a direct stochastic midpoint or Stratonovich Euler scheme. Independent expert/ mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
