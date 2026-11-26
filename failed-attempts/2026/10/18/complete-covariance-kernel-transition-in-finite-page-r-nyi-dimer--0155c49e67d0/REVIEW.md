# Independent mathematical audit

## correctness

PASS

A covariance null vector is exactly a linear form constant on the positive-probability support. At positive finite time the all-late and unique-early events have positive probability, yielding zero and all single-dimer vectors. These are enough to force a_i+a_{i+1}=0, and every realized matching is balanced across the bipartition. At jamming all and only maximal matchings appear: any given maximal matching can have its disjoint edges tried first with positive probability. Every maximal matching covers both sites 2 and n−1, and the alternating relation persists. The listed n=4..7 supports give affine ranks 1,2,3,4; the determinant witnesses are valid. For n≥8, conditioning on inclusion of the first, respectively last, edge leaves a full maximal-matching support on the remaining length n−2 path. The two induction restrictions agree on the alternating multiplier at site 3 and jointly cover all sites except 2 and n−1 (the only possible internal exception clash would be 4=n−3). This proves there are no other null directions. A restricted principal submatrix is positive definite exactly when no nonzero full null vector is supported on its retained indices, giving the deletion consequences. At t=0 all indicators are deterministic. Exact independent replay: python3 /workspace/reproductions/frozen_checks.py 3 enumerates all edge orders for each n=4..8, forms rational full covariance matrices at the binomially mixed half-arrival prefix and at jamming, and checks ranks, null relations and all stated principal-minor selections. Finite and jammed rank sequences were (3,4,5,6,7) and (1,2,3,4,5); this is finite corroboration.

## originality

FAIL

The decisive terminal support question is covered by Tural's exact tree maximal-matching polytope: after restriction to a path the affine hull follows immediately from the two leaf equalities and a point strict in every other inequality. The early rank in Gerin's known exponential random-priority model follows from the positive-probability empty and single-edge events and the fixed bipartition equation. Combining these two mechanical implications gives the entire transition, even though neither source prints it as a covariance theorem. Unavailable historical texts are not the reason for failure.

## value

FAIL

The full positional-rank question is natural and the path induction is correct, but the endpoint affine constraints are directly extractable from the prior exact tree polytope. The finite-time half of the transition is an empty/single-edge support check, and the principal minors are standard PSD restrictions. Neither narrowing to that finite-time rank nor repackaging the terminal calculation yields a distinct worthwhile claimed invariant. No repair is submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
