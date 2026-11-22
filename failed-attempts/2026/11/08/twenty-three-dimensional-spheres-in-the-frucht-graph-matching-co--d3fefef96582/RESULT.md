# Twenty three-dimensional spheres in the Frucht graph matching complex

## Finding

For the classical twelve-vertex Frucht graph \(F\), the ordinary matching complex has the exact **integral homotopy type**
\[
\mathcal M(F)\simeq\bigvee^{20}S^{3}.
\]
Here a vertex of \(\mathcal M(F)\) is an **edge** of \(F\), and a simplex is a nonempty collection of pairwise vertex-disjoint graph edges, together with the empty face by convention. Consequently,
\[
\widetilde H_k(\mathcal M(F);\mathbb Z)\cong
\begin{cases}\mathbb Z^{20},&k=3,\\0,&k\neq3.\end{cases}
\]
The complex is nonpure: its inclusion-maximal matchings have sizes four (21 matchings), five (104 matchings), and six (eight matchings). Thus its maximal simplex dimension is five, although its homotopy type is three-dimensional.

## Assumptions and scope

The graph has vertex set \(\{0,1,\ldots,11\}\). For \(i=0,\ldots,11\), insert the cyclic edge \(\{i,i+1\pmod{12}\}\) and the chord \(\{i,i+d_i\pmod{12}\}\), where
\[
(d_0,\ldots,d_{11})=(-5,-2,-4,2,5,-2,2,5,-2,-5,4,2).
\]
Remove duplicate undirected edges. This gives the standard LCF presentation of the twelve-vertex cubic Frucht graph from Frucht's 1949 construction, with exactly 18 graph edges; it is also isomorphic to the graph depicted in Figure 1 of that paper. For complete reproducibility, sorted graph edges (zero-based) are

```text
(0,1), (0,7), (0,11), (1,2), (1,11), (2,3), (2,10), (3,4),
(3,5), (4,5), (4,9), (5,6), (6,7), (6,8), (7,8), (8,9),
(9,10), (10,11).
```

The assertion concerns the **ordinary matching complex** \(\mathcal M(F)=\operatorname{Ind}(L(F))\), not the ordinary vertex independence complex \(\operatorname{Ind}(F)\), an induced-forest complex, a perfect-matching subcomplex, or the discrete Morse complex of \(F\). All homotopy and homology statements are integral and nonequivariant. Classification: MSC2020 55U10.

## Proof

Index the 18 sorted graph edges by \(0,\ldots,17\). Encode each nonempty matching as an 18-bit integer whose set bits select its graph edges. A mask represents a face precisely when the selected graph edges have pairwise disjoint endpoints. Exhaustive enumeration of all \(2^{18}-1\) nonempty masks gives the face vector, indexed by dimension \(0,1,\ldots,5\),
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(18,117,333,397,152,8).
\]
There are precisely 1,025 nonempty faces. A separate recursive backtracking enumerator, which branches only on adding graph edges disjoint from those already chosen, produces exactly the same set of masks.

To construct a combinatorial Morse matching, use the fixed sequence of 18 edge indices

```text
9, 3, 4, 17, 15, 1, 0, 8, 13, 12, 2, 14, 10, 16, 6, 11, 5, 7
```

Start with every nonempty face unpaired. For each pivot \(j\) in the displayed order, traverse still-unpaired faces \(\sigma\) in increasing numerical mask order; whenever \(j\notin\sigma\), both \(\sigma\) and \(\sigma\cup\{j\}\) are still unpaired faces, pair those two and remove them from the pool. Each pair is a face/coface covering relation and no face is used twice.

This deterministic rule constructs **502 pairs**. Exactly 21 faces remain unpaired: one dimension-zero face (the vertex indexed nine) and twenty dimension-three faces. For a complete, machine-independent check of acyclicity, build the directed face-poset Hasse graph, orienting every covering relation from a smaller simplex to a larger one, **except reverse each matched covering relation**. The complete complex has **3,629 covering relations**. Kahn's topological sorting algorithm processes all **1,025 vertices** of this directed graph; therefore it is acyclic. This is exactly the acyclic-matching criterion of Forman's discrete Morse theory.

