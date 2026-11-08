# A sharp Euclidean inball transition for biclique-deleted perfectly matchable subgraph polytopes

## Finding

For integers \(n\ge 2\) and \(1\le s<n\), partition each color class of \(K_{n,n}\) into blocks of sizes \(s\) and \(t=n-s\), and delete every edge between the two size-\(s\) blocks. Let \(P_{n,s}\) be the convex hull of incidence vectors of vertex sets whose induced subgraph has a perfect matching (including the empty set). Distances below are measured in its intrinsic Euclidean affine hull.

Define
\[
\ell_n=\sqrt{\frac{2n-1}{2n}},\qquad h_n=\sqrt{\frac n2},\qquad
r_{\mathrm{box}}=\frac1{2\ell_n},\qquad
r_{\mathrm{Hall}}=\frac{n-s}{n\ell_n+h_n}.
\]
The exact intrinsic Euclidean inradius is
\[
\boxed{\operatorname{inrad}_2(P_{n,s})=\min\{r_{\mathrm{box}},r_{\mathrm{Hall}}\}.}
\]
Its incenter is unique for every admissible pair. Writing \(A=A_0\sqcup A_1\), \(B=B_0\sqcup B_1\), with \(|A_0|=|B_0|=s\), the unique incenter is the all-\(1/2\) vector when \(r_{\mathrm{box}}<r_{\mathrm{Hall}}\). Otherwise it has coordinates \(r\ell_n\) on \(A_0\cup B_0\) and \(1-r\ell_n\) on \(A_1\cup B_1\), where \(r=r_{\mathrm{Hall}}\).

There is **never an equality of the two candidate radii** at integer \((n,s)\). The transition occurs at the nonintegral threshold
\[
\boxed{s_*(n)=\frac12\left(n-\frac{n}{\sqrt{2n-1}}\right).}
\]
For \(s<s_*(n)\), all \(4n\) coordinate facets touch the unique largest inscribed sphere, and its Hall facet does not. For \(s>s_*(n)\), exactly \(2n+1\) facets touch: the \(2s\) lower coordinate facets at \(A_0\cup B_0\), the \(2t\) upper coordinate facets at \(A_1\cup B_1\), and the single nontrivial Hall facet. There are no other tangent facets.

For example, when \(n=8\), the case \(s=2\) has radius \(2/\sqrt{15}\) and 32 tangent facets; the case \(s=3\) has radius \(5/[2(\sqrt{15}+1)]\) and 17 tangent facets. Thus a single increase in deleted-biclique size changes which facet orbit determines the inball.

## Assumptions and scope

The graph is unweighted, balanced, and simple. Both deleted blocks have exactly \(s\) vertices, with \(1\le s<n\). The input data are its vertex-incidence vectors in the fixed standard coordinates of \(\mathbb R^{2n}\), **not** the edge-incidence matching polytope or the edge-root polytope. The affine span is
\[
H=\left\{(x,y)\in\mathbb R^{n}\times\mathbb R^{n}:\sum_{i\in A}x_i=\sum_{j\in B}y_j\right\},
\]
of dimension \(2n-1\), and the inradius is computed in the Euclidean norm inherited by this hyperplane. The graph is connected for every admissible \(n,s\).

The following standard description of bipartite perfectly matchable subgraph polytopes is used as an established premise: its points are precisely those satisfying \(0\le z_v\le1\), the color-class sum equality, and the Hall inequalities \(x(S)\le y(\Gamma(S))\). For this graph, the only Hall inequality not implied by the box conditions and the sum equality is
\[
\sum_{i\in A_0}x_i\le\sum_{j\in B_1}y_j.\tag{H}
\]
Indeed, a nonempty \(S\subseteq A_0\) has neighborhood \(B_1\), and its inequality follows from \((\mathrm H)\); any set meeting \(A_1\) has neighborhood all of \(B\), giving an inequality implied by the total-sum constraint. The converse matching interpretation for \(0/1\) points follows from Hall's theorem, and the full convex-hull inequality description follows from Balas--Pulleyblank.

