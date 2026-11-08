# The \(J(6,3)\) neighborhood complex has a Moore summand and 141 three-spheres

## Finding

The ordinary Lovász *open-neighborhood complex* \(X=\mathcal N(J(6,3))\) of the middle-layer Johnson graph on six letters has exact integral homotopy type

\[
X\simeq M(\mathbb Z/2\mathbb Z,2)\vee\bigvee^{141}S^3,
\]

where \(M(\mathbb Z/2\mathbb Z,2)\) is the mapping cone of a degree-two map \(S^2\to S^2\). Hence

\[
\widetilde H_i(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z/2\mathbb Z&i=2,\\
\mathbb Z^{141}&i=3,\\
0&\text{otherwise}.
\end{cases}
\]

This is a genuine integral two-torsion phenomenon, invisible to rational homology alone. The complex is pure of dimension eight, but its entire homotopy type has a three-dimensional CW representative.

## Assumptions and scope

Let \(U=\{0,1,2,3,4,5\}\), and order the 20 elements of \(\binom{U}{3}\) lexicographically, using indices 0 through 19. The simple Johnson graph \(G=J(6,3)\) has vertices \(\binom{U}{3}\) and an edge between two distinct triples if their intersection has cardinality 2. It is 9-regular. The simplicial complex \(X\) has a face \(F\subseteq V(G)\) precisely if some graph vertex is adjacent to *every* member of \(F\). The empty face is included.

A dimension-\(q\) simplex is a \((q+1)\)-element subset of \(V(G)\). All integer chain groups are oriented in increasing order of the indices 0 through 19. The result concerns the entire finite complex \(X\), not a sampled subcomplex, rationalization, or quotient by graph automorphisms. No equivariant homotopy equivalence is asserted.

## Proof

**1. Exact faces.** Each vertex of \(G\) has nine neighbors. Taking all subsets of its neighborhood and deduplicating yields exactly \(8621\) faces including the empty face. Independently, a subset \(F\) is a face if and only if the intersection of the open-neighborhood masks of all members of \(F\) is nonempty. The latter criterion was tested on all \(2^{20}=1,048,576\) vertex subsets and agrees exactly. The face counts by cardinality \(0,1,\ldots,9\) are

\[
(1,20,180,960,2340,2520,1680,720,180,20).
\]

Every nine-element open neighborhood is a distinct facet; no face has more than nine vertices.

**2. A finite acyclic matching.** Encode each face by its 20-bit membership mask. Starting from all nonempty faces, process bit positions in the order

```text
10,18,16,14,0,17,11,2,3,9,5,7,4,19,6,15,8,1,13,12
```

At each position \(v\), pair every currently unmatched face not containing \(v\) with the face obtained by adjoining \(v\), provided that the larger face is also currently unmatched. Remove both members of each pair. This produces exactly \(4238\) disjoint face pairs, with remaining critical cells: one vertex, one two-simplex, and 142 three-simplices. The critical vertex has graph index 10 (triple \(\{1,2,3\}\)); the critical two-simplex has mask 458752, with vertices \(\{2,3,4\},\{2,3,5\},\{2,4,5\}\).

Orient every face-incidence relation *downward* from the larger simplex to its codimension-one face, except reverse the \(4238\) matched incidences. Exhaustive directed topological sorting on the resulting 8620-vertex, 41940-edge Hasse digraph visits every node and leaves no directed cycle. Thus this is an acyclic discrete-Morse matching, not merely a collection of disjoint pairs. The associated Morse CW complex has one cell in dimension 0, one in dimension 2, and 142 in dimension 3, and no other cells. In particular it is simply connected.

**3. Exact integral attaching degrees.** For an oriented simplex \([i_0,\ldots,i_q]\) with increasing graph-vertex indices, use the boundary \(\partial[i_0,\ldots,i_q]=\sum_{j=0}^q(-1)^j[i_0,\ldots,\widehat{i_j},\ldots,i_q]\). Assign a weight \(w(\tau)\in\mathbb Z\) to each two-simplex \(\tau\): set \(w=1\) on the unique critical two-simplex, set \(w=0\) on a two-simplex matched downward to an edge, and for a two-simplex \(\tau\) matched upward to a three-simplex \(\sigma\), enforce the exact equation

\[
\sum_{\eta\subset\sigma,\,|\eta|=3}[\eta:\sigma]w(\eta)=0,
\]

solving for \(w(\tau)\), where \([\eta:\sigma]=\pm1\) is the signed simplicial incidence coefficient. Acyclicity makes this recursion terminating and unambiguous. Under elementary integral cellular cancellation the coefficient of a critical three-simplex \(\sigma\) on the single critical two-cell is \(\sum_{\eta\subset\sigma,\,|\eta|=3}[\eta:\sigma]w(\eta)\). Evaluating all 142 coefficients gives exactly 95 zeros, 30 copies of \(+2\), and 17 copies of \(-2\). In particular the integral differential

\[
\partial^{\mathrm{Morse}}_3:\mathbb Z^{142}\longrightarrow\mathbb Z
\]

has image exactly \(2\mathbb Z\). For an explicit nonzero witness, the critical three-simplex with bitmask 8707, whose graph vertices are \(\{0,1,2\},\{0,1,3\},\{0,4,5\},\{1,3,4\}\), has coefficient \(+2\). Every displayed coefficient is checked by the supplied exact integer verifier.

**4. Homotopy classification.** The Morse two-skeleton is \(S^2\) (one vertex, no edges, one two-cell). The attaching maps of the 142 three-cells therefore represent integers in \(\pi_2(S^2)\cong\mathbb Z\), and these integers are the signed degrees computed above. Integral unimodular changes of basis among these 142 attaching spheres convert the degree row to \((2,0,\ldots,0)\), since its greatest common divisor is 2. Such a change is realized by a self-homotopy equivalence of the wedge of 142 two-spheres in the attaching domain and preserves the mapping cone up to homotopy. The resulting CW complex is the degree-two Moore space \(M(\mathbb Z/2\mathbb Z,2)\) wedged with 141 three-spheres. This proves the *integral homotopy equivalence*, not just a calculation over a field.

## Verification

Run the included `verify.py` with Python 3.9 or later. It uses only the Python standard library and requires no external data. It recomputes all faces using two different criteria, verifies the 4238 pair matching and all 41940 oriented face incidences, checks the entire directed Hasse graph for acyclicity, performs the signed integer recursive reduction, checks the gcd of all 142 Morse attaching degrees, and independently computes the full chain-boundary ranks over \(\mathbb F_2\) on the original unreduced simplices. The direct mod-two ranks of \(\partial_1,\ldots,\partial_8\) are

\[
(19,161,798,1400,1120,560,160,20).
\]

These imply mod-two reduced Betti numbers 1 in degree 2 and 142 in degree 3, agreeing with the universal-coefficient theorem applied to the integral result. The recorded full verifier output is included as `verification_output.txt`.

## Relationship to prior work

Lovász's neighborhood complex is a classical graph-homomorphism invariant. Shukla's paper [1], first posted February 13, 2018, analyzes neighborhood complexes of graphs with maximum degree at most three and of four-regular circulant graphs; neither family contains the nine-regular graph \(J(6,3)\). Hujdurović and Mitrović [2], published online August 7, 2023, identify \(J(6,3)\) as a special nontrivially unstable Johnson graph, but their Section 3.8 classifies graph-double-cover automorphisms rather than the neighborhood complex or its homotopy type.

A published research record [3] classifies the *scale-one Vietoris–Rips (clique)* complexes of all Johnson graphs, in particular \(J(6,3)\). That theorem does not imply the present result: the clique complex and open-neighborhood complex have distinct face rules, and in this case the former is a sphere wedge while the latter has integral two-torsion. The standard \(\operatorname{Hom}(K_2,G)\) formulation shares a homotopy type with \(\mathcal N(G)\), but the inspected sources do not compute it for this specific graph. No known-table entry is used as evidence of the new homotopy type. The named database/literature searches did not locate an equivalent calculation; this negative search is not a general proof of novelty.

## Limitations

This determines one natural, finite, highly symmetric Johnson graph. It does not classify all \(J(n,k)\), give the action of the full automorphism group on the free summand, identify torsion generators by short geometric cycles, or establish an equivariant splitting. Possible unindexed results or inaccessible complete manuscripts remain a residual bibliographic risk. The acyclic matching and attaching-degree claim are finite exact computations, not an induction or an asymptotic assertion.

## References

[1] S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526 (first posted 2018-02-13); *Electronic Journal of Combinatorics* 26 (2019), P2.4.

[2] A. Hujdurović and Đ. Mitrović, *Some conditions implying stability of graphs*, *Journal of Graph Theory* 105 (2024), 98–109, DOI: 10.1002/jgt.23018 (first online 2023-08-07); Section 3, Definition 3.7 and Theorem 3.8.

[3] *Sphere-wedge collapse of scale-one Johnson-graph Rips complexes*, published-finding corpus published research record 2026/10/11/SCOPE-sphere-wedge-collapse-of-scale-one-johnson-graph-rips-complexes--c10287ed1518; statement accessed via indexed abstract. This work concerns a different simplicial construction.