Forman's theorem supplies a CW complex homotopy equivalent to \(\mathcal M(F)\) with one zero-cell and twenty three-cells, and **no cells in any other positive dimension**. Every three-cell is attached to the single point, so that CW complex is a wedge of twenty three-spheres. This establishes the claim over \(\mathbb Z\), including the absence of torsion and any unrecorded attaching-map conditions.

The inclusion-maximal faces can additionally be found by testing that no other graph-edge index can be inserted. Their counts by matching size are \(21,104,8\) for sizes \(4,5,6\), respectively. A concrete \(K_4\) graph minor has connected and disjoint branch sets \(\{0,6,7,11\},\{1,2,3,10\},\{4,8,9\},\{5\}\); every pair of branch sets is joined by a graph edge. Thus \(F\) is **not outerplanar**, making outerplanar matching-complex classifications inapplicable.

## Verification

The self-contained Python 3 standard-library program `frucht_matching_verify.py` implements the full graph, both independent face enumerations, deterministic Morse pairs, all directed Hasse incidences, and the directed-cycle test. Run

```sh
python3 frucht_matching_verify.py
```

from a folder containing the embedded file. A successful execution ends with `FRUCHT_MATCHING_WEDGE_20_S3_PASS`. The text file `frucht_matching_verify.out` records the expected output. Checks include 1,025 nonempty simplices, 502 pairs, 21 critical simplices, 3,629 Hasse relations, and 1,025 vertices reached in the acyclicity topological sort. Independently, simplicial chain-matrix reductions over each of the fields with 2, 3 and 5 elements return boundary ranks \((17,100,233,144,8)\) in degrees one through five, yielding a single nonzero reduced Betti number, 20 in degree three. The field checks corroborate but **do not substitute for** the integer homotopy proof via acyclic matching.

## Relationship to prior work

Frucht's original graph paper defines the graph and studies prescribed automorphism groups, not matching-complex topology [1]. Generic discrete-Morse matching-tree techniques apply in principle but do not independently imply the specific critical-cell structure or multiplicity established here [2]. Bayer–Jelić Milutinović–Vega [3, Theorem 2] classify the matching complexes of **outerplanar** graphs as contractible or wedges of spheres. The explicit \(K_4\) minor above shows that this theorem does not apply to \(F\), and it gives no count for \(\mathcal M(F)\). Standard identity \(\mathcal M(F)=\operatorname{Ind}(L(F))\) [3, Proposition 4] explains the alias checked in literature searches; it does not equate \(\mathcal M(F)\) with \(\operatorname{Ind}(F)\).

Searches for Frucht graph matching-complex homotopy, line-graph independence homotopy and the exact sphere count found no inspected published statement implying the present classification. This is a best-knowledge originality assessment, **not a proof of global publication priority**; unindexed or inaccessible equivalent calculations may exist.

## Limitations

Only this specified graph and this ordinary matching complex are classified. The result is not a homotopy theorem for every cubic, planar or asymmetric graph, and it does not determine a representation under a symmetry group or a separate simple-homotopy class. Finite chain computations alone cannot establish the homotopy claim, which instead rests on the complete acyclic Morse certificate and Forman's theorem. Independent mathematical audit and definitive literature-priority verification remain outstanding.

## References

1. R. Frucht, “Graphs of Degree Three with a Given Abstract Group,” *Canadian Journal of Mathematics* 1 (1949), 365–378, issued 1 August 1949, DOI: 10.4153/CJM-1949-033-6. Figure 1 and the asymmetry discussion.
2. D. Taylan, “Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs,” arXiv:1501.06754v1 (27 January 2015), sections 2–5.
3. M. Bayer, M. Jelić Milutinović and J. Vega, “Matching Complexes of Outerplanar Graphs,” arXiv:2411.04601v1 (7 November 2024), Theorem 2 and Proposition 4.
4. R. Forman, “Morse Theory for Cell Complexes,” *Advances in Mathematics* 134 (1998), 90–145; discrete Morse theorem for finite complexes.
