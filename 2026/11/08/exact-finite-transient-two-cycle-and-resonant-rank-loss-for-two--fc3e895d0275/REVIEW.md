# Scientific assessment

**Correctness.** The mean-normalized, signed two-entry update gives the contrast map, and the logarithmic exponent gives the exact entry and rank-loss times. The nonresonant map is an involution, with a fixed contrast at \(\sqrt{|1-\alpha|}\); the signed matrix return law remains valid there. The root convergence factors of the nonresonant and rank-one branches coincide at \(4-2\sqrt2\), although the ranks and update laws are still different. The rank-loss, equal-singular and zero-error cases are handled separately. The finite package checks are supplementary to the proof.

**Originality.** The commuting one-step magnitude law and the distinct line-search case already appear in Shulgin et al. (arXiv:2610.30280v1). Uniform convergence bounds are also available from Jawanpuria et al. (arXiv:2610.27747v1). The distinct claim is the complete finite-entry and rank-loss classification at fixed steps other than exact line search, including the signed matrix law. The source comparisons do not establish historical priority.

**Value.** This is a complete orbit classification for the first nontrivial row dimension. It identifies exact spectral resonances, distinguishes positive-rank decay from fixed- or period-two contrast, and separates rank behavior from the size of the asymptotic norm factor.

**Limitations.** The result applies to isotropic quadratic curvature, two rows, exact arithmetic and exact thin-polar updates; it does not classify numerical rank decisions or approximate polar dynamics.
