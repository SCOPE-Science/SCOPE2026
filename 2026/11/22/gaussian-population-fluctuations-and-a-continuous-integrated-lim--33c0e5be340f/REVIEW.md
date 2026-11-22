# Scientific review

## Correctness

**PASS (self-review).** The Poisson excursion lifetime tail is obtained by integrating the documented symmetric Brownian entrance law. Joint count covariance equals the overlap intensity of the two alive-indicator kernels. For arbitrary fixed finite linear combinations of normalized counts, the compensated Poisson characteristic exponent differs from its Gaussian quadratic exponent by at most one sixth of the integrand supremum times its quadratic intensity; the supremum is \(O(T^{-1/4})\), while the quadratic intensity is exactly invariant under the scaling. The same proof applies to time-integrated counts. Uniform integrated increment second moments then establish tightness in \(C([0,L])\). The covariance integration and fractional-Brownian local tangent were independently rederived. The executable standard-library checker passed 1,017 numerical and structural assertions. None of its finite checks substitutes for the analytic infinite-limit proof.

## Originality

**PASS against inspected literature, with residual priority risk.** Kou's *Singular Birth-Death model* (arXiv:2611.19362v1) supplies the same Poisson object and the one-time Poisson spatial law; those are credited and are not new. Kou's power-sum central limit theorem is for one deterministic time and positive spatial powers. A full-text search and material review of Section 4 found a joint Laplace-functional construction, not the combined multitime Gaussian population and continuous integrated-population limit. Pang and Taqqu (2019, doi:10.1002/hf2.10028) consider finite-rate Poisson power-law shot response with centered marks. Marynych and Verovkin (2017, doi:10.15559/17-VMSTA76) treat finite renewal immigration with a stable inverse-time limit. Seppäläinen (2005, arXiv:math/0310044) obtains one-quarter Gaussian particle-current fluctuations in a different lattice system. Neither matching terms nor missing search hits are novelty proof; stronger general sigma-finite Poisson-occupation theorems may entail this as a special case and remain a genuine historical-priority uncertainty.

## Value

**PASS.** The decisive mathematical gap concerns a natural time-aggregated population observable: count paths have a dense exceptional set of infinities and cannot satisfy an ordinary path-level functional central limit theorem, while their integrals exist continuously and do satisfy one. The explicit covariance, the distinct global versus local Gaussian laws, and the exact integrated variance distinguish genuinely different dependence scales, enabling quantitative study of accumulated live-particle exposure. No independent validation has been performed.

## Limitations and source comparison

All assertions concern the one-dimensional symmetric Itô Brownian excursion normalization used by Kou. The count convergence is only finite-dimensional; the integrated function-space convergence holds on each compact horizon; the tangent law concerns the already-taken Gaussian limit. The exact marginal count and overlap covariance are preliminary deductions of the source's Poisson construction rather than independent novelty claims. Potential broader functional-limit and Gaussian-kernel precedence is documented in AUDIT.json. Primary-source and near-overlap comparisons are cited in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