## Proof

**Step 1: Intrinsic facet-normal lengths.** In \(\mathbb R^{2n}\) put \(w=(\mathbf1_A,-\mathbf1_B)\). The orthogonal projector onto the tangent space of \(H\) is \(Q=I-ww^{\mathsf T}/(2n)\). Each coordinate bound has projected unit normal of length
\[
\|Qe_v\|=\sqrt{1-\frac1{2n}}=\ell_n.
\]
The Hall inequality \((\mathrm H)\) has ambient normal \(g=\mathbf1_{A_0}-\mathbf1_{B_1}\). Since \(\|g\|^2=s+t=n\) and \(g\cdot w=n\), its projected length is
\[
\|Qg\|=\sqrt{n-\frac{n^2}{2n}}=h_n.
\]
These are the genuine Euclidean lengths in the affine span, not the generally different lengths obtained by eliminating one coordinate.

**Step 2: Global upper bounds.** Suppose a Euclidean ball of radius \(r\) with center \(c\in H\) lies in the polytope. For every coordinate, the two parallel coordinate inequalities require
\[
r\ell_n\le c_v\le1-r\ell_n,
\]
and hence \(r\le r_{\mathrm{box}}\). The Hall inequality requires
\[
\sum_{B_1}c_j-\sum_{A_0}c_i\ge r h_n.
\]
Using the coordinate bounds on the left gives
\[
r h_n\le t(1-r\ell_n)-s r\ell_n=t-nr\ell_n.
\]
Thus \(r\le r_{\mathrm{Hall}}\). Both bounds apply to arbitrary centers, not merely symmetric ones.

**Step 3: Attainment and uniqueness.** Put \(r=\min\{r_{\mathrm{box}},r_{\mathrm{Hall}}\}\). If \(r=r_{\mathrm{box}}\), set every center coordinate equal to \(1/2\). Its Hall slack is \((t-s)/2\), which is at least \(r h_n\) exactly when \(r_{\mathrm{box}}\le r_{\mathrm{Hall}}\). The projected distances to coordinate hyperplanes are \(r\), so the ball is feasible and optimal. Because simultaneously \(c_v\ge r\ell_n=1/2\) and \(c_v\le1-r\ell_n=1/2\), every incenter equals this point.

If \(r=r_{\mathrm{Hall}}\), assign \(c_v=r\ell_n\) to each vertex in \(A_0\cup B_0\), and \(c_v=1-r\ell_n\) to each vertex in \(A_1\cup B_1\). The two equal-size color classes have the same coordinate sum, so \(c\in H\). All box cushions are at least \(r\ell_n\) because \(r\le r_{\mathrm{box}}\), and the Hall cushion equals \(t-nr\ell_n=r h_n\). Thus the ball is feasible and optimal. At any optimal center the Hall upper estimate above is an equality: this forces every \(A_0\) coordinate to its lower limit and every \(B_1\) coordinate to its upper limit. The color-class sum equality forces all \(A_1\) coordinates to their upper limits and all \(B_0\) coordinates to their lower limits. Hence the center is unique.

**Step 4: Strict transition.** The equality \(r_{\mathrm{box}}=r_{\mathrm{Hall}}\) is equivalent to
\[
n-2s=\frac{n}{\sqrt{2n-1}}.
\]
This cannot hold for integers \(n\ge2\), \(1\le s<n\). If \(\sqrt{2n-1}\) is irrational the right side is irrational. Otherwise \(2n-1=d^2\) for an odd integer \(d>1\). Equality implies \(d\mid n\); but \(2n=d^2+1\) yields \(2n\equiv1\pmod d\), impossible. This also proves that the two regimes are determined by the stated strict comparison with \(s_*(n)\).

