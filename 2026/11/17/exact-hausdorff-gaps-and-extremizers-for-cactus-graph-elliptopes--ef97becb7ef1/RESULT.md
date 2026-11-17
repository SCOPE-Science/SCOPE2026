# Exact Hausdorff gaps and extremizers for cactus graph elliptopes

## Finding

For a finite connected simple cactus graph \(G=(V,E)\), let \(\mathcal C(G)\) be its edge-correlation cut polytope and \(\mathcal E(G)\) its edge-correlation elliptope. With the ordinary Euclidean norm on \(\mathbb R^E\), their exact Hausdorff distance is
\[
\boxed{d_H(\mathcal E(G),\mathcal C(G))^2
 =\sum_{C\in\mathscr C(G)}\frac{\bigl(|C|\cos(\pi/|C|)-|C|+2\bigr)^2}{|C|},}
\]
where \(\mathscr C(G)\) is the collection of simple cycles of the cactus, and the empty sum is zero. Thus a tree has zero gap; multiple cycles contribute by a Pythagorean rather than a maximum rule.

For a single cycle of length \(n\ge3\), the gap is strictly positive and equals
\[
\boxed{\delta_n=\frac{n\cos(\pi/n)-n+2}{\sqrt n}.}
\]
The complete set of farthest points of \(\mathcal E(C_n)\) from \(\mathcal C(C_n)\) is
\[
\boxed{\{\cos(\pi/n)\,\xi:\xi\in\{-1,1\}^n,\ \prod_{i=1}^n\xi_i=-1\}.}
\]
There are exactly \(2^{n-1}\) such points. The unique nearest point of the cut polytope to the farthest point indexed by \(\xi\) is \(\frac{n-2}{n}\xi\). Every unit direction maximizing the support-function difference is \(\xi/\sqrt n\) with odd sign product, and there are no others.

For a cactus with at least one cycle, all its farthest elliptope points are exactly the independent choices of these cycle extremizers, together with arbitrary coordinates in \([-1,1]\) on bridge edges. In particular, with \(b\) bridge edges there are \(2^{\sum_{C}(|C|-1)}\) disjoint axis-parallel \(b\)-cubes of farthest points; a \(0\)-cube is a point. The nearest cut point is obtained by replacing each cycle block \(\cos(\pi/|C|)\xi\) by \((|C|-2)\xi/|C|\) and leaving all bridge coordinates unchanged.

The asymptotic cycle law is
\[
\delta_n=\frac{2}{\sqrt n}-\frac{\pi^2}{2n^{3/2}}+O(n^{-7/2}).
\]

## Assumptions and scope

All graphs are finite, connected, undirected and simple, with at least one edge; a cactus means every edge belongs to at most one simple cycle. Let \(\mathbb S_+^V\) denote real positive-semidefinite symmetric matrices indexed by vertices. Define
\[
\mathcal E(G)=\{(X_{uv})_{uv\in E}:X\in\mathbb S_+^V,\ X_{vv}=1\ \text{for every }v\in V\},
\]
\[
\mathcal C(G)=\operatorname{conv}\{(\sigma_u\sigma_v)_{uv\in E}:\sigma\in\{-1,1\}^V\}.
\]
Thus \(\mathcal C(G)\subseteq\mathcal E(G)\subseteq[-1,1]^E\). Hausdorff distance is measured in the edge-correlation coordinates above, **not** the \(0\)-\(1\) cut coordinates. Changing to \(0\)-\(1\) cut coordinates by \(z_e=(1-x_e)/2\) divides all stated distances by two. A cycle of length three is included. All formulas are exact for arbitrary finite cactus sizes; no assumption of equal cycle lengths is made.

## Proof

**1. Cut support on a single cycle.** Order cycle edges cyclically. Edge sign vectors of cuts are exactly \(z\in\{-1,1\}^n\) with \(\prod_i z_i=1\); this follows by multiplying successive vertex signs around the cycle, and conversely by reconstructing vertex signs from a consistent edge-sign word. Given a linear functional \(w\in\mathbb R^n\), let \(a_i=|w_i|\). If any coefficient vanishes or the product of the nonzero coefficient signs can be completed to even parity, the maximum cut support is \(h_{\mathcal C}(w)=\sum_i a_i\). In the remaining case all coefficients are nonzero and their signs \(\xi_i=\operatorname{sgn}(w_i)\) have \(\prod_i\xi_i=-1\). With \(m=\min_i a_i>0\), exactly one sign must be corrected, optimally at a minimum-weight coordinate, so
\[
 h_{\mathcal C}(w)=\sum_i a_i-2m. \tag{1}
\]
In the first case \(h_{\mathcal E}(w)=h_{\mathcal C}(w)=\sum_i a_i\), since every elliptope coordinate lies in \([-1,1]\) and a cut vector realizes the upper bound.

