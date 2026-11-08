# Integral mixed-dimensional homotopy type of the octagonal-prism matching complex

## Finding

Let \(G=C_8\square K_2\) be the graph of an octagonal prism, and let \(\mathcal M(G)\) be its **ordinary** matching complex. Then
\[
\mathcal M(G)\simeq \bigvee^3 S^4\vee\bigvee^7 S^5.
\]
Consequently, \(\widetilde H_4(\mathcal M(G);\mathbb Z)\cong\mathbb Z^3\), \(\widetilde H_5(\mathcal M(G);\mathbb Z)\cong\mathbb Z^7\), and all other reduced integral homology groups vanish. The conclusion is an integral homotopy classification, not merely a computation over a field.

## Assumptions and scope

Write the sixteen graph vertices as \((r,i)\), with \(r\in\{0,1\}\) and \(i\in\mathbb Z/8\mathbb Z\). Two vertices are adjacent if they are in the same layer and their indices differ by one modulo eight, or if they have equal indices and lie in opposite layers. Thus the graph has sixteen vertices, two eight-edge rim cycles, eight spokes, and twenty-four edges. The simplices of \(\mathcal M(G)\) are **all** sets of pairwise disjoint graph edges, including matchings not extendible to perfect matchings. In particular, this complex is generally distinct from the perfect-matching complex \(\mathcal M_p(G)\), the subcomplex of extendible matchings.

For reproducibility, number graph vertices as \(8r+i\). List the twenty-four unordered graph edges by lexicographically sorting pairs of integer endpoints. Encode a simplicial face by a twenty-four-bit integer whose set bits index the selected graph edges. The bit value zero denotes the empty face. The accompanying standard-library Python program specifies the complete finite computation with no external data.

## Proof

**1. Exhaustive face set.** Form the lexicographically ordered edge list described above. Start with the empty face; for each graph edge in increasing order, adjoin that edge to exactly the existing faces disjoint from it. Every matching has a unique maximal indexed edge and therefore appears exactly once in this recursion; no inadmissible set appears. This yields exactly \(11{,}396\) faces including the empty face, covering all simplices in every dimension.

**2. An explicit acyclic augmented Morse matching.** Order the twenty-four candidate simplex vertices by the following zero-based edge indices (in the lexicographic graph-edge order):

```text
0,22,16,3,18,1,13,10,8,4,17,5,11,15,23,7,2,14,12,9,21,19,20,6
```

For each pivot index successively, traverse the remaining faces in increasing integer order. Pair any remaining face not containing the pivot edge with its remaining coface obtained by inserting that edge, and remove both from further consideration. Every recorded pair differs by one simplex vertex and therefore is a codimension-one incidence. The program enumerates \(5{,}692\) disjoint pairs, leaving precisely four critical simplices of dimension four and eight of dimension five. In this **augmented** convention the empty face is matched, corresponding to reduced chains and one implicit CW basepoint.

To establish acyclicity rather than infer it from a heuristic pivot rule, orient each codimension-one face incidence downward except the selected matched incidence, which is oriented upward. The program enumerates exactly \(55{,}296\) incidences of the full finite face poset and performs a topological sort of the directed Hasse diagram. All \(11{,}396\) vertices of that diagram are removed by the sort, proving there is **no directed cycle**. Standard discrete-Morse cancellation therefore gives a reduced CW chain model with four generators in degree four and eight in degree five, and no others.

**3. Integral Morse boundary, with orientations.** Orient a simplex by increasing indices of its graph-edge vertices. Removing the \(j\)-th such vertex has boundary sign \((-1)^j\). For a matched dimension-four simplex \(a\) paired upward with dimension-five simplex \(b\), eliminate \(a\) by substituting the signed boundary of \(b\), divided by the incidence \(\langle\partial b,a\rangle\in\{\pm1\}\). Apply this substitution recursively to every relevant four-face in the boundary of each critical five-simplex. The acyclic Hasse orientation ensures these substitutions terminate. The verifier implements precisely this signed recursion on actual faces.

