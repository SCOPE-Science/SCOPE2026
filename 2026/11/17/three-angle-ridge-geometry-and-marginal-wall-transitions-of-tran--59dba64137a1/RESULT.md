# Three-angle ridge geometry and marginal-wall transitions of transportation polytopes

## Finding

Let \(m,n\ge3\), let positive row margins \(a_1,\ldots,a_m\) and positive column margins \(b_1,\ldots,b_n\) have common total \(T\), and equip the affine transportation polytope
\[
\mathcal T(a,b)=\left\{X\in\mathbb R_{\ge0}^{m\times n}:\sum_jx_{ij}=a_i,\quad\sum_ix_{ij}=b_j\right\}
\]
with its intrinsic Frobenius Euclidean metric. Its coordinate facet \(F_{ij}=\{X:x_{ij}=0\}\) exists precisely when \(a_i+b_j<T\). Distinct coordinate facets \(F_{ij}\) and \(F_{k\ell}\) meet in a ridge if and only if the applicable condition holds:

1. If \(i=k\) and \(j\ne\ell\): \(a_i+b_j+b_\ell<T\).
2. If \(j=\ell\) and \(i\ne k\): \(a_i+a_k+b_j<T\).
3. If \(i\ne k\) and \(j\ne\ell\): both individual facet inequalities \(a_i+b_j<T\) and \(a_k+b_\ell<T\) hold.

Every ridge is obtained exactly once in this way. The corresponding *interior* dihedral angles, in the same order, are
\[
\arccos\frac1{n-1},\qquad \arccos\frac1{m-1},\qquad
\pi-\arccos\frac1{(m-1)(n-1)}.
\]
Thus the angles depend only on the matrix shape, while the exact labeled ridge graph depends only on the signs of pair and triple margin sums relative to \(T\). The three classes need not all be present; if \(m=n\), the first two numerical angles coincide.

For the *central transportation polytope* with \(a_i=T/m\), \(b_j=T/n\), every pair of facets is ridge-adjacent when \((m,n)\ne(3,3)\). The three classes (same row, same column, distinct row and column) have multiplicities respectively
\[
 m\binom n2,\quad n\binom m2,\quad 2\binom m2\binom n2.
\]
When \(m=n=3\), only the last class survives, consisting of 18 ridges. For central \((m,n)\ne(3,3)\), the mean interior angle \(\overline\theta\) over all \(\binom{mn}{2}\) ridges is strictly smaller than \(\pi/2\). As both dimensions diverge,
\[
 mn\left(\overline\theta-\frac\pi2\right)\longrightarrow-1,
\]
although \(mn(\Theta-\pi/2)\) converges in probability to \(1\) for a uniform random ridge \(\Theta\). This last distinction comes from vanishing proportions of acute ridges.

## Assumptions and scope

The margins are strictly positive real numbers, the two totals agree, and \(m,n\ge3\). No generic-position assumption is imposed: all strict-equality boundary cases are covered. A ridge means a nonempty face of codimension two *inside the affine hull*, and angles refer to the ambient Frobenius inner product restricted to the affine hull. This is not a claim about arbitrary transportation polytopes with structural zeros prescribed in advance or about cases with one dimension two.

## Proof

**Facets and strict support.** The matrix \(X_{ij}=a_ib_j/T\) is strictly positive, so the polytope has affine dimension \((m-1)(n-1)\). An allowed-edge support graph \(H\subseteq K_{m,n}\) that is connected carries a feasible matrix strictly positive on every edge if and only if every nonempty proper row subset \(S\) has
\[
\sum_{i\in S}a_i<\sum_{j\in N_H(S)}b_j.
\]
Necessity follows because connectedness guarantees an allowed edge from a row outside \(S\) into \(N_H(S)\). For sufficiency, put a small positive \(\varepsilon\) on every allowed edge, subtract the corresponding degree-weighted amounts from the margins, and invoke the standard fractional bipartite-flow Hall criterion for the remaining nonnegative flow; all finitely many proper-subset inequalities stay valid for sufficiently small \(\varepsilon\). For \(S\) with all column vertices in \(N_H(S)\), strictness is automatic from positive margins outside \(S\).

When one coordinate \((i,j)\) is deleted from \(K_{m,n}\), the only nonautomatic row-subset condition is \(a_i<T-b_j\). Hence \(x_{ij}=0\) gives a true facet exactly under the stated inequality. With two deleted coordinates, the support graph is still connected. If they lie in one row, the only nonautomatic condition is \(a_i<T-b_j-b_\ell\); if in one column, it is \(a_i+a_k<T-b_j\); if they are in distinct rows and columns, the only conditions are the two singleton-row facet tests. This proves the strict-support criteria above.

If a positive-on-every-remaining-edge matrix exists, precisely two independent coordinate restrictions are active, giving a ridge. Conversely, when strict support fails while the two designated coordinate facets exist, every point in their intersection has at least one further common zero coordinate: otherwise an average of matrices witnessing positivity at each remaining coordinate would give a fully positive matrix. Deleting any three distinct coordinates from \(K_{m,n}\) leaves it connected unless all three deleted edges isolate one row or column, which is impossible for a nonempty transportation face with strictly positive margins. Consequently those three zero constraints are independent in the affine hull (their zero-row/zero-column tangent space has codimension three). The intersection therefore has codimension at least three and is not a ridge. Every ridge is the intersection of two facets, so the classification is exhaustive.

