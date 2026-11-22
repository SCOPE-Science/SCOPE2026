# Signed-pairing symmetry of first homology in triangular-graph monophonic-position complexes

## Finding
Let \(n\ge4\), let \(T_n=L(K_n)=J(n,2)\) be the triangular graph, and let \(\mathcal P_n\) be the simplicial complex of all vertex subsets meeting every induced path of \(T_n\) in at most two vertices. Relabelling the \(n\) ground points induces a natural action of \(\mathfrak S_n\) on this complex. Write \(H=(\mathfrak S_2\wr\mathfrak S_2)\times\mathfrak S_{n-4}\): this is the stabilizer of an unordered pair of disjoint two-element ground sets. Let \(\varepsilon\) be the one-dimensional representation of \(H\) which is \(-1\) when the two two-element blocks are exchanged, and \(+1\) when the blocks are preserved, independent of permutations within blocks or on unused labels.

**The new equivariant theorem** identifies the first *integral* homology, including every symmetry action, as the signed matching-pair permutation lattice:
\[
\boxed{\widetilde H_1(\mathcal P_n;\mathbb Z)
\cong_{\mathbb Z[\mathfrak S_n]}
\operatorname{Ind}_{H}^{\mathfrak S_n}\varepsilon.}
\]
Its rank is \(3\binom n4\). For a ground-label permutation \(\sigma\), the integral first-homology character is exactly
\[
\chi_n(\sigma)=\#\{\text{fixed unordered two-edge matchings with no block exchange}\}
-\#\{\text{fixed unordered two-edge matchings with block exchange}\}.
\]
In particular, the rational representation is multiplicity-free with the **complete Specht decomposition**
\[
\boxed{\widetilde H_1(\mathcal P_n;\mathbb Q)
\cong \bigoplus_{\substack{\lambda\vdash n\\\lambda/(3,1)\ \text{a horizontal strip}}} S^\lambda.}
\]
For \(n\ge7\), exactly six constituents occur, indexed by
\[
(n-1,1),\ (n-2,2),\ (n-3,3),\ (n-2,1,1),\ (n-3,2,1),\ (n-4,3,1).
\]
The horizontal-strip formula gives the correct exceptions for \(n=4,5,6\). No nonzero rational first-homology class is fixed by all ground-label permutations. More generally, for any subgroup \(Q\le\mathfrak S_n\), the rank of the invariant integral first-homology lattice equals the number of \(Q\)-orbits on two-edge ground matchings whose pointwise orbit stabilizer never exchanges their two component edges.

**Previously implied underlying structure (credited).** Theorem 20 on strong two-monophonicity of Johnson graphs by Brešar, Cornet and Dravec (arXiv:2509.18784, 2025) implies that the monophonic-position faces of cardinality at least three are exactly the cliques of \(T_n\). Accordingly \(\mathcal P_n\) is its clique complex with one extra, unfilled edge for each unordered matching of two disjoint root edges. The resulting ordinary face and facet polynomials are
\[
P_n(z)=1+Nz+\binom N2z^2+\binom n3z^3+n\sum_{k=3}^{n-1}\binom{n-1}{k}z^k,
\qquad N=\binom n2,
\]
\[
M_n(z)=3\binom n4z^2+\binom n3z^3+n z^{n-1}.
\]
The nonequivariant homotopy type \(\bigvee^{3\binom n4}S^1\vee\bigvee^{\binom{n-1}3}S^2\) follows directly from that published strong-two-monophonic result and the earlier line-graph clique-complex homotopy theorem of Goyal, Shukla and Singh. These plain counts and nonequivariant homotopy types are supplied for context, not asserted as the original advance. The assertion here is the exact *natural integral symmetry module*, signed trace formula and multiplicity-free rational irreducible classification.

## Assumptions and scope
All graphs are finite, simple and undirected. The vertex set of \(T_n\) is the set of unordered pairs of distinct labels in \([n]\). Two vertices are adjacent precisely when their represented pairs intersect. An *induced path* has no edges between its nonconsecutive vertices. A subset \(S\) is *monophonic position* if no induced path contains three distinct vertices of \(S\), regardless of whether these vertices are endpoints or internal to that path. The empty set is allowed. The monophonic-position complex is the abstract simplicial complex of all such subsets, and its realization is used for the homotopy claim. A facet is an inclusion-maximal face, not merely a face of maximum cardinality. A full root star is the set of all \(n-1\) edges incident to a fixed label. All counts refer to labelled graphs, and all polynomial identities are identities in \(\mathbb Z[z]\).

