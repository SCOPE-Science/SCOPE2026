# Review — Sharp circular heat variation contraction and its exponentially flat onset

## Correctness — PASS

Distributional differentiation commutes with circle heat convolution. Exact Jordan normalization \(Df=(V(f)/2)(p-q)\) gives the correct half-L1 Dobrushin ratio; strict radial monotonicity produces the strictly increasing angular separation function, uniquely maximized at antipodal displacement. The equality proof forces each Jordan factor to be a Dirac mass. The time derivative follows from the heat equation, strict semigroup comparison follows from equality rigidity, and both endpoint expansions are derived from analytic series. The independent-standard-library numerical checker cross-compares Fourier, Gaussian, shifted-kernel and Jordan-mixture evaluations; these finite checks are supplementary only.

## Originality — PASS, qualified

Known ingredients are not counted as new: Dobrushin's zero-mass coefficient, classical circular Gaussian heat kernel, and spherical heat-kernel radial monotonicity. The additional claim is the optimized **sharp** circle heat BV coefficient, the unique semicircle equality class, strict semigroup coefficient and explicit exponentially small onset and Fourier tail. Baudoin (2013) supplies the kernel but not these conclusions; Angeloni–Vinti (2016) discuss BV approximation without this exact periodic heat stability; the radial kernel theorem covers monotonicity without BV coefficient. published-finding corpus nearest items have different metrics/domains (finite-cycle Wasserstein-one, Neumann reflecting-square heat distance, Hilbert fractional heat). Unindexed earlier results remain a historical priority risk, and the indexed published comparisons were read as title/summary rather than complete scientific texts.

## Mathematical value — PASS

This is an exactly evaluated natural operator seminorm over all real BV signals on the continuum circle; it determines the complete equality geometry and shows why positive-time strict contraction is invisible to any algebraic short-time expansion. The small-time defect has an exact leading exponential rate and prefactor and the long-time law has sharp spectral terms. These facts are more informative than elementary nonexpansivity.

## Limitations

Only standard homogeneous real one-dimensional circular heat flow is covered. No variable diffusivity, nonuniform weighted variation, higher-dimensional torus or complex-valued claim is made. Earlier unindexed work may already contain individual exact expressions. Numerical stress tests do not establish the theorem. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
