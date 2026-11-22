# Self-review

## Correctness: PASS
The kernel is the nondegenerate stationary AR(1) covariance. Its conditional-variance formula is established by direct two-site inversion plus the Markov property. All sums, finite boundaries, and strict separation of pivots are given. The uniform expansion uses \(n(1-\rho_n^2)\to0\), and global convergence follows from a strictly convex continuum objective on a compact triangle. The minimax and maximin greedy endpoints are checked carefully: the *maximum* limiting greedy loss occurs at a first pivot at an endpoint **or the midpoint**, not only at an endpoint. Exact rational program checks provide corroboration without substituting for proof.

## Originality: PASS on checked sources, with residual risk
The tested statement is the sharp \(5/4\)-to-\(5/3\) two-pivot diagonal-greedy trace-loss interval on stationary exponential Toeplitz kernels in the joint large-size/high-correlation limit. Liu–Matthies (2015) specifies the greedy mechanism, and Chen–Epperly–Tropp–Webber (2024) recognizes generic first-pivot tie problems but does not provide this family or its sharp ratio. Mukherjee (2002) and Baldi Antognini–Zagoraiou (2010) treat OU optimal prediction designs: their broader design question could cover the *unrestricted* two-point optimum, which is credited and not itself claimed novel. The sharp **relative penalty under the diagonal-greedy constraint** is not given by the inspected material. Their inaccessible full texts remain a material source-priority risk; this judgment is not proof of uniqueness.

## Value: PASS
Constant kernel diagonals make the initial diagonal-greedy decision completely indifferent, so tie handling is an algorithmically natural concern. The fact that even the best possible tie break incurs at least a 25% asymptotic trace-error penalty and that a determinant-optimal endpoint pair incurs 66.7% supplies a sharp benchmark for subset selection in a standard Markov covariance family. The conclusion is limited to two columns and the specified double limit; no universal low-rank error claim is made.

## Literature comparison and limitations
Liu–Matthies arXiv:1505.06195 is read as a primary full-text source. The open-access full text of Chen et al., doi:10.1002/cpa.22234, was inspected, notably its discussion of ties and the comparison of greedy and randomized pivoting. Harbrecht et al., doi:10.1016/j.apnum.2011.10.001, was available only as a repository abstract. The Mukherjee dissertation record (2002) provided an abstract but not the dissertation text; the 2010 optimal-design paper was accessible at abstract level. This is a qualified self-review rather than independent priority certification.

Self-review: passed. Independent audit: not yet performed.
