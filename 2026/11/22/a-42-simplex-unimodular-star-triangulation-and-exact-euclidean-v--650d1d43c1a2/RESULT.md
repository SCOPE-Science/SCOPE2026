# A 42-simplex unimodular star triangulation and exact Euclidean volume of the Petersen eigenpolytope

## Finding
Let \(G=KG(5,2)\), the Petersen graph with vertices indexed by the ten two-element subsets of \([5]\), and let \(W\) be its five-dimensional adjacency-eigenvalue-\(1\) subspace, equipped with the Euclidean metric inherited from \(\mathbb R^{10}\). Let \(Q\) be orthogonal projection onto \(W\), and set \(X=\operatorname{conv}\{Qe_{ij}:1\le i<j\le5\}\). Then the intrinsic five-dimensional Euclidean volume is
\[
\boxed{\operatorname{Vol}_5(X)=\frac{7}{180\sqrt2}.}
\]
More structurally, coning from the interior point \(0\) over a triangulation of the boundary produces **42 five-simplices of exactly equal Euclidean volume** \(1/(1080\sqrt2)\). Under the integral coordinate map \(x\mapsto Z^{\mathsf T}x\) defined below, these 42 simplices are unimodular in \(\mathbb Z^5\): the transformed polytope has normalized lattice volume exactly \(42\) and ordinary coordinate volume \(7/20\).

## Assumptions and scope
The claim uses the **orthonormal spectral normalization**, not arbitrary rescaled eigenvectors. Let \(E=\binom{[5]}2\) in lexicographic order. Let \(B\) be the unsigned \(5\times10\) vertex-edge incidence matrix of \(K_5\), \(B_{i,e}=\mathbf1_{i\in e}\). Then \(W=\ker B\subset\mathbb R^E\), \(\dim W=5\), and \(Q=I-B^{\mathsf T}(BB^{\mathsf T})^{-1}B\). The graph adjacency matrix equals \(J+I-B^{\mathsf T}B\), hence \(W\) is precisely its eigenvalue-\(1\) subspace. Because \(Q\mathbf1=0\) and \(Q\) has full rank on \(W\), the average of the ten spectral vertices is \(0\), an interior point of \(X\).

This is a statement about this named five-dimensional Euclidean polytope. No claim is made that the known \(10\)-vertex, \(22\)-facet face vector, or the classification of fractional-matching extreme points, is new. The regular four-dimensional Petersen eigenpolytope associated with a **different** eigenspace is not the object here.

## Proof
**1. Facets via the matching polar.** Direct calculation gives \(BB^{\mathsf T}=3I_5+J_5\) and \(\det(BB^{\mathsf T})=648\). The polar of \(X\) in \(W\) is \(X^\circ=\{h\in W:h_e\le1\}\). The affine substitution \(h=\mathbf1-4u\) identifies it with the fractional perfect-matching polytope \(F=\{u\ge0:Bu=\mathbf1\}\).

For completeness, a point of \(F\) is extreme exactly when the incidence columns corresponding to its positive support are linearly independent. A degree-one vertex in that support forces its incident edge to have weight one, isolating a matched-edge component. Every remaining connected component has minimum degree two and, by incidence-column independence, as many edges as vertices. It is therefore a cycle; even cycles have alternating column dependencies, so only odd cycles survive, with weight one-half on each edge. Conversely, disjoint unions of unit matched edges and half-weight odd cycles yield independent columns and are extreme. On five graph vertices the possibilities are precisely one \(5\)-cycle (\(12\) choices) or one triangle plus the edge joining its two complementary vertices (\(10\) choices). Hence the facets of \(X\) are indexed by the *complements* of these support sets: twelve facets with five vertices, and ten with six vertices. The former are simplices, and the latter have the six crossing edges of a \(K_{2,3}\).

**2. Triangulating the nonsimplicial facets.** For a \(K_{2,3}\) facet, write its bipartition as \(\{a,b\}\sqcup T\), \(|T|=3\). Among its six vertices there is a unique affine circuit
\[
\sum_{t\in T}Qe_{at}=\sum_{t\in T}Qe_{bt},
\]
indeed the difference of the two incidence-edge sums is \(B^{\mathsf T}(e_a-e_b)\) and is killed by \(Q\). Its unique \(3\)-against-\(3\) Radon partition yields the standard circuit triangulation into three four-simplices: delete in turn one of the three vertices \(Qe_{at}\), retaining the other five. Their relative interiors are disjoint and their union is the facet. The twelve original simplex facets together with three simplices on each of the ten \(K_{2,3}\) facets give \(12+3\cdot10=42\) boundary four-simplices. Coning each from \(0\) triangulates \(X\).

