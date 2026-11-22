# Scientific review: fixed-step local primal–dual mean slowdown

## Correctness — PASS

The statement is limited to first moments of exact scalar quadratics and includes the zero-sum dual normalization. Conditional SAGA-style control-variate unbiasedness is an identity for every stored table; affine gradients therefore close the conditional mean recursion exactly. The inner geometric series and fixed point are reconstructed explicitly. The mean error matrix tends to a semisimple projector, and its first-order slow block is minus the curvature-weighted graph operator, which has precisely the nonzero eigenvalues claimed. The exact two-agent scalar recurrence gives equality for every integer local budget. The companion verifier checks 3,840 exact-rational trajectory assertions, 144 exhaustive within-round stochastic-mean cases, and 960 supplementary numerical spectral assertions. A finite check alone would not support the spectral limit; that limit is proved analytically.

## Originality — PASS, qualified

The full accessible texts of Liu et al. (arXiv:2610.41927, Algorithm 1 and strong-convexity analysis), Alghunaim (arXiv:2302.00620, LED Algorithm 1 and Appendix A), Yang et al. (arXiv:2407.02689, decentralized Algorithm 3), and Nguyen et al. (arXiv:2210.04757, local gradient-tracking algorithm) were compared by update identity and implications, not just title. In particular, the earlier LED paper already specifies the deterministic update with dual coefficient \(\beta=1/\tau\), which is fully credited. Its graph-only comparison matrix and general rate bounds do not state the exact quadratic first-moment slow eigenvalue \(\mu_*\), and its algorithm does not include the finite-sum table estimator used in the exact stochastic witness. The later LPDVR paper has strongly convex expectation bounds but does not give the fixed-step sharp graph-curvature rate or the finite-budget stochastic witness. The other two papers use different primal and dual or tracking rules. Dedicated search queries and prior-claim comparisons found no covering result. An unindexed equivalent dual-ascent/LED eigenanalysis remains a priority risk, and one potentially related DIGing study was assessed only through its abstract.

## Value — PASS

The structural eigenvalue formula gives a sharp, graph- and curvature-specific communication-rate diagnostic for a method intended to amortize communication with local work. The genuinely stochastic example shows that increasing the local-work budget can *strictly worsen* convergence of the mean disagreement at every budget, despite each extra local step using valid variance-reduced samples; the resulting local-gradient requirement scales quadratically with the budget for a fixed relative reduction. This is a concrete scheduling/design boundary, not a claim that general local updates are always harmful. The exact sample-path variance rules out treating the example as deterministic gradient descent in disguise.

## Scientific limitations and literature risks

The results concern mean dynamics only, with a fixed local gradient stepsize that does not follow the source's \(1/\tau\)-scaling sufficient condition as the budget grows. Mean-square and sample-path convergence, nonquadratic extensions, and performance under other dual coefficients are unproved. LED and other primal–dual methods remain a plausible venue for earlier equivalent exact eigenvalue results that are not indexed by the searches performed. The relevant Wang–Wang local DIGing work was not inspected in full. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
