# Three-sphere wedges and an integral exterior-power lattice on three nonzero Hamming layers

## Finding

For each integer \(n\ge4\), let \(\mathcal B_n^{[1,3]}=\{S\subseteq[n]:1\le |S|\le3\}\), with symmetric-difference distance \(d(S,T)=|S\triangle T|\). Let \(X_n\) be its **inclusive distance-two** Vietoris–Rips complex, containing a simplex precisely when every distinct pair of its vertices has distance at most two. Then

\[
 |X_n|\simeq \bigvee^{\binom n4}S^3,\qquad
 \widetilde H_3(X_n;\mathbb Z)\cong\bigwedge^4\mathbb Z^n
\]

as an integral module under the coordinate-permutation action of \(S_n\). Every other reduced integral homology group vanishes. For \(1\le n\le3\) the space is contractible.

For each four-subset \(U\subseteq[n]\), the eight vertices \(\{\{i\}:i\in U\}\cup\{U\setminus\{i\}:i\in U\}\) span a full subcomplex isomorphic to the boundary of a four-dimensional cross-polytope. Its fundamental class is an element \(z_U\) of the third integral homology. Orienting the four opposite-pair factors in increasing coordinate order makes \(z_U\) an integral basis indexed by the four-subsets; it obeys \(\sigma_*z_U=\operatorname{sgn}(\sigma|_{U\to\sigma U})z_{\sigma U}\), with the sign of the induced ordered bijection. This is the standard exterior-fourth-power lattice.

## Assumptions and scope

The underlying metric space is an induced **three-rank subspace**, not the full Boolean cube and not the rank-at-most-three sublevel: **the empty support is absent**. Every \(n\) is a positive integer, edges at distance exactly two are included, and \(\mathbb Z^n\) is the natural integral permutation lattice on the labels. Only coordinate permutations act; arbitrary bit flips do not preserve the three-rank subspace. The asserted wedge decomposition is ordinary (nonequivariant) homotopy, while the module is an actual integral homology representation. No infinite certification is inferred from finite experiments.

## Proof

**1. Three rank-specific adjacency rules.** For two singleton vertices adjacency is automatic. A singleton \(\{i\}\) is adjacent to a rank-two or rank-three vertex \(S\) exactly when \(i\in S\), because otherwise the symmetric-difference distance is respectively three or four. A rank-two vertex \(P\) is adjacent to a rank-three vertex \(T\) exactly when \(P\subset T\). Two rank-two vertices are adjacent exactly when they intersect; two distinct rank-three vertices are adjacent exactly when they share two elements. These exhaustive tests follow directly from the distance formula.

**2. First matching, eliminating nonempty intersections.** For a face \(F\), let \(\tau(F)\) be its set of rank-two and rank-three vertices, and put \(I(\tau)=\bigcap_{S\in\tau}S\), with \(I(\varnothing)=[n]\). Once \(\tau\) is fixed, a face is \(\tau\) together with any subset of singleton vertices indexed by \(I(\tau)\), by the adjacency rules. If \(I(\tau)\ne\varnothing\), choose \(i=\min I(\tau)\) and match each face lacking the singleton \(\{i\}\) to its union with that singleton. This pairs the complete Boolean fiber over \(\tau\). It is acyclic: matched upward edges preserve \(\tau\), unmatched downward edges either preserve \(\tau\) and remove a singleton other than the chosen one, or strictly decrease the number of rank-two/three vertices. Within one fiber an upward edge adds the chosen singleton, which cannot subsequently be removed along a downward unmatched edge; no directed cycle can exist. All faces surviving this stage have no singleton vertices and satisfy \(I(\tau)=\varnothing\).

**3. Classifying surviving cliques.** A pairwise-intersecting family of rank-two subsets with empty total intersection is exactly the three edges of some three-subset \(T\): three pairwise-intersecting edges either share one vertex or form a triangle, and further edges compatible with a triangle must be one of its three edges. A family of rank-three subsets with pairwise two-element overlaps is either a Johnson star (a common pair) or lies among the four triples of one four-subset. The latter family has empty total intersection only when all four triples occur. For mixed families, every rank-two vertex lies inside every rank-three vertex; if their total intersection is empty, the rank-two vertices must be the three edges of a three-subset \(T\) and the only possible rank-three vertex is \(T\) itself.

Thus the surviving faces are precisely

\[
 A_T=\{P\subset T:|P|=2\},\quad
 B_T=A_T\cup\{T\}\quad (|T|=3),
 \qquad C_U=\{U\setminus\{i\}:i\in U\}\quad(|U|=4).
\]

**4. Second matching and global acyclicity.** Match \(A_T\) upward to \(B_T\), for every three-subset \(T\). Every remaining unmatched nonempty face is exactly one \(C_U\). This remains a globally acyclic matching: along all directed Hasse edges the number of rank-two vertices never increases (matched upward edges add a singleton or one rank-three vertex). Immediately after any second-stage matched arrow \(A_T\to B_T\), a downward edge cannot remove \(T\), since that reverses the matched edge; it must remove a rank-two vertex, strictly decreasing the rank-two count. Such an arrow can therefore occur in no directed cycle. A cycle using only first-stage matching arrows is already excluded by the fiber argument. On the augmented face poset the empty face is matched with the singleton \(\{\min[n]\}\); unmatch this pair and omit the empty face, leaving one critical 0-cell and exactly \(\binom n4\) critical 3-cells. Forman's discrete-Morse theorem now gives a CW complex with only these cells, and all 3-cell attachments are to a point, so it is the stated wedge of three-spheres. For \(n\le3\), no \(C_U\) exist and the resulting complex is contractible.

