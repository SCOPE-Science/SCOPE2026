# A two-torsion Moore summand in the cyclic \(2,2,4\) multipath complex

## Finding

Let \(D\) be the eight-vertex digraph with vertex sets \(A=\{a_0,a_1\}\), \(B=\{b_0,b_1\}\), and \(C=\{c_0,c_1,c_2,c_3\}\). Include every possible arc \(A\to B\), \(B\to C\), and \(C\to A\), and no other arcs. Let \(X(D)\) be the simplicial complex whose vertices are the twenty arcs and whose simplices are unions of vertex-disjoint directed paths, including isolated vertices of the digraph.

Its complete **integral homotopy type** is
\[
X(D)\simeq\bigvee^{3} S^3\vee\bigvee^{28} S^4\vee M(\mathbb Z/2\mathbb Z,3),
\]
where \(M(\mathbb Z/2\mathbb Z,3)=S^3\cup_2 e^4\) is the Moore space obtained by attaching a four-cell with degree two. In particular,
\[
\widetilde H_i(X(D);\mathbb Z)\cong\begin{cases}
\mathbb Z^3\oplus\mathbb Z/2\mathbb Z,&i=3,\\
\mathbb Z^{28},&i=4,\\
0,&\text{otherwise}.
\end{cases}
\]
This is a natural finite, strongly connected, simple cyclically oriented tripartite digraph with integral two-torsion in its directed-multipath topology.

## Assumptions and scope

The graph has precisely the twenty specified arcs, each used at most once. A selected arc set is a face if and only if each vertex has selected indegree and outdegree at most one and the selected arcs contain no directed cycle. Directed cycles of length three or six are therefore excluded, while directed paths may contain more than one arc. The result concerns the ordinary multipath complex, **not** regular path homology, the directed flag complex, or a graph matching complex. No assertion is made for other shore cardinalities.

## Proof

The proof is finite and fully constructive. Order the arcs lexicographically, first the four \(A\to B\) arcs, next the eight \(B\to C\) arcs, and last the eight \(C\to A\) arcs. Label their positions \(0,\ldots,19\) and encode a face by the sum of the corresponding powers of two. Enumerating all legal faces by adding only higher-index arcs gives the exact face vector \((20,154,560,976,720,144)\), in dimensions zero through five, for a total of 2,574 nonempty faces. The Euler characteristic is 26.

Define a matching on the nonempty face poset using the toggle sequence

`[17,13,6,2,4,3,15,11,1,0,8,14,10,7,19,9,12,18,16,5]`.

At each position, pair every currently unmatched legal face not containing that arc to its currently unmatched coface formed by adding it, whenever both are still unmatched. Exactly 1,269 pairs result, leaving one critical vertex, five critical three-faces, and thirty critical four-faces. The critical three-face bitmasks, in increasing order, are

`[4420,8722,25092,66580,270342]`.

The thirty critical four-face bitmasks are

`[4425,5142,24866,25097,25105,25634,37153,37394,65862,66585,98822,98945,99361,270722,271490,272393,272401,295554,295970,296993,528769,529448,530450,541313,542754,590466,590888,590977,591878,591905]`.

For an acyclic discrete-Morse matching, orient every matched Hasse edge from the lower to the upper face and every unmatched Hasse edge from upper to lower. Complete depth-first inspection of this finite directed Hasse graph finds no directed cycle. Consequently the matching gives a homotopy-equivalent CW complex with precisely the stated critical cells. This is a complete finite certificate: the complete face set and pairing can be regenerated from `verify.py` without relying on a precomputed log.

For a matched pair \(L\subset U\), write \(\varepsilon=[U:L]=\pm1\) for the signed simplex incidence. The integral Morse projection on a matched lower face is recursively
\[
R(L)=-\varepsilon^{-1}\sum_{F\subset U,\ F\ne L,\ |F|=|L|}[U:F]R(F),
\]
with \(R(F)=F\) on critical faces and \(R(F)=0\) on matched upper faces. The acyclic matching guarantees that the recursion terminates. On a critical cell \(S\), its Morse differential is \(\partial_M S=\sum_{F\subset S,\ |F|=|S|-1}[S:F]R(F)\).

