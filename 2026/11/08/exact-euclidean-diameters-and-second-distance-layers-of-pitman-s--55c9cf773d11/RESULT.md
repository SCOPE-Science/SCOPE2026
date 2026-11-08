# Exact Euclidean diameters and second-distance layers of Pitman–Stanley polytopes

## Finding
Let \(n\ge2\), let \(\alpha_1,\ldots,\alpha_n>0\), and put \(B_k=\sum_{i=1}^k\alpha_i\). For the standard-coordinate Pitman–Stanley polytope
\[
P_n(\alpha)=\left\{x\in\mathbb R_{\ge0}^n:\sum_{i=1}^kx_i\le B_k\quad(1\le k\le n)\right\},
\]
the exact Euclidean diameter is
\[
\operatorname{diam}_2P_n(\alpha)=\sqrt{B_n^2+B_{n-1}^2}.
\]
The **only unordered diametral pair** is \(\{B_ne_n,B_{n-1}e_{n-1}\}\), where \(e_i\) denotes the \(i\)-th coordinate basis vector.

For the canonical family \(\alpha_i=1\) and \(n\ge3\), the largest and second-largest **distinct squared Euclidean distances between distinct vertices** are, respectively,
\[
D_1(n)=n^2+(n-1)^2,\qquad D_2(n)=n^2+(n-2)^2+1.
\]
The maximum is realized by one unordered vertex pair. The second distance is realized by precisely two unordered pairs for \(n\ge4\), or one for \(n=3\): they join \(ne_n\) to the vertices \(e_1+(n-2)e_{n-1}\) and \((n-2)e_{n-2}+e_{n-1}\), which coincide when \(n=3\). The **sharp top-level squared-distance gap** is
\[
D_1(n)-D_2(n)=2(n-2).
\]

## Assumptions and scope
All \(\alpha_i\) are strictly positive real numbers; the ambient metric is the ordinary Euclidean metric on the displayed \(x\)-coordinates. In particular an arbitrary invertible affine transformation to a flow-polytope or parking-function realization does not preserve the asserted distances. The second-level statement concerns distances between the finite set of distinct vertices, not the continuum of distances attained by all points of the polytope. No integrality hypothesis is needed for the general diameter theorem.

## Proof
**Vertices.** At any feasible point, the inequalities \(x_i\ge0\) and \(S_i=\sum_{j\le i}x_j\le B_i\) cannot both be tight at an index \(i\): when \(x_i=0\), one has \(S_i=S_{i-1}\le B_{i-1}<B_i\), taking \(S_0=B_0=0\). Hence at most one inequality from each indexed pair is active. A vertex requires \(n\) independent active inequalities, so precisely one from every indexed pair must be tight. Conversely, selecting either \(x_i=0\) or \(S_i=B_i\) at each index determines a feasible point by induction, since \(B_i>B_{i-1}\), and its triangular active-normal matrix is nonsingular. Thus the \(2^n\) vertices are indexed by subsets \(I=\{i_1<\cdots<i_r\}\subseteq[n]\), with \(x_{i_j}=B_{i_j}-B_{i_{j-1}}\) for \(B_{i_0}=0\) and with all other coordinates zero. The empty subset gives the origin.

**Diameter.** Every vertex with last positive coordinate \(k\) has nonnegative coordinates summing to \(B_k\); consequently \(\|x\|_2^2\le B_k^2\), with equality only for the single-support vertex \(B_ke_k\). A vertex with last index less than \(n\), or the origin, has norm at most \(B_{n-1}\).

If neither member of a vertex pair has a positive last coordinate, nonnegativity yields
\[\|x-y\|_2^2\le\|x\|_2^2+\|y\|_2^2\le2B_{n-1}^2.\]
If both have positive last coordinates, set \(u=\sum_{i<n}x_i\), \(v=\sum_{i<n}y_i\). Vertex activity at the last index gives \(x_n=B_n-u\), \(y_n=B_n-v\), with \(0\le u,v\le B_{n-1}\). Then
\[
\|x-y\|_2^2=\|x_{<n}-y_{<n}\|_2^2+(u-v)^2
\le u^2+v^2+(u-v)^2\le2B_{n-1}^2.
\]
For the last inequality, the convex quadratic \(u^2+v^2+(u-v)^2\) attains its maximum \(2B_{n-1}^2\) at corners of the square \([0,B_{n-1}]^2\). As \(B_n>B_{n-1}>0\), this is strictly less than \(B_n^2+B_{n-1}^2\).