**Euclidean angles.** Write \(P_m=I_m-J_m/m\) and \(P_n=I_n-J_n/n\). The orthogonal projector onto the zero-row/zero-column tangent space is \(Z\mapsto P_m ZP_n\). Thus the projected outward normal to \(F_{ij}\) is \(-P_me_i e_j^{\mathsf T}P_n\), with squared norm \((1-1/m)(1-1/n)\). Two unit outward normals have scalar product
\[
\frac{(\delta_{ik}-1/m)(\delta_{j\ell}-1/n)}{(1-1/m)(1-1/n)}.
\]
For distinct cells it equals \(-1/(n-1)\), \(-1/(m-1)\), or \(1/((m-1)(n-1))\), respectively. The interior angle is \(\pi\) minus the angle between the two outward normals. This proves the angle formulas and also independence of the first two normal constraints.

**Central case and asymptotics.** For equal margins, the same-row strict inequality is \(1/m+2/n<1\), and the same-column inequality is \(2/m+1/n<1\). For integers \(m,n\ge3\) they both hold unless \((m,n)=(3,3)\), when equality holds. The disjoint-pair condition always holds. Counting unordered pairs gives the stated multiplicities.

Put \(A=m-1\), \(B=n-1\). For the central case other than \((3,3)\), direct substitution into the weighted mean yields
\[
\overline\theta-\frac\pi2=
\frac{AB\arcsin(1/(AB))-A\arcsin(1/A)-B\arcsin(1/B)}{mn-1}.
\]
The function \(t\mapsto\arcsin(t)/t\) is increasing on \((0,1)\), so \(AB\arcsin(1/(AB))\le A\arcsin(1/A)\), and the remaining negative term ensures strict negativity. For \(A,B\to\infty\), the three terms in the numerator tend to \(1,-1,-1\), respectively, yielding the limiting mean. The disjoint-pair fraction \(AB/(mn-1)\to1\), and on that class \(mn(\Theta-\pi/2)=mn\arcsin(1/(AB))\to1\), proving convergence in probability. The means do not converge to that limit, because the two acute classes have vanishing but consequential weights.

## Verification

A standalone checker, `checker.py`, tests the strict facet-pair conditions against an independently formulated linear program maximizing a common positive slack on all other coordinates. It passed 7,068 facet-pair cases across 54 deterministic balanced and random positive-margin instances for matrix shapes \(3\times3\) through \(5\times5\). A second independent rational-arithmetic calculation checks the intrinsic normal Gram values in all shapes from \(3\times3\) through \(8\times8\). The infinite-dimensional quantifiers and sharp equality cases follow from the proof, not from the finite checks. `python checker.py` requires Python, NumPy and SciPy.

## Relationship to prior work

The classical support-graph description and the exact criterion for a single coordinate facet occur in De Loera and Kim's 2013 survey, including its attribution of the facet criterion to an earlier transportation-polytope monograph. Warrington (first public October 2016) derives orthogonal bases for the zero-margin matrix subspace, and Blanchard, De Loera and Louveaux (first public January 2020) study monotone paths of transportation polytopes. Those established results and general max-flow feasibility are not claimed as new. The claim here is the explicit *complete* two-facet margin-wall/ridge incidence law coupled with its intrinsic Euclidean three-angle distribution and the central-case rare-angle consequence. This combination is elementary enough that an unindexed equivalent statement may exist; priority is not independently certified.

## Limitations

No classification is asserted for higher-codimension faces, nonpositive margins, structural-zero transportation graphs, or dimensions with two rows or two columns. The finite checker is a diagnostic rather than an infinite proof. Priority remains subject to inspection of the full historical transportation-polytope literature, particularly the 1967 Klee–Witzgall facet/vertex report and older monographs on face lattices. The 2013 survey explicitly establishes the individual-facet condition, which is not part of the novelty claim. Independent validation has not been performed.

## References

- M. Blanchard, J. A. De Loera, and Q. Louveaux, *On the Length of Monotone Paths in Polyhedra*, arXiv:2001.09575 (first public 2020-01-27), https://arxiv.org/abs/2001.09575.
- J. A. De Loera and E. D. Kim, *Combinatorics and Geometry of Transportation Polytopes: An Update*, arXiv:1307.0124 (first public 2013-06-29), https://arxiv.org/abs/1307.0124.
- G. S. Warrington, *Orthogonal Bases for Transportation Polytopes Applied to Latin Squares, Magic Squares and Sudoku Boards*, arXiv:1610.04259 (first public 2016-10-13), https://arxiv.org/abs/1610.04259.

- V. Klee and C. Witzgall, *Facets and Vertices of Transportation Polytopes*, technical report (1967), https://ntrl.ntis.gov/NTRL/dashboard/searchResults/titleDetail/AD661124.xhtml (bibliographic abstract consulted; full text not inspected).
