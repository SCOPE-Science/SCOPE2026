# Scientific review: exact two-clock Bernoulli collapse

## Correctness — PASS

The reduced odd-numerator representation is bijective with the specified normal/subnormal IEEE-style number set, including all exponent extremes. The modular doubling update lowers its reduced denominator exponent by one; the corresponding depth is exactly the first zero time. Exhaustive odd-numerator counts give the hitting histogram, and constructing a predecessor by adding powers of two to the denominator proves the full image-set description. Summing these finite counts gives the support and equal-state distribution, including agreement at both piecewise boundaries. `check.py` independently constructs exponent-significand values and compares the complete exact hitting histogram and all image sets for 43 formats covering 18,789 initial numerical states, including every binary16 value in the interval.

## Originality — PASS within inspected evidence

Ah-Weng and Coveney, arXiv:2611.15344v1 (11 November 2026), numerically track support for four maps and report 149-step collapse for doubling but do not derive arbitrary-precision exact first-hitting histograms, the entire support sequence, or the distinction between support and uniform-over-floats absorption clocks. Boghosian, Coveney, and Wang (2019) give the well-known eventual zero pathology; Klöwer et al. (2023) study low-precision periodic orbit pathologies and explicitly report the binary32 state-space count of 1,065,353,216; neither that count nor eventual collapse is claimed as new. The most relevant published mathematical-search records concern non-integer beta shifts, logistic finite-precision maps, and finite grids, not this complete floating-point transient law. Negative searching does not certify uniqueness; the remaining risk is an unindexed equivalent count in finite-arithmetic or numerical-chaos literature.

## Mathematical value — PASS

Both diagnostics here—number of reachable computer states and probability already absorbed under equal-state initialisation—are natural exact finite-state dynamical invariants directly motivated by a recent study of statistical reliability. Their different transition clocks, together with closed formulas at every time and every binary precision/exponent range, give a non-asymptotic benchmark capable of distinguishing support loss from mass concentration. The theorem is elementary once the correct dyadic state representation is isolated, but the complete two-clock law is not merely a restatement of eventual collapse or a finite numerical table.

## Scope and limitations

Arithmetic must be exact doubling with gradual underflow; no general finite-precision chaotic map is classified. Uniform-over-floats is not continuous-uniform sampling. Exhaustive numerical enumeration includes binary16 but not binary32 or binary64; the latter are covered by the symbolic proof. Potential historical equivalences not indexed in the searched literature remain possible. The 2023 full publisher PDF was not accessed; its public full-text indexed excerpts, metadata and abstract were compared, so that work remains a stated uncertainty.

Self-review: passed. Independent audit: not yet performed.
