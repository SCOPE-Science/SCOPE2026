# Scientific review: directional KL projections of circular Poisson mixtures

## Correctness
PASS. The regular-polygon Fourier filter gives the exact mixture identity. Harmonic logarithmic averages give both directed-KL objectives. A complete derivative-sign analysis establishes all global minimizers, unique tie parameters, strict branch order, and large-order asymptotics; periodic quadrature and numerical grid checks independently corroborate the formulas. Finite numerical checks are not substituted for infinite proofs.

## Originality
PASS, best-knowledge with historical-priority risk. Full-text inspection of Nielsen–Okamura (2021), especially the circular/wrapped Cauchy Theorems 4–5 and the mixture discussion, distinguishes pairwise symmetric divergences from optimizing a single candidate against a nontrivial mixture. Full-text comparison with Nielsen (2020) confirms a focus on pairwise information geometry and Voronoi structures, not equiangular KL-compression phase transitions. Kalantan–Einbeck (2019) treats estimation of real-line Cauchy mixtures. A wrapped-Cauchy MLE article by Kent–Tyler (1988) was only accessible in abstract; this leaves a nonzero residual historical risk. Separate indexed comparisons found related squared-error Poisson compression but not the directed-KL statement. Searches cannot prove priority.

## Mathematical value
PASS. The exact change from a unique uniform fit to \(m\) distinct peaks has a genuinely different transition order at \(m=2\) and \(m\ge3\). The result gives sharp critical radii for all polygon sizes and a universal \(m^{-2}\) boundary scale, while proving that swapping KL arguments eliminates every transition. This resolves a complete natural approximation problem rather than an arbitrary parameter sample.

## Limitations
The source mixture is equal-weight and equiangular. No statement is made about irregular mixtures, other divergences, or historical uniqueness. The analytic proof, not the finite checker, is responsible for the global claims.

Self-review: passed. Independent audit: not yet performed.
