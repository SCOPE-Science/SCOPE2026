# The ordinary four-cut complex of the Petersen graph and its symmetric-group character

## Finding
Let \(P=KG(5,2)\) be the Petersen graph: its ten vertices are the two-element subsets of \(\{1,2,3,4,5\}\), and two vertices are adjacent precisely when their subsets are disjoint. For a finite graph \(G\), define the ordinary \(k\)-cut complex \(\Delta_k(G)\) to have facets \(V(G)\setminus T\) for exactly those \(k\)-element vertex sets \(T\) for which the induced graph \(G[T]\) is disconnected.

The integral homotopy type of its ordinary four-cut complex is
\[
\Delta_4(P)\simeq\bigvee^{26}S^5.
\]
Under the natural action of \(\mathfrak S_5\) on two-element subsets, the rational fifth-homology representation is
\[
\widetilde H_5(\Delta_4(P);\mathbb Q)
\cong S^{(5)}\oplus 2S^{(4,1)}\oplus S^{(3,2)}\oplus 2S^{(3,1,1)},
\]
where \(S^\lambda\) is the rational Specht module indexed by the partition \(\lambda\). Thus there is precisely one \(\mathfrak S_5\)-invariant rational fifth-homology class. All other reduced integral homology groups vanish, and the fifth is free of rank \(26\).

The face vector by dimensions zero through five is \((10,45,120,210,240,140)\). All \(210\) possible four-vertex faces occur. The twelve absent five-vertex faces are precisely complements of the twelve induced pentagons in \(P\).

## Assumptions and scope
The graph is the simple Kneser graph \(KG(5,2)\) described above. The definition is the **ordinary**, not total, cut complex: disconnectivity is strictly weaker than the requirement that an induced set be independent. The simplicial realization uses integral cellular homotopy, and the symmetry statement is over \(\mathbb Q\). Vertices of every face are ordered lexicographically by their underlying two-subsets for oriented-chain calculations. No statement about other Kneser graphs, larger cut parameters, or integral representation splitting is asserted.

## Proof
**Facet and face construction.** Order the ten two-subsets lexicographically and encode each graph vertex subset by a ten-bit integer. Among the \(\binom{10}{4}=210\) four-subsets, a breadth-first connectivity test identifies exactly \(70\) connected and \(140\) disconnected induced graphs. The \(140\) complements of the latter sets are distinct six-element facets. Their Boolean downward closures give exactly \(766\) faces including the empty face, with the displayed face vector. An independent membership test uses the equivalence: \(F\in\Delta_4(P)\) exactly when \(V(P)\setminus F\) contains a disconnected four-subset. The two sets of faces agree for every one of the \(2^{10}\) vertex subsets.

**Pentagon boundary phenomenon.** A five-element face \(F\) is absent exactly when every four-subset of the complementary five-set \(T\) induces a connected graph. The latter means that \(P[T]\) remains connected on deletion of each vertex. Since \(P\) has girth five, any five-vertex induced subgraph with that property is a five-cycle. Conversely, deletion of any vertex of a five-cycle leaves a connected four-vertex path. The exact enumeration shows twelve such pentagons; their complements are exactly the twelve missing four-dimensional simplices. This explains the failure of the complete codimension-one skeleton condition that would otherwise yield the familiar high-girth face-count formula.

**Discrete-Morse certificate.** Use the finite element-matching algorithm in `verify.py`, with the 369 pairs listed in `morse_pairs.json`. Start with every nonempty face unmatched. For graph-vertex indices \(v=0,1,\dots,9\) in order, pair each currently unmatched face \(F\) not containing \(v\) with \(F\cup\{v\}\), when both are present and unmatched. The table gives precisely \(369\) disjoint matched Hasse incidences among \(765\) nonempty faces. Orient each matched Hasse edge from its lower to its upper face, and every remaining Hasse edge from upper to lower. The verifier constructs the complete directed graph with \(3{,}330\) incidences and explicitly topologically sorts it, visiting every face. Thus the matching is acyclic. Exactly one zero-dimensional face and \(26\) five-dimensional faces are critical; there are no other critical cells. Forman's discrete-Morse theorem provides a CW model with one zero-cell, \(26\) five-cells, and no cells in intermediate dimensions. All five-cell attaching maps have the one-point four-skeleton as target, hence are nullhomotopic. The resulting CW model is a wedge of \(26\) five-spheres, proving the integral homotopy statement.

