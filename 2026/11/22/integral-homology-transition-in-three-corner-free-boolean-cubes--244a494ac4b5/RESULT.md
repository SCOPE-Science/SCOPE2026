# Integral homology transition in three-corner-free Boolean cubes

## Finding
Let \(V_n=\{0,1\}^{n}\) be the vertex set of the standard \(n\)-cube. Define the three-corner complex \(L_n\) to consist of all subsets \(S\subseteq V_n\) such that every coordinate square of the cube meets \(S\) in at most two vertices. For every integer \(2\le n\le5\), its complete reduced integral homology is
\[
\widetilde H_j(L_n;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{3},& (n,j)=(2,1)\text{ or }(3,2),\\
\mathbb Z^{16},&(n,j)=(4,3),\\
\mathbb Z,&(n,j)=(4,4),\\
\mathbb Z^{681},&(n,j)=(5,7),\\
0,&\text{otherwise}.
\end{cases}
\]
In particular every listed homology group is torsion-free, and the mixed-dimensional reduced homology at \(n=4\) is followed by concentration in dimension seven at \(n=5\). The claim concerns integral homology, not a complete homotopy type.

## Assumptions and scope
A coordinate square is a subset of \(V_n\) obtained by fixing \(n-2\) coordinates and allowing the other two to vary. A *forbidden triple* is any three of its four vertices. The complex \(L_n\) is the ordinary simplicial independence complex of the three-uniform hypergraph of forbidden triples. There are \(4\binom n2 2^{n-2}\) listed triple incidences before deduplication, and in fact each forbidden triple determines its square uniquely. Faces include the empty face, used for the augmented chain complex. All enumeration and homology assertions are restricted to the four stated dimensions \(n\); no extrapolation is claimed.

## Proof
A face is generated recursively by traversing binary vertices in ascending numeric order, adding a new vertex only if it completes none of the explicitly enumerated forbidden triples with two earlier selected vertices. This checks every possible face and no nonface. Its enumerated face totals, including the empty face, are \(11,77,3055,3302633\) for \(n=2,3,4,5\), respectively. For \(n=5\), the counts by cardinalities \(0,1,\ldots,16\) are
\[
(1,32,496,4640,28520,118656,337200,650784,841860,719040,404064,149952,38064,7680,1440,192,12).
\]

We apply an acyclic matching to the *augmented* face poset: at each vertex \(v\) in increasing order, pair every currently unmatched face avoiding \(v\) with its also-unmatched coface formed by adding \(v\), whenever that coface is a face. To see acyclicity, view each stage as the standard elementary toggle matching in the residual subposet, with matched cofaces deleted before the next stage; a hypothetical closed gradient path has a least toggle stage, and along that stage its indicator cannot change in the direction necessary to return. Equivalently, this is the iterated toggle/patchwork discrete Morse construction, with the empty face included algebraically.

The resulting critical-cell vectors \((\text{dimension}:\text{multiplicity})\) are
\[
\begin{array}{c|l}
 n&\text{critical cells}\\\hline
2&(1:3)\\
3&(2:3)\\
4&(3:17),(4:6),(5:4)\\
5&(5:1),(6:16),(7:757),(8:73),(9:12),(10:1),(11:1).
\end{array}
\]

The signed integral Morse differential is obtained from the simplicial boundary by eliminating every matched pair with its signed incidence coefficient \(\pm1\). For an upper partner \(\sigma\), its lower partner \(\tau\), and any remaining codimension-one faces \(\rho\), this substitution reads
\[
[\tau]=-\epsilon(\tau,\sigma)\sum_{\rho\ne\tau}\epsilon(\rho,\sigma)[\rho].
\]
Recursive expansion terminates by acyclicity and yields explicit integral matrices between critical cells. A separate checker verifies all successive compositions vanish, applies actual unimodular integer row and column operations at each \(\pm1\) pivot, and verifies the residual matrix is identically zero. The nonzero differential ranks are \(1,4\) in degrees \(4,5\) for \(n=4\) and \(1,15,61,12,1\) in degrees \(6,7,8,9,11\) for \(n=5\); all other differential ranks vanish. Every nonzero Smith invariant is one, so all integral homology is free. Subtracting adjacent ranks from the critical-cell counts gives exactly the displayed reduced homology groups, including the \(681\) degree-seven classes for \(n=5\).

## Verification
Run `python3 verify.py` in the same directory as `corner_morse.cpp` with a C++17 compiler (`g++`) available. The checker recompiles the source, enumerates every face independently of the recorded counts, generates signed Morse boundaries, verifies consecutive boundary compositions are zero, reduces every boundary by explicit integral unit Smith pivots, asserts zero residuals and checks the resulting reduced Betti ranks for every \(2\le n\le5\). Its success marker is `CUBE_THREE_CORNER_INTEGRAL_HOMOLOGY_OK`.

The complete degree-seven rank calculation for \(n=5\) uses the actual \(73\)-by-\(757\) and \(757\)-by-\(16\) adjacent integral boundaries, rather than a field-only calculation or Euler characteristic alone. Euler characteristics independently agree with the face counts.

## Relationship to prior work
Conant and Thistlethwaite's 2008 cubical theta complexes investigate avoidance of *complete square faces* (all four square vertices), whereas \(L_n\) forbids each *three-vertex* subset of a square; these are distinct hypergraphs and their face complexes are not interchangeable. Their general hypergraph/discrete-Morse viewpoint motivates considering this natural stronger local threshold. The ternary-coordinate cube hypergraph appearing in 2024 work on independent sets in hypercubes is also a different construction: its vertex set is ternary and its hyperedges are coordinate lines, rather than triples in binary coordinate squares. The published topology of \(\operatorname{Ind}_2(Q_4)\) concerns three-vertex-path avoidance in the cube's graph and is not an implication of the present square-corner avoidance statement.

## Limitations
No integral or equivariant homotopy equivalence is asserted. No formula for \(n\ge6\) is established, and neither the apparent concentration at \(n=5\) nor the absence of torsion is extrapolated. The exact numerical calculation is reproducible and finite, not a theoretical general-family classification. Complete exclusion of equivalent unpublished or unindexed work is not possible.

## References
- J. Conant and P. Thistlethwaite, *Boolean Formulae, Hypergraphs and Combinatorial Topology*, arXiv:0808.0739, version 1 publicly posted 2008-08-05, https://arxiv.org/abs/0808.0739.
- O. Cooley, J. H. M. Machata and M. Pasch, *Independent sets in hypercubes*, arXiv:2406.00401, 2024, https://arxiv.org/abs/2406.00401. Its 3-uniform cube hypergraph is structurally different.
