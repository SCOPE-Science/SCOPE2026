# A sharp five-vertex threshold for torsion in bidirected multipath complexes

## Finding
For every finite simple undirected graph \(G\) on at most five vertices, form the fully bidirected digraph \(D=\overleftrightarrow G\) by replacing each edge by both directed arcs. Let \(X(D)\) be the simplicial complex of arc sets which form pairwise vertex-disjoint directed simple paths, with no directed cycle. **The reduced integral homology of \(X(D)\) has torsion if and only if \(G\cong K_{1,1,3}\)**, the three-page triangular book (three triangles sharing a common edge).

For the unique exceptional graph,
\[
\widetilde H_k(X(\overleftrightarrow{K_{1,1,3}});\mathbb Z)\cong
\begin{cases}
\mathbb Z/2,&k=1,\\
\mathbb Z^7,&k=2,\\
0,&\text{otherwise}.
\end{cases}
\]
The threshold is sharp: every graph on at most four vertices has torsion-free multipath homology, whereas precisely one isomorphism class on five vertices has torsion. Exactly ten of the \(2^{10}=1024\) labelled simple five-vertex graphs are in that class.

## Assumptions and scope
Graphs are finite, undirected, simple and loopless; no orientation choices are made because every underlying edge receives **both** directions. A multipath is any arc set in which every vertex has at most one incoming and at most one outgoing selected arc, and all directed cycles (including length two) are forbidden. The empty arc set is included as the augmented empty simplex for reduced chains. The graph order refers to original vertices, not to the number of vertices (arcs) of its multipath complex. No theorem is asserted for arbitrary orientations or for six or more underlying vertices.

Label the exceptional graph by \(\{0,1,2,3,4\}\) and its edges by
\[
\{01,02,03,04,12,13,14\}.
\]
Thus vertices zero and one are the common edge of all three triangles. Its bidirected digraph has fourteen arcs. The complex has face-vector (including the augmented empty simplex)
\[
(f_{-1},f_0,f_1,f_2,f_3)=(1,14,54,60,12).
\]

## Proof
**Complete isomorphism coverage.** For each number of vertices \(n=1,2,3,4,5\), enumerate every bitmask on the \(\binom n2\) possible undirected edges. For each bitmask, apply all \(n!\) vertex permutations and compute its entire relabeling orbit. Select exactly one representative of each orbit. The class counts are respectively \(1,2,4,11,34\). The sum of the orbit sizes at each order equals \(2^{\binom n2}\), certifying complete coverage of all labelled graphs. In particular, on five vertices there are 34 and not merely an arbitrarily chosen sample of types.

**Exact complexes and acyclic matchings.** For each class representative, enumerate arc subsets recursively, rejecting a new arc when it would give more than one outgoing or incoming selected arc or close a directed cycle. This enumerates all and only multipaths. The checker then constructs the following face-poset matching: visit the arcs in fixed order and pair each remaining face not containing the arc with the face obtained by adjoining it, whenever both are still unmatched. It explicitly directs every face-poset covering relation downward except matched relations, which are directed upward, and topologically sorts the *entire* finite directed Hasse graph to verify acyclicity. Thus the resulting algebraic Morse chain complex has the same reduced integral homology as the original simplicial complex.

**Integer homology in every class.** Signed boundaries of critical cells are computed by exact recursive Morse reduction; the sign for deleting arc of index \(j\) is determined by its position in the increasing ordered arc set. For each integral boundary matrix, exact elementary unimodular row and column operations eliminate all entries \(\pm1\) as invariant factors equal to one. Among **every boundary of all 52 isomorphism classes**, the reduced matrix is zero except for the degree-two boundary of the single five-vertex exceptional class. The latter reduces to a single row with nonzero entries \((2,2,2)\), so its sole remaining invariant factor is the gcd, \(2\); the complete Smith factors are \((1,2)\). There are no higher or other nonunit invariant factors. Since elementary integer row and column operations preserve the cokernel up to free summands, this proves torsion-freeness in all other cases and exact order-two torsion for the exceptional case.

