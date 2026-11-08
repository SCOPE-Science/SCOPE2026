# Integral sphere-wedge homotopy and regular peg symmetry of the three-disk Hanoi independence complex

## Finding
Let \(H_3^3\) be the graph of legal configurations of three disks on three pegs, and let \(X=\operatorname{Ind}(H_3^3)\) be its ordinary simplicial independence complex. There is a homotopy equivalence
\[
X\simeq\bigvee^6 S^6\vee\bigvee^6 S^7.
\]
Moreover, the full graph automorphism group is \(G\cong S_3\), and the complete reduced **integral** homology representation is
\[
\widetilde H_j(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z[G],&j=6,7,\\
0,&j\notin\{6,7\}.
\end{cases}
\]
In particular, both homology groups have rank six, with a primitive basis freely permuted by all six peg permutations. The two rational invariant ranks under \(G\) are each one.

## Assumptions and scope
The graph of **physical legal moves**, \(H_3^3\), has 27 vertices \(x=(a_0,a_1,a_2)\) encoding the pegs of three disks, largest first. Two states are connected exactly when they differ in one coordinate \(h\), while every smaller disk \(t>h\) remains on the third peg, distinct from the source and destination pegs of disk \(h\). Both the physical graph and a convenient **Sierpiński swap-presentation graph** have 39 edges. The swap graph has the same ternary-word vertex set, ordered lexicographically, but its adjacency instead holds when \(x[:h]=y[:h]\), \(x_h\ne y_h\), and \(x_t=y_h\), \(y_t=x_h\) for every \(t>h\). These are **different labeled graph rules**. The accompanying code explicitly proves they are isomorphic **equivariantly under all peg permutations**: the three distances to the pure corner states \(000,111,222\) distinguish all 27 vertices in both graphs; the unique bijection preserving these distance triples maps all 39 edges to physical edges and commutes with all six peg relabelings. Thus the swap graph provides an exact, equivariant computational model of the physical Hanoi graph. A face of \(X\) is a set of nonadjacent states. Park's theorem establishes that the full automorphism group is \(S_3\).

For the exact computational certificate, encode a face by the 27-bit integer \(\sum_{i\in F}2^i\), where \(i\) is the lexicographic vertex index; oriented faces list their vertex indices increasingly. All calculations use exact integers.

## Proof
**Exact equivariant graph model.** The code independently constructs the physical legal-move adjacency and the Sierpiński swap adjacency. In each graph, breadth-first-search distance triples to the three pure corner states are injective and have the same 27-element image. Their canonical distance-preserving map is verified on all 39 edges and all six peg permutations, so computations with the swap encoding establish claims about the physical graph and its peg-symmetry action.

**Exhaustive faces.** The executable `verify_hanoi.py` enumerates all independent subsets recursively: choose the least unused candidate vertex and, when including it, exclude its neighbors. The f-vector by cardinality from zero through nine is
\[
(1,27,312,2016,7983,19953,31211,29151,14565,2925),
\]
so there are 108,144 faces including the empty face. This agrees with the independently published number of independent sets on the three-disk graph (not with a prior homotopy computation). No face has ten or more vertices.

**Discrete Morse matching.** Begin with all 108,143 *nonempty* faces. Process vertices in increasing index order; for each index \(i\), pair every remaining face \(F\) not containing \(i\) with the remaining face \(F\cup\{i\}\) whenever both remain. Both faces are then removed from further matching. The program reconstructs the entire Hasse diagram, with exactly 672,537 nonempty-to-nonempty cover incidences, reverses precisely the paired cover arrows, and topologically sorts the resulting directed graph. The sort visits every one of the 108,143 faces, proving the matching has no closed alternating path. There are exactly 54,065 paired cells and 13 critical cells: one vertex, six in dimension six, and six in dimension seven.

**Integral Morse differential and ordinary homotopy.** For an increasing-order oriented face \(F=\{i_0<\cdots<i_k\}\), use the actual signed simplicial boundary \(\partial F=\sum_{j=0}^k(-1)^j(F\setminus\{i_j\})\). The code recursively cancels each matched lower cell with its matched upper cell using its incidence coefficient \(\pm1\), producing the exact integral Morse projection. The resulting complete Morse differential from six critical seven-cells to six critical six-cells is the zero \(6\)-by-\(6\) integer matrix. Discrete Morse theory therefore supplies a CW complex with only one zero-cell, six six-cells and six seven-cells, all the attaching *degrees* zero. The degree vector completely classifies each seven-cell attaching map because \(\pi_6(\bigvee^6S^6)\cong\mathbb Z^6\). Thus every such attaching map is nullhomotopic, establishing the stated **ordinary** wedge-of-spheres homotopy type. No torsion can occur.

**Integral regular modules.** To exhibit honest integral cycles, start with the critical six-cell represented by bitmask `18911508`, and the critical seven-cell represented by `72370452`. The code eliminates boundary coefficients in a topological order of matched lower faces, adding integral multiples of paired upper faces until the entire simplicial boundary is identically zero. The resulting cycles contain 200 and 256 nonzero oriented simplices, respectively; their boundaries are then recomputed independently. Apply all six peg permutations to each cycle, including their induced orientation signs. Project the six orbit cycles into the respective critical Morse bases. The resulting exact integer matrices have determinants \(-1\) in degree six and \(+1\) in degree seven. Each orbit is consequently a **primitive integral basis**, not merely a rational spanning family; the group permutes the basis regularly. This proves both \(\mathbb Z[S_3]\)-module isomorphisms.

Finally, signed simplicial Lefschetz traces computed independently on all nonempty faces give the **ordinary** Lefschetz number \(1\) for every group element, as predicted by the two regular modules in consecutive degrees (whose traces cancel) together with \(H_0(X;\mathbb Z)\cong\mathbb Z\). This is a consistency check, not a substitute for the integral cycle certificates.

## Verification
Run `python3 verify_hanoi.py` with Python 3.10 or later; the program uses only the standard library. The exactly reproduced console output is bundled as `verification_output.txt`. The code checks the equivariant graph isomorphism, every adjacency, face, matching edge, directed-acyclicity condition, signed Morse differential coefficient, lifted-cycle boundary, group automorphism, primitive orbit determinant and signed Lefschetz trace. No floating-point arithmetic or finite-field inference is involved. The integral matrix and primitive cycles, rather than sample experiments, establish the finite theorem.

## Relationship to prior work
Park's 2008 graph-symmetry theorem identifies the entire automorphism group and the legal-move model but does not study independence-complex topology. Chen, Wu, Huang and Deng's 2017 article, published online in 2016, determines recurrences and asymptotic counts of independent vertex sets; its 108,144 count agrees with the cardinality of the simplicial face set here, but does **not** determine attaching maps, homotopy type, or integral group actions. Sreeja, Vinodkumar and Ramkumar's 2021 paper likewise treats independence polynomials and identifies the same 108,144 count. A published-result semantic search was compared against homotopy and symmetry computations for other named graphs; those statements concern different graph complexes and do not imply the present graph-specific results. No uniqueness guarantee is claimed from the search.

## Limitations
This is a calculation for **exactly** three disks and three pegs, not a uniform classification for all Hanoi graphs. The isomorphisms describe the integral homology group actions but do not provide an equivariant wedge-of-spheres homotopy decomposition, integral quotient cohomology, or higher-stage recursion. An equivalent, possibly differently named calculation in unindexed literature remains a priority risk; the result has not undergone independent mathematical review.

## References
1. So Eun Park, *The Group of Symmetries of the Tower of Hanoi Graph*, arXiv:0809.1179, first public 2008-09-07, https://arxiv.org/abs/0809.1179 .
2. H. Chen, R. Wu, G. Huang and H. Deng, *Independent sets on the Towers of Hanoi graphs*, Ars Mathematica Contemporanea **12** (2017), 247–260; first online 2016-12-07. Full article: https://dlib.si/stream/URN:NBN:SI:DOC-8L0DJRCU/25688b45-2a8d-433b-8e3b-297e461d9763/PDF .
3. K. U. Sreeja, P. B. Vinodkumar and P. B. Ramkumar, *Independence polynomial of the Sierpinski gasket graph and the tower of Hanoi graph*, Journal of Mathematical and Computational Science **11** (2021), 7072–7081, DOI:10.28919/jmcs/6053, https://scik.org/index.php/jmcs/article/download/6053/3113 .
