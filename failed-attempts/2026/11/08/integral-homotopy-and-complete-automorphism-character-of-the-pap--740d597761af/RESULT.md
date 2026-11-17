# Integral homotopy and complete automorphism character of the Pappus induced-forest complex

## Finding
Let \(P\) be the eighteen-vertex cubic Pappus incidence graph and let \(\mathcal F(P)\) consist of all subsets of its vertices inducing forests. The complete integral homotopy type is
\[
\boxed{\mathcal F(P)\simeq\bigvee^{40}S^{10}.}
\]
The full graph automorphism group \(G=\operatorname{Aut}(P)\), of order \(216\), acts on the unique nonzero reduced rational homology group, and its **entire character** is the following formula. If \(\mathcal C(g)\) denotes the set of vertex cycles of \(g\), then for every \(g\in G\),
\[
\boxed{\chi(g)=\sum_{J\subseteq\mathcal C(g)}(-1)^{|J|-1}\mathbf 1\!\left\{P\!\left[\bigcup_{O\in J} O\right]\text{ is a forest}\right\}.}
\]
The contribution from the empty collection is \(-1\). In particular,
\[
\dim_{\mathbb Q}\widetilde H_{10}(\mathcal F(P);\mathbb Q)^G=1,
\qquad \langle\chi,\chi\rangle_G=10.
\]
All other reduced integral homology groups vanish. The full thirteen-class table, with exact representatives, is produced by the accompanying executable certificate. Two distinct order-three classes, each acting on graph vertices as six three-cycles, have character values \(1\) and \(4\); thus the graph-vertex cycle type does not determine the homology character.

## Assumptions and scope
The Pappus graph is the eighteen-vertex Levi graph of the Pappus configuration, **not** the unrelated nine-vertex graph sometimes called by that name. Label its vertices \(0,1,\ldots,17\). Include the cycle edges \(\{i,i+1\pmod {18}\}\) and the LCF chord edges \(\{i,i+s_i\pmod {18}\}\), where \((s_i)_{i=0}^{17}\) is the six-term sequence `[5,7,-7,7,-7,-5]` repeated three times. These prescriptions give twenty-seven distinct edges and degree three at every vertex. Faces are precisely masks \(F\subseteq\{0,\ldots,17\}\) for which \(P[F]\) contains no cycle, together with the empty face. Ordinary (unreduced) geometric realization and integral homotopy are used. The action on faces is induced by all graph automorphisms; the representation is over \(\mathbb Q\) unless an integral coefficient group is written explicitly.

## Proof
**1. Exhaustive definition of the finite complex.** Enumerate all \(2^{18}\) vertex masks. On each induced subgraph, insert its edges into a disjoint-set structure. A repeated union of vertices already connected is equivalent to a cycle, so this enumerates *all* induced forests, not merely a sample. An independent component-count implementation verifies the criterion \(|E(P[F])|=|F|-c(P[F])\) for every mask. The complex contains \(204{,}492\) faces including the empty face, with the following numbers of nonempty simplices in dimensions \(0\) through \(12\):

`[18, 153, 816, 3060, 8568, 18546, 31608, 42516, 44228, 33660, 16776, 4290, 252]`.

**2. A fully specified discrete-Morse matching.** Process vertices in the exact toggle order

`[17,11,13,7,3,0,9,16,5,12,10,14,8,6,4,2,15,1]`.

At each stage, pair every still-unpaired forest face missing that vertex with its one-vertex extension, when both are still unpaired. Remove paired faces from later stages. The empty face is provisionally included in this *augmented* matching. This produces \(102{,}223\) pairs and leaves exactly forty-three dimension-ten faces and three dimension-eleven faces. The empty face is paired with one vertex; omitting this single augmented pair when passing to the ordinary nonempty face poset leaves that vertex as the sole critical zero-cell. Removing the empty face cannot introduce a directed cycle.

To verify acyclicity, orient every face-poset covering relation downwards, reversing precisely the selected matching relations. There are exactly \(1{,}704{,}456\) such relations. The topological-sort algorithm implemented in `pappus_forest_certificate.py` visits all \(204{,}492\) augmented face-poset vertices. This proves, by finite exhaustion, that the matching is acyclic. Discrete-Morse theory thus gives a CW model consisting of a point, forty-three ten-cells and three eleven-cells, with no cells in intermediate dimensions.

**3. Signed integral attaching maps.** Orient each simplex using increasing vertex labels. For every ten-face \(f\) paired upward with an eleven-face \(u\), eliminate \(f\) via the relation \(\partial u=0\), with the incidence coefficient \(\pm1\) of \(f\) inverted. Descend recursively along the other ten-faces in \(\partial u\). Critical ten-faces remain basis vectors; ten-faces paired downward with nine-faces contribute zero. Acyclicity guarantees termination. This yields the integer boundary matrix from three critical eleven-cells to forty-three critical ten-cells, with rows listed by increasing upper-face bit masks and columns by increasing lower-face bit masks. Its *nonzero* entries, indexed from zero, are:

