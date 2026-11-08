# Scientific review of the sharp composite gap

## Correctness
**PASS.** Multiplicative prime-power formulas split every composite into the squarefree, prime-cube, or cube-free nonsquarefree cases. Each case has an explicit strict estimate except \(n=4\), for which direct evaluation gives exactly \(4^k+3\). The only non-elementary numerical identity used is the classical Euler product \(\zeta(2)^2/\zeta(4)=5/2\), and the necessary comparisons hold uniformly at the boundary \(k=2\). A direct-convolution integer verifier corroborates all \(2\le n\le10000\) for \(2\le k\le8\).

## Originality
**PASS, with residual historical-priority risk.** Liu, arXiv:2609.33278v2, proves that the detector vanishes only on primes for integer \(k\ge2\), but does not determine its minimal nonzero composite magnitude. The published analysis *Sharp parameter stability for mixed Dirichlet-inverse prime criteria* establishes a stronger sign lemma for one factorization case and a real-parameter zero-set interval, not the exact global minimum or unique extremizer. These precursors and their proof techniques are acknowledged rather than presented as new. Exact-constant and equivalent-form searches yielded no stronger result; absence of a match cannot certify priority.

## Mathematical value
**PASS.** The prime-detector was introduced precisely to distinguish prime inputs from composites. The closest composite to zero and exact separation magnitude are canonical, quantitative invariants of that detector, not an arbitrary finite slice. The theorem supplies an optimal uniform error margin (at each fixed \(k\)) and uniquely identifies the most nearly vanishing composite across the infinite domain, strengthening qualitative nonvanishing without claiming algorithmic speed.

## Limitations
The detector has a composite zero at \(k=1\); the result makes no assertion there. The proof depends on the classical Euler-product inequality and standard local identities, not on an external computational certificate. Finite verification cannot replace the unrestricted proof. Earlier equivalent unpublished or unindexed statements remain possible; independent audit is not performed.

Self-review: passed. Independent audit: not yet performed.
