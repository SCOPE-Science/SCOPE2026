# Mixed circle-and-two-sphere homotopy of one-tolerance complexes of disjoint cliques

## Finding

For pairwise disjoint nonempty finite vertex sets \(A_1,\ldots,A_r\), \(r\ge2\), with \(a_i=|A_i|\), the one-tolerance complex of the disjoint union of full simplices has the integral homotopy type
\[
\mathcal T_1\!\left(\bigsqcup_{i=1}^r\Delta(A_i)\right)
\simeq\bigvee^{\binom{r-1}{2}}S^1\ \vee\
\bigvee^{\sum_{i<j}(a_i-1)(a_j-1)}S^2.
\]
Zero wedge multiplicities are omitted. There is also a natural integral refinement:
\[
H_1\cong H_1(K_r;\mathbb Z),\qquad
H_2\cong\bigoplus_{i<j}U(A_i)\otimes_{\mathbb Z}U(A_j),
\]
where \(K_r\) is the complete graph on the block indices and \(U(A)=\ker(\mathbb Z^{A}\xrightarrow{\sum}\mathbb Z)\). These identifications respect the action of \(\prod_i \mathfrak S_{A_i}\) (trivial on the first group). All higher reduced integral homology vanishes. For \(r\ge3\) and two or more blocks of size at least two, both displayed homology degrees are nonzero.

## Assumptions and scope

A simplicial complex includes the empty face. \(\Delta(A)\) is the simplex on a finite nonempty set \(A\), and \(D(A)\) is its zero-dimensional subcomplex consisting of the empty face and all singletons. The disjoint union \(K\) has faces exactly the subsets of individual blocks. A set \(\sigma\) is a face of \(\mathcal T_1(K)\) if a deletion of at most one vertex from \(\sigma\) leaves a face of \(K\). All spaces are geometric realizations of the finite abstract simplicial complexes, and all homology groups are with integer coefficients unless noted otherwise.

## Proof

**1. Pair-support decomposition.** For each unordered pair \(i<j\), set
\[
E_{ij}=\left(\Delta(A_i)*D(A_j)\right)
\cup\left(D(A_i)*\Delta(A_j)\right).
\]
The tolerance condition says that a face is supported on one block, or on precisely two blocks with all but at most one vertex in one of them. Hence \(X=\bigcup_{i<j}E_{ij}\). Distinct pair spaces intersect in exactly \(\Delta(A_i)\) when they share precisely block \(i\), and do not intersect when their block pairs are disjoint (except for the conventional empty face). In particular, the intersections of their nonempty geometric realizations are the asserted simplices or the empty set. No face of \(X\) meets three blocks.

**2. The two-block edge space.** The subcomplexes \(P_{ij}=\Delta(A_i)*D(A_j)\) and \(Q_{ij}=D(A_i)*\Delta(A_j)\) are both contractible, since joining with a full nonempty simplex is a cone. Their intersection is \(D(A_i)*D(A_j)\), the complete bipartite graph \(K_{a_i,a_j}\). Simplicial inclusions are cofibrations. The homotopy-pushout description therefore gives
\[
E_{ij}\simeq\Sigma K_{a_i,a_j}\simeq
\bigvee^{(a_i-1)(a_j-1)}S^2.
\]
This includes singleton blocks: if either size is one, the graph is a tree and \(E_{ij}\) is contractible. Each inclusion of the connected simplex \(\Delta(A_i)\) or \(\Delta(A_j)\) into \(E_{ij}\) is nullhomotopic, and both simplices are disjoint within \(E_{ij}\).

**3. Global graph of spaces.** Order the edges of \(K_r\) so that the first \(r-1\) form a spanning tree and the remaining edges are chords. Start with the disjoint block simplices, then attach one edge space \(E_{ij}\) for each tree edge along its two boundary simplices. Tree attachments connect components without adding any circle, while retaining the independent wedge-of-two-spheres contribution from each \(E_{ij}\). For a chord, the two boundary simplices are already in one connected component, and the attaching maps are each nullhomotopic; its homotopy pushout adds exactly one free circle in addition to the wedge of two-spheres of \(E_{ij}\). There are \(\binom r2-(r-1)=\binom{r-1}{2}\) chords. The graph-of-spaces argument is valid because every gluing subcomplex is a CW cofibration and each vertex space is contractible. This proves the claimed homotopy decomposition, including vanishing of all reduced homology above degree two.

