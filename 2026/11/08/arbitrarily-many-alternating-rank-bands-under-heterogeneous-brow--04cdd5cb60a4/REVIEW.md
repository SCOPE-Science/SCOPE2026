# Scientific review

## Correctness — PASS

The result is a theorem about the **right derivative at zero resetting rate**, not an assertion about finite-rate global optimization. The Brownian survival transform follows from the reflection principle. Differentiating the first-reset Volterra equation gives the exact first-order survival response. Two elementary Laplace inversions produce the stated complementary-error-function kernel; an independent time-domain convolution calculation agrees. Standard small- and large-argument expansions of the complementary error function establish opposite signs at the short- and long-distance observation scales. The scale-separation induction is fully quantified: all finitely many old sign samples persist as each new distance diverges, while the contribution from the new distance is quadratic in that distance and all older contributions grow at most linearly at its own observation times. Strictly positive no-reset hitting-time densities transfer the signs, and each consecutive opposite-sign pair forces a distinct sign-changing zero. No numerical root count is used in the universal proof.

The standalone program checks the inversion independently by integrating the renewal convolution, checks the Laplace-domain derivative against time-domain quadrature, reproduces the exact signs for an explicit three-scale witness, and examines asymptotic scalings. The checks support, but do not replace, the proof.

## Originality — PASS, with named publication-priority uncertainty

Closest known comparison: R. Vatash, E. Goldfarb, V. Yu. Rudyak, and Y. Roichman, *Rank-dependent optimal resetting in multiparticle search*, arXiv:2609.23542 (2026-09-20), studies ordered arrival times and finds a single critical rank fraction for **identical** starts, together with changes caused by heterogeneous initial positions. The present theorem is not a restatement of the source's monotonic homogeneous rank-optimum: it constructs arbitrarily many alternating **zero-rate quantile-response** bands for any fixed number of positive-weight distance classes, by a general scale-separation induction. The accessible abstract does not report an unbounded-oscillation theorem. However, the complete preprint was not available for inspection, so unpublished-in-abstract heterogeneity results remain a specific residual risk and the priority assessment is conditional on accessible material.

The renewal transform is established earlier, including the accessible first-passage analysis of Górska et al. (2024), and is not claimed as new. Evans, Majumdar and Mallick (2013) study resetting searches and multiparticle survival, Evans and Ray (2024) study mean completion time with distributed targets, and Singh and Pal (2022) develop resetting first-passage functionals; none of the inspected statements directly gives arbitrary rank-dependent alternation. Indexed mathematical finding searches for the preprint, the derivative formula, heterogeneous rank-response reversals, and equivalent formulations did not return an identified stronger matching theorem. Failed searches cannot establish novelty conclusively.

## Value — PASS

The 2026 multiparticle work makes rank-dependent resetting and the role of starting-distance heterogeneity a physically motivated question. Identical starts exhibit a simple rank threshold. The new result proves a fundamental, nonperturbative-in-heterogeneity **limitation on any universal single-threshold classification**: with noninteracting Brownian dynamics alone, spatial heterogeneity can create as many separate helpful and harmful rank bands as desired. The response is an experimentally interpretable infinitesimal change in completion quantile. This is structural rather than an isolated parameter substitution, and the conclusion does not depend on an arbitrary finite cutoff or a numerical census.

## Closest sources and limitations

- Vatash et al., arXiv:2609.23542 (2026): directly motivates rank-dependent search; only the accessible abstract and bibliographic summary could be inspected, leaving priority uncertainty.
- Górska et al., *Entropy* 26 (2024), 665, https://pmc.ncbi.nlm.nih.gov/articles/PMC11353880/: accessible full-text first-passage renewal-transform sections; supplies standard methodology, not quantile-scale alternation.
- Evans, Majumdar and Mallick (2013), https://doi.org/10.1088/1751-8113/46/18/185001: multiparticle search and resetting, but the available abstract does not address the oscillation count.
- Evans and Ray, arXiv:2410.01941 (2024): target-distance distributions with a mean-time objective; not the present population quantile-response claim.
- Singh and Pal, arXiv:2202.02715 (2022): first-passage functionals and resetting, not an arbitrary count of rank sign changes.

Only zero-rate linear response for Poisson resetting on a half-line is proved. Distances may require strong separation. A three-scale numerical example is a witness of five sign reversals, not proof of an exact total number. There is no claim for finite-population means or global finite-reset-rate optima.

Self-review: passed. Independent audit: not yet performed.
