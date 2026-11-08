# Three-degree integral homology and cyclic symmetry of a seven-vertex tournament multipath complex

## Finding

Let \(T\) be the directed tournament on \(\mathbb Z/7\mathbb Z\) with an arrow \(u\to v\) precisely when \(v-u\pmod 7\in\{1,2,3\}\). Let \(X(T)\) be its **multipath complex**: the vertices of the simplicial complex are the 21 directed edges of \(T\), and a set of edges is a face if every component of that directed edge set is a directed simple path or an isolated graph vertex. Directed cycles, branching, and merging are excluded.

Then the **complete reduced integral homology** is

\[
\widetilde H_i(X(T);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{13},&i=3,\\
\mathbb Z^{43},&i=4,\\
\mathbb Z^{17},&i=5,\\
0,&\text{otherwise}.
\end{cases}
\]

For the natural rotation group \(C_7\), acting by translating the tournament vertices, the rational fixed-subspace dimensions in degrees \(3,4,5\) are respectively \(1,7,5\). Every nonidentity rotation has rational homology traces \((-1,1,3)\) in those degrees. Equivalently, as rational \(C_7\)-representations, with \(W=\mathbb Q(\zeta_7)\) the six-dimensional cyclotomic irreducible,

\[
\widetilde H_3(X(T);\mathbb Q)\cong\mathbb Q\oplus W^{\oplus2},\quad
\widetilde H_4(X(T);\mathbb Q)\cong\mathbb Q^{\oplus7}\oplus W^{\oplus6},\quad
\widetilde H_5(X(T);\mathbb Q)\cong\mathbb Q^{\oplus5}\oplus W^{\oplus2}.
\]

The homology is torsion-free. **No wedge-of-spheres homotopy decomposition, full tournament automorphism representation, or general formula for larger cyclic tournaments is claimed.**

## Assumptions and scope

The tournament is the regular **consecutive-difference** tournament, not the distinct quadratic-residue (Paley) tournament on seven vertices. The simplicial complex is built on **arcs**, not on tournament vertices. Its face size is at most six, because a directed path forest on seven vertices has at most six arcs. Homology is reduced, over \(\mathbb Z\) unless a field is specified, and dimensions are simplicial dimensions (face size minus one). All group actions act on the oriented simplicial chain groups with the induced permutation signs.

## Proof

**Finite face classification.** Enumerate all arc subsets of cardinality at most six. The path-forest criterion is equivalent to indegree and outdegree at most one at each graph vertex, with no directed cycle. Independent exhaustive-subset and extension-backtracking enumerators agree on the face-cardinality vector

\[
(f_{-1},f_0,f_1,f_2,f_3,f_4,f_5)=(1,21,168,630,1113,819,175).
\]

There are 2,927 faces including the empty face and exactly 11,844 codimension-one incidences.

**Integral chain reduction.** On the augmented face poset, process the 21 arcs in lexicographic order. At each arc, match every as-yet-unmatched face not containing that arc to its remaining face obtained by adjoining the arc. This produces 1,416 distinct pairs. Orient every unmatched Hasse incidence downward and every matched incidence upward. A full topological-sort test on all 2,927 faces and 11,844 incidences shows that this directed graph has no directed cycle. The only critical faces have dimensions \(3,4,5\), with counts \(24,54,17\).

For each matched lower face \(\tau\) and its upper mate \(\sigma\), use the unit oriented boundary coefficient \([\sigma:\tau]\in\{+1,-1\}\) to eliminate \(\tau\). Recursively substituting across all acyclic gradient paths yields an *integral* Morse chain complex. Its only potentially nonzero differential is an integer matrix \(\partial_4^{\mathrm M}\) of size \(24\times54\); \(\partial_5^{\mathrm M}\) is identically zero. Exact Smith-normal-form calculation gives rank eleven and every nonzero invariant factor equal to one. Independently, the submatrix with zero-based row indices

`1,2,3,4,5,10,11,12,13,14,20`

and zero-based column indices

`5,9,14,15,17,23,25,27,32,46,47`

has determinant \(+1\); exact rank calculation verifies that eleven is the full rank. The reduced homology ranks are therefore \(24-11=13\), \(54-11=43\), and \(17\) in dimensions \(3,4,5\), and no torsion occurs. The empty-face matching implements reduced chains correctly.

**Independent chain corroboration.** Reversing the arc-processing order yields another acyclic matching, with 1,408 matched pairs and critical dimensions \(2,3,4,5\) of sizes \(1,32,61,17\). Its exact integral Morse differentials have respective ranks \(0,1,18,0\) and only unit nonzero Smith factors, giving the same integral homology. On the unreduced simplicial chain complex, an independent mod-two calculation yields differential ranks \(20,148,482,618,158\) in degrees \(1\) through \(5\).

**Rotation character.** Translation by one modulo seven preserves the arc set. Because any nonempty face has at most six arcs, no nontrivial rotation can fix its underlying face: each arc orbit has size seven. Consequently the degreewise rational invariant chain groups have dimensions \(3,24,90,159,117,25\) (simplicial dimensions zero through five). Form the invariant boundary using one oriented face per seven-element orbit and the exact signs of rotation. Its rational boundary ranks in degrees one through five are \(2,22,68,90,20\). Since taking \(C_7\)-invariants is exact over \(\mathbb Q\), the invariant homology dimensions are \(1,7,5\) in degrees three through five. The only irreducible rational representations of \(C_7\) are the trivial one and \(W=\mathbb Q(\zeta_7)\), of dimensions one and six. Comparing total ranks and invariant dimensions forces the displayed decomposition and traces.

## Verification

Run `python verify.py` in an environment with Python 3.10 or later and SymPy. The script uses no data files or external services. It checks independent face enumerations, the full Hasse-graph acyclicity of both matchings, exact integral Morse differentials and Smith factors, the specified unimodular minor, the unreduced mod-two ranks, and the full signed rotation-orbit chain differential. Its expected deterministic output is provided in `verification_output.json`.

## Relationship to prior work

Caputi, Collari and Di Trani introduced the path-poset simplicial viewpoint, including its relationship to homology. Caputi, Collari, Di Trani and Smith classify multipath complexes of transitive tournaments; their corresponding theorem does not cover a regular tournament with directed cycles. The quiver-minor and blow-up comparisons of Caputi, Collari and Ramos require acyclicity for the specific matching-complex equivalence and do not determine this example. Work on bidirected polygons treats a different class of digraphs. Directed flag complexes and tournaplexes are also different constructions: their simplices are based on tournament vertex sets rather than arc subsets forming path forests.

## Limitations

This is an exact computation for one natural tournament, not an assertion of novelty proof by unsuccessful search. No full homotopy type is determined: torsion-free integral homology does **not** on its own imply a wedge of spheres, and possible higher attaching maps are not eliminated. No persistence statement, integral equivariant splitting, or general odd-order theorem is asserted. An equivalent calculation in unindexed literature is a residual bibliographic possibility. The review recorded here is not an independent external audit.

## References

1. L. Caputi, C. Collari and S. Di Trani, *Combinatorial and Topological Aspects of Path Posets, and Multipath Cohomology*, arXiv:2110.11206 (initial public version 2021-10-21), Journal of Algebraic Combinatorics 57 (2023), 617–658. https://arxiv.org/abs/2110.11206 ; https://doi.org/10.1007/s10801-022-01180-9
2. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the Homotopy Type of Multipath Complexes*, arXiv:2208.04656 (initial public version 2022-08-09), Mathematika 70 (2024), e12235. https://arxiv.org/abs/2208.04656 ; https://doi.org/10.1112/mtk.12235
3. L. Caputi, C. Collari and E. Ramos, *The Weak Categorical Quiver Minor Theorem and Its Applications: Matchings, Multipaths, and Magnitude Cohomology*, arXiv:2401.01248 (2024). https://arxiv.org/abs/2401.01248
4. L. Caputi, C. Collari and J. P. Smith, *Multipath Complexes of Bidirectional Polygonal Digraphs*, arXiv:2601.05670 (2026). https://arxiv.org/abs/2601.05670
5. D. Govc, R. Levi and J. P. Smith, *Complexes of Tournaments, Directionality Filtrations and Persistent Homology*, Journal of Applied and Computational Topology 5 (2021), 313–337. https://doi.org/10.1007/s41468-021-00068-0
