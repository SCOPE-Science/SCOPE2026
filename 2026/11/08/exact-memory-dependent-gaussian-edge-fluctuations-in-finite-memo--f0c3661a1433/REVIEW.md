# Review: finite-memory Pólya threshold-graph edge fluctuations

## Correctness

**PASS.** The theorem has explicit quantifiers: fixed \(M\ge1\), \(0<\rho<1\), \(\delta>0\), natural Pólya initialization followed by the specified sliding-window predictive law, and the off-diagonal edge count \(E_N\). A stationary, irreducible, aperiodic \(2^M\)-state history chain makes the martingale conditional-variance averages converge. The martingale innovation is bounded and has the exact variance \(v\mathcal D_M/(1+M\delta)^2\), computed using the Pólya-block pair covariances. Discrete summation by parts transfers the functional martingale limit to the weighted edge count with a deterministic uniform remainder \(O_M(N)\). The limiting covariance and scalar normalization then follow. Exact rational state-space verification across 12 parameter combinations passed 402 assertions. These finite checks confirm algebra, not the infinite limit, which has its own proof.

## Originality

**PASS on the material examined, subject to priority risk.** The 2026 model paper gives finite-memory simulations and explicitly identifies stochastic limit analysis of the finite-memory model as future work. Alajaji–Fuja (1993/1994) already proves the stationary block distribution and ergodicity; Zhong–Alajaji–Takahara (2007) confirms this and studies a more general communications channel. Those precursor statements are fully credited. The new object is the graph-level age-weighted edge count and the exact memory coefficient \(\mathcal D_M\) in a functional Gaussian limit. The old stationary law and a generic finite-state Markov invariance principle give a route to a limit, but do not themselves state its exact polynomial coefficient or graph-indexed Gaussian covariance. Targeted mathematical-record and literature searches identified related threshold-graph findings but no covering statement. Residual risk remains that the coefficient is implicit in an older covariance computation not located in this search; an independent priority assessment has not been made.

## Mathematical value

**PASS.** This resolves a precise question about stochastic properties of the finite-memory model singled out in the motivating paper. The globally important edge density is random under unbounded reinforcement memory but deterministic under any fixed finite memory, with a nontrivial Gaussian fluctuation field in the latter regime. Its exact variance multiplier grows quadratically in memory, quantifying the sensitivity rather than merely giving a qualitative central limit theorem. The fixed-memory restriction and the exclusion of connectivity conditioning are intrinsic boundaries, not claimed results.

## Limitations and nearest sources

The conclusion applies neither to simultaneous growth of memory and graph size nor to graph statistics other than edge count. It does not furnish independent mathematical validation. Closest sources: Yu–Alajaji–Gharesifard, arXiv:2603.18452v1, Sections 4.2 and 5; Alajaji–Fuja, *A Communication Channel Modeled on Contagion*, 1993 technical report, pp. 17–20 (1994 journal version); Zhong–Alajaji–Takahara (2007), especially its finite-memory contagion comparison and stationary law. See `AUDIT.json` for statement-level comparisons and the remaining historical risk.

Self-review: passed. Independent audit: not yet performed.
