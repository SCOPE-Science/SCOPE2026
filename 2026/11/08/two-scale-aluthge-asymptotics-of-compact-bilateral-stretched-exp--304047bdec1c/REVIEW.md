# Scientific review of two-scale bilateral Aluthge asymptotics

## Correctness — PASS

The proof derives the exact binomial log-weight recursion from the polar decomposition. A centered-binomial CLT with moment uniform integrability and strict Gaussian small-ball unimodality proves the general norm exponent. At the Laplace exponent, an exact telescoping binomial identity, local Stirling expansion, Berry--Esseen comparison of absolute-deviation increments, and a global quadratic/linear lower bound together justify the Gaussian local window and the **whole infinite** Schatten sum, not just a pointwise limit. At the quadratic exponent, the moment identity is exact and the irrational/rational cluster classification follows from the rotation orbit. The independent finite script passed 3,276 assertions but is not substituted for the infinite proof.

## Originality — PASS, qualified

The general binomial convolution identity and qualitative convergence of Aluthge iterates are prior-covered. Bala's 2026 compact-operator result proves norm convergence but no two-scale rate. The 2005 generalized-transform work and Stanković's November 2026 analysis cover qualitative Schatten convergence and a unilateral-shift binomial formula, but not the present **bilateral** Laplace prefactor or quadratic arithmetic pinning. The closest unilateral boundary-layer result has a fixed endpoint rather than a drifting Gaussian interior, with a different leading norm scale. The claim is limited to the new bilateral quantitative results. Priority risk: broader published discrete heat-kernel or Laplace asymptotics could imply the constants in another guise; an older weighted-shift paper was accessible only through its abstract.

## Mathematical value — PASS

For compact shifts, knowing convergence to zero says nothing about the number of singular values contributing to a Schatten norm. The theorem supplies an explicit sharp stretch-exponential norm exponent for all shape parameters and exhibits a **structural transition** between a widening Gaussian singular-value window and a lattice-pinned theta profile. The exact Schatten prefactor, its divergence relative to operator norm, and the rational/irrational modulation are quantitative invariants that require analysis beyond standard qualitative convergence. The scope is an explicit natural bilateral family and fixed parameters; universality outside that family is not claimed.

## Limitations and closest literature

The proof does not give uniform parameter limits or exact Schatten prefactors for arbitrary stretch exponent. Bala (arXiv:2602.07916), Antezana–Massey–Stojanoff (2005), Stanković (arXiv:2611.07728), and Rion (2017) are the closest literature considered. The first two are qualitative/general; Stanković's full relevant unilateral-shift proposition was compared by statement; Rion's full text was not accessible, so its absence of exact covering statements was not assumed. No independent mathematical audit was performed.

Self-review: passed. Independent audit: not yet performed.
