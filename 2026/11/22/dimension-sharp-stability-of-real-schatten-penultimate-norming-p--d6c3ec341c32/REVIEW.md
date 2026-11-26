# Independent mathematical audit

## correctness

PASS

For every normalized X in the plane, the nuclear norm is at most N, so s_max <= 1+epsilon. Subtracting the other N−1 squares from N bounds each squared singular value below by 1−(N−1)(2epsilon+epsilon²). Thus both the Gram defect and distance to the polar factor are at most delta=3N epsilon. Apply this to A, B and (A+B)/sqrt(2) to obtain a cross-Gram defect at most 4delta. Moving to their polar factors U,V adds at most 6delta to the symmetrized defect, so the symmetric part H of W=U^T V has norm at most 5delta. The commuting skew part K has K^T K=I−H²; its polar factor J is skew and orthogonal, and is within 2||H|| of W. This proves 3 and 33 in spectral norm; the coefficient bound gives sqrt(1098)<34. At epsilon=0 the frame is exactly conformal; conversely every linear combination in such a plane has all singular values equal. For the block witness, the ratio of the small and large block singular values is minimized at the pure skew element, giving epsilon=t/(m−1) exactly. Every conformal target has zero singular-value spread, so the distance from the normalized skew element is at least half its spread, giving the stated lower bound. The strict comparison at proof line 108 is only strict when epsilon>0; it is equality at zero, and the theorem's non-strict bound is valid there. I inspected the checker; its finite angle grid and explicit block examples are diagnostics, not proof of the uniform estimates or of the exact supremum.

## originality

PASS

Pass for the quantitative even-order N≥4 frame and plane stability theorem, including matching order from the explicit family. Not a new Gelfand number or a claim of priority for the scalar optimum, orthogonal complex structures, or the structural ingredients. No inspected statement or implication covers the all-even-order uniform spectral-norm bound together with the matching dimension-dependent obstruction.

## value

PASS

The exact width alone says nothing about how much singular-value imbalance can be hidden in nearly optimal two-planes. The uniform rounding theorem and the construction concentrating the loss on a single real skew block show that distance can be of order N times a very small deficit. This is a sharp stability modulus for a standard matrix-norm extremal problem, useful even without optimal constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
