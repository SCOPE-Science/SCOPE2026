# Scientific review of the two-parameter sink-side law

## Correctness — PASS

The exact generating function follows by the unique reverse sink-layer decomposition into alternating labeled nonempty blocks. Acyclic orientations have at least one sink and, in a complete bipartite graph, all sinks lie in one vertex class. The marked last-block exponential numerator follows from an explicit geometric series; the all-orientation coefficient matches the classic poly-Bernoulli count. For every fixed positive sink multiplicity, the denominator is identical to that in Khera–Lundberg–Melczer (2019/2020), which proves strict minimality and provides the smooth critical-point transfer with positive curvature for arbitrary bounded positive part-size ratios. The nonvanishing numerators therefore enter only through their values at the same saddle. The two limiting side-specific mass functions sum to one, establishing total-variation convergence. The included checker confirms the finite formula against 15 independent exhaustive DAG enumerations and 81 total-count identities. The checks are finite, and the asymptotic claim is proved analytically rather than inferred from them.

## Originality — PASS, qualified

Cameron et al. (2014) and Khera–Lundberg–Melczer (2019) establish the graph enumeration and the underlying generic multivariate asymptotic method, not this joint mark. Ayyer et al. (2020) enumerate unique-sink orientations but not the distribution for all sink counts in a growing unequal bipartition. Hwang et al. (2019) give a general sink polynomial and chromatic-symmetric function formulas without this specialized unequal-class limit. Khera–Lundberg (2024) study longest paths. A previously indexed balanced-case theorem already establishes the single zero-truncated Poisson limit for equal part sizes, which this work expressly excludes from its novelty claim. The unequal-ratio joint law, side weights and strictly mixed distribution were not found in relevant published comparisons. The generic transfer theorem makes the analysis possible but does not by itself supply the exact marked combinatorial numerator. Uninspected early articles remain a historical-priority risk.

## Value — PASS

The number and location of sinks measure termination/bottleneck structure in directed acyclic bipartite networks. The natural balanced model conceals the distinction between two possible sink classes; under a fixed unequal density, the statistic has a genuinely two-component limiting law, not just a shifted zero-truncated Poisson parameter. The explicit sink-side weights and full mass function quantify the qualitative asymmetry and remain useful for random dependency graphs and lonesum-matrix endpoint classes. This is a distributional classification, not an arbitrary numerical slice or a routine bound on an already computed statistic.

## Closest literature and limits

The main analytic building blocks are [Cameron et al., arXiv:1412.3685] and [Khera, Lundberg and Melczer, arXiv:1912.08850]. The strongest directly adjacent claims are Ayyer–Hathcock–Tetali's unique-sink enumeration (arXiv:2010.11236) and the previously published equal-class sink limit; the latter agrees exactly with the \(\rho=1\) specialization and is not recast as novel. The proof does not provide a rate in total variation or a result for strongly unbalanced ratios tending to zero or infinity; some older sources were inaccessible in full. General originality cannot be proved by a database search, and independent mathematical validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
