# Independent mathematical audit

## correctness

PASS

All used edges meet zero isolated vertices, so subtracting E_t only from the zero-isolate class counts unused sets exactly. The drift of D_t=I_t-rN_t is -qkD_t/N_t plus the used-edge fraction correction. For deterministic sufficiently large t on N_t≥pt/2 the used-edge correction is O(t^(1-k)) and exhaustion is impossible; off that event define the correction from the actual null-step drift, which is bounded, with exponentially small event probability. In the second- and fourth-moment expansions the principal drift terms are nonpositive. On the good event the correction contributes at most O(1) and O(1+D_t²), respectively (use |D_t|≤N_t=O(t)); on the bad event its polynomial bound times the Chernoff probability is summable. This gives E D_t²=O(t) and E D_t⁴=O(t²); the former also gives D_t/t→0 almost surely by Borel–Cantelli on t=m² and bounded increments between those times. The asymptotic increment of D is 1-r on birth and −Bin(k,r) on an edge step, centered by the true conditional mean; its variance is p(1-r)[2+(k−2)r], and its covariance with the centered birth indicator is p(1-r). Replacing N_t by pt in the damping term costs O(t^−1) in L² by Cauchy–Schwarz with the fourth moments of D_t and N_t−pt, and by the same concentration split. Starting at a deterministic index >a=kq/p, the recursion uses weights in [0,1] tending uniformly to (j/t)^a away from j/t=0; the omitted initial segment is O(ε) in normalized quadratic variation when j≤εt. The accumulated L² error is O(log t). Bounded martingale increments verify the triangular-array Lindeberg condition, and integration of the predictable covariances yields the factors 1/(1+a)=r and 1/(1+2a)=r/(2−r). The same deterministic weights and martingale orthogonality give covariance convergence, separately from weak convergence. Returning from D to I gives all displayed entries, including (1/4,5/32,41/224) for k=3,p=1/2. Conditional edge-count randomness makes the innovation covariance positive definite; weighted integration and the invertible final coordinate change preserve it. The frozen rational checker and optional simulation were inspected, not executed; their finite tests are diagnostics, not needed in this proof.

## originality

PASS

The closest growth-model source explicitly leaves isolation fluctuations uncomputed; general martingale machinery supports the proof but does not give the particular transition, its second-order coefficients or normalized moment convergence without this analysis. No inspected prior result covers the full covariance or the precise joint theorem.

## value

PASS

The model's motivating paper isolates this variance as a missing second-order quantity. The theorem supplies that coefficient and the otherwise lost cross-covariance with the expanding, random vertex pool, so it is useful for interpreting singleton counts and proportions at the true fluctuation scale. It applies to both percolation regimes without invoking a component law. The contribution is the exact all-parameter matrix and the limit in the stipulated process, not a new martingale CLT or a giant-component fluctuation theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
