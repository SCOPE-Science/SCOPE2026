# Complete attracting-cycle classification for farthest-facet projection on regular simplices

## Finding
For every integer \(d\ge 3\), the farthest-orthogonal-facet-projection map on the relative interiors of the facets of a regular Euclidean \(d\)-simplex has exactly \(d!\) nonconstant periodic orbits. Each has prime period \(d+1\), and each is exponentially attracting on its strict barycentric-order basin. Its orbit coordinates form the same arithmetic progression
\[
0,\ \frac{2}{d(d+1)},\ \frac{4}{d(d+1)},\ \ldots,\ \frac{2d}{d(d+1)}.
\]
Every point with distinct positive barycentric coordinates has a purely periodic *facet itinerary* from its first step, visiting each of the \(d+1\) facets exactly once per block, and its actual positions converge to the corresponding periodic orbit. If two positive barycentric coordinates agree, the orbit reaches a fixed point in at most \(d-1\) iterations. The \(d!\) attracting periodic measures have equal physical basins, each occupying exactly \(1/d!\) of normalized facet-area measure. The sorted-coordinate gap dynamics is explicitly linear, with characteristic polynomial
\[
p_d(z)=d z^d-\sum_{j=0}^{d-1}z^j,
\]
whose nonunit roots all lie strictly inside the open unit disk.

## Assumptions and scope
Fix \(d\ge3\). Let \(S\) be any regular Euclidean \(d\)-simplex, with vertices \(v_0,\ldots,v_d\) and opposite facets \(F_i\). The state space is the disjoint union \(X=\bigsqcup_{i=0}^d\operatorname{relint}(F_i)\). From a point \(x\) in \(\operatorname{relint}(F_i)\), orthogonally project onto each other facet \(F_j\), \(j\ne i\), and select a projection with strictly maximal Euclidean displacement. If there is a tie for the greatest displacement, set \(T(x)=x\). This definition excludes edges and lower-dimensional face intersections, where a current facet would not be unique. It is invariant under Euclidean similarities of the simplex. Every selected orthogonal projection actually belongs to the relative interior of the target facet, so \(T:X\to X\) is well-defined.

Write \(\lambda_i(x)\) for the barycentric coefficients: \(x=\sum_i\lambda_i v_i\), \(\lambda_i\ge0\), \(\sum_i\lambda_i=1\). At a point of \(\operatorname{relint}(F_i)\), exactly \(\lambda_i=0\), and all other coefficients are positive. A strict-order point means these \(d\) positive coefficients are pairwise distinct. An attracting periodic measure is the uniform probability measure on one nonconstant periodic orbit; its physical basin consists of points whose time-averaged empirical measures converge to it. Facet area means the sum of \((d-1)\)-dimensional Hausdorff measures on the open facets, normalized to total mass one.