With the four critical four-faces ordered by their integer encodings and the eight critical five-faces likewise ordered, the complete integer boundary (rows indexed by degree-five cells, columns by degree-four cells) is

\[
\begin{pmatrix}
0&0&0&0\\
0&1&-1&-1\\
0&0&0&0\\
0&0&0&0\\
0&0&0&0\\
0&0&0&0\\
0&1&-1&-1\\
0&-1&1&1
\end{pmatrix}.
\]
Every nonzero row is a sign multiple of the primitive vector \((0,1,-1,-1)\), which has a coefficient of absolute value one. Thus the map from the eight free degree-five groups to the four free degree-four groups has rank one with **primitive image**, and its Smith factors are \((1,0,0,0)\) (allowing the usual zero padding for the rectangular matrix).

**4. From integer Morse boundary to homotopy type.** The Morse CW complex has one implicit basepoint, four four-cells and eight five-cells. Its four-skeleton is a wedge of four copies of \(S^4\). By the Hurewicz theorem, \(\pi_4(\bigvee^4S^4)\cong H_4(\bigvee^4S^4;\mathbb Z)\cong\mathbb Z^4\), so each five-cell attaching map is determined by its signed degree vector. Unimodular changes of the four-sphere basis and elementary five-cell slides reduce the primitive rank-one matrix to a single degree-one attaching map with all remaining maps nullhomotopic. Cancelling that sphere/five-cell pair yields a wedge of three four-spheres and seven five-spheres, as asserted.

## Verification

The included `verify_morse.py` is standalone Python 3 using only the standard library. From this directory run:

```sh
python3 verify_morse.py
```

The expected exact terminal output is in `verification_output.txt`. Its checks regenerate all graph edges and all faces, validate each matching pair, test global acyclicity of the **complete** Hasse diagram, compute the signed integer Morse boundary and its primitive rank-one structure, and independently compute all mod-two simplicial boundary ranks from the uncollapsed faces. The independent mod-two computation gives nonzero reduced Betti numbers three in degree four and seven in degree five. This auxiliary field check does not replace the signed integral computation or the attaching-map argument.

## Relationship to prior work

Agarwal and Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs* (arXiv:2608.30601v2, first posted August 31, 2026), determine the **independence and perfect-matching** complex homotopy types. Their Section 6, Problem 26 explicitly identifies ordinary matching complexes of circular ladders as a distinct topic for investigation. The present classification concerns precisely that ordinary complex, in a concrete octagonal-prism instance, and is not implied by their perfect-matching result.

Matsushita, *Matching complexes of small grids* (Electronic Journal of Combinatorics 26(3), P3.1, 2019), treats rectangular open-ended ladders \(P_n\square K_2\); the periodic closure producing \(C_8\square K_2\) changes the line graph and lies outside the stated open-ladder recursion. Bayer, Jelić Milutinović and Vega, *Matching Complexes of Outerplanar Graphs* (arXiv:2411.04601), prove a broad sphere-wedge result under **outerplanarity**, not a numerical homotopy classification of the octagonal prism. Other public classifications of cut complexes, independence complexes, or Möbius ladders cannot be directly substituted because their simplices or underlying graphs are different.

## Limitations

The result applies only to the octagonal prism, not every circular ladder or every generalized Petersen graph. It does not determine the action of the graph's dihedral symmetries on these homology groups, nor give a closed formula for arbitrary cycle lengths. Exhaustive computational verification is a valid proof for this explicitly finite complex because every simplex, incidence, matched pair and necessary integer boundary coefficient is generated and checked. It is not an extrapolation to infinite families. Unindexed equivalent computations of the same finite complex could exist; no absolute novelty guarantee is implied.

## References

1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2 (2026), especially Section 6, Problem 26. https://arxiv.org/pdf/2608.30601v2
2. T. Matsushita, *Matching complexes of small grids*, Electronic Journal of Combinatorics 26(3), P3.1 (2019). https://www.combinatorics.org/ojs/index.php/eljc/article/download/v26i3p1/pdf/
3. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v2 (first posted 2024). https://arxiv.org/pdf/2411.04601v2
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (standard discrete Morse background).
