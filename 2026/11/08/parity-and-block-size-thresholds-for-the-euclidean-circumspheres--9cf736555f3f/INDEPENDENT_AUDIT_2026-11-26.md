# Independent mathematical audit

## correctness

PASS

The path edge-incidence constraints on block sums give an integral stable-set polytope: signing the columns by bipartition turns the transposed edge-incidence into oriented incidence, with the coordinate bounds preserving total unimodularity. A convex decomposition of the sums lifts by conditional choices with probabilities x_ij/s_i, and each resulting colored independent-set indicator is a vertex since it is a cube vertex. At a block-constant trial center with block masses p_i, direct expansion gives the common baseline sum p_i^2/a and weights 1-2p_i/a. For even m and a>1 the largest objective is the maximum independent support size k; compressing the k ordered positions gives k+1 supports. At a=1 all weights vanish and the independent-set recurrence gives F_(m+2). For odd m and 1<a<=m+1, the proposed h and ell balance (k+1)w_o=k w_e. The positive alternating edge multipliers sum to the corresponding weight at each vertex, so equality requires exactly one occupied endpoint on each edge and forces one of the two alternating supports. This includes a=m+1, where ell=0. Above it the same edge multipliers dominate the even weights strictly, so only the odd alternating support reaches equality. Uniform coordinate choice on the stated supports (with a mixture giving the candidate block masses) puts their barycenter at the center. The variance identity proves the claimed radius and uniqueness against every other center, and strict convexity rules out nonvertex contacts. Both odd radius expressions agree at the threshold; substituting h gives the first branch, and the all-odd mixture gives the second. An independent bounded calculation compared exact coordinate distances and contact counts at 49 parameter pairs, 245593 colored vertices and 491501 rational assertions, including each of m=3,5,7 at and beyond a=m+1. It used separately constructed colored independent sets and exact rational distances; no separate durable replay script was delivered for that check. The source's verify.py and VERIFICATION.md were inspected, not executed; their recorded tests corroborate, but do not replace, the all-parameter proof.

## originality

PASS

The path block polytope, colored stable-set structure, and general algorithms for enclosing spheres are known; the a=1 sphere is standard binary geometry and the simplest graph slices overlap other exact results. The supported distinct theorem is the all-block-size parity classification, in particular the odd saturation a=m+1 and the complete equality families on both sides and at the boundary. The strongest inspected same-family or same-invariant statements do not give this transition. Same-day ordering is not inferred.

## value

PASS

This determines the precise Euclidean center, radius and extremal supports for a natural colored path family. In the odd case the center reaches the boundary at a=m+1 while both contact families still remain; only above it does one family disappear. That distinction, the exact counts and the all-parameter classification provide meaningful information beyond stable-set integrality, a generic optimization algorithm, or the standard cube-center argument for a=1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
