# Exact Hausdorff and volume deficits of the Euclidean alternahedron

## Finding
For each integer \(n\ge3\), write \(m=(n+1)/2\), let \(p_\sigma=(\sigma(1)-m,\ldots,\sigma(n)-m)\) for \(\sigma\in S_n\), and form the standard centered permutohedron \(P_n=\operatorname{conv}\{p_\sigma:\sigma\in S_n\}\) and alternahedron \(A_n=\operatorname{conv}\{p_\sigma:\sigma\in A_n^{\mathrm{grp}}\}\), where \(A_n^{\mathrm{grp}}\) denotes the even-permutation subgroup. All distances and intrinsic volumes below are Euclidean in the zero-sum hyperplane.

The **metric–volume deletion theorem** is
\[
 d_H(P_n,A_n)=\sqrt{\frac{12}{n(n^2-1)}},\qquad
 \operatorname{Vol}_{n-1}(A_n)=\sqrt n\left(n^{n-2}-\frac n2\right),
\]
and hence
\[
 \frac{\operatorname{Vol}_{n-1}(P_n\setminus A_n)}{\operatorname{Vol}_{n-1}(P_n)}
 =\frac{1}{2n^{n-3}}.
\]
Despite deleting half the vertices, the volume deficit is \(1/(2n^{n-3})\), whereas the Hausdorff deficit is asymptotic to \(\sqrt{12}\,n^{-3/2}\).

More precisely, for every *odd* \(\sigma\), let \(s_i\sigma\) mean the permutation obtained by exchanging **values** \(i\) and \(i+1\) in \(\sigma\). The unique nearest point in \(A_n\) to \(p_\sigma\) is
\[
 z_\sigma=\sum_{i=1}^{n-1}\frac{6i(n-i)}{n(n^2-1)}p_{s_i\sigma}.
\]
Every coefficient is strictly positive: all \(n-1\) neighboring even vertices participate. In particular, the squared vertex-robustness is exactly \(12/[n(n^2-1)]\).

A related width identity, obtained by applying the earlier parity rearrangement principle to this specific metric normalization, is as follows. Let \(u\) have pairwise distinct coordinates and put \(\delta(u)=\min_{i<n}(u_{(i+1)}-u_{(i)})\), where \(u_{(i)}\) are the increasingly ordered coordinates. Then
\[
 W_{P_n}(u)-W_{A_n}(u)=\delta(u)\,k_n(u),
\]
where \(k_n(u)=1\) if \(n\equiv2,3\pmod4\), and \(k_n(u)\in\{0,2\}\) otherwise. For a direction uniform on the unit sphere, the two latter alternatives have probability \(1/2\) each. This width identity is included as a geometrical comparison, not asserted to be a new rearrangement theorem.

## Assumptions and scope
The statement uses the regular arithmetic-progression orbit \((1,\ldots,n)\), not arbitrary strictly increasing labels. The containing full permutohedron and the alternahedron are \((n-1)\)-dimensional. Intrinsic volume is unnormalized Euclidean \((n-1)\)-volume. The Hausdorff distance is symmetric; because \(A_n\subseteq P_n\), only distance from \(P_n\) to \(A_n\) contributes. Width \(W_K(u)\) is \(\max_{x\in K}\langle u,x\rangle-\min_{x\in K}\langle u,x\rangle\). The spherical width statement excludes the measure-zero tie directions.

## Proof
**1. Exact vertex cuts.** Put \(R^2=\|p_\sigma\|^2=n(n^2-1)/12\). For any two permutation vertices,
\[
\langle p_\sigma,p_\tau\rangle=R^2-\tfrac12\|p_\sigma-p_\tau\|^2.
\]
Every distinct pair has squared separation at least \(2\), with equality precisely when their values differ by an adjacent-value transposition. Distinct permutations of the same parity have squared separation at least \(4\): the only possible squared separation \(2\) is one adjacent transposition, of odd parity. Therefore, for odd \(\sigma\), the inequality
\[
H_\sigma:\quad \langle p_\sigma,x\rangle\le R^2-1
\]
contains all even vertices; its equality vertices are exactly \(p_{s_i\sigma}\), \(1\le i<n\). The open cap of \(P_n\) beyond this plane is the interior portion of the simplex
\(C_\sigma=\operatorname{conv}\{p_\sigma,p_{s_1\sigma},\ldots,p_{s_{n-1}\sigma}\}\).
Indeed the plane lies at the endpoints of the only edges from \(p_\sigma\), and all other vertices are strictly on the safe side; clipping introduces no new edge-intersection vertices.

The cuts can be applied in any order: every unremoved odd vertex is strictly safe for the other cuts; every even vertex is safe; and a cut introduces only the previously present even neighbors of its removed odd vertex. Thus
\[
 A_n=P_n\cap\bigcap_{\sigma\ \mathrm{odd}}H_\sigma.
\]
For two different odd permutations \(\sigma,\tau\), at every vertex \(p_\rho\),
\(\langle p_\sigma+p_\tau,p_\rho\rangle\le2R^2-2\): if \(\rho\) is even, each summand is at most \(R^2-1\); if \(\rho\) is odd, at most one summand can be \(R^2\) and the other is at most \(R^2-2\). The same inequality holds throughout \(P_n\), proving that the open caps for distinct odd vertices cannot intersect. Their interiors are disjoint, and their intersections have zero intrinsic \((n-1)\)-volume.