## Proof
**Established preliminary and its direct reconstruction.** The 2025 strong-two-monophonic theorem applies to all Johnson graphs, including \(T_n\). We independently reconstruct the needed special case for precise boundary and sign conventions, before deriving the new equivariant result.

**1. Two disjoint root edges cannot coexist with a third selected edge.** Suppose the represented set contains the disjoint root edges \(ab\) and \(cd\), along with a distinct root edge \(uv\). We produce a *simple root path* containing all three edges, so that its consecutive edges form an induced path in the line graph. There are three cases, up to renaming the endpoints of \(ab\) and \(cd\).

If \(uv\) has both endpoints in \(\{a,b,c,d\}\), it must cross the two original edges; take \(uv=ac\) and the simple path \(b-a-c-d\). If \(uv\) has one endpoint among those four and one new endpoint \(x\), take \(uv=ax\) and the simple root path \(b-a-x-c-d\). If \(uv\) is disjoint from all four endpoints, write \(uv=xy\) and take \(a-b-x-y-c-d\). Every indicated bridge is available in the complete graph; all root vertices on each path are distinct. The line-graph vertices corresponding to nonconsecutive edges of a simple root path are nonadjacent, so the resulting line-graph path is induced. Thus any selection containing disjoint root edges and a third edge violates monophonic position. This also establishes the claim when \(n=4\) or \(5\), since cases requiring additional root vertices are then simply absent.

Conversely, if a family of root edges is pairwise incident, its corresponding vertices form a clique in \(T_n\). No induced path can contain three vertices from a clique: of any three path positions, at least two are nonconsecutive, and their adjacency would be a chord. Hence every pairwise-incident family is monophonic position. Any set of at most two vertices is vacuously monophonic position. This proves the characterization, including all quantifiers.

**2. Pairwise-intersecting edge families are stars or triangles.** In any family of at least three distinct pairwise-intersecting two-subsets, choose \(ab\) and \(ac\). If every edge contains \(a\), it is a root star family. Otherwise an edge missing \(a\) must be \(bc\), and then no other edge can meet all of \(ab,ac,bc\); the family is exactly the triangle \(\{ab,ac,bc\}\). A star of at least three edges has a uniquely determined center, and a three-edge triangle is never a star.

**3. Count faces and facets.** Let \(N=\binom n2\). All zero-, one-, and two-element sets qualify, yielding the first three terms of \(P_n\). A three-edge root triangle contributes one face for each three-subset of labels, giving \(\binom n3z^3\). For each \(k\) with \(3\le k\le n-1\), a size-\(k\) root star is specified by its unique center and a \(k\)-subset of its \(n-1\) incident edges. This gives the remaining sum, without double counting.

A disjoint pair of root edges cannot accept a third edge, so it is a facet. Each four-label subset has exactly three pairings into two disjoint edges, hence exactly \(3\binom n4\) such facets. A root triangle cannot accept another root edge while preserving pairwise incidence, hence every one of the \(\binom n3\) root triangles is a facet. A proper star of size at least three can be enlarged by an unused edge at its center; the \(n\) full root stars are facets. No size-one or incident size-two set is maximal for \(n\ge4\). These are all facets. The claimed sizes, counts and gaps follow.

**4. Topological identification of the complex.** Let \(C_n=\operatorname{Cl}(T_n)\) denote the *clique* complex of the triangular graph. By Step 1, the only faces of \(\mathcal P_n\) that are not already faces of \(C_n\) are the pairs of disjoint root edges. There are exactly \(3\binom n4\) such pairs. Each is a newly attached one-simplex and belongs to no two-simplex of \(\mathcal P_n\). The space \(|C_n|\) is path-connected for \(n\ge4\); adding \(r\) one-cells between points in an already path-connected CW complex therefore wedges on \(r\) circles, up to homotopy. Thus
\[
|\mathcal P_n|\simeq |C_n|\vee \bigvee^{3\binom n4}S^1.
\]

The established line-graph clique-complex equivalence of Goyal, Shukla and Singh (Lemma 3.2 of arXiv:2009.12130v2) gives \(|C_n|\simeq |\operatorname{Cl}(K_n)^{(2)}|\), the two-skeleton of the simplex on \([n]\). This previously known topological equivalence is an explicit premise, not a new lemma. For completeness, in the two-skeleton take the subcomplex consisting of all vertices and edges and all triangles containing label \(1\). It is the cone with apex \(1\) over the complete graph on the other \(n-1\) labels and is contractible. Every other triangle is on three labels distinct from \(1\), and its attaching boundary is wholly in that contractible subcomplex. Collapsing the contractible subcomplex (a CW cofibration) is a homotopy equivalence and leaves one two-sphere for each of the \(\binom{n-1}3\) remaining triangles. Therefore \(|C_n|\simeq\bigvee^{\binom{n-1}3}S^2\), establishing the full wedge, integral homology and fundamental-group claims. At \(n=4\), this specializes to \(\bigvee^3S^1\vee S^2\), not an exceptional case.


