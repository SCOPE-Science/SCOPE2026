# Independent mathematical audit

## correctness

PASS

Gaussian column-space invariance makes P a uniform rank-k projector (one can choose positive diagonal R for Haar Q; P is unaffected by QR sign conventions). Rotating e_i against the projected coordinate subspace gives B=P_ii with the stated beta law for k<n. Idempotence gives squared off-diagonal length B(1-B). The stabilizer of e_i acts transitively on directions at that radius, so the conditional direction is uniform and independent of B. The error divided by h_i is sqrt(D/Y) U, with independent chi-squares D,Y of n-k and k degrees and independent spherical coordinate U. Write Z=sqrt(R)U, with Gaussian radius R~chi-square(n-1) independent of U, and independently V with beta shapes (n-k)/2,(k-1)/2. Then VR has law D and is independent of U,Y; this proves the independent attenuation representation. Conditional Gaussian regression against the i-th row gives Z/sqrt(Y) for the iid comparator. Strictness follows from its positive absolute density and 0<V<1. Gamma integrals give the moment formulas, including the divergent boundary through the inverse chi-square. For the tail ratio, regular variation of the Student tail gives pointwise limit V^(k/2), while the conditional tail ratio is bounded by 1, justifying dominated convergence. The zero-row, single-probe and full-basis cases are covered (mean and MSE thresholds apply only to nontrivial errors). The frozen NumPy checker and verification note were inspected, not replayed; quantile simulation is corroboration, not the distributional proof.

## originality

FAIL

The distinct indexed real rank-one least-squares sketch theorem 3e196d12ddfb is strictly broader and covers the allegedly additional independent beta attenuation and its threshold, moment and tail consequences by an exact reduction. The nontrivial range 2<=k<n is fully covered. The remaining endpoints are immediate identities. This is a scientific coverage decision, not a finding of historical priority, copying or record identity; the comparator is catalogued later than the frozen path.

## value

PASS

The mathematical law is useful: at the same probe count, exact one-coordinate quantile improvement and unchanged heavy-tail moment thresholds distinguish quantile and mean-square risk, which are natural metrics for diagonal estimation. This is value of the law and its application, not credit for a new theorem beyond the indexed rank-one result or justification of simultaneous risk improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
