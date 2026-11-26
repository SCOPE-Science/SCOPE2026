# Independent mathematical audit

## correctness

PASS

The frozen headline and assumptions overlap the one- and two-update cases: with X_star=e_1 e_1^T and X_0=e_2 e_1^T, exactly one factor is orthogonal, but the right factor is already aligned and W=X_star, so the target is reached in one update, not two. The repaired Finding, scope and proof explicitly give precedence to any aligned factor and reserve exactly two steps for one orthogonal factor and a strictly interior angle on the other side. I rechecked the repaired theorem. The double-orthogonal projection is zero; with exactly one orthogonal and the other strictly interior the first projection is rank one with the orthogonal-side span corrected and the nonaligned opposite span unchanged. In the interior the old-factor Gram off-diagonals are positive and the left dominant eigenvalue is strictly between c^2 and c^2+a^2 d^2. Its slope is strictly between zero and a/c, with the symmetric argument on the right. This yields simple leading singular values, strictly decreasing positive angle sines, and convergence to zero by continuity on the compact region bounded away from double orthogonality. The target-basis Gram entries are exactly ab^2 c^3 and a^2 b d^3. The dominant-eigenvector formula in that basis yields the two cubic angle recurrences with uniform relative errors O(a^2+b^2). The scale deficit is bounded by a^2 b^2 and is negligible relative to the new maximum angle. Negative log angle sums satisfy S_{k+1}=3S_k+o(1) and differences D_{k+1}=-D_k+o(1), giving S_k=C 3^k+O(1) with C>0 by divergence, and D_k=O(k). The log matrix error equals minus the smaller negative log angle up to a bounded term, proving log 3 for the relative double-log precision limit. The correction leaves this interior theorem and the basin intact.

## originality

PASS

The repaired result uses a prior SVD-retracted Gauss–Newton algorithm. Its supported distinct claim is the deterministic full-data rank-one basin and sharp double-log exponent for all interior starts, not the update itself. Rechecking after boundary correction does not change this comparison. The exact two-step condition is not credited as a separate originality claim.

## value

PASS

The repaired all-start classification supplies a deterministic baseline for a published algorithm: it finds exactly when the method is not defined, distinguishes finite termination from the interior dynamics, and gives an exact precision exponent strictly more informative than a local quadratic bound. The different population outcome under orthographic retraction makes the exact SVD analysis useful rather than a mere rescaling or a generic local estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