If exactly one vertex has a positive last coordinate, nonnegativity and the norm bound give
\[\|x-y\|_2^2\le B_n^2+B_{n-1}^2.\]
Equality requires both individual norm bounds to be equalities and their scalar product to vanish. Hence the only unordered equality pair is \(B_ne_n\) and \(B_{n-1}e_{n-1}\). A squared distance is convex separately in each argument, so its global maximum over the compact product \(P_n(\alpha)\times P_n(\alpha)\) is attained at vertices. Moreover, strict convexity in each argument means any maximizer whose coordinate is a nontrivial convex combination of distinct vertices would be strictly below the greater of the endpoint values. Therefore the exhibited unordered pair is the only diametral pair in the full polytope.

**Second distance level for unit increments.** All positive coordinates of a canonical vertex are integer gaps of its selected indices. If a vertex has final positive coordinate at \(k\) and has at least two positive coordinates, its gap sizes are positive integers summing to \(k\); therefore their squared sum is at most \((k-1)^2+1\). Equality holds exactly for a two-part composition with sizes \(1\) and \(k-1\), interpreted as a single composition when \(k=2\).

Consider any vertex pair other than the unique diametral one. If neither has positive \(n\)-th coordinate or both do, the preceding diameter proof bounds squared distance by \(2(n-1)^2\). If exactly one has positive \(n\)-th coordinate, but is not \(ne_n\), the sum-of-squares bounds imply
\[\|x-y\|_2^2\le (n-1)^2+1+(n-1)^2=2(n-1)^2+1.\]
Both bounds are strictly less than \(n^2+(n-2)^2+1\) for \(n\ge3\). It remains to pair \(ne_n\) with a vertex \(y\) supported in the first \(n-1\) coordinates, other than \((n-1)e_{n-1}\). Orthogonality gives \(\|ne_n-y\|_2^2=n^2+\|y\|_2^2\). Among such \(y\), the largest remaining squared norm is exactly \((n-2)^2+1\); the only choices attaining it are the two stated two-gap vertices, coincident for \(n=3\). This proves the second level and its multiplicity. Subtraction yields the sharp gap. \(\square\)

## Verification
The accompanying `pitman_stanley_diameter_checker.py` enumerates all vertices from the active-constraint parametrization using exact rational arithmetic. It checks 72 deterministically seeded positive rational increment configurations in dimensions \(2\) through \(7\), including uniqueness of the diametral pair. It also computes the two highest distinct squared-distance layers and their exact multiplicities for every dimension \(3\) through \(10\). The reproducible command is `python3 pitman_stanley_diameter_checker.py`; successful execution prints `PITMAN_STANLEY_DIAMETER_TWO_TOP_LEVELS_CHECKS_PASSED 72 8`. The mathematical proof establishes all stated dimensions and all strictly positive real increments; finite checks alone cannot do this.

## Relationship to prior work
Pitman and Stanley introduced the polytope and its coordinate inequalities and studied volume, subdivisions, parking functions, and lattice points. Benedetti and collaborators' 2018 preprint analyzes a corresponding flow-polytope model, focusing on normalized volumes and their combinatorial models. Dugan and collaborators' 2023 preprint gives vertices and faces for higher-column generalizations. Hanada, Lentfer, and Vindas-Meléndez study other generalized parking-function polytopes and integer-equivalent realizations. Those results are context for the objects but do not state the exact Euclidean diameter, its unique realizing pair, or the canonical second-largest vertex-distance layer. In particular, integral/affine equivalence by itself does not preserve the specific Euclidean metric used here. Comparison with earlier literature remains subject to historical-priority verification.

## Limitations
The gap and the classification of second-level pairs are proved for unit increments only; for general increments the diameter and its complete equality class are determined, but the next-largest vertex distance may depend on more parameters. The theorem is specific to prefix-sum Pitman–Stanley polytopes in their standard-coordinate Euclidean realization, and is not an assertion about all flow polytopes, nor about edge-graph diameters. The proof does not identify a minimum enclosing Euclidean ball. Independent mathematical audit has not been performed.

## References
1. J. Pitman and R. P. Stanley, *A polytope related to empirical distributions, plane trees, parking functions, and the associahedron*, preprint 1999, arXiv:math/9908029, published in Discrete & Computational Geometry 27 (2002), 603–634.
2. C. Benedetti, R. S. González D’León, C. R. H. Hanusa, P. E. Harris, A. Khare, A. H. Morales, and M. Yip, *A combinatorial model for computing volumes of flow polytopes*, arXiv:1801.07684, first submitted 2018-01-23, Trans. Amer. Math. Soc. 372 (2019), 3369–3404.
3. W. T. Dugan, M. Hegarty, A. H. Morales, and A. Raymond, *Generalized Pitman–Stanley polytope: vertices and faces*, arXiv:2307.09925, first submitted 2023-07-19.
4. M. Hanada, J. Lentfer, and A. R. Vindas-Meléndez, *Generalized Parking Function Polytopes*, arXiv:2212.06885, first submitted 2022-12-13, Ann. Comb. 28 (2024), 575–613.
