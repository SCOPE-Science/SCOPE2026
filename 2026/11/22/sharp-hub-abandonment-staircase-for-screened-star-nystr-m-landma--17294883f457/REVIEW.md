# Independent mathematical audit

## correctness

PASS

For A=μI+L positive definite and G=A⁻¹, the only nonzero residual block is the Schur complement of G_SS in G, which equals A_UU⁻¹. Write q=μ+1, r=m−k and b=μ(μ+m+1)+k. When the hub is selected the unselected principal matrix is qI of size r+1, so E_H=(r+1)/q. When only leaves are selected the remaining hub has Schur complement b/q after eliminating r leaves. The inverse trace is r/q+q/b+r/(qb), with r=0 reducing to 1/(μ+m). Complementary principal minors give D_H/D_L=det A_{U_H,U_H}/det A_{U_L,U_L}=q²/b, also for r=0. As b−q²=(m−1)μ+k−1>0, determinant preference is always strict. Further, E_L−E_H=−∂_μ log(q²/b), since ∂_μ log det A_UU=tr(A_UU⁻¹); differentiating gives exactly [m+1−2k−(m−1)μ]/(qb). Its positive root exists precisely for k≤floor(m/2), and decrements by 2/(m−1) per added landmark. For larger k the numerator is strictly negative on μ>0, including the zero-numerator-at-μ=0 odd-m boundary. Leaf symmetry exhausts both types and gives the binomial counts and ties, and selecting all vertices leaves zero residual. At 0<μ<1 the singleton threshold forces the hub; at budget m keeping that hub leaves a diagonal leaf inverse 1/(μ+1) instead of the smaller hub inverse 1/(μ+m). This proves nonnesting and the exact conditional append-only ratio. Independent exact matrix enumeration confirms all small-m set types, tie counts and determinant comparisons, including every positive threshold tested and the full-budget endpoint.

## originality

PASS

Credit generic Schur-complement/grounded-leader methodology and the indexed all-budget weighted-star result at zero screening. The reviewed contribution is the exact positive-screening all-budget transition and determinant comparison with its growing near-full append-only penalty. The closest screened-cone result has a single-landmark theorem on connected noncomplete walk-regular bases; an unweighted star with at least two leaves has a disconnected edgeless base. No available stronger or equivalent statement covers this positive-screening all-budget combination. Priority remains qualified because the closest weighted-star full text and the Fornace–Lindsey star section were not independently retrievable.

## value

PASS

A canonical sparse graph gives a complete sharp A-type trace versus determinant comparison under a common physically and numerically natural shift. The all-budget result is useful even if only the objective conflict is needed. More importantly it furnishes an exact unbounded worst-case price for preserving a globally optimal first landmark as the budget grows, not just a numerical failure of a chosen greedy algorithm. The qualification that the sequence starts at the trace-optimal singleton is essential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