**3. Equality of all volumes.** For any five-element set \(S\subset E\), with complement \(T=E\setminus S\), the complementary-minors formula for an orthogonal projector gives
\[
\det Q_{S,S}=\frac{\det(B_T)^2}{\det(BB^{\mathsf T})}.
\]
For a simplex facet of the five-cycle type, its complementary five-edge graph is another five-cycle. For any simplex selected from a \(K_{2,3}\) facet in step 2, its complementary five-edge graph is a triangle with two tree edges attached. In both cases this graph has exactly one odd cycle and the remaining edges form trees; peeling leaves reduces its unsigned-incidence determinant to that of the odd cycle, namely \(\pm2\). Consequently
\[
\det Q_{S,S}=\frac{4}{648}=\frac1{162},
\]
and the Euclidean volume of its pyramid with apex \(0\) is \(\sqrt{\det Q_{S,S}}/5!=1/(1080\sqrt2)\). Summing the \(42\) disjoint-interior pyramids proves the volume formula.

**4. The unimodular coordinate model.** The columns of the integer \(10\times5\) matrix
\[
Z=\begin{pmatrix}
0&0&1&1&1\\
1&1&0&0&1\\
-1&0&-1&0&-1\\
0&-1&0&-1&-1\\
-1&-1&-1&-1&-1\\
1&0&0&0&0\\
0&1&0&0&0\\
0&0&1&0&0\\
0&0&0&1&0\\
0&0&0&0&1
\end{pmatrix}
\]
form a basis of \(\ker B\). Its last five rows are the identity, and \(\det(Z^{\mathsf T}Z)=162\). The isomorphism \(x\mapsto Z^{\mathsf T}x\) maps the ten projected vertices to the ten integer rows of \(Z\), and scales five-volume by \(\sqrt{162}\). For each of the \(42\) chosen five-vertex sets, the row determinant of \(Z\) is \(\pm1\), either by the complementary-minor identity above or direct integer computation. The resulting star triangulation is therefore unimodular in the full lattice \(\mathbb Z^5\) (the last five vertex images already form its basis). It has normalized volume \(42\), coordinate volume \(42/5!=7/20\), and intrinsic spectral volume \((7/20)/\sqrt{162}=7/(180\sqrt2)\).

## Verification
Run `python3 artifacts/verify.py` from the extracted package directory. It uses only the Python standard library and checks the exact kernel and Gram identities, exhaustively reconstructs every facet using all \(\binom{10}{5}=252\) candidate five-vertex hyperplanes, obtains \(12\) five-vertex and \(10\) six-vertex facet sets, compares them with independently enumerated five-cycle and triangle-plus-edge supports, and checks the \(42\) integer determinants and their complementary incidence minors. The checker prints `PETERSEN_EIGENPOLYTOPE_42_UNIMODULAR_PYRAMIDS_PASS`. The proof of the triangulation and its volume is mathematical; a successful finite checker run independently tests the complete finite object rather than standing in for an infinite argument.

## Relationship to prior work
Babecki and Thomas, *Graphical Designs and Gale Duality* (first public 2022-04-04), Example 3.10, study exactly the Petersen five-dimensional eigenpolytope in an equivalent eigenbasis and state its \(10\) vertices, \(22\) facets, and \(12+10\) facet-type split. Those **are previously known and not part of the novelty claim**. Winter's spectral-polytope account explains the orthonormal normalization and cites earlier work on Petersen eigenpolytopes. A previously published *Parity-controlled John and Löwner ellipsoids of Kneser pair-eigenpolytopes* explicitly identifies the all-\(n\) fractional-matching polar and characterizes metric ellipsoid contacts; its \(n=5\) case also implies the above facets and is credited. Neither its full result nor the inspected full Petersen passage of Babecki–Thomas determines this intrinsic volume, the equal-volume decomposition, or the integer unimodular triangulation. Facet counts and enclosing-ball radii alone do not imply a five-dimensional volume. A possible earlier equivalent exact volume/triangulation in the inaccessible 1986 Petersen-polytopes report remains an originality risk.

## Limitations
The metric result applies to the eigenvalue-\(1\) projector normalization; an arbitrary linear rescaling of an eigenbasis changes volume. The result is one precisely identified five-dimensional polytope and does not claim a formula for all Kneser graphs or all eigenpolytopes. Historical priority is provisional: Powers' 1986 report was not available in full, and an equivalent unindexed triangulation or computation could exist. No independent audit is asserted.

## References
1. C. Babecki and R. R. Thomas, *Graphical Designs and Gale Duality*, arXiv:2204.01873, first submitted 2022-04-04, Example 3.10, https://arxiv.org/abs/2204.01873 .
2. M. Winter, *Eigenpolytopes, Spectral Polytopes and Edge-Transitivity*, arXiv:2009.02179, 2020, https://arxiv.org/abs/2009.02179 ; and *Spectral Realizations of Symmetric Graphs*, doctoral thesis (2021), chapter 3, https://warwick.ac.uk/fac/sci/maths/people/staff/winter/thesis.pdf .
3. *Parity-controlled John and Löwner ellipsoids of Kneser pair-eigenpolytopes*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-parity-controlled-john-and-l-wner-ellipsoids-of-kneser-pair-eige--71ae72613d53 .
4. D. L. Powers, *The Petersen Polytopes*, Clarkson University technical report (1986), known bibliographically; full text not obtained.
5. C. Babecki and D. Shiroma, *Eigenpolytope Universality and Graphical Designs*, arXiv:2209.06349, first submitted 2022-09-13, https://arxiv.org/abs/2209.06349 .