**5. Primitive integral generators and full symmetry.** Fix \(U\) of size four. The induced subgraph on the four singleton vertices and four complementary rank-three vertices is complete except for the four disjoint opposite pairs \(\{i\}\) and \(U\setminus\{i\}\). Hence the full subcomplex is \((S^0)^{*4}=S^3\), yielding a simplicial fundamental cycle \(z_U\) with coefficient \(\pm1\) on each facet. The tetrahedron \(C_U\) consisting of all four triple vertices is maximal in the ambient \(X_n\): no singleton belongs to all four triples, no two-subset is contained in all four, and no distinct three-subset meets all four triples in at least two positions. Its indicator is therefore a simplicial integral 3-cocycle \(\phi_U\). The pairing is \(\langle\phi_U,z_V\rangle=\pm\delta_{UV}\), with an orientation choice making it exactly \(\delta_{UV}\). These \(\binom n4\) cycles form a **primitive integral basis**, since the Morse theorem proved that the total degree-three group is free of precisely this rank. A coordinate permutation maps the opposite-pair factors of the cross-polytope sphere by permuting their four coordinates, without interchanging the members of a pair; exchanging two \(S^0\) join factors reverses the three-sphere's orientation. Thus the basis transforms by the signed permutation action on oriented four-subsets, which is precisely \(\bigwedge^4\mathbb Z^n\). This is an integral, not merely rational, identification.

## Verification

Run `python3 verify_rank_interval.py` to enumerate the complete Rips face poset, check every proposed matching pair, topologically sort the full directed Hasse graph, count the critical cells, and check the octahedral antipodal pairs and maximal cocycle facets for \(4\le n\le8\). Run the independent `python3 verify_rank_interval_mod2.py` to enumerate maximal cliques by Bron–Kerbosch and compute complete reduced boundary ranks over \(\mathbb F_2\) for \(4\le n\le7\). Both programs use the Python standard library only. Their recorded outputs are included as text. The exact all-\(n\) proof is the structural argument above; these finite checks are corroboration, not extrapolation.

## Relationship to prior work

Bendersky, Elia and Grbić (arXiv:2605.00705, first public May 1, 2026), especially Sections 1, 5 and 6, develop a global hypercube Vietoris–Rips cohomology theory, including cross-polytope representatives, but do not classify this three-nonzero-rank subspace or its integral coordinate-permutation lattice. Adamaszek and Adams (arXiv:2103.01040), especially Lemma 7 and Theorem 8, prove sphere-wedge theorems for full cubes and initial binary-order subgraphs, rather than this Hamming-weight **rank interval**.

The closest indexed cumulative-level result, *Coordinate-permutation homology of the weight-three function–Rips sublevel on Boolean cubes* (published record `2026/10/11/SCOPE-coordinate-permutation-homology-of-the-weight-three-function-rip--a0730d2d2cdd`), was read in full: it treats **weights zero through three**, and proves the rational \(S_n\)-module \(\bigwedge^3\mathbb Q^n\oplus\bigwedge^4\mathbb Q^n\). It does not state the topology after **deleting the zero vector**, nor a primitive integral homology basis for this rank interval. The asserted rank \(\binom n4\) is consistent with, but not determined by, that representation statement alone: a deleted-vertex attachment and its integral maps must be analyzed. The present explicit two-stage Morse theorem and cross-polytope cocycle pairing do that. Another published record studies **two adjacent** Hamming-weight layers, not the three ranks here. An implicit derivation from existing general techniques remains an originality risk, and no universal novelty certification is claimed.

## Limitations

This is one inclusive metric threshold for the ranks exactly one to three. It does not determine higher-rank intervals, all function–Rips persistence maps, the complete hyperoctahedral action, or an equivariant homotopy equivalence. The proof is an exact nonequivariant Morse collapse plus an integral action on homology. The novelty comparison is limited to the publicly inspected literature and indexed results.

## References

1. M. Bendersky, S. Elia, J. Grbić, *Cohomological properties of the Vietoris–Rips Complex of a Hypercube Graph*, arXiv:2605.00705, v1 May 1, 2026, v2 July 17, 2026, Sections 1, 5, 6. https://arxiv.org/html/2605.00705v2
2. M. Adamaszek, H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040, March 1, 2021, Lemma 7 and Theorem 8. https://arxiv.org/html/2103.01040v3
3. *Coordinate-permutation homology of the weight-three function–Rips sublevel on Boolean cubes*, public record `2026/10/11/SCOPE-coordinate-permutation-homology-of-the-weight-three-function-rip--a0730d2d2cdd`, RESULT.md (full text inspected), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-coordinate-permutation-homology-of-the-weight-three-function-rip--a0730d2d2cdd
4. *Symmetric-group homology of two adjacent Hamming-weight Rips layers*, public record `2026/10/25/SCOPE-symmetric-group-homology-of-two-adjacent-hamming-weight-rips-lay--148e2ea930e9` (indexed summary), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-symmetric-group-homology-of-two-adjacent-hamming-weight-rips-lay--148e2ea930e9