**2. Volume.** At a removed odd vertex, the \(n-1\) simplex edge vectors are a coordinate permutation of \(e_i-e_{i+1}\), \(1\le i<n\). Their Gram matrix has diagonal entries \(2\) and adjacent off-diagonal entries \(-1\); the determinant is \(n\) by the tridiagonal recurrence \(D_k=2D_{k-1}-D_{k-2}\). Thus each cap simplex has volume \(\sqrt n/(n-1)!\). There are \(n!/2\) such simplices, so total lost volume equals \(n\sqrt n/2\). The usual full permutohedron is a translate of the zonotope \(\sum_{i<j}[0,e_i-e_j]\). Its zonotope volume expansion sums one parallelepiped of volume \(\sqrt n\) for each spanning tree of \(K_n\), and there are \(n^{n-2}\) such trees. Hence \(\operatorname{Vol}_{n-1}(P_n)=\sqrt n\,n^{n-2}\), proving the formula.

**3. Unique metric projections.** Fix odd \(\sigma\). Since \(A_n\subseteq H_\sigma\), the distance from \(p_\sigma\) is at least the distance to the plane \(\partial H_\sigma\), namely \(1/R\). Its perpendicular foot is \(z=p_\sigma-p_\sigma/R^2\). For \(\sigma\) in increasing order, replacing values \(i,i+1\) produces an edge vector \(e_i-e_{i+1}\), and the telescoping identity
\[
\sum_{i=1}^{n-1}\frac{6i(n-i)}{n(n^2-1)}(e_i-e_{i+1})=-\frac{p_{\mathrm{id}}}{R^2}
\]
holds componentwise. Coordinate permutation gives the same identity for every odd \(\sigma\). Thus \(z=z_\sigma\) is a convex combination of surviving even vertices, and achieves the lower bound. Uniqueness follows from uniqueness of orthogonal projection to a closed convex set. Finally the distance-to-a-convex-set function is convex, so its maximum on \(P_n\) is achieved at a vertex; even vertices contribute zero, and all odd vertices have distance \(1/R\). This proves the Hausdorff formula.

**4. Width comparison (prior rearrangement mechanism).** For a direction \(u\) with distinct entries, the rearrangement inequality selects the unique optimal permutation by assigning increasing labels to increasing coordinates. Constraining this choice to the opposite parity costs exactly \(\delta(u)\): any differing assignment has at least one inversion, removing which increases the objective by a positive integer label difference times an ordered coordinate gap, at least \(\delta(u)\); swapping the adjacent labels across a least gap attains equality. The maximum and minimum unconstrained permutations differ by reversal, whose parity is \((-1)^{n(n-1)/2}\). Therefore exactly one extremal permutation is odd when \(n\equiv2,3\pmod4\), and either both or neither are odd when \(n\equiv0,1\pmod4\). For a permutation-invariant continuously distributed direction, these two latter cases occur equally often. The width identity follows.

## Verification
The standalone `check.py` uses exact rational arithmetic to verify nearest-point barycentric weights, supporting inequalities, and separation bounds, checks hundreds of independent directional-width cases against direct permutation optimization, and independently compares Euclidean hull volumes and supporting-hyperplane counts for \(3\le n\le6\) using SciPy. It checks the tridiagonal determinant recurrence through size \(199\). Execute `python check.py` in an environment with Python 3, NumPy and SciPy. The infinite-dimensional claims are proved by the preceding arguments; finite tests are not their substitute.

## Relationship to prior work
The alternahedron itself, its vertex cuts and its face structure are **prior mathematics**, not claimed here as new. Steinkamp (1999, §3.2) gives a specific family of alternahedron inequalities and numerical facet data; Cruickshank and Kelly (first public appearance October 25, 2005; published 2006) establish a rearrangement inequality and describe its face lattice. The width statement is a transparent metric specialization of such parity rearrangement. The quantitative focus of the present theorem is instead the *exact Euclidean Hausdorff deficit, the unique metric projection with strictly positive quadratic weights, and the exact intrinsic volume deficit under removal of half the permutation vertices*. Awasthi, Kalantari and Zhang (public preprint February 5, 2018) motivate point-to-remaining-hull vertex robustness in convex-hull algorithms, but do not establish these particular alternahedral metric or volume formulas.

## Limitations
Historical priority is not established definitively. The full text of the 2005 Cruickshank–Kelly article was not accessible for a complete comparison, although its abstract, publication metadata, and Steinkamp's complete earlier alternahedron discussion were inspected. Because the earlier literature already treats the face lattice and parity rearrangements, **no novelty is asserted for those underlying components**. The quantitative formulas have been independently proved here, but an unlocated older computation could contain them. No independent mathematical audit has been performed. This is not a claim about arbitrary orbit vectors, matrix-valued even permutation polytopes, or a higher-order deletion rule.

## References
1. P. Awasthi, B. Kalantari and Y. Zhang, “Robust Vertex Enumeration for Convex Hulls in High Dimensions,” arXiv:1802.01515, first posted 2018-02-05; AISTATS (2018). https://arxiv.org/abs/1802.01515
2. J. Cruickshank and S. Kelly, “Rearrangement Inequalities and the Alternahedron,” *Discrete & Computational Geometry* 35 (2006), 241–254; first published online 2005-10-25. https://doi.org/10.1007/s00454-005-1199-6
3. H. Steinkamp, *Convex Polytopes of Permutation Matrices*, Reed College thesis (1999), §3.2. https://people.reed.edu/~davidp/homepage/students/steinkamp.pdf
4. F. Ardila, F. Castillo, C. Eur and A. Postnikov, “Coxeter submodular functions and deformations of Coxeter permutahedra,” *Advances in Mathematics* 365 (2020), 107039. https://doi.org/10.1016/j.aim.2020.107039
5. A. Postnikov, “Permutohedra, Associahedra, and Beyond,” *International Mathematics Research Notices* (2009), 1026–1106. https://doi.org/10.1093/imrn/rnn153
