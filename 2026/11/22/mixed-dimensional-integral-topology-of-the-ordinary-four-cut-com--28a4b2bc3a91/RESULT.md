# Mixed-dimensional integral topology of the ordinary four-cut complex of the ternary three-cube

## Finding
Let \(G=H(3,3)=K_3\square K_3\square K_3\), the graph on the 27 ternary words of length three with an edge precisely when two words differ in one coordinate. Let \(\Delta_4(G)\) be the *ordinary four-cut complex*: its facets are the complements of four-element vertex sets whose induced graph is disconnected. Set \(D=\Delta_4(G)^\vee\), the combinatorial Alexander dual on the full 27-vertex set. Then
\[
\boxed{D\simeq\left(\bigvee^{1386}S^2\right)\vee\left(\bigvee^{109}S^3\right).}
\]
Consequently the complete reduced **integral** homology of the ordinary four-cut complex is
\[
\boxed{\widetilde H_i(\Delta_4(G);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{109},&i=21,\\
\mathbb Z^{1386},&i=22,\\
0,&\text{otherwise}.
\end{cases}}
\]
The four-cut complex is pure of dimension 22 and is not shellable. The displayed homotopy equivalence concerns the Alexander **dual**; only the integral homology, not the homotopy type, of the original cut complex is claimed.

## Assumptions and scope
The vertex order is lexicographic on \(\{0,1,2\}^3\), encoded by integers \(0,\ldots,26\). Graphs are simple and undirected, and connectedness always refers to the induced subgraph on the specified four vertices. For a subset \(A\subseteq V(G)\), the exact dual membership criterion is
\[
A\in D\iff\text{every four-element subset of }A\text{ induces a connected subgraph of }G.
\]
Thus **every** vertex, pair and triple belongs to \(D\), even triples that are disconnected in \(G\). Integral simplicial and cellular chain groups use the standard alternating orientation on increasing vertex lists. Wedges of spheres mean ordinary integral homotopy equivalence, not a finite-field Betti-number analogy.

## Proof
**1. Exhaustive classification of the dual.** For each of the \(\binom{27}{4}\) four-subsets, test connectivity by repeatedly adjoining all its graph-neighbors until no new vertices appear. Exactly 1,593 connected induced quadruples are found. All faces of cardinality at most three are present. For cardinality at least five, a candidate set is a face if and only if all its codimension-one deletions are faces. This recursion is equivalent to the all-quadruples criterion: a forbidden quadruple remains in some codimension-one deletion whenever the set has at least five elements. Generate the candidates by appending a larger vertex to every preceding-size face; this enumerates each possible increasing tuple. The resulting numbers of nonempty faces, by cardinalities one through seven, are exactly
\[
(27,351,2925,1593,324,54,0).
\]
No face of cardinality seven exists; hence no larger face exists, and the entire dual has 5,274 nonempty simplices. The executable `CHECK.py` performs these operations and checks every generated codimension-one face.

**2. A complete acyclic discrete-Morse matching.** Process graph vertices in order \(0,1,\ldots,26\). At vertex \(v\), pair each currently unmatched nonempty face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), provided the latter is also still unmatched. The numbers of pairs whose lower faces have cardinalities one through five are
\[
(26,325,1202,270,54).
\]
There are precisely 1,877 pairs, and the unmatched faces consist of one vertex, 1,398 triangles (2-cells) and 121 tetrahedra (3-cells). For complete rather than assumed acyclicity, orient every codimension-one Hasse edge from the upper face to the lower, except reverse the 1,877 matched edges. The checker constructs **all 17,793 cover relations** on **all 5,274 faces** and verifies by topological sorting that every face is removed; the directed graph is acyclic. Forman's matching theorem therefore gives a CW complex with one 0-cell, 1,398 cells in dimension two, 121 in dimension three, and no other cells. In particular it is simply connected.

**3. Exact integral Morse boundary.** Let \(C^M_3\cong\mathbb Z^{121}\) and \(C^M_2\cong\mathbb Z^{1398}\) be the Morse chains. For a matched lower two-face \(f\) paired with an upper three-face \(g\), substitute the signed boundary of \(g\) after solving for \(f\) using its incidence coefficient \(+1\) or \(-1\); repeat recursively along the gradient matching. Retain critical two-faces and set zero any two-face paired as an *upper* face with a one-face. For each critical three-cell, apply the standard alternating simplicial boundary and this signed recursive reduction. This gives the exact Morse matrix, rather than a mod-two substitute. It contains only 264 nonzero entries, all \(+1\) or \(-1\), in 24 active rows and 84 nonzero columns. The checker performs exact rational Gaussian elimination and obtains matrix rank 12.