**5. The new integral equivariant identification.** Let \(C_n=\operatorname{Cl}(T_n)\subseteq\mathcal P_n\). From the established clique-complex equivalence, \(C_n\) is connected and has \(H_1(C_n;\mathbb Z)=0\), for all \(n\ge4\). The relative simplicial chain groups \(C_i(\mathcal P_n,C_n;\mathbb Z)\) vanish for all \(i\ne1\): the complexes have identical vertices and all higher-dimensional faces, and the only new one-faces are unordered pairs of disjoint ground edges. Every such one-face \(e=[ab,cd]\) has boundary in \(C_n\), so its relative boundary is zero. Thus \(H_1(\mathcal P_n,C_n;\mathbb Z)\) is free on *oriented* disjoint-pair edges, with relation \([cd,ab]=-[ab,cd]\).

The exact sequence of the pair reads
\[
0=H_1(C_n)\longrightarrow H_1(\mathcal P_n)
\longrightarrow H_1(\mathcal P_n,C_n)
\longrightarrow H_0(C_n)\xrightarrow{\cong}H_0(\mathcal P_n).
\]
The middle injection is therefore an isomorphism, canonically equivariant for every relabelling permutation. For a basis vector \([ab,cd]\), relabelling sends it to \([\sigma(a)\sigma(b),\sigma(c)\sigma(d)]\); reversing the two unordered ground edges changes its sign. The group \(\mathfrak S_n\) acts transitively on the \(3\binom n4\) pairs of disjoint ground edges, with stabilizer \(H\) as stated, and its stabilizer action on an oriented generator is exactly \(\varepsilon\). This proves the integral induced-module isomorphism and the signed-fixed-matching trace formula without division by group order or rational coefficients. For a subgroup \(Q\le\mathfrak S_n\), an invariant vector supported on one orbit of matchings must have coefficients related by their orientation signs. A nonzero integral solution exists exactly when every element of the stabilizer of one matching preserves its two component edges individually; then this orbit contributes one primitive invariant generator. This proves the subgroup-invariant rank formula.

