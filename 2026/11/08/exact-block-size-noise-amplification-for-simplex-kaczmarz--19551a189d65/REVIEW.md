# Independent mathematical audit

## correctness

PASS

For all d>=2, 1<=k<=d, all fixed observed responses b and deterministic starts, unit regular-simplex Gram spectrum gives A^T A=(d+1)/d I and ker A^T=span{1}. A size-k block has Gram eigenvalue (d-k+1)/d along its ones vector. Thus the forcing z_S=delta d/(d-k+1) sum_{i in S}a_i lies in the selected row span and is pointwise orthogonal to Q_S e. Permutation invariance and rank give E Q_S=(1-k/d)I; E z_S=0 and E z_S z_S^T=delta^2 k/(d-k+1)I. The conditional Pythagorean recurrence yields exactly E||e_t||^2=(1-k/d)^t||e_0||^2+delta^2 d^2(1-(1-k/d)^t)/(d-k+1); the centered-start covariance equals delta^2 d(1-(1-k/d)^t)/(d-k+1) I. Checks include k=d (alpha=0), delta=0 and t=0. Independent rational projector/shift calculations for all subsets for d=2..5 and all k agree; they corroborate rather than replace the all-d proof.

## originality

PASS

Best-of-knowledge PASS for the simultaneous all-k exact finite-time mean, second moment, centered covariance and strict d-factor stationary block-size reversal on a regular-simplex frame. Gan and Wu derive general convergence-neighborhood estimates for doubly perturbed block Kaczmarz, but accessible abstract and PDF preview do not establish the exact all-subset simplex identity. Needell–Tropp use a fixed row paving; Needell–Zhao–Zouzias add residual correction. All exact formulas remain subject to a material priority risk: Gan–Wu full text was not accessible, and authorized institutional retrieval returned vpn_disconnected. A failed search alone is not novelty evidence.

## value

PASS

PASS: uniform block size is a natural algorithmic tuning parameter on the canonical minimally redundant tight frame. The exact conditional equality and covariance quantify a dimension-unbounded noise-floor tradeoff absent from general upper bounds; the result fixes both data and least-squares target while changing k. This is a motivated, sharp all-d family, not a generic performance promise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