**4. Primitive image and homotopy.** Crucially, rank alone would not exclude integral torsion. The code prints and verifies a fully specified 12-by-12 submatrix, using columns with critical-three-face indices \((0,1,2,3,4,5,19,20,21,22,23,24)\), where the ordering is lexicographic, and rows indexed by the twelve actual critical triangles
\[
\begin{gathered}
(1,2,13),(1,2,16),(1,2,22),(1,2,25),\\
(1,12,13),(1,15,16),(1,21,22),(1,24,25),\\
(2,12,14),(2,15,17),(2,21,23),(2,24,26).
\end{gathered}
\]
Its determinant is exactly \(-1\), computed by integer Bareiss elimination. The Smith normal form therefore has twelve unit diagonal entries and all other entries zero: the gcd of its maximal minors is one, and a rank-12 minor is unimodular. Consequently
\[
H_2(D;\mathbb Z)=\mathbb Z^{1398-12}=\mathbb Z^{1386},\quad
H_3(D;\mathbb Z)=\mathbb Z^{121-12}=\mathbb Z^{109},
\]
with no torsion and no other reduced homology. Because the Morse CW complex has one vertex and no one-cells, its two-skeleton is a wedge of 1,398 two-spheres. The attaching maps of the three-cells are determined up to homotopy by their integral degree vectors, since \(\pi_2\) of that two-skeleton is the free group \(\mathbb Z^{1398}\) as an abelian group by Hurewicz. Unimodular changes of cellular bases and elementary three-cell slides put the primitive boundary matrix into a diagonal block of twelve identities and zeros. Each identity block is a cancellable two/three-cell pair and each zero three-cell attaches nullhomotopically. This proves the asserted wedge of 1,386 two-spheres and 109 three-spheres; it is more than an additive homology statement.

**5. Integral duality and shellability.** Combinatorial Alexander duality on the fixed 27-vertex set gives
\[
\widetilde H_i(\Delta_4(G);\mathbb Z)\cong
\widetilde H^{24-i}(D;\mathbb Z).
\]
Since the dual integral homology is free, its reduced cohomology has ranks 1,386 in degree two and 109 in degree three. Therefore the original has ranks 1,386 in degree 22 and 109 in degree 21, with no torsion or other groups. Every facet is the complement of a disconnected quadruple and hence has 23 vertices, so the complex is pure of dimension 22. Its nonzero reduced homology in degree 21 contradicts the top-dimensional homology concentration required for a pure shellable complex. Thus it is not shellable.

## Verification
Run `python3 CHECK.py` in a standard Python 3 environment; no additional packages are required. It independently generates all dual faces, checks the connectivity criterion and absence of larger faces, verifies the entire oriented Hasse digraph acyclic, reconstructs the signed integral Morse boundary, performs exact rational rank elimination and evaluates a determinant-one full-rank minor over the integers. As an additional non-integral cross-check, a separate raw simplicial boundary calculation obtains mod-two boundary ranks \((26,325,1214,270,54)\) in degrees one through five. Its direct mod-two homology agrees with the Morse prediction. The script reports `ALL CHECKS PASSED`, with the numerical intermediate certificates in `CHECK_OUTPUT.txt`.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduce ordinary cut complexes and determine cut topology for several graph families, including complete multipartite graphs and clique prisms; they do not state the ordinary four-cut homology of \(K_3\square K_3\square K_3\). Their sequel treats path grids and disjoint unions, not this product of three complete graphs. The published all-alphabet Hamming-product classification and the specific ternary three-cube result concern the **ordinary three-cut** complex, with different forbidden subsets and different homology. Previously indexed ordinary four-cut classifications cover the binary four-cube \(Q_4\) and the two-coordinate 4-by-4 rook graph, neither of which is this ternary three-coordinate graph. An independence complex, a Rips complex or a *total* cut complex of the same graph has a different face predicate and does not imply this claim. Precise overlap comparisons are documented in `AUDIT.json`.

## Limitations
The homotopy theorem applies to this one 27-vertex Alexander dual, not to all ternary cube dimensions or alphabet sizes. It does not establish the integral homotopy type of the original cut complex, a homology representation under its automorphism group, cup products, persistence maps between cut thresholds or any infinite-family formula. The finite proof is exhaustive on this specified object; its correctness relies on the complete checker and elementary discrete-Morse and CW-topology arguments. The reviewed literature and database searches cannot rule out an unindexed equivalent theorem; independent external verification has not been performed.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first public version 2023-04-26, especially the definition and Sections 4–7. https://arxiv.org/abs/2304.13675
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first public version 2024-07-11, especially the grid sections. https://arxiv.org/abs/2407.08158
3. *Mixed-alphabet Hamming graphs: complete integral three-cut homology*, indexed mathematical research result, 2026-10-25, identifier `397f4b160890`; compares the adjacent but distinct cut threshold. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-mixed-alphabet-hamming-graphs-complete-integral-three-cut-homolo--397f4b160890
4. *Integral four-cut homology separates the Shrikhande and rook graphs*, indexed mathematical research result, 2026-11-02, identifier `de2f98e55b1f`; differs in its graph and ground-set size. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-integral-four-cut-homology-separates-the-shrikhande-and-rook-gra--de2f98e55b1f
5. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), pp. 90–145; the acyclic-matching theorem.
