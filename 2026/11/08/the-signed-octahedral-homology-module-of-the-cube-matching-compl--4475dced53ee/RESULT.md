# The signed-octahedral homology module of the cube matching complex

## Finding
Let \(Q_3\) be the graph on \(\mathbb F_2^3\), with two vertices adjacent when their Hamming distance is one, and let \(X=\mathcal M(Q_3)\) be its ordinary matching complex. The full graph automorphism group is \(G=\mathbb F_2^3\rtimes S_3\), of order \(48\), acting on cube vertices by \(g_{b,\sigma}(v)=b+\sigma(v)\). Write \(V\) for the natural three-dimensional rational *signed-coordinate* representation, in which \(g_{b,\sigma}\) sends the basis vector \(e_i\) to \((-1)^{b_{\sigma(i)}}e_{\sigma(i)}\). Let \(\delta(g_{b,\sigma})=(-1)^{b_0+b_1+b_2}\), trivial on coordinate permutations.

Then the complete reduced rational homology representation is
\[
\widetilde H_j(X;\mathbb Q)\cong
\begin{cases}
\bigwedge^2 V\oplus\mathbb Q_\delta,&j=2,\\
0,&j\ne2.
\end{cases}
\]
The underlying integral homotopy type is \(X\simeq\bigvee^4 S^2\). In particular the four-dimensional homology representation splits over \(\mathbb Q\) into a three-dimensional irreducible constituent and a one-dimensional constituent. Its complete character is, for every \(g\in G\),
\[
\chi(g)=\delta(g)+\frac{\operatorname{tr}(V(g))^2-\operatorname{tr}(V(g)^2)}2.
\]
The restrictions to the eight translation automorphisms \(g_{b,1}\), with \(b\) numbered \(0,\ldots,7\) in binary order, have traces \((4,-2,-2,0,-2,0,0,2)\). Neither summand contains a translation-invariant vector; hence the finite symmetry quotient satisfies \(H^*(|X|/G;\mathbb Q)\cong\mathbb Q\), concentrated in degree zero.

## Assumptions and scope
There are no parameters other than the fixed three-dimensional cube. The twelve edges of \(Q_3\), indexed \(0\) through \(11\), are, in order:
\[
(0,1),(0,2),(0,4),(1,3),(1,5),(2,3),(2,6),(3,7),(4,5),(4,6),(5,7),(6,7).
\]
A face of \(X\) is a nonempty subset of this edge list in which distinct graph edges have no common endpoint. A \(k\)-element face is a simplex of dimension \(k-1\). The automorphism group acts simplicially by sending each edge to its image under the indicated affine cube automorphism. Homology is reduced and rational except when integral homotopy or integral homology is explicitly mentioned. The representation is not claimed to split integrally.

## Proof
**1. Exact topology.** Exhausting all subsets of the twelve cube edges gives exactly \((12,42,44,9)\) nonempty faces by simplex dimension \(0,1,2,3\). On this face poset perform the following sequential-element partial matching. For each edge index in the order \((2,3,9,10,8,1,6,11,4,0,5,7)\), pair any still-unpaired face \(\tau\) not containing that index with the face obtained by adjoining the index, whenever that larger face remains unpaired. No empty face is included. This makes exactly \(51\) pairs. The five critical faces are
\[
\{2\},\quad\{0,5,8\},\quad\{0,7,8\},\quad\{6,7,8\},\quad\{1,4,11\}.
\]
The complete Hasse diagram has \(107\) faces and \(252\) cover relations. Directly orienting the matched covers upward and every other cover downward yields a directed acyclic graph: topological sorting visits all \(107\) faces. This is a finite exhaustive, reproducible acyclicity certificate; the exact checker is `verify.py`. Forman's discrete Morse theorem yields a CW complex with one zero-cell and four two-cells and no other cells; because there are no one-cells, all attaching maps of the two-cells are constant. Consequently \(X\simeq\bigvee^4S^2\), and the integral reduced homology is free of rank four in degree two only.

**2. Exact group action.** A cube automorphism is uniquely determined by the image of vertex \(0\) (eight choices) and a permutation of its three neighbors (six choices). All forty-eight maps \(v\mapsto b+\sigma(v)\) are graph automorphisms, so they exhaust the full group. Equip each matching simplex with the orientation given by increasing indices in the displayed edge list. If \(g\) sends a fixed simplex's ordered edge indices to a permutation of themselves, its contribution to the signed chain trace is the parity of that permutation. The reduced Lefschetz identity and the homology concentration of Step 1 give
\[
\operatorname{tr}\bigl(g\mid\widetilde H_2(X;\mathbb Q)\bigr)
=-1+\sum_{k=0}^3(-1)^k\operatorname{tr}\bigl(g\mid C_k(X;\mathbb Q)\bigr).
\]
The leading \(-1\) is the augmented empty face; omitting it would change the answer.

