# Contractibility of the full symmetry quotient of the Heawood independence complex

## Finding
Let \(H\) be the Heawood graph, realized as the incidence graph of the Fano projective plane, and let \(K=\operatorname{Ind}(H)\) be its simplicial independence complex. Let \(G=\operatorname{Aut}(H)\), including all point–line dualities, act by permuting the vertices of \(K\). Then the **ordinary geometric orbit space** is contractible:
\[
\boxed{|K|/G\simeq * .}
\]
Equivalently, its fundamental group is trivial and its positive-degree reduced integral homology vanishes. This is a statement about the geometric quotient, not the complex on orbit vertices and not a fixed-point space.

## Assumptions and scope
Take the seven Fano points to be the nonzero vectors of \(\mathbb F_2^3\), and the seven Fano lines to be its two-dimensional linear subspaces. A point and a line are adjacent in \(H\) exactly when incident. A face of \(K\) is a subset of the fourteen graph vertices containing no adjacent pair. The full graph automorphism group \(G\) has 336 elements: 168 collineations and their composites with point–line polarity. The claimed homotopy equivalence concerns only this graph, this complex and this full group.

## Proof
**Automorphisms and cells.** The invertible binary linear maps are determined by the images of three basis vectors, giving \(7\cdot6\cdot4=168\) collineations. A polarity exchanges points and lines. Since the incidence graph is connected and bipartite, each graph automorphism either preserves or interchanges the two parts. Every part-preserving automorphism is a Fano collineation; hence these maps and their polarity composites exhaust all 336 automorphisms.

The independent-set counts, by cardinality from zero through seven, are
\[
(1,14,70,154,147,56,14,2).
\]
Thus \(K\) has 457 nonempty faces. Pass to the barycentric subdivision whose vertices are nonempty independent sets and whose simplices are strict inclusion chains \(A_0\subsetneq\cdots\subsetneq A_k\). An automorphism preserves the cardinality of every \(A_i\), so no automorphism can nontrivially permute the vertices of any simplex that it stabilizes. Therefore the orbit of each simplex gives a genuine oriented cell of the quotient, with no orientation-reversing stabilizer. Faces of different cells may be identified, so the quotient need not be an ordinary abstract simplicial complex.

Exhaustive enumeration yields the following numbers of quotient cells in dimensions zero through six:
\[
(c_0,c_1,c_2,c_3,c_4,c_5,c_6)=(14,64,149,218,210,120,30).
\]
On an oriented orbit-chain cell the integral cellular boundary is
\[
\partial[A_0\subsetneq\cdots\subsetneq A_k]
=\sum_{i=0}^{k}(-1)^i[A_0\subsetneq\cdots\subsetneq\widehat{A_i}\subsetneq\cdots\subsetneq A_k],
\]
where the right-hand chains are reduced to their actual group orbits. The complete integer boundary matrices, reconstructed by `verify.py`, have ranks
\[
(r_1,r_2,r_3,r_4,r_5,r_6)=(13,51,98,120,90,30).
\]
For **every** boundary matrix, all nonzero Smith invariant factors are equal to one; the verifier performs exact integer Smith reduction, not finite-field inference. Consequently the zero-th homology is \(\mathbb Z\), while all positive-degree integral homology groups vanish, without torsion.

**Fundamental group.** The quotient one-skeleton is connected with fourteen vertices and 64 edges. Contract a spanning tree of thirteen edges. The remaining 51 oriented edges give generators. Each of the 149 two-cell orbits supplies the triangular attaching relation \(e_{ab}e_{bc}e_{ac}^{-1}=1\), with tree-edge symbols set equal to one. These are genuine polygonal attaching relations, even when two distinct sides map to the same orbit edge. The exact verifier freely reduces these 149 words, repeatedly identifies a length-one relator and deletes its generator from all words. The process deletes **all 51 generators**, after which every relator is empty. Each deletion is a valid Tietze move, so \(\pi_1(|K|/G)=1\).

**Conclusion.** The quotient is a connected finite CW complex, simply connected and acyclic over \(\mathbb Z\). If any higher homotopy group were nonzero, the least such degree would give nonzero integral homology by the Hurewicz theorem. Hence all its homotopy groups vanish, and Whitehead's theorem gives \(|K|/G\simeq *\).

## Verification
Run `python3 verify.py` with Python 3 and SymPy installed. The script constructs the Fano incidence graph, verifies all 336 distinct automorphisms on its 21 edges, checks all 457 nonempty independent sets, enumerates every barycentric chain orbit, constructs every integral boundary matrix, confirms all six Smith forms, and carries out the 51-generator one-relator elimination. It also verifies \(\partial^2=0\). A successful run prints `HEAWOOD_FULL_AUTOMORPHISM_ORBIT_CONTRACTIBLE_OK`, the orbit-cell counts, boundary ranks and fundamental-group certificate. No stored census, numerical approximation or proprietary input is used.

## Relationship to prior work
The Heawood independence complex itself has been calculated to have homotopy type \(\bigvee^6 S^3\), so its **ambient** topology is not new here. The previously determined irreducible rational homology character under the 168 Fano collineations has no invariant vector; over rational coefficients this already implies that the full quotient has no positive-degree rational homology. It does **not** determine integral torsion or the fundamental group, and therefore does not imply contractibility. A separate complete classification of the fixed-point spaces for nonidentity subgroups of the full 336-element group does not compute the ordinary geometric orbit space. Barmak's star-cluster results and Tsukuda's incidence/Alexander-dual equivalences are nonequivariant structural tools, not integral classifications of this 336-element quotient. The new contribution is the full homotopy determination, including elimination of both possible integral torsion and nonabelian fundamental-group obstructions.

## Limitations
The result does not classify quotients by all proper subgroups, higher-order projective-plane incidence graphs, or equivariant homotopy models. The finite enumeration is exhaustive for the specified Fano graph and group, but supplies no family theorem. Searches and full-text comparisons cannot rule out every differently phrased or unindexed equivalent computation. Independent mathematical auditing is not asserted.

## References
- J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, posted 2010-07-02, https://arxiv.org/html/1007.0418v1.
- S. Tsukuda, *Independence complexes and incidence graphs*, *Contributions to Discrete Mathematics* 12 (2017), 28–46, https://doi.org/10.55016/ojs/cdm.v12i1.62277.
- *The Heawood independence complex is a wedge of six three-spheres*, publicly available result, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-heawood-independence-complex-is-bigvee-6-s-3--dbd95019d1e2.
- *The exceptional rational homology representation of the Heawood independence complex*, publicly available result, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-exceptional-rational-homology-representation-of-the-heawood--213fded46807.
- *All nonidentity subgroup-fixed homotopy types of the Heawood independence complex*, publicly available result, 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-all-nonidentity-subgroup-fixed-homotopy-types-of-the-heawood-ind--3552c24fcce8.