**2. Exact signed-cycle semidefinite maximum.** Fix \(\xi\in\{-1,1\}^n\) with odd sign product. Let \(A_\xi\) be the symmetric signed adjacency matrix of the cycle, with entry \(\xi_i\) at its \(i\)-th edge (and the transpose), and zero diagonal. Multiplying rows and columns by vertex signs switches all but the final edge to \(+1\), with final edge \(-1\). Its antiperiodic Fourier modes give the eigenvalues
\[
 2\cos\left(\frac{(2k+1)\pi}{n}\right),\quad k=0,\ldots,n-1.
\]
The maximum is \(2t\), where \(t=\cos(\pi/n)\), and its eigenspace has dimension exactly two. For a Gram matrix \(X\succeq0\) with unit diagonal,
\[
 \xi\cdot x=\tfrac12\operatorname{tr}(A_\xi X)
 \le\tfrac12(2t)\operatorname{tr}X=nt. \tag{2}
\]
The bound is attained by planar unit vectors with successive arguments \(0,\pi/n,\ldots,(n-1)\pi/n\), followed by the vertex switches, producing exactly the edge coordinates \(x=t\xi\).

For uniqueness in *edge coordinates*, equality in (2) forces the range of \(X\) into the top two-dimensional eigenspace. In the switched coordinates, write its rows as \(p_j=(\cos(j\pi/n),\sin(j\pi/n))\), with \(j=0,\ldots,n-1\). Any such PSD matrix is \(X_{ij}=p_i^{\mathsf T}Qp_j\) for some positive-semidefinite \(2\times2\) matrix \(Q\). The diagonal equations \(p_j^{\mathsf T}Qp_j=1\) are samples of a trigonometric polynomial of degree one in \(2j\pi/n\). Its deviation from one has at least three distinct zeros for \(n\ge3\), hence vanishes identically. Thus \(Q=I_2\), and the **unique edge-coordinate maximizer** is \(x=t\xi\).

**3. Optimization over all support directions.** In the odd-parity case of step 1, write
\[
 w=m\xi+\sum_i(a_i-m)\xi_i e_i.
\]
Each elliptope coordinate lies between \(-1\) and \(1\), so by (2)
\[
 h_{\mathcal E}(w)\le mnt+\sum_i(a_i-m).
\]
Combining with (1) yields
\[
 0\le h_{\mathcal E}(w)-h_{\mathcal C}(w)
 \le m\bigl(nt-n+2\bigr)
 \le\frac{nt-n+2}{\sqrt n}\,\|w\|_2. \tag{3}
\]
The last inequality uses \(m\sqrt n\le\|w\|_2\). The numerator is positive: \(n(1-\cos(\pi/n))\le\pi^2/(2n)<2\) for \(n\ge3\). Equality in the final inequality in (3) requires all \(a_i=m\), and then (2) supplies equality. All maximizing unit directions are therefore exactly \(\xi/\sqrt n\) with odd sign product.

For nested compact convex sets \(\mathcal C\subseteq\mathcal E\), the Euclidean Hausdorff distance equals \(\max_{\|w\|_2=1}(h_{\mathcal E}(w)-h_{\mathcal C}(w))\). This follows from support-function characterization of Minkowski inclusion \(\mathcal E\subseteq\mathcal C+\delta B_2\). Formula (3) gives the displayed exact \(\delta_n\).

**4. All farthest points and their projections.** Fix odd \(\xi\). The \(n\) even-parity cut vectors obtained by flipping exactly one coordinate of \(\xi\) have barycenter
\[
 y=\frac1n\sum_{j=1}^n(\xi-2\xi_j e_j)=\frac{n-2}{n}\xi\in\mathcal C(C_n).
\]
The point \(x=t\xi\in\mathcal E(C_n)\) satisfies \(\|x-y\|_2=\delta_n\). Moreover, the valid supporting halfspace \(\xi\cdot z\le n-2\) contains \(\mathcal C(C_n)\), and \(y\) is the orthogonal projection of \(x\) onto its boundary hyperplane. Hence \(y\) is the unique metric projection of \(x\) onto the cut polytope.

Conversely, suppose \(x\in\mathcal E(C_n)\) has cut-distance \(\delta_n\). Let \(y\) be its unique metric projection and put \(w=(x-y)/\delta_n\). The projection variational inequality gives \(w\cdot y=h_{\mathcal C}(w)\); therefore
\[
 \delta_n=w\cdot x-h_{\mathcal C}(w)
 \le h_{\mathcal E}(w)-h_{\mathcal C}(w)\le\delta_n.
\]
All inequalities are equalities. Step 3 forces \(w=\xi/\sqrt n\) with odd parity, and step 2 forces \(x=t\xi\). This proves **exhaustiveness** of the farthest-point and nearest-point classifications, not merely existence of the displayed witnesses.

