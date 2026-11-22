# Scientific review: sharp squared-SLEM rigidity on a path

## Correctness — PASS

The proof reconstructs the feasible symmetric stochastic tridiagonal kernels, gives the normalized cosine mode, and verifies the exact nonnegative dual-slack identity with strict interior equality conditions. Squared spectral norm control yields the global energy estimate; the complete alternating-mode diagonalization checks that the constant is attained and precisely identifies equality. Centered partial sums provide the coordinate recovery bound, and the alternating family witnesses the optimal square-root exponent. The analytical proof includes all lengths \(n\ge3\), all admissible zero edges and boundary weights. The standalone finite checker passed on 4,899 matrices, but is not an infinite proof.

## Originality — PASS on inspected evidence

The exact path optimizer and value are established by Boyd–Diaconis–Sun–Xiao (2006); the general graph framework is Boyd–Diaconis–Xiao (2004). Fill–Kahn (2011) provides time-by-time mixing comparisons from designated starts. None of the inspected relevant claims states the sharp squared spectral *remainder* for arbitrary nonuniform path weights, its iff alternating equality family, or the quantitative edge recovery with sharp exponent. Searches considered formulations through tridiagonal kernels, absolute spectral radius, parameter inverse stability, dual inequalities, and alternating weights. The available indexed crown-graph stability finding is for a different graph, and does not logically dominate the path-specific sharp identity. Publication priority is not independently established; uninspected general semidefinite error-bound results may contain equivalent statements.

## Value — PASS

Fastest-mixing path weights are a basic design model for load balancing. This global inequality is a quantitative performance-to-design guarantee, not merely a restatement that uniform edge weights are optimal: the sharp energy coefficient, complete equality family, all-edge recovery bound, and proof that a square-root rate is unavoidable are structural information. The statement compares *every* admissible edge-weight vector and has a concrete operational interpretation in diagnosing near-optimal mixing designs.

## Scientific limitations

The setting is symmetric, uniform-stationary and path-supported; no directed or general-graph result follows. Pointwise edge-recovery constants may be conservative, although the energy coefficient and recovery exponent are sharp. The complete original five-page path theorem was inspected, while the full 23-page general-graph SDP article and every piece of subsequent literature were not. The numerical checker supplies only finite supporting tests.

Self-review: passed. Independent audit: not yet performed.