There is one possible nonzero Morse boundary, a signed integer \(5\times30\) matrix from critical four-cells to critical three-cells. Only six columns are nonzero. In the increasing critical-cell orders given above, they are:

| Four-face mask | Five signed coefficients |
|---|---|
| `98945` | `[-1,0,0,1,0]` |
| `295970` | `[-1,2,-2,1,2]` |
| `529448` | `[0,-2,2,0,-2]` |
| `590466` | `[-1,2,-2,1,2]` |
| `590888` | `[0,-2,2,0,-2]` |
| `591905` | `[1,-2,2,-1,-2]` |

All remaining columns vanish. The matrix has exact rational rank two, the gcd of all entries is one, and the gcd of all \(2\times2\) minors is two. Its complete nonzero Smith invariants are therefore \((1,2)\). The reduced cellular homology is \(\mathbb Z^3\oplus\mathbb Z/2\mathbb Z\) in degree three and \(\mathbb Z^{28}\) in degree four, with no other groups.

Because the Morse CW complex has no cells in dimensions one or two, its three-skeleton is a wedge of five three-spheres. The degree-four attaching maps lie in \(\pi_3(\bigvee^5 S^3)\cong\mathbb Z^5\) and are classified by the integral boundary matrix; no higher Whitehead-product obstruction occurs in this dimension. Integral changes of bases (realized by self-homotopy equivalences of the three-sphere wedge and rearrangements of the attaching four-cells) bring the attaching matrix into Smith form. The unit degree-one pair cancels, the degree-two pair produces \(M(\mathbb Z/2\mathbb Z,3)\), and the remaining cells produce three three-spheres and twenty-eight four-spheres. This proves the stated integral homotopy equivalence.

## Verification

Run `python3 verify.py` (Python standard library only) in the directory containing the accompanying standalone source. It regenerates all legal arc sets, checks every matching pair and the complete Hasse-DAG acyclicity, derives the signed Morse differential, computes rank and gcd-of-minors Smith data over the integers, and independently computes full simplicial boundary ranks over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\). Three other deterministic toggle orders recover the same rational and characteristic-two rank discrepancy. The supplied `verify_output.txt` records the actual run. For example, the full-field Betti ranks in degrees three and four are \((4,29)\) over \(\mathbb F_2\) and \((3,28)\) over odd fields, exactly as the universal coefficient theorem predicts.

## Relationship to prior work

Caputi, Collari, Di Trani and Smith define multipath complexes and study paths, polygons, small grids, complete bipartite orientations and transitive tournaments [1]. Their statements do not compute the cyclic tripartite \((2,2,4)\) instance. Caputi, Collari and Ramos prove bounded-genus torsion bounds and give a matching-complex comparison for directed acyclic graphs [2]; neither specifies this cyclic graph's integral torsion or homotopy type. An indexed analysis of the cyclic doubled triangle concerns shore sizes \((2,2,2)\), whereas this calculation uses \((2,2,4)\); its torsion-free calculation does not imply the present group. Existing bidirected complete-bipartite examples exhibiting order-two torsion have a different arc set and cannot be identified with this cyclic tripartite graph. This comparison is not an absolute novelty guarantee; unindexed equivalences remain possible.

## Limitations

The result is an exact finite homotopy classification only for the specified eight-vertex digraph. It does not extrapolate to arbitrary \((2,2,n)\), nor show that this is the smallest directed-multipath example with torsion. All numerical certificate checks are complete on this finite complex. No independent mathematical audit has been performed.

## References

1. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (first public 2022-08-09), https://arxiv.org/abs/2208.04656.
2. L. Caputi, C. Collari and E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248v1 (2024-01-02), https://arxiv.org/abs/2401.01248.