**4. Canonical integral modules.** Collapse each block simplex to a point, and each \(E_{ij}\) to an edge at the level of first homology; the natural map to the block graph identifies \(H_1(X;\mathbb Z)\) with the cycle lattice \(H_1(K_r;\mathbb Z)\). For each pair, the Mayer–Vietoris connecting map for \(E_{ij}=P_{ij}\cup Q_{ij}\) is the natural isomorphism from \(H_2(E_{ij};\mathbb Z)\) to \(H_1(K_{a_i,a_j};\mathbb Z)\). Oriented bipartite edges identify the latter with \(U(A_i)\otimes U(A_j)\). For chosen basepoints \(x_i\in A_i\) and \(x_j\in A_j\), the fundamental basis consists of boundaries \(\partial[x_i,x,x_j,y]\) for \(x\in A_i\setminus\{x_i\}\) and \(y\in A_j\setminus\{x_j\}\). The four triangular faces are all allowed, although the corresponding four-simplex is not. No three-block simplices can relate different pair contributions. Natural Mayer–Vietoris maps, or equivalently the cellular graph-of-spaces chain sequence, identify their direct sum with \(H_2(X;\mathbb Z)\) and prove integrality, primitivity and equivariance for independent blockwise permutations. Blockwise permutations act trivially on \(H_1(K_r;\mathbb Z)\).

## Verification

The standalone `check_tolerance.py` constructs every allowable simplex directly from the one-deletion definition and computes boundary ranks over the prime fields \(\mathbf F_2\), \(\mathbf F_3\) and \(\mathbf F_5\). Its ten nonidentical block-size samples give 30 matching Betti-vector comparisons, including cases with singleton blocks, three and four blocks, and nonuniform sizes. For example the three blocks of sizes \((2,2,2)\) give \((b_0,b_1,b_2)=(1,1,3)\), and four blocks of sizes \((2,2,2,2)\) give \((1,3,6)\). These finite field calculations are consistency checks, not an infinite proof or a torsion certificate; the all-size integral assertion follows from the homotopy-pushout proof above.

To replay, run `python3 check_tolerance.py` using Python 3 and no third-party packages. The program reports `PASS: 30 independent characteristic-field homology comparisons`.

## Relationship to prior work

Kim and Lew defined tolerance complexes and proved Leray bounds. Their 2021 paper, *Leray numbers of tolerance complexes*, explicitly uses **two** disjoint equal-sized simplex facets, at tolerance equal to one less than their size, to attain a boundary-sphere example. In the overlapping case of two size-two blocks, this is the already-known sphere \(S^2\), not a new special-case claim. Selvaraja's November 2026 paper *Tolerance complexes of chordal graphs and squarefree symbolic powers* proves that one-tolerance complexes of arbitrary chordal clique complexes satisfy the sharp three-collapsibility bound and related numerical invariant equalities. The disjoint clique unions here are chordal graphs, but those bounds do not determine their complete homotopy type, circle multiplicities, integral two-homology lattice, or natural symmetry action. The contribution here is the full arbitrary-block, all-rank mixed-dimensional homotopy classification and integral module identification, not the definition of tolerance or the known Leray/collapsibility bounds.

## Limitations

Only one-deletion tolerance is addressed. Higher tolerance thresholds, overlapping-clique graphs, and arbitrary chordal graphs are not classified. The decomposition is nonequivariant as a wedge decomposition; only the stated integral homology identifications are equivariant. Finite-field checks do not independently certify the integral homotopy result. Equivalent results in unindexed literature may exist, and independent mathematical validation has not been performed.

## References

- M. Kim and A. Lew, *Leray numbers of tolerance complexes*, arXiv:2109.03030 (first public 7 September 2021), https://arxiv.org/html/2109.03030v1.
- S. Selvaraja, *Tolerance complexes of chordal graphs and squarefree symbolic powers*, arXiv:2611.14384 (first public 10 November 2026), https://arxiv.org/html/2611.14384v1.