```
row 0: {6:-1, 26:-1, 27:1, 31:-1, 33:-1, 34:1, 35:1}
row 1: {9:1, 10:1, 35:-1, 36:-1}
row 2: {11:1, 13:-1, 39:1, 40:-1}
```

All remaining entries vanish. Columns \(6,9,11\) form a diagonal minor \(\operatorname{diag}(-1,1,1)\), of determinant \(-1\). The boundary image is therefore primitive of rank three, and there is no integral homology torsion. More strongly, because \(\pi_{10}(\bigvee^{43}S^{10})\cong\mathbb Z^{43}\), every eleven-cell attaching map is determined up to homotopy by its integral degree vector. A unimodular basis change of the ten-sphere wedge identifies the three attachment vectors with three coordinate generators. Their cofibers cancel three ten-sphere factors, leaving exactly \(40\) copies of \(S^{10}\). This proves the *homotopy equivalence*, not just Betti ranks.

**4. Automorphism character.** Enumerate adjacency-preserving permutations by exhaustive backtracking, testing both edges and nonedges. Exactly \(216\) permutations occur; conjugating them partitions the group into thirteen classes. An invariant vertex subset is a union of permutation cycles of \(g\). On the oriented simplicial chain corresponding to such a subset \(F\), \(g\) acts by the sign \((-1)^{|F|-|J|}\) when \(J\) is its collection of included cycles. Multiplying by the reduced Lefschetz degree sign \((-1)^{|F|-1}\) gives \((-1)^{|J|-1}\). The augmented empty face contributes \(-1\). The integral homotopy theorem shows that reduced homology is supported only in even degree ten, so this Lefschetz sum **equals the degree-ten homology trace**. The certificate evaluates it for every element of all thirteen classes and independently recomputes signed simplex traces on class representatives. The identity trace is \(40\); class-weighted character sums give invariant dimension \(1\) and inner product \(10\). The two six-three-cycle order-three classes have traces \(1\) and \(4\).

## Verification
Run `python3 pappus_forest_certificate.py` using only the Python standard library, preferably Python 3.9 or later. The program reconstructs the Pappus graph, checks every vertex subset by two graph-acyclicity criteria, constructs the complete matching, checks *all* directed Hasse relations by topological sorting, expands the signed Morse boundary and verifies a unit minor, independently enumerates all graph automorphisms and conjugacy classes, and computes full and directly signed Lefschetz character values. Its output is saved as `pappus_forest_certificate.txt`; the final line must be `PAPPUS_FOREST_CERTIFICATE_PASS`. A second toggle order is independently evaluated in `pappus_crosscheck.py`; its Morse boundary has four independent mod-two rows, corroborating degree-ten Betti rank forty. The proof depends on finite exhaustive checks at specified finite bounds and the standard discrete-Morse and attaching-map theorems; it makes no infinite-family inference from finite experiments.

## Relationship to prior work
Taylan's 2015 paper establishes the general notion of devoid complexes and provides matching-tree reductions for other graph families, but contains no Pappus induced-forest classification. Carnero Bravo's *The Forest Filtration of a Graph* (initial arXiv version 2023) studies the **same** induced-acyclic vertex complex in general and gives results for paths, cycles, double stars, cactus graphs, joins, selected products and complete multipartite graphs. Its inspected introductory scope and Sections 4.1–4.2 do not classify the Pappus graph. In particular, the Pappus graph is not a cactus graph or a complete multipartite graph, nor one of the specially treated graph products. The ordinary Pappus matching complex has a separately published integral homotopy classification as a wedge of forty five-spheres. It is a complex on *sets of disjoint edges*, not on vertex sets inducing forests, and does not imply the present ten-dimensional homotopy type or vertex-automorphism character. Previous Pappus independence-complex calculations likewise concern vertex sets inducing no edges, a proper subcomplex of the present forest complex. The new theorem is an exact fixed-graph topological and equivariant classification; bibliographic priority beyond the inspected material is not certified by a failed search.

## Limitations
The theorem treats only the specified eighteen-vertex Pappus graph. It does not classify the induced-forest complexes of all cubic symmetric graphs or determine an equivariant homotopy decomposition or integral irreducible representation decomposition. The character is rational, though the homotopy equivalence is integral. The executable finite certificate must be inspected and run for computational confidence; no independent external scientific audit is asserted. An equivalent result could occur in unindexed or inaccessible literature.

## References
1. Demet Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1, first publicly available 2015-01-27, Sections 2–5. https://arxiv.org/abs/1501.06754
2. Andrés Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first publicly available 2023-07-25; version 3 text inspected, especially Sections 1 and 4. https://arxiv.org/abs/2307.13271
3. Eric W. Weisstein, *Pappus Graph*, MathWorld, for the LCF graph identification. https://mathworld.wolfram.com/PappusGraph.html
4. *Integral homotopy type of the Pappus graph matching complex*, publicly indexed mathematical record, 2026; matching-complex definition and proof inspected, different ground set and face criterion. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-integral-homotopy-type-of-the-pappus-graph-matching-complex--db6c6c11f317