**Step 5: Exact contacts.** The quoted facet description contains only the box facets and the single Hall facet (in either orientation under the sum equality). In the box-controlled regime, every box constraint is tight at radius \(r_{\mathrm{box}}\), whereas the Hall constraint is strictly slack; moreover this regime entails \(t\ge3\), so every coordinate has degree at least two and no vertex is a cut vertex, proving that all \(4n\) coordinate hyperplanes are genuine facets. In the Hall-controlled regime, the above center is tight on the lower coordinate inequalities at \(A_0\cup B_0\), upper coordinate inequalities at \(A_1\cup B_1\), and the Hall inequality, and strictly slack on the other coordinate constraints. The \(A_0\cup B_0\) vertices are not cut vertices, the \(A_1\cup B_1\) vertices have degree \(n\ge2\), and the Hall facet criterion holds because \(G[A_0\cup B_1]=K_{s,t}\) and \(G[A_1\cup B_0]=K_{t,s}\) are connected. Consequently all \(2n+1\) listed contacts are genuine facets and there are no others, as claimed. \(\square\)

## Verification

The companion standalone `verify_pms_inball.py` independently enumerates all \(0/1\) candidate vertex sets for \(2\le n\le5\), checks each candidate's induced perfect matching by brute-force permutations (not by reusing the Hall test), and compares the result with the Hall inequality. It verifies that the polytope has affine dimension \(2n-1\), and confirms active-hyperplane facet ranks. It also solves intrinsic Chebyshev-center linear programs for all \(2\le n\le6\), \(1\le s<n\), using explicitly projected facet normals. All 15 parameter pairs passed: `PMS_BICLIQUE_INBALL_HALL_AND_FACET_CHECKS_PASSED 15`.

Run using Python 3 with NumPy and SciPy: `python verify_pms_inball.py`. These finite tests are not substitutes for Steps 1--5, which establish the infinite-family claim.

## Relationship to prior work

Balas and Pulleyblank (1983) established the bipartite perfectly matchable subgraph polytope's Hall-type linear and facet description. Mori's arXiv preprint (initial public version October 31, 2022) studies the same polytope's toric rings, Gorenstein properties, and facets; its Propositions 3.3 and 3.4 provide an accessible statement of the needed facet criteria. Neither paper's inspected statements establish the present intrinsic Euclidean inradius formula, nonintegral threshold, uniqueness, or complete tangent-facet transition.

Under the isometry replacing each \(B\) coordinate \(y_j\) by \(1-y_j\), the polytope becomes the hypersimplex \(\Delta_{n,2n}\) cut by one additional subset-rank inequality. This is an elementary split-matroid base-polytope representation. In particular, the unrestricted hypersimplex inball does **not** imply the sharp cut-dependent radius. Ferroni and Schröter's split-matroid face enumeration gives combinatorial information but not this metric optimization. Polytopes of matchings **on edges**, bipartite root polytopes, and graph associahedra are different geometric objects.

## Limitations

Only balanced bipartite graphs with one deleted square biclique are covered; the formula does not apply unchanged to unequal color classes or to multiple deleted blocks. Every statement uses the standard incidence-coordinate Euclidean metric on the affine span and is not invariant under arbitrary affine equivalence. The exact Hall representation and facet characterization are invoked from established primary literature. Historical priority under alternative terminology, especially the split-matroid/Chebyshev-center formulation, is not independently certified. Numerical checks are finite; no independent mathematical audit has been performed.

## References

1. E. Balas and W. R. Pulleyblank, *The perfectly matchable subgraph polytope of a bipartite graph*, Networks 13 (1983), 495--516. DOI: 10.1002/net.3230130405. The abstract and bibliographic material were accessible; its complete published text was not available in the present comparison.
2. K. Mori, *Toric rings of perfectly matchable subgraph polytopes*, arXiv:2210.17147 (first posted October 31, 2022), Graphs and Combinatorics 39 (2023), article 121. DOI: 10.1007/s00373-023-02719-8. In particular, Propositions 3.3 and 3.4.
3. L. Ferroni and B. Schröter, *Face enumeration for split matroid polytopes*, Combinatorics, Probability and Computing (2025), DOI: 10.1017/S0963548325000021, especially the main face-enumeration results.
