# The Clebsch independence complex is a wedge of nine 3-spheres
## Finding
Let \(FQ_5\) be the 5-folded cube, equivalently the 5-regular Clebsch (Greenwood–Gleason) graph on the even-weight vectors of \(\mathbb F_2^5\), with two vertices adjacent exactly when their Hamming distance is \(4\). Then
\[
\operatorname{Ind}(FQ_5)\simeq\bigvee^{9}S^3.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. The vertex set used for the finite model is
\[
V=\{x\in\mathbb F_2^5:\operatorname{wt}(x)\equiv0\pmod 2\},
\]
and distinct \(x,y\in V\) are adjacent when \(\operatorname{wt}(x+y)=4\). This gives a 16-vertex, 40-edge, 5-regular graph with strongly regular parameters \((16,5,0,2)\). The independence complex consists of all independent vertex subsets. The assertion concerns this one graph and does not claim a homotopy formula for higher folded cubes.

## Proof
The verifier enumerates all \(2^{16}\) vertex subsets and retains exactly the nonempty independent sets. There are \(392\) nonempty faces, with face vector by simplex dimension
\[
(16,80,160,120,16).
\]

On this complete face poset, use the vertex-toggle order
\[
01001,00011,01100,00101,11011,10100,11000,11110,
10001,10111,01010,01111,11101,00110,00000,10010.
\]
At each stage, among the faces still unmatched, pair a face \(\sigma\) not containing the current vertex \(v\) with \(\sigma\cup\{v\}\) whenever the latter is also still unmatched. The resulting matching has \(191\) pairs.

The complete Hasse diagram has \(1200\) cover relations. Directing every unmatched cover downward and every matched cover upward produces a directed acyclic graph: a topological sort visits all \(392\) faces. Thus this is an acyclic discrete-Morse matching. Its only critical simplices are one vertex and nine 3-simplices. Forman's discrete Morse theorem therefore replaces the independence complex by a CW complex with exactly one 0-cell and nine 3-cells, and no cells in dimensions 1 or 2. Every 3-cell consequently attaches to the unique 0-cell by the constant map, so the CW complex is a wedge of nine 3-spheres. This proves the displayed homotopy equivalence.

## Verification
Run `python3 verify_clebsch_independence.py`. The script uses only the Python standard library. It reconstructs the graph from the even-weight binary vectors, checks the strongly regular parameters, exhaustively enumerates all independent sets, recreates the 191-pair matching, generates all 1200 Hasse covers, and topologically sorts the entire Morse-oriented Hasse graph.

As an independent algebraic cross-check, it constructs the full simplicial boundary matrices over \(\mathbb F_2\). Their ranks in positive degrees are
\[
(15,65,95,16),
\]
so the unreduced Betti vector is \((1,0,0,9,0)\). The reduced Euler characteristic is \(-9\). A successful replay ends with `ACYCLIC_MATCHING_OK` and `VERIFY_OK`.

## Relationship to prior work
The public table OEIS A355227 already records the independence polynomial of the 5-folded cube as
\[
1+16t+80t^2+160t^3+120t^4+16t^5,
\]
so the face vector above is not claimed as new. OEIS A355559 correspondingly records evaluation at \(-1\) equal to \(9\), which determines the reduced Euler characteristic but not the homotopy type.

Barmak proved that the independence complex of every triangle-free graph has the homotopy type of a suspension. Since the Clebsch graph is triangle-free, that theorem applies, but it does not determine the suspended space or the number and dimension of spheres. Matsushita and Wakatsuki give exact wedge-of-spheres results for square-grid graph families and emphasize that exact independence-complex homotopy types are generally difficult; their family does not contain the Clebsch graph. Chen, Naserasr, and Sarti identify the dimension-4 projective cube with the graph commonly called the Clebsch or Greenwood–Gleason graph, providing an alias check for the object.

Targeted searches under Clebsch, Greenwood–Gleason, Segre graph, 5-folded cube, projective cube \(PC(4)\), and complementary-clique-complex terminology did not locate a source stating the displayed wedge decomposition. This search evidence supports the originality assessment but is not a proof that no unindexed source exists.

## Limitations
The proof is a finite exact computation for one 16-vertex graph. It does not produce a uniform formula for \(FQ_n\), and the particular toggle order was found computationally rather than derived from a general symmetry principle. The public independence-polynomial and Euler-characteristic data predate this calculation, so only the exact homotopy refinement is claimed. An equivalent computation may exist in literature not surfaced by the alias searches. No independent audit has been performed.

## References
1. OEIS A355227, independent-set counts for folded cube graphs; row \(n=5\) is \((1,16,80,160,120,16)\), author date 2022-06-24.
2. OEIS A355559, independence polynomial of the folded cube evaluated at \(-1\); the \(n=5\) value is \(9\), author date 2022-07-06.
3. T. Matsushita and S. Wakatsuki, *Independence complexes of \((n\times6)\)-grid graphs*, arXiv:2207.10363v1, first posted 2022-07-21; primary MSC 55P10.
4. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first posted 2010-07-02; Theorem 3.4 gives the suspension result for triangle-free graphs.
5. M. Chen, R. Naserasr, and A. Sarti, *Signed projective cubes, a homomorphism point of view*, arXiv:2406.10814v1, first posted 2024-06-16; identifies the dimension-4 projective cube with the Clebsch/Greenwood–Gleason graph.