The standalone exact checker enumerates all forty-eight affine maps, every simplex, and the signed image action. It verifies all \(4560\) nontrivial signed boundary equivariance identities and evaluates the displayed Lefschetz sum for each group element. For the candidate \(\mathbb Q_\delta\oplus\bigwedge^2V\), the elementary exterior-power trace identity supplies the character on the right side of the claimed formula. All forty-eight computed chain Lefschetz numbers equal that formula exactly. Semisimplicity of finite-group representations over \(\mathbb Q\), together with equality of rational characters, proves the asserted \(G\)-module isomorphism.

**3. Irreducibility and quotient.** Restrict to the normal translation subgroup \(N=\mathbb F_2^3\). The constituent \(\mathbb Q_\delta\) has nontrivial weight \((1,1,1)\). The three basis vectors of \(\bigwedge^2 V\) have the three distinct weights \((1,1,0)\), \((1,0,1)\), \((0,1,1)\), cyclically permuted by \(S_3\). Any \(G\)-invariant subspace of \(\bigwedge^2 V\) is a sum of some of these distinct \(N\)-weight lines and must be stable under their transitive \(S_3\)-action; hence this constituent is irreducible over \(\mathbb Q\). None of the four weights is trivial on \(N\), so the full-group invariant reduced homology is zero. For a finite group acting simplicially, characteristic-zero averaging identifies the rational cohomology of the ordinary orbit space with the invariant rational cohomology of the original complex. The complex is connected, proving the displayed quotient statement.

## Verification
Run `python3 verify.py` in the directory containing the included verifier. It independently reconstructs all edges and faces, checks the complete acyclic matching and critical faces, verifies the full group action and chain-map signs, evaluates all forty-eight Lefschetz traces, checks the exterior-power character formula, and confirms that the translation-subgroup character has exactly four nonzero weights. The recorded `verification_output.txt` is the exact output from this run. The computation exhausts finite structures; no sampled or probabilistic inference is used. The only external theoretical ingredients are Forman's discrete Morse theorem, the Hopf trace identity, rational character theory of finite groups, and characteristic-zero transfer for finite orbit spaces.

## Relationship to prior work
The previously published result *The cube matching complex is a wedge of four two-spheres* gives the same underlying homotopy type, using an acyclic matching, but does not identify the automorphism action. We use an independently reconstructed finite matching and claim novelty only for the signed-coordinate and exterior-square representation, its complete character, and the quotient calculation. The published cube three-cut-complex representation also concerns \(Q_3\), but defines different faces and has nonzero homology in different dimensions; it cannot be substituted for the present matching-complex calculation. Braun and Hough's 2016 paper concerns two-row planar grid matching complexes and their comb generalization, not the \(2\times2\times2\) cube or its full homology character. Jonsson's book supplies the wider graph-matching-complex setting. Object equality, stronger implications and potential nomenclature substitutions were compared; the absence of a search hit alone is not a novelty proof.

## Limitations
The theorem addresses one cube graph and rational representation structure; it gives neither an integral decomposition of its homology lattice nor an equivariant homotopy classification. The nonequivariant wedge decomposition is previously known and is not claimed as original. The full text of Jonsson's 2007 book was not accessible in the sources examined; equivalently phrased, unindexed literature remains a genuine publication-priority risk. All code checks certify finite enumerations specified here and do not establish a general higher-dimensional hypercube theorem. No independent mathematical audit is asserted.

## References
1. J. Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928, Springer, softcover publicly dated 2007-11-15, eBook dated 2007-12-10, DOI: 10.1007/978-3-540-75859-4.
2. B. Braun and W. K. Hough, *Matching and Independence Complexes Related to Small Grids*, arXiv:1606.01204, first public 2016-06-03.
3. *The cube matching complex is a wedge of four two-spheres*, published research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-cube-matching-complex-is-bigvee-4-s-2--79d70fe8b67e.
4. *Automorphism module structure of the cube three-cut complex*, published research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-automorphism-module-structure-of-the-cube-three-cut-complex--7e5f41a11a8d.