## Proof
**1. Orthogonal projection is a maximal-coordinate reset.** By similarity, realize the regular simplex in \(H=\{y\in\mathbb R^{d+1}:\sum_i y_i=0\}\) with \(v_i=e_i-\mathbf1/(d+1)\). A point with barycentric vector \(\lambda\) has Euclidean coordinate vector \(y_i=\lambda_i-1/(d+1)\). The supporting hyperplane of \(F_j\) is \(y_j=-1/(d+1)\); its normal within \(H\) is \(v_j\), with squared norm \(d/(d+1)\). Hence the distance to that hyperplane is \(\sqrt{(d+1)/d}\,\lambda_j\). The orthogonal projection onto it has barycentric update
\[
\lambda'_j=0,\qquad
\lambda'_k=\lambda_k+\frac{\lambda_j}{d}\quad(k\ne j).
\tag{1}
\]
All \(\lambda'_k\) with \(k\ne j\) are strictly positive when \(\lambda_j>0\). Thus the projected point lies inside the facet, and the farthest facet is precisely the index of the largest positive coordinate. The tied-max convention is exactly the fixed-point convention in the statement.

**2. The facet order rotates without changing relative ranks.** At a strict-order state on \(F_{i_0}\), name the remaining labels in decreasing barycentric order \(i_1,\ldots,i_d\). Equation (1) resets the largest coordinate \(i_1\) to zero and adds the same positive amount to every other coordinate. Consequently the new strict order, starting from the zero label, is \((i_1;i_2,\ldots,i_d,i_0)\). This repeats. Thus the chosen facet labels follow \(i_1,i_2,\ldots,i_d,i_0,i_1,\ldots\) exactly, with primitive symbolic period \(d+1\). Conversely, an equality among two positive coordinates persists while larger coordinates are reset, and becomes a tied maximum within at most \(d-1\) steps. At that time the map fixes the point forever. In particular no nonconstant periodic orbit can involve a tie, and fixed points are precisely states with at least two maximal positive coordinates.

**3. The gap dynamics is a primitive Markov matrix.** In any strict-order state write its sorted coefficients as \(0=u_0<u_1<\cdots<u_d\), and put \(g_k=u_{k+1}-u_k\) for \(0\le k<d\). Equation (1) and the rank rotation give exactly
\[
(g'_0,g'_1,\ldots,g'_{d-1})
=\left(\frac{g_0+\cdots+g_{d-1}}d,\ g_0,\ldots,g_{d-2}\right)=Bg.
\tag{2}
\]
The nonnegative \(d\times d\) matrix \(B\) has first row \((1/d,\ldots,1/d)\) and ones immediately below the diagonal. Its row sums are one, its associated directed graph is irreducible, and the positive self-loop at state zero makes it aperiodic. Thus it is primitive. Perron--Frobenius theory gives one simple eigenvalue \(1\) and all other eigenvalues of modulus strictly below one. Its characteristic polynomial is \(p_d(z)/d\), as follows by solving the eigenvector shift equations (zero is not an eigenvalue). The unique positive right eigenvector for eigenvalue \(1\) has all entries equal. The exact normalization
\[
1=\sum_{k=0}^d u_k=\sum_{k=0}^{d-1}(d-k)g_k
\tag{3}
\]
forces its common entry to equal \(2/[d(d+1)]\). Equations (2)--(3) prove exponential convergence of sorted gaps to that value, hence of sorted barycentric coefficients to the asserted arithmetic progression. More precisely, for any \(r\) strictly between the largest modulus of the nonunit roots of \(p_d\) and one, the error is \(O(r^m)\) after \(m\) steps.

**4. Existence, completeness, and counting.** For any cyclic ordering \((i_0,i_1,\ldots,i_d)\) of the \(d+1\) facet labels, set
\[
\lambda_{i_0}=0,\qquad
\lambda_{i_k}=\frac{2(d+1-k)}{d(d+1)}\quad(1\le k\le d).
\tag{4}
\]
The coefficients are positive except at \(i_0\) and sum to one. Equation (1) successively resets \(i_1,i_2,\ldots,i_d,i_0\), returning exactly to (4) after \(d+1\) steps. These are strict cycles with prime period \(d+1\). Every other strict-order orbit has the same cyclic rank pattern as one of these cycles and converges to it by Step 3. Every non-strict orbit eventually fixes by Step 2. There are \((d+1)!/(d+1)=d!\) distinct cyclic label orderings, hence exactly \(d!\) nonconstant periodic orbits.

**5. Equal physical basins.** On each open facet there are \(d!\) strict chambers, one for each ordering of its \(d\) positive barycentric coefficients. Permuting the vertices other than that facet preserves intrinsic facet area and acts transitively on those chambers, so each occupies exactly \(1/d!\) of that facet's area. A given cyclic orbit attracts one chamber on each of the \(d+1\) facets. Tie sets are contained in finitely many affine hyperplanes of codimension one in the facets and have zero facet area. Consequently each orbit's complete physical basin has normalized facet area \(1/d!\), and there are no other physical measures for the given reference area.

## Verification
The standalone `check_simplex.py` uses exact rational arithmetic, independently computes orthogonal projection in the centered Euclidean embedding, enumerates all cyclic-orbit formulas for dimensions three through seven, checks their exact return and facet choices, checks the gap recurrence on random strict-order states, and checks finite-time arrest of tied examples. Running `python3 check_simplex.py` prints `PASS: 138033 exact-rational assertions (dimensions 3 through 7)`. This finite test supports but does not establish the all-dimensional theorem; the proof is Steps 1--5 above.

## Relationship to prior work
Everett's *A Piecewise Contractive Map on Triangles* (published online January 7, 2021; subsequently available as arXiv:2408.16019) studies three complete lines in the plane and explicitly raises the higher-dimensional farthest-facet analogue for convex polytopes in its closing discussion. The present result solves that higher-dimensional question for regular simplices: the ambient dimension is at least three, the domain consists of relative interiors of facets, and the finite classification and basin proportions are explicit. It neither claims a classification for arbitrary polytopes nor reproduces the complete-line planar dynamics. A related publicly indexed classification of two orientations of primitive three-cycles concerns the original planar three-line map, not these higher-dimensional facet systems. Wang and Zhang's *A geometric iterated function system on triangles* studies ordered-triangle moduli under different geometric maps, and does not state this facet-projection theorem. Farthest-*point* dynamics on polyhedra uses a different operation from selecting an orthogonal projection onto a supporting facet.

## Limitations
The theorem is restricted to regular Euclidean simplices in dimensions at least three, with the current facet uniquely determined (relative interiors only), and with ties fixed. It does not classify the map on shared edges, on exterior supporting hyperplanes, or on irregular simplices and other convex polytopes. The Euclidean projection update does not immediately extend to those settings. The nonunit spectral roots determine exponential convergence but no dimension-uniform relaxation constant is asserted. No independent mathematical audit or publication-priority guarantee is asserted; related work on projection algorithms may use different terminology.

## References
1. Samuel Everett, *A Piecewise Contractive Map on Triangles*, Journal of Dynamical Systems and Geometric Theories **18** (2020/2021), 183--192, DOI: 10.1080/1726037X.2020.1847765, first publicly verified online January 7, 2021; freely accessible publisher full text: https://tarupublications.com/journals/jdsgt/volume/18/issue/2/a-piecewise-contractive-map-on-triangles/pdf ; preprint arXiv:2408.16019.
2. Jiajun Wang and Ying Zhang, *A geometric iterated function system on triangles*, arXiv:1605.01794 (2016), https://arxiv.org/abs/1605.01794 .
3. *Exact two-orientation classification of primitive three-cycles for the farthest-projection triangle map*, publicly indexed mathematical finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-two-orientation-classification-of-primitive-three-cycles-f--2944d54e59d8 .
4. Zili Wang, *Farthest Point Map on a Centrally Symmetric Convex Polyhedron*, arXiv:1802.06934 (2018), https://arxiv.org/abs/1802.06934 (different map; context only).
