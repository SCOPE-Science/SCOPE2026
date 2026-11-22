# The complete Euclidean chord spectrum of the three-bar first-refinement barcode polytope

## Finding

For the canonical permutation-coordinate embedding of the first midpoint-refined three-bar barcode polytope \(P_{3,1}\), the complete unordered vertex-pair squared-distance spectrum consists of **75 distinct values**,
\[
\{2,4,6,\ldots,146,150,152\},
\]
with each exact multiplicity in `CHORD_SPECTRUM.csv`. Thus the only absent positive even squared distance up to the maximum is \(148\). Of the \(\binom{280}{2}=39060\) unordered distinct-vertex pairs, exactly \(45\) have squared distance \(152\), and \(15\) have squared distance \(150\). The diameter graph is a matching of \(45\) edges together with \(190\) isolated vertices. The arithmetic mean squared distance over all distinct unordered vertex pairs is exactly \(15206/217\).

The squared Euclidean diameter is therefore \(152\), or diameter \(\sqrt{152}=2\sqrt{38}\). The list in `CHORD_SPECTRUM.csv` is a complete finite classification, not a conjectural pattern in the number of bars or refinement depth.

## Assumptions and scope

The vertex coordinates use the ambient Euclidean norm of \(\mathbb R^9\) and the exact integer-permutation embedding in Jaramillo-Rodriguez's definition of \(P_{n,k}\), **without** changing to the graph metric of the polytope or to a bottleneck/Wasserstein distance between persistent-homology barcodes. Identify the ordered copies \(1_1,1_2,1_3,2_1,2_2,2_3,3_1,3_2,3_3\) with labels \(1,2,3,4,5,6,7,8,9\), respectively. A canonical representative is a permutation \(p=(p_1,\ldots,p_9)\) satisfying precisely the strict precedence relations
\[
1\prec2\prec3,\qquad 4\prec5\prec6,\qquad 7\prec8\prec9,\qquad 1\prec4\prec7,
\]
where \(a\prec b\) means the entry \(a\) appears before \(b\). There are no additional precedence restrictions. The polytope is their convex hull. Every pair of vertices is counted once and only pairs of distinct vertices are included.

The stated Euclidean measurements refer only to this specific standard realization, not to its arbitrary affine images. No conclusion about larger \(P_{n,k}\), or about persistence-diagram metrics, is asserted.

## Proof

**Exact vertex set.** The canonical representative condition requires birth times (first copies) in order and copies within a bar in order. These conditions are exactly the displayed finite precedence poset. Its Hasse graph is a rooted tree; the subtree cardinalities, in label order, are \((9,2,1,6,2,1,3,2,1)\). The hook-length formula for rooted-tree linear extensions gives
\[
|V|=\frac{9!}{9\cdot2\cdot6\cdot2\cdot3\cdot2}=280.
\]
Each permitted vector is a vertex: for a permutation vector \(p\), the linear functional \(x\mapsto \langle p,x\rangle\) is uniquely maximized at \(p\) over **all** permutations of \(\{1,\ldots,9\}\), by the strict rearrangement inequality. It remains unique on the restricted convex hull. Thus no enumerated representative is redundant.

**Certified exhaustive distance count.** Every precedence-compatible permutation is generated exactly once by the following complete branching rule: begin with the empty prefix; append any unused label whose immediate predecessors are all present; stop at length nine. Necessity holds for every linear extension, while induction on prefix length proves no extension is omitted. A separate exhaustive filter over all \(9!\) permutations gives the same set and count. The supplied `verify.py` implements both and checks set equality (not merely equality of cardinalities).

For each ordered-by-index distinct pair \(p,q\) of these \(280\) vectors, compute the integer
\[
\delta(p,q)=\sum_{i=1}^{9}(p_i-q_i)^2.
\]
Increment the bin for \(\delta(p,q)\) exactly once. The two independent generators produce identical exact integer histograms, and the script compares them with every row of `CHORD_SPECTRUM.csv`. There are exactly \(\binom{280}{2}=39060\) loop iterations. Exhaustiveness of the branching rule and of this finite double loop proves the histogram for the entire polytope vertex set, rather than merely sampling distances.

Because every vertex has the same coordinate-square sum, \(\delta(p,q)=2(\sum_{i=1}^{9}i^2-\langle p,q\rangle)\) is even. The histogram has exactly the support stated above. Its largest bin indices are \(152\) and \(150\), with multiplicities \(45\) and \(15\). In the same loop, adding one incidence to each endpoint of a \(152\)-pair gives exactly \(90\) vertices of degree one and no higher degree; hence the diameter graph is a \(45\)-edge matching and \(190\) isolated vertices. Finally, exact integer accumulation gives \(\sum_{p<q}\delta(p,q)=2737080\), whose division by \(39060\) reduces to \(15206/217\).

## Verification

Place `verify.py` beside `CHORD_SPECTRUM.csv` and execute `python3 verify.py`. The verifier uses only the Python standard library and checks all constraints, all vertices, all pairwise distances, the complete comma-separated histogram, degree distribution at the diameter, the mean, and the absence of the \(148\) shell. It is intended as a self-contained finite exhaustion and was run successfully on the delivered file contents; see `VERIFICATION.md` for the replayed command and limitations. A pair of diametral vertices, as an independent witness for the attained bound, is
\[
(1,4,5,2,3,7,6,8,9),\qquad (1,4,7,8,9,5,6,2,3).
\]

## Relationship to prior work

Jaramillo-Rodriguez introduced the power-refined barcode polytope construction and identified it as a Bruhat interval polytope; the source supplies the canonical permutation embedding, the fact that the ambient dimension is \(9\) for the present case, and the intrinsic affine dimension \(7\). The cited original work emphasizes order and links between refined combinatorial barcode signatures and conventional barcode distances, rather than a repeated ambient Euclidean chord spectrum. Tsukerman and Williams gave general combinatorial structure of Bruhat interval polytopes. Their theorem that a Bruhat interval polytope has diameter equal to a Bruhat-length difference refers to the **edge-count metric on its one-skeleton**, not the Euclidean vertex-chord metric used here. Gaetz determined structural properties of one-skeleton posets and simplicity; these do not specify the Euclidean chord counts here. Other published exact chord spectra on distinct families do not imply the present finite histogram without a demonstrated isometry or vertex-set reduction.

## Limitations

The result is a complete **finite**, realization-dependent invariant for the first three-bar midpoint refinement, not an all-parameter formula or a topological-persistence classification. Pairwise chord thresholds alone do not determine higher-dimensional Vietoris–Rips homology or any bottleneck distance between actual barcode diagrams. The novelty comparison is based on the inspected primary literature and indexed related claims; an unindexed earlier explicit computation cannot be categorically excluded.

## References

- E. Jaramillo-Rodriguez, *Barcode Posets: Combinatorial Properties and Connections*, arXiv:2206.05613, first public 2022-06-11; see especially Section 4.3 and its definition of \(P_{n,k}\). https://arxiv.org/abs/2206.05613
- E. Tsukerman and L. Williams, *Bruhat Interval Polytopes*, arXiv:1406.5202, first public 2014-06-19; see especially Section 4.4 for graph diameter rather than Euclidean diameter. https://arxiv.org/abs/1406.5202
- C. Gaetz, *One-skeleton posets of Bruhat interval polytopes*, arXiv:2208.13826, first public 2022-08-29. https://arxiv.org/abs/2208.13826
