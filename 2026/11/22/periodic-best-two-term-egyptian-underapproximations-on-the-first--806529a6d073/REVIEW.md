# Independent mathematical audit

## correctness

PASS

Admissibility forces a≥u; for a≥2u the sum is ≤1/u, strictly below the admissible greedy sum with a=u. For each remaining a=u+s the best ordered second denominator is max{a,floor(qa/(5a−q))+1}; the plus-one remains necessary when the residual is a unit fraction. With d_s=5s+4 and X_s=q(u+s), the unordered minimum error is d_s t_s/[X_s(X_s+t_s)] for t_s=d_s−(X_s mod d_s); it is a lower bound on legal error even when ordering is active. For s=0 the numerator is 16 at even u and 12 at odd u. For s=1 the t_s values at u residues 0 through 8 are 4,7,9,1,1,9,7,4,9. Expanding the comparisons in RESULT.md lines 55–82 verifies strict improvement exactly at residues 3 and 4 of u in the unbounded range (the other-case positive cubic is already positive at u=3). For s=2, monotonicity in t_s and parity give the two bounds in lines 84–103; the cross-multiplied differences are 4q²(u−6)(3u+2) and 2q²(u²−24u−21), excluding s=2 for even u>6 and odd u≥25. For s≥3, the coarser lower bound with t_s replaced by 1 in the numerator and d_s in the denominator yields D_u(s); its quadratic coefficient is −80u−16. Both endpoint polynomials are positive from u=34, so concavity excludes every s=3,…,u−1. Legal ordering of T₀ and T₁ in that range follows from d_s<q. The required finite range was independently replayed in exact Fractions: /workspace/branches/fffe1c3d-efa1-4ee2-94fa-74cd16606304/replay_boundary.py with output replay_boundary.txt in the same directory. The small test used 14 candidates; the complete 2≤u≤33 run used 560, found no discrepancy, and reproduced the sole (6,40),(8,15) tie at 23/120 and the two specified exceptions. All boundary winners have distinct denominators. The supplied checker was inspected, not executed, and the additional frozen sample up to u=500 is not needed. Translating the two residues to m and adding the two isolated failures gives density 2/9, excluding the tie where greedy is still best. Finally, coprimality for 2≤p≤4 forces the least positive shift to be at most p−1 (and p=1 has shift 1); for p=5 the shift 4 occurs precisely at q≡1 mod 5.

## originality

PASS

Known exact coverage includes the low harmonic intervals and individual numerator-five targets, notably 5/16 in Chu and in the first-denominator-four catalogue classification. The supported distinct claim is a uniform all-m classification on the full threshold-four ray, with both modulo-nine winner classes, the two sporadic failures and the only tie. Neither the pointwise algorithm nor the checked existence or eventual-greediness theorems supply that uniform result.

## value

PASS

The ray is the first possible numerator at a threshold not covered by the greedy-uniqueness guarantee. An explicit periodic rule with a complete census of nonperiodic exceptions and the unique tie is more useful than pointwise enumeration or additional failure examples: it answers exactly when greedy wins and identifies the true maximizers when it does not. The finite boundary is justified by uniform estimates rather than an arbitrary computational cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
