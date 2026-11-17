# Scientific review: sharp rooted-tree variation sensitivity of Euclidean ball projection

## Correctness — PASS

The anchored incidence matrix is invertible, its inverse columns are subtree indicators, and the Euclidean-ball projector has the radial tangent derivative \(R(I-uu^\top)/\|x\|_2\) outside. The symmetric rank-two eigenvalue identity produces the exact signed dual maximum. The uniform bound \(\|D^\top s\|_2^2\le\sum_v(1+d_v)^2\) is attained simultaneously at every vertex by alternating-depth signs. The root column then gives the largest subtree norm, completing the exact constant. Derivative integration gives a global bound and strict finite-pair nonattainment, while a boundary-approaching explicit tangent witness proves sharpness. The two extremal rooted-tree structures follow from exact integer child-count squares. Exhaustive and numeric checks in `verify.py` support, but do not replace, these steps.

## Originality — PASS, with a historical priority caveat

The 2015 full-text tree-TV reference analyzes energy minimization with edge penalties, not the Lipschitz modulus of projection onto a global Euclidean ball in the anchored tree norm. Thele's 1974 and de Figueiredo–Karlovitz's 1967 radial results use the same norm for the radial ball and for sensitivity, so their known framework does not give the cross-norm rooted-tree formula. Previously indexed planar cross-norm Euclidean disk results likewise do not cover arbitrary finite rooted trees or the degree-square extremal law. Searches for radial projection, rooted graph TV and mixed-norm Lipschitz analogues found no directly dominating statement. Full access to two classical radial articles was unavailable, so independent historical priority checking is still advisable.

## Mathematical value — PASS

The result gives a natural exact stability coefficient for Euclidean clipping of graph signals under anchored total variation. The same operation is Euclidean-nonexpansive, but has a sharp all-tree instability governed only by child degrees: \(\Theta(n)\) for paths and \(\Theta(n^{3/2})\) for stars. The complete rooted-tree extremal classification, nonattainment of the sharp pairwise modulus, and explicit near-boundary witnesses distinguish the finding from a numerical example or a generic norm-equivalence bound.

## Limitations and comparison risks

The result is for real signals on finite, unweighted rooted trees, with centered Euclidean balls and the specified root anchor. It is neither a weighted-tree theorem nor a statement about the unanchored graph-TV seminorm. The proofs are analytical; the checker only covers finite diagnostics. The accessible material for the classical radial Banach-space papers was abstract/bibliographic level, which cannot exclude all alternative earlier formulations.

Self-review: passed. Independent audit: not yet performed.
