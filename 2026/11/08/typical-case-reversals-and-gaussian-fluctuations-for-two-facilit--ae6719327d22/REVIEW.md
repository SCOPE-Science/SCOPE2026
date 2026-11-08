# Scientific review: two-facility typical-case comparison

## Correctness (C): PASS

The result distinguishes conditional expected cost from the noise of selecting a facility pair. The empirical measure formulas are exact even with repeated reports. For a uniform population the two-site service integral, distance-degree function, and Proportional division give \(T_P=-1/18+7\pi/96\), while the optimum per agent is exactly \(1/8\). The V-statistic contamination calculation gives explicit first-order polynomials; the empirical two-median value has the unique-optimizer influence \(g_{1/4,3/4}-1/8\). Rational integration of the resulting ratio influence gives variance \(147113/504000\). The finite exact checker tests both mechanism definitions against replicated three-site masses; the asymptotic proof uses the iid central limit theorem and stochastic equicontinuity rather than extrapolating from experiments. Risk: the CLT depends on the stated smooth population optimum and is not claimed for general distributions or ex-post cost.

## Originality (O): PASS, qualified

The primary works of Ma–Peng (arXiv:2608.09061, August 10, 2026), Jia (arXiv:2608.19633, August 20, 2026), and Chan–Lin–Wang (arXiv:2608.22484, August 23, 2026) define the same distance-weighted pair mechanism and prove worst-case approximation and strategyproofness. The already-known Global Pair uniform-sample \(7/5\) mean, implied by a general Product-Gap Dirichlet law, is specifically **excluded** from the novelty claim. The genuinely assessed conclusions are the exact Proportional \(\pi\)-constant and mechanism ranking, the sharp three-site reversal, and the variance of the sample-conditional empirical approximation ratio. Targeted text and research-record searches yielded no equivalent claim; broad empirical-process theorems provide tools but no computed mechanism-specific constant. Residual risk: an unindexed average-case mechanism analysis or unpublished application of these methods may cover the same statements. The record search alone cannot establish uniqueness.

## Value (V): PASS

A small but strict typical-case welfare preference for the older mechanism runs counter to the worst-case motivation for mixing in the 2026 papers; the three-site mass-threshold theorem shows why such a choice is population-dependent, rather than an arbitrary isolated numerical comparison. The rational Gaussian variance quantifies population sampling uncertainty in that comparison and is distinct from pair-selection noise. These are directly interpretable, exact mechanism performance benchmarks, not a relabeling of the existing worst-case results. Limits: they do not optimize over all strategyproof mechanisms or all sampling distributions.

Self-review: passed. Independent audit: not yet performed.