**5. Cactus products.** A connected cactus is assembled by successive one-vertex unions of cycle blocks and bridge edges. Under disjoint edge-coordinate sets,
\[
 \mathcal C(G_1\cup G_2)=\mathcal C(G_1)\times\mathcal C(G_2),\qquad
 \mathcal E(G_1\cup G_2)=\mathcal E(G_1)\times\mathcal E(G_2)
\]
when the subgraphs meet in at most one vertex. For cuts, one combines compatible vertex signs; for the elliptope, one aligns the common unit Gram vector and places components perpendicular to it in orthogonal subspaces. A bridge edge has both bodies equal to \([-1,1]\). Since for Euclidean products
\[
 \operatorname{dist}((x_j),\prod_j C_j)^2=\sum_j\operatorname{dist}(x_j,C_j)^2,
\]
maximizing independently in every cycle block gives the stated sum of squared gaps and the complete product set of farthest points. In a tree the two bodies coincide. This completes all cases.

## Verification

The accompanying `verify.py` uses only the Python standard library. Running `python verify.py` prints `PASS: 9057 finite numerical and combinatorial assertions`. It checks the planar Gram witness, signed edge values, explicit projection barycenters, cut support by complete sign enumeration in small dimensions, the signed-cycle spectral formula, weighted objective bounds for sampled directions, and the Pythagorean product identity for pairs of cycle blocks with free bridge coordinates. This reproducibility test is not a substitute for the unrestricted spectral and support-function proof above.

## Relationship to prior work

Laurent and Varvitsiotis (2011), Theorem 3.3, established the *multiplicative* Grothendieck constant for a cycle, \(\kappa(C_n)=n\cos(\pi/n)/(n-2)\), and computed the special signed uniform semidefinite support \(n\cos(\pi/n)\). These are explicitly used as precedent. Their multiplicative theorem does not state the exact **Euclidean additive Hausdorff gap**, its complete equality cases, or the metric projection of each extremizer. The current proof analyzes all weighted unit support directions and proves uniqueness of their equality points; the numerical special case alone does not supply those classifications.

Avis, Devroye, and Deza (initial arXiv release April 17, 2026) gave volume formulas for cut polytopes of sparse graphs, an exact volume formula for a cycle elliptope, and one-vertex product results for both graph-body families. Their volumetric results and product decompositions motivate the metric question here; the product statements are credited and reproved briefly for clarity. Unlike the maximum rule for the multiplicative Grothendieck constant of a one-vertex union, the Euclidean additive Hausdorff error follows a square-sum law. Laurent, Mascarin, and Telen (May 4, 2026) studied the algebraic boundaries of graph elliptopes and cycle polynomials, rather than the metric extremizers classified here.

## Limitations

The result applies to *edge-correlation coordinates and their standard Euclidean metric*, not to arbitrary weighted coordinate metrics or all series-parallel graphs. The statement of historical novelty concerns the **combined exact additive metric, all farthest points, nearest cut projections, and cactus Pythagorean composition**, not the already known cycle semidefinite support value or the graph decomposition identities. No independent external mathematical validation has been conducted; a differently indexed treatment of Euclidean relaxation gaps may exist. The finite verifier does not certify the infinite theorem and uses floating-point tolerances for trigonometric values.

## References

1. M. Laurent and A. Varvitsiotis, *Computing the Grothendieck constant of some graph classes*, 2011, Theorem 3.3 and Lemmas 2.1, 2.6. Full text: https://optimization-online.org/wp-content/uploads/2011/06/3060.pdf ; arXiv:1106.2735.
2. D. Avis, L. Devroye, and A. Deza, *On the volumes of the elliptope, metric polytope, and cut polytope*, first public preprint April 17, 2026, arXiv:2604.16735. In particular Propositions 3.2 and 3.7, Theorem 3.9, Corollary 3.10. https://arxiv.org/abs/2604.16735
3. M. Laurent, F. M. Mascarin, and S. Telen, *The Algebraic Boundary of Graph Elliptopes*, first public preprint May 4, 2026, arXiv:2605.02484. https://arxiv.org/html/2605.02484v1
4. L. Solus, C. Uhler, and R. Yoshida, *Extremal positive semidefinite matrices whose sparsity pattern is given by graphs without \(K_5\) minors*, Linear Algebra and its Applications **509** (2016), 247–275, arXiv:1506.06702. Geometric results on facet normals and sparse PSD extreme rays, distinct from the metric Hausdorff extremum.
