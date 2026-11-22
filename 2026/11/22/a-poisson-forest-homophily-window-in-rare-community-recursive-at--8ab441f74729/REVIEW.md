# Scientific review: A Poisson–forest homophily window in rare-community recursive attachment

## Correctness — PASS

The claim specifies a fixed initial graph with both types, a triangular rare-birth regime, the soft \(\gamma=0\) attachment kernel, fixed \(q_B\in(0,1)\), and all possible limits \(nq_{A,n}\to\theta\in[0,\infty]\). The exact B-target and A-target kernels follow from per-type weights. The total minority birth count is tight and its times converge to a Poisson point process. Uniform conditional estimates off the lower-time boundary prove independent Poisson child marks; a triangular-array multivariate CLT gives the founder Gaussian and a temporal truncation proves asymptotic independence. At the escape endpoint, Poisson thinning and an explicit Gamma integral give the degree intensity. Each approximation is justified under a bounded rare-birth count and a positive lower age cutoff, with those restrictions removed by tightness and a probability bound. The packaged finite checker passes 3,662 assertions. Its finite checks are not substituted for the limit argument.

## Originality — PASS against examined sources

Ben-Hamou, Broutin and Cazaux, arXiv:2611.06904, study fixed-parameter empirical measures; their Model 2 definition supplies the attachment law, but their displayed limiting empirical distribution theorem does not imply the tight rare-community Poisson forest under \(p_n=c/n\), nor the window \(nq_{A,n}\to\theta\). Bhamidi, Fan, Fraiman and Nobel, arXiv:2004.02697, develop fixed-composition community-modulated recursive tree laws; geometric limiting degrees for a typical vertex do not imply the joint independent Poisson counts of rare vertices or their coupling to founder fluctuations. Closest mathematical-index hits on soft-community assortativity and linear de-preferential attachment address different scales or dynamics. A general rare-type marking theorem may subsume components of this argument, and unindexed coverage remains a priority risk.

## Value — PASS

Fixed-proportion empirical laws lose all information about a community of tight population size. The theorem supplies its full finite ancestry and birth-time-marked child structure and simultaneously separates its randomness from Gaussian fluctuations of the persistent original vertices. The inverse-size homophily scaling and explicitly geometric Poisson degree intensities form a natural, parameter-complete critical boundary for this rare-population regime. The result is more informative than merely observing a binomial-to-Poisson birth-count limit.

## Limitations

The theorem does not cover positive degree reinforcement, other attachment models, random growing seed size, or the actual identities of B-type parents. Search failure cannot establish historical novelty; priority remains provisional and independent mathematical validation is required.

Self-review: passed. Independent audit: not yet performed.