**6. All rational irreducible constituents.** Restrict to the four involved ground labels. The three-oriented-pairing representation of \(\mathfrak S_4\) has character \(\#\operatorname{Fix}(\sigma)-1\) on every \(\sigma\in\mathfrak S_4\); directly, its values on the cycle types \(1^4,2\,1^2,2^2,3\,1,4\) are \(3,1,-1,0,-1\). This is the standard irreducible Specht module \(S^{(3,1)}\). Induction in stages now identifies the rational homology representation as
\[
\operatorname{Ind}_{\mathfrak S_4\times\mathfrak S_{n-4}}^{\mathfrak S_n}
\bigl(S^{(3,1)}\boxtimes\mathbf1\bigr).
\]
By the horizontal-strip (Pieri) rule, its Frobenius characteristic is \(s_{(3,1)}h_{n-4}\), and the decomposition in the finding follows with multiplicity one in every valid shape. Equivalently, all partitions \(\lambda\) are characterized by
\(\lambda_1\ge3\ge\lambda_2\ge1\ge\lambda_3\ge0\), with \(\lambda_i=0\) for \(i\ge4\) and \(|\lambda|=n\). The trivial shape \((n)\) never occurs, so the rational invariant subspace is zero. This completes the new representation-theoretic claim. The integral formula is stronger than its rational decomposition because it retains the precise signed permutation lattice.

## Verification
Three independent standalone Python 3 scripts accompany the theorem. `verify_monophonic_triangular.py` reconstructs the line graphs and all induced paths, then checks all \(2^{\binom n2}\) subsets for \(3\le n\le6\), the face and facet counts, and Euler characteristic, returning `VERIFY_OK`. `verify_homology.py` independently generates the complex and computes mod-two boundary ranks for \(4\le n\le7\), obtaining \((\beta_1,\beta_2)=(3,1),(15,4),(45,10),(105,20)\) and returning `HOMOLOGY_OK`. `verify_equivariance.py` computes the actual signed action of every permutation of \(\mathfrak S_4\) on the three pairing edges and checks the exact \(S^{(3,1)}\) character on all 24 permutations. For \(4\le n\le9\), it checks the number of oriented-pairing basis elements, character traces for representative permutations, and the exact hook-length dimensions of all Pieri constituents against \(3\binom n4\); it reports `EQUIVARIANCE_OK`. These are finite checks of the calculation and sign conventions; the long exact sequence and induction argument prove the integral statement for every order.

## Relationship to prior work
**Decisive stronger prior coverage for the underlying face characterization.** Brešar, Cornet and Dravec, *Monophonic number of Kneser graphs and strongly 2-monophonic graphs* (arXiv:2509.18784v1, 2025-09-23), Theorem 20, prove that **every Johnson graph** is strongly 2-monophonic: between each nonadjacent vertex pair, an induced path may be chosen through any prescribed third vertex. This implies that any monophonic-position set of cardinality at least three must be a clique; hence the face characterization and ordinary face/facet polynomials for \(T_n\) are direct combinatorial consequences, **not** a new foundational theorem. Thomas et al., arXiv:2012.10330 (2020-12-18), supply the original monophonic-position definition. Goyal, Shukla and Singh, arXiv:2009.12130 (2020-09-25), give the line-graph clique-complex two-skeleton equivalence. The published 2026 *equivariant star-collapse model for line-graph clique complexes* strengthens the latter to determine the integral \(\mathfrak S_n\)-module on the **second** homology of \(C_n\). Consequently the nonequivariant sphere wedge and previously known \(H_2\) equivariant lattice are likewise not claimed as new.

The new object of calculation is \(H_1(\mathcal P_n;\mathbb Z)\), which vanishes on the old clique subcomplex but is created by oriented disjoint-edge pair cells. The signed swap action on those cells is *not* determined by an ordinary Betti count, and none of the inspected results gives its integral induced module, exact trace on every relabelling or rational Specht decomposition. The published `Full general-position polynomial of triangular graphs by star–triangle components` (2026) treats the geodesic rather than all-induced-path condition; the published `Two-round induced-path closure and strictly log-concave lattices of triangular graphs` (2026) treats an induced-three-path Horn closure rather than homological symmetry of the monophonic-position complex. Both were inspected at statement and proof level and neither supplies this integral module. Publication priority remains provisional, and an unindexed equivalent representation calculation is possible.

## Limitations
The genuinely new claim is the equivariant \(H_1\) lattice and its character/decomposition, not strong two-monophonicity, the ordinary cardinality polynomials, the nonequivariant homotopy wedge, or the published \(H_2\) module. The theorem concerns only triangular graphs \(L(K_n)\) with \(n\ge4\); it does not determine integral homology representations for all Johnson graphs. The Specht decomposition is rational and does not purport to split the signed integral lattice into integral Specht summands. Finite calculations check low orders, while the relative exact sequence, stabilizer action, and Pieri proof cover every \(n\). Independent validation and exhaustive publication-priority clearance have not been performed.

## References
0. B. Brešar, M. G. Cornet and T. Dravec, *Monophonic number of Kneser graphs and strongly 2-monophonic graphs*, arXiv:2509.18784, first posted 2025-09-23, https://arxiv.org/abs/2509.18784.
1. E. J. Thomas, S. V. U. Chandran, J. Tuite and G. Di Stefano, *On monophonic position sets in graphs*, arXiv:2012.10330, first posted 2020-12-18, https://arxiv.org/abs/2012.10330.
2. S. Goyal, S. Shukla and A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130, first posted 2020-09-25, especially Lemma 3.2 of v2, https://arxiv.org/abs/2009.12130.
3. G. Di Stefano, S. Klavžar, A. Krishnakumar, J. Tuite and I. G. Yero, *Lower General Position Sets in Graphs*, arXiv:2306.09965, first posted 2023-06-16, https://arxiv.org/abs/2306.09965.
4. *Full general-position polynomial of triangular graphs by star–triangle components*, published research note, 2026-10-13, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-full-general-position-polynomial-of-triangular-graphs-by-star-tr--9b9fdc66bc5e.
5. *Two-round induced-path closure and strictly log-concave lattices of triangular graphs*, published research note, 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-two-round-induced-path-closure-and-strictly-log-concave-lattices--50136b5228e5.
6. *Rigidity and exact dual-general-position polynomial of triangular graphs*, published research note, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-rigidity-and-exact-dual-general-position-polynomial-of-triangula--4acb8f5dae33.
7. *An equivariant star-collapse model for line-graph clique complexes*, published research note, 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-an-equivariant-star-collapse-model-for-line-graph-clique-complex--559a0d730ca9.
