# The forbidden-diagonal five-by-five chessboard complex is \(S^2\vee\bigvee^{13}S^3\)

## Finding
Let \(G=K_{5,5}\setminus M\) be obtained by deleting a designated perfect matching from the five-by-five complete bipartite graph. The **ordinary matching complex** \(X=\mathcal M(G)\), not the complex generated solely by perfect matchings, satisfies
\[
X\simeq S^2\vee\bigvee^{13}S^3.
\]
Thus \(\widetilde H_2(X;\mathbb Z)\cong\mathbb Z\), \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^{13}\), and all other reduced integral homology groups vanish.

The standard full five-by-five chessboard complex has \(\widetilde H_2(\mathcal M(K_{5,5});\mathbb Z)\cong\mathbb Z/3\) by Jonsson's theorem. The diagonal-deleted subcomplex has free second homology instead, although its dimensional range is identical.

## Assumptions and scope
Rows and columns are indexed by \(\{0,1,2,3,4\}\). There are exactly twenty allowed cells \((i,j)\) with \(i\ne j\). A nonempty face is a set of allowed cells having distinct first coordinates and distinct second coordinates. The empty set is a face. A cell subset is interpreted as an ordinary graph matching; maximal faces may have fewer than five edges. The homotopy statement concerns this specific complex and is not a formula for all square board sizes.

The numbers of faces of dimensions \(0,1,2,3,4\) are respectively \(20,130,320,265,44\), so there are \(779\) nonempty faces and the Euler characteristic is \(-11\).

## Proof
Enumerate every face independently by (a) choosing rows and injecting them into distinct allowed columns, and (b) recursively processing rows and optionally selecting an available off-diagonal column. These enumerate the same \(780\) subsets when the empty face is included.

For each allowed square in the following zero-based sequence, match a currently unmatched nonempty face not containing that square to the face obtained by adjoining it, provided both are currently unmatched. The fixed square sequence is:

`(2,4),(0,2),(3,1),(1,3),(4,0),(4,3),(2,0),(3,4),(4,2),(2,1),(0,4),(1,0),(3,2),(3,0),(1,2),(2,3),(4,1),(0,3),(1,4),(0,1)`.

The executable certificate checks \(382\) disjoint matching pairs. The remaining critical cells have dimensions \(0,2,3\), of multiplicities \(1,1,13\). For each of all \(2500\) covering incidences in the nonempty face poset, direct the incidence from upper face to lower except reverse it for matched pairs. A complete topological sort visits all \(779\) nonempty faces and proves that this matching is acyclic. Forman's discrete-Morse theorem yields a homotopy-equivalent CW complex with exactly one zero-cell, one two-cell, and thirteen three-cells, no other cells.

To determine the attaching degrees, compute the signed simplicial boundary matrix in each degree over \(\mathbb Q\) from the independently enumerated faces, always orienting a simplex by increasing row-major index. Sparse exact Gaussian elimination gives the ranks \(19,111,208,44\) of boundary operators from dimensions one through four. Consequently the rational third Betti number is \(265-208-44=13\). In the Morse CW complex, the cellular differential from the thirteen three-cells to its single two-cell is an integer row. Since its rational kernel has dimension thirteen, the differential is zero over \(\mathbb Q\), hence it is exactly zero over \(\mathbb Z\).

The two-skeleton is \(S^2\). Each three-cell attaches through a map \(S^2\to S^2\) of degree zero, hence a nullhomotopic map because \(\pi_2(S^2)\cong\mathbb Z\) via the degree. Attaching all thirteen three-cells trivially gives \(S^2\vee\bigvee^{13}S^3\), proving the statement integrally. No appeal to finite sampling as an infinite theorem occurs: the object is finite and every face and incidence was checked.

## Verification
Run `python3 artifacts/verify.py` with Python 3 and its standard library. The script re-enumerates every face by two distinct constructions, verifies downward closure, reconstructs and checks every matching pair, tests all \(2500\) directed incidences for acyclicity by topological sort, and calculates the exact rational signed boundary ranks. The expected full stdout is supplied in `artifacts/verification_output.txt`. All operations are deterministic and finite.

## Relationship to prior work
Johnston, Kayll and Palmer's work on derangements identifies the perfect matchings in \(K_{n,n}\setminus M\) with fixed-point-free permutations, motivating this natural forbidden-diagonal family; their paper concerns enumerative counting, not the ordinary matching-complex homotopy type. Jonsson's Theorem 3.1 establishes the three-torsion in degree two of the **full** five-by-five chessboard complex, not its diagonal-deleted subcomplex. Published calculations of perfect-matching complexes for crown graphs concern a different complex; those results do not determine this ordinary matching complex, which includes nonextendable partial matchings. Related neighborhood complexes with a crown graph in an intermediate construction are also different functors. A targeted literature and research-index comparison found no statement covering this particular integral homotopy equivalence.

## Limitations
This is a finite classification at board size five. It does not determine all diagonal-deleted chessboard complexes, canonical equivariant splittings, or the induced map from the deleted-board complex to the full chessboard complex. Self-review is not an independent mathematical audit. Indexing and terminology variation leaves a residual possibility of equivalent prior work.

## References
Daniel Johnston, P. Mark Kayll, Cory Palmer, “Deranged matchings: proofs and conjectures,” arXiv:2209.11319, first public 2022-09-22, https://arxiv.org/abs/2209.11319.

Jakob Jonsson, “On the 3-torsion Part of the Homology of the Chessboard Complex,” arXiv:1203.5644, Theorem 3.1, https://arxiv.org/html/1203.5644v1.

Robin Forman, “Morse theory for cell complexes,” *Advances in Mathematics* 134 (1998), 90–145.
