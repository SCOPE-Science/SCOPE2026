# Independent mathematical audit

## correctness

PASS

For Q=I+L and a selected set S, the nonzero block of the Nyström residual is the Schur complement of K[S,S], namely Q[R,R]^{-1} for R=V\S by block inversion. I used principal-minor determinant quotients to compute every remaining diagonal and hence every trace, without forming K. Exhausting the labeled connected graphs and both sets of argmax ties gives connected counts (1,4,38,728), and both any-bad and all-bad counts (0,0,0,60). Canonical relabeling puts all 60 in the same class, the specified pendant-on-shared-edge diamond (automorphism group of order two). On the specified labels the first pivot is uniquely 0 and its remaining diagonal is (2/7,13/35,46/105,46/105) on vertices 1–4. Independent comparison of all ten traces uniquely minimizes at {0,2}; the two greedy pairs {0,3},{0,4} both have trace 22/23 versus 37/39, giving exactly 7/897 and 858/851. The n=2 case has empty residual trace 0 and no issue with the second pivot.

## originality

PASS

The distinct result is the minimal connected unweighted graph order and complete, tie-independent failure classification at that order, for the unit regularized graph covariance and budget two. Neither general pivoted-Cholesky suboptimality nor the existing theory of greedy graph V-optimality covers this combination of matrix family, rule and quantifiers.

## value

PASS

This identifies a sharp boundary and unique minimal obstruction for a common low-cost surrogate for choosing sensor/landmark columns. The small regret is not the reason for acceptance: the noteworthy fact is that exact optimality holds uniformly, including ties, up to a provable smallest example, then fails for every tie-breaking on that topology. The explicit rational witness and complete nearby census form a concrete regression benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
