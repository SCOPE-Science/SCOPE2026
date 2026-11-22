# Review: short- versus long-horizon heat-trace design on paths

## Correctness — PASS

For each \(n\ge4\) and \(B>0\), strict convexity of the spectral exponential trace proves uniqueness for every \(t>0\). The uniform small-time expansion reduces the first weight-dependent term to a strictly positive quadratic form; its tridiagonal linear system is solved explicitly, and its entries are positive. For the long-time limit, a centered linear test vector gives a universal spectral-gap bound, while a degree-preserving polynomial argument verifies the full eigenvalue spectrum of the parabolic design. Equality in the Rayleigh bound forces the unique allocation, and the exponential spectral estimate transfers this to the heat-trace limit. The first-neighbor priority reversal and the Riemann-sum limit \(6/5\) follow without relying on finite computation. The standalone checker replays 1157 finite tests. It cannot certify the quantified infinite theorem independently.

## Originality — PASS on inspected evidence, qualified

A full published reversible-path spectral-gap theorem gives the parabolic long-horizon optimizer under more general prices and masses. That optimizer and its uniqueness are **prior**, not a new result here. The closest published path-cap theorem also contains its uncapped specialization. Neither inspected complete `RESULT.md` states the short-horizon tridiagonal boundary-layer profile, a crossing of optimal edge priorities for heat-trace designs, or the limiting \(6/5\) second-moment penalty. The inspected foundational path mixing, electrical-resistance optimization, and continuous-time synchronizability papers use distinct objectives or constraints. Actual full-record retrievals and targeted primary-text inspections are described in `AUDIT.json`. An unindexed equivalent finite-horizon design theorem cannot be excluded, and older foundational spectral-gap literature is not claimed as new.

## Value — PASS

A single natural budgeted diffusion network can demand opposite edge-priority decisions depending on the measurement horizon. The theorem classifies both limiting allocations for *every* path order, proves the existence of a genuine intermediate crossing without artificial graph slices, and quantifies a nonvanishing 20-percent penalty in the physically motivated first design-sensitive short-horizon coefficient when a long-horizon-optimal design is reused. The alternating exponential boundary correction also identifies the precise spatial structure behind short-time optimization. No complete finite-time transition diagram or general-network extension is claimed.

## Scientific boundaries

Only undirected unnormalized continuous-time Laplacians on paths with nonnegative edge rates and one total linear budget are covered. The theorem does not prove one crossing only, global monotonicity of weights, or finite-time closed formulas. The penalty is a ratio of second Laplacian moments, not a ratio of the heat traces. Publication novelty remains qualified pending independent literature review.

Self-review: passed. Independent audit: not yet performed.
