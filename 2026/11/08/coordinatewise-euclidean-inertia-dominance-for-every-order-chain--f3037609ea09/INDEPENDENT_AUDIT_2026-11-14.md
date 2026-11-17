# Independent mathematical audit

## correctness

PASS

The actual RESULT.md proves the transfer map is piecewise triangular with unit Jacobian, so couples uniform order/chain volume. Conditioning on all other coordinates makes X_v uniform on [L_v,U_v] and Y_v uniform on [0,U_v−L_v], giving covariance exactly by total variance. Order-polytope lattice closure makes its uniform density MTP2; FKG implies covariance≥0. Conditional slices ordered by X_v satisfy Holley cross-lattice inequality, making ℓ(t)=E[L|X_v=t], ν(t)=E[U|X_v=t] monotone and nonconstant when v has both a predecessor and a successor. Strict Chebyshev covariance then yields strictness; at extreme vertices one endpoint is constant. Equal-volume linear-extension simplices with Dirichlet order statistics establish the rational formula and the 1/80 chain example. Independently recomputed exactly the three-chain gap 1/80; source check_order_chain_inertia.py enumerates 5230 naturally labeled posets to n=6 and 250 n=7 cases, not a universal proof.

## originality

PASS

No directly dominating all-poset uniform-interior-volume coordinate-variance theorem was identified. The FKG/Holley inequalities and Stanley transfer are prior tools; a published layered-poset exact inertia identity is a special case, while vertex-cloud variance and edge-length comparison involve different measures or objects. Originality is best-knowledge, not an exhaustive priority certificate.

## value

PASS

A uniform-volume metric monotonicity for the two canonical polytopes of every finite poset, with exact per-coordinate strictness and a structural height-two equality classification, is a natural cross-polytope invariant and useful beyond specific enumerated posets. It is neither vertex-count bookkeeping nor a finite numerical census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
