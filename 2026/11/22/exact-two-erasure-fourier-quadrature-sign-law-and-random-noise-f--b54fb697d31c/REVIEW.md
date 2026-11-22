# Scientific review: exact two-erasure Fourier quadrature

**Correctness: PASS.** Fourier interpolation uniqueness follows from the polynomial-root bound, and the full-grid DFT reduces the quadrature weights to a two-mode cosine with two forced zeros. The sign, negative-mass, and squared-norm formulas follow from an explicit cosine comparison and exact orthogonality. Uniform-pair counting and a standard cosecant-squared identity prove the average-noise law for every odd grid size. Direct finite tests cover 14,235 erased pairs and 98 separate mean identities, but cannot replace the analytic proof.

**Originality: PASS, provisionally.** Closest literature includes Kircheis and Potts (2023) on exact nonequispaced Fourier quadrature, Peherstorfer (2010) on general positive trigonometric quadrature, and Yu and Townsend (2022) on perturbed-grid stability. These establish shared foundations, not the checked explicit two-deletion random-noise floor. A published Fourier pair-collision result treats moved nodes and its full text was not accessible; existing positivity criteria and unlocated erasure literature remain genuine priority risks. No claim of independent historical certification is made.

**Value: PASS.** Two erasures are the minimal failure case with only two nodes of redundancy beyond an exact Fourier quadrature grid. The exact positive-design probability, negative-weight count and noise-floor limit show a significant design trade-off: polynomial/Fourier exactness after erasure does not retain vanishing mean observation-noise variance as resolution increases. This is an exact structural limit, not just a small-grid numerical counterexample.

**Scientific limitations.** Odd equispaced grids, exactly two missing nodes, maximal admissible Fourier degree, iid missing pairs only for the distribution, independent homoscedastic additive error only for the variance. No generic irregular-grid, all-dropout, computational-conditioning, or floating-point theorem. Historical priority provisional; independent audit not yet performed.

Self-review: passed. Independent audit: not yet performed.