**Free ranks.** For the witness, the ascending-order matching has 65 pairs and critical chain ranks \((2,9)\) in degrees one and two, with no other critical cells; the degree-two differential has rank two and Smith factors \((1,2)\). Hence \(\widetilde H_1\cong\mathbb Z/2\) and \(\widetilde H_2\cong\mathbb Z^7\). The decreasing-order matching independently has 66 pairs and critical chain ranks \((1,8)\) in these degrees, with degree-two boundary entries \((2,-2)\). Its homology agrees exactly. Both matchings were separately checked acyclic across all 350 Hasse incidences.

## Verification
Run `python3 verify_minimal_bidirected.py` with Python 3.8 or newer and only the standard library. It enumerates all 52 unlabelled graphs on one through five vertices, all 1,099 corresponding labelled graphs by orbit-size totals, and checks all their multipath complexes. For the witness it independently tests all \(2^{14}\) arc subsets using a direct in/out-degree and directed-cycle predicate, verifying equality to the recursive face list. It also forms the **unreduced** signed simplicial boundary operators, verifies \(\partial^2=0\), and obtains raw boundary ranks \((13,40,12)\) over \(\mathbb F_2\) and \((13,41,12)\) over \(\mathbb F_3\). These imply respectively one versus zero first-dimensional homology classes over those fields, in agreement with the integral two-torsion.

An additional independent exact Smith calculation on the original (non-Morse) witness chain complex gave nonzero diagonal factors: \(\partial_1\): thirteen units; \(\partial_2\): forty units and one \(2\); \(\partial_3\): twelve units. The executable checker supplies the full enumeration and reduced integer certificates rather than relying on this separate symbolic calculation. The recorded standard-library execution is in `CHECKER_OUTPUT.txt`.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith introduce multipath complexes, dynamical regions and a torsion-stability conjecture in *On the Homotopy Type of Multipath Complexes*, arXiv:2208.04656v1, initially made public on 2022-08-09. Their paper calculates other graph families (including transitive tournaments, paths, polygons and selected grids), but its inspected statements do not classify bidirected graph complexes through five underlying vertices or calculate the three-page triangular book.

Caputi, Collari and Ramos, *The Weak Categorical Quiver Minor Theorem and Its Applications*, arXiv:2401.01248v1, prove bounded-torsion principles and a matching-complex comparison for **acyclic** digraphs. The latter does not apply here because every bidirected edge forms a two-cycle; no five-vertex exact threshold follows from their bounded-torsion result. Caputi, Collari and Smith, *Multipath Complexes of Bidirectional Polygonal Digraphs*, arXiv:2601.05670v1, addresses bidirected paths and cycles, not this common-edge triangular book. Earlier exact results for bidirected complete bipartite graphs already exhibit torsion on **six** underlying vertices; they neither imply torsion on five vertices nor the uniqueness of its five-vertex graph class. This finding claims only the stronger minimal/unique threshold, not discovery of the first torsion counterexample in any digraph.

## Limitations
The uniqueness statement is confined to **fully bidirected simple undirected** graphs on at most five underlying vertices. It makes no claim about the smallest arbitrary directed graph, and it does not determine the witness's full homotopy type or all graph orders. The complete finite classification uses a reproducible exhaustive algorithm and exact elementary-integer reductions; it is not an infinite-family classification. A published equivalent under another terminology or an unindexed computation remains a bibliographic possibility. The result has received no independent external audit.

## References
1. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the Homotopy Type of Multipath Complexes*, arXiv:2208.04656v1 (first public 2022-08-09), https://arxiv.org/abs/2208.04656.
2. L. Caputi, C. Collari and E. Ramos, *The Weak Categorical Quiver Minor Theorem and Its Applications: Matchings, Multipaths, and Magnitude Cohomology*, arXiv:2401.01248v1 (2024-01-02), https://arxiv.org/abs/2401.01248.
3. L. Caputi, C. Collari and J. P. Smith, *Multipath Complexes of Bidirectional Polygonal Digraphs*, arXiv:2601.05670v1 (2026-01), https://arxiv.org/abs/2601.05670.