**Symmetry.** Every permutation of the underlying five symbols acts simplicially. For a group element \(g\) and dimension \(d\), its cellular chain trace is the sum over setwise fixed \(d\)-simplices of the sign of the induced vertex-order permutation. Subtracting the trace on the augmentation gives the reduced Lefschetz number \(L_{\mathrm{red}}(g)\). The Morse calculation shows only reduced fifth homology, so \(\operatorname{tr}(g\mid\widetilde H_5)=-L_{\mathrm{red}}(g)\). Exhaustive evaluation of all \(120\) permutations gives this character table:

| Cycle type | Class size | Fifth-homology trace |
|---|---:|---:|
| \((1,1,1,1,1)\) | 1 | 26 |
| \((2,1,1,1)\) | 10 | 6 |
| \((2,2,1)\) | 15 | -2 |
| \((3,1,1)\) | 20 | 2 |
| \((3,2)\) | 20 | 0 |
| \((4,1)\) | 30 | 0 |
| \((5)\) | 24 | 1 |

Taking exact character inner products against the seven irreducible rational characters of \(\mathfrak S_5\), computed using the Frobenius coefficient formula, gives multiplicities \((1,2,1,2,0,0,0)\) in partition order \((5),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1)\). Their dimensions sum to \(1+2\cdot4+5+2\cdot6=26\), as required.

## Verification
The package includes `verify.py` (Python standard library only), `morse_pairs.json` (all lower/upper face masks and critical masks), and `verification_output.txt` (the actual run result). Run `python3 verify.py` alongside the pair file. It checks connectivity and all faces by two methods, the pentagon characterization, the complete directed acyclicity of two differently ordered matchings, the displayed critical cells, exact mod-two simplicial boundary ranks \((9,36,84,126,114)\), all \(120\) signed group actions and the full irreducible character decomposition. These finite checks are exhaustive for this ten-vertex complex. The mod-two calculation is corroborative; integral homotopy follows from the acyclic Morse certificate, not from mod-two ranks alone.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced and systematically developed ordinary cut complexes, including a theorem for the **two-cut** of the Petersen graph; this does not determine the four-cut complex. Their conditional complete-skeleton result does not apply here, since the twelve pentagons cause missing four-dimensional simplices. Their continuation studies disjoint unions, squared paths and grids, not this Kneser-graph four-cut. Their work on total cut complexes instead uses independent four-subsets, producing a different subcomplex. An independently indexed high-girth cut-complex theorem requires girth at least \(k+2\), namely six for \(k=4\), while \(P\) has girth five. An indexed four-cut calculation of the complementary triangular graph \(J(5,2)\) concerns a different graph and produces a different homotopy type. No inspected source implies the exact four-cut homotopy and character calculated here.

## Limitations
This is a finite, computer-assisted but exhaustive homotopy and rational character classification of this single canonical graph. It does not classify all five-girth graphs, prove shellability, compute integral isotypic lattices, or determine any higher-dimensional Kneser families. Finite searches and inspected sources do not establish bibliographic uniqueness; equivalent work could exist under another description. No independent external audit has been performed.

## References
1. M. Bayer et al., *Total Cut Complexes of Graphs*, arXiv:2209.13503 (first posted September 27, 2022).
2. M. Bayer et al., *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first posted April 26, 2023); SIAM J. Discrete Math. 38 (2024), 1630–1675.
3. M. Bayer et al., *Topology of Cut Complexes II*, arXiv:2407.08158 (first posted July 11, 2024).
4. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145.
