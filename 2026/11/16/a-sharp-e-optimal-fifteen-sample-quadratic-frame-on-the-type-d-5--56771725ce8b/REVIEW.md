# Self-review

**Final claim reviewed:** The complete E-optimal fifteen-sample quadratic frame classification on the twenty type-\(D_5\) projective root directions, including common squared determinant, exact smallest-eigenvalue trichotomy, counts and geometric optimizers.

## Correctness — PASS

The domain is all real symmetric \(5\)-by-\(5\) matrices with Frobenius norm; the precise sample directions and unweighted operator are specified. A fifteen-row invertible selection must select both signs for exactly five edges of \(K_5\), and its doubled-edge graph must be connected odd-unicyclic. Row sum/difference reduction yields unsigned incidence determinant magnitude \(2\), so every invertible squared Gram determinant is \(1/256\). Graph enumeration has four unlabelled classes of respective labeled counts \(12,60,30,60\); each has \(32\) possible singleton signs. The Schur-complement polynomial is derived directly from the coefficient blocks. Four independent rational fifteen-row Gram characteristic-polynomial comparisons and exact rational Sturm root counts establish the optimal two graph shapes and their sharp shared quartic root. `verify_exact.py` replays these checks; `verify_numeric.py` separately evaluates all \(5,184\) nondegenerate selected operators. No infinite-dimensional extrapolation is claimed.

## Originality — PASS, qualified historical priority

The inspected 2023 Xiao–Zhuang manuscript treats spherical designs and framelets, not this prescribed type-\(D_5\) E-optimal measurement selection. Monfared–Mallik establishes the signless graph-Laplacian determinant framework; the current graph criterion is not presented as an original general combinatorial principle. Previously published cuboctahedral rank/erasure work treats a different fixed grid in three dimensions, and a perfect-matching Walsh sampling theorem already captures related odd-unicyclic determinant and D-optimal basis phenomena. Those results do not give the present four exact \(15\)-row Gram spectra, three least-eigenvalue levels or two E-optimal geometric classes. Searches for equivalent quadratic matrix tomography, projective root measurements, graph-incidence designs and implied E-optimality identified no specific encompassing theorem. A specialist historical table or a spectral equivalence that was not indexed remains a real priority risk.

## Mathematical value — PASS

Fifteen samples are the information-theoretic minimal number to recover a general symmetric \(5\)-by-\(5\) matrix. The twenty candidate directions form a standard root-system orbit. The striking phenomenon is that all \(5,184\) available bases have **identical volume**, so determinant optimization cannot distinguish them, whereas the exact least eigenvalue separates three stability levels, and precisely \(2,304\) are sharp E-optimal. This supplies a fully classified natural minimal-sampling stability benchmark; it neither claims general weighted-optimality nor universal spherical-design performance.

## Unresolved limitations and comparison risk

The claim is for this explicit finite set and the Frobenius-normalized unweighted model only. Root-line phase signs are irrelevant to quadratic evaluation except as the two distinct \(e_i+e_j\) and \(e_i-e_j\) directions. The exact determinant graph identity uses established signed-incidence ideas, and direct root-system/projective-design tabulations could potentially contain an equivalent E-optimal result. The additional generality of unrelated frame constructions cannot be inferred to prove this particular discrete spectral trichotomy without a concrete reduction.

Self-review: passed. Independent audit: not yet performed.
