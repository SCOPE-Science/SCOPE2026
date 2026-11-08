# The Chvátal three-cut complex is an integral Moore space

## Finding

Let \(C\) denote the twelve-vertex Chvátal graph. Its ordinary three-cut complex has the homotopy type

\[
\Delta_3(C)\simeq M(\mathbb Z/2\mathbb Z,7)=S^7\cup_{\deg 2}e^8.
\]

Consequently

\[
\widetilde H_j(\Delta_3(C);\mathbb Z)\cong
\begin{cases}
\mathbb Z/2\mathbb Z,&j=7,\\
0,&j\ne7.
\end{cases}
\]

This is genuine **integral two-torsion**, not a rational or mod-two Betti-number statement. Since the complex is pure of dimension eight, it is not shellable.

## Assumptions and scope

The vertex set is \(\{0,1,\dots,11\}\); the graph is simple and has exactly the twenty-four undirected edges given in `verify.py` (the constant `EDGES`). The adjacency list matches the standard Chvátal graph. Exhaustive tests also verify that the graph is four-regular, triangle-free and four-chromatic and contains exactly seventeen four-cycles, some sharing edges.

For any finite simple graph \(G=(V,E)\), the ordinary three-cut complex \(\Delta_3(G)\) is the simplicial complex with facets \(V\setminus T\), for each three-element subset \(T\subseteq V\) such that the induced graph \(G[T]\) is disconnected. All simplices are subsets of such facets; the empty face is present but is omitted from ordinary CW cellular counts.

The assertion concerns only this single labeled graph, but is invariant under relabeling. It does not assert a general result for all triangle-free four-chromatic or four-regular graphs.

## Proof

**1. Exhaustive definition and face set.** Enumerating all \(\binom{12}{3}=220\) triples gives 148 disconnected triples, hence 148 maximal eight-simplices. Taking their downward closures gives 3,927 nonempty faces and, in dimensions zero through eight, the face vector

\[
(12,66,220,495,792,924,792,478,148).
\]

The verifier compares this construction with the independently evaluated criterion that a nonempty set \(\sigma\) is a face if and only if its complement contains a disconnected triple. It checks every one of the 4,095 nonempty vertex subsets, not a sample.

**2. Explicit acyclic matching.** Let the vertex order be the integer list

```text
[1, 11, 6, 10, 8, 3, 4, 0, 9, 2, 5, 7]
```

Start with all faces including the empty face. For each vertex \(v\) in this list, pair every as-yet-unmatched face \(\sigma\) lacking \(v\) with \(\sigma\cup\{v\}\), when both remain unmatched. Remove both before proceeding to the next vertex. After these stages, remove the pair containing the empty face and regard its vertex as critical in the ordinary face poset. The resulting matching contains exactly 1,962 pairs and three critical nonempty simplices: one vertex (bitmask `2`), one seven-simplex (bitmask `3572`), and one eight-simplex (bitmask `1981`). Bitmasks use \(\sum_{v\in\sigma}2^v\).

To certify acyclicity directly, orient each matched cover relation from its lower to its upper face, and every other cover relation downward. The verifier constructs all 22,976 nonempty-face Hasse incidences and applies a complete topological sort to this directed graph; all 3,927 faces are removed, so there is no directed cycle. Forman's theorem gives a CW homotopy model with exactly one cell in dimensions zero, seven, and eight.

**3. Integral attaching degree.** Orient every simplex by its increasing vertex order. For a face \(\sigma\) with matched upper coface \(\tau\), its signed contribution to the Morse boundary is obtained from the relation \(\partial\tau=\varepsilon\sigma+\sum_{\rho\ne\sigma}a_\rho\rho\) with \(\varepsilon\in\{1,-1\}\), replacing \(\sigma\) by \(-\varepsilon\sum a_\rho\rho\). The acyclic matching makes the recursive evaluation terminate. Projecting the signed simplicial boundary of the unique critical eight-simplex onto the unique critical seven-simplex yields integer coefficient exactly \(2\).

Independently, exact integer unit-pivot column cancellation of all 147 matched seven-to-eight pairs leaves the unique critical-eight column with coefficient \(2\) in the critical-seven row; the remaining rows correspond to cells paired from dimension six and disappear in the lower cancellations. The two calculations agree, and both use the actual listed graph and matching rather than a numerical homology oracle.

The attaching map of the eight-cell has degree \(2\) on the seven-sphere. Since maps \(S^7\to S^7\) are classified by degree, the resulting CW complex is precisely the Moore space \(M(\mathbb Z/2\mathbb Z,7)\), establishing the asserted integral homotopy type.

**4. Nonshellability.** A pure shellable eight-dimensional complex is homotopy equivalent to a wedge of eight-spheres and has torsion-free integral homology. The computed nonzero seventh-homology torsion contradicts that conclusion.

## Verification

Execute `python3 verify.py` with Python 3.10 or newer; it uses only the standard library and returns `CHVATAL_CUT3_VERIFIED`. `verify_output.txt` records a successful replay. In addition to the two exact integer attaching-degree procedures, the verifier independently computes all mod-two simplicial boundary ranks, finding nonreduced mod-two Betti numbers equal to one in dimensions zero, seven and eight and zero otherwise. Direct mod-three rank calculations give ranks 330 and 148 for the boundaries in degrees seven and eight respectively, corroborating vanishing rational-like odd-characteristic homology in those degrees. Neither finite-field calculation alone is mistaken for an integral Smith certificate: the integral Morse-degree computation supplies that certificate.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced the modern systematic study of ordinary cut complexes and proved general shellability and homotopy results for several graph families [1]. Their Theorem 6.1 yields torsion-freeness under a complete-codimension-one-skeleton hypothesis, which fails here: seventeen potential dimension-seven faces are absent. Their Theorem 6.4 concerns the two-cut complex of connected triangle-free graphs, not the present three-cut complex. Their general construction permitting torsion does not determine this graph's homotopy type.

The continuation [2] studies disjoint unions, squared paths and grid graphs. It does not identify the Chvátal complex. Other previously studied triangle-free three-cut cases with no four-cycles or pairwise edge-disjoint four-cycles do not cover this graph: its seventeen four-cycles have overlapping edges. A published study of the Chvátal graph's independence and neighborhood complexes concerns different simplicial constructions and does not imply this Moore-space classification.

## Limitations

The proof is exhaustive for one fixed twelve-vertex graph; no formula is asserted for arbitrary graph families, other cut parameters or any equivariant homotopy structure. The computation is deterministic and self-contained, but an independent external audit has not been performed. Unindexed literature may contain equivalent calculations.

## References

1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first public 2023-04-26, https://arxiv.org/abs/2304.13675.
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first public 2024-07-11, https://arxiv.org/abs/2407.08158.
3. V. Chvátal, *The smallest triangle-free 4-chromatic 4-regular graph*, Journal of Combinatorial Theory 9 (1970), 93–94, DOI: 10.1016/S0021-9800(70)80057-6 (graph identification, not the motivating cut-complex research source).
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (the discrete-Morse homotopy theorem).
