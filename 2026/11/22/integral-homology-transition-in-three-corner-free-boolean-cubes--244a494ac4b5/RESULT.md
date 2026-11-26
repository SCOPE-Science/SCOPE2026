# Integral homology of the two-independence complex of the five-cube

## Finding

Let \(Q_5\) be the graph on \(\{0,1\}^5\) in which two vertices are adjacent when they differ in one coordinate. Let \(L_5\) be the simplicial complex of sets meeting each coordinate square in at most two vertices. This is the two-independence complex \(\operatorname{Ind}_2(Q_5)\). Its complete reduced integral homology is
\[
\widetilde H_j(L_5;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{681},&j=7,\\
0,&j\ne7.
\end{cases}
\]
In particular, it has no integral torsion. This computes the next dimension after the known mixed-dimensional case \(\operatorname{Ind}_2(Q_4)\simeq \bigvee^{16}S^3\vee S^4\) and shows that mixed-degree homology does not persist at dimension five.

## Assumptions and scope

A coordinate square is obtained by varying two coordinates and fixing the remaining three. Every three vertices of a coordinate square form a path of length two in \(Q_5\). Conversely, the two edges of any path of length two flip distinct coordinates, so its triple lies in a coordinate square. A subset avoids such triples if and only if its induced graph has maximum degree at most one, or equivalently each induced connected component has at most two vertices. Thus the identification with \(\operatorname{Ind}_2(Q_5)\) is equality on the given vertex set. We include the empty face in the augmented chain complex.

## Proof

Use the unsigned binary integers from \(0\) to \(31\) as vertex labels and sort face vertices by this order to orient them. Generate each face recursively in ascending vertex order by adding a vertex only when no forbidden triple is completed with two earlier selected vertices. A triple is forbidden exactly when it is one of the four triples of a coordinate square; it determines that square uniquely. Enumeration gives the following counts in cardinalities \(0,1,\ldots,16\), and no larger faces:
\[
(1,32,496,4640,28520,118656,337200,650784,841860,719040,404064,149952,38064,7680,1440,192,12).
\]

On the augmented face poset, go through the vertices in label order. At vertex \(v\), match each still-unmatched face not containing \(v\) with its still-unmatched coface formed by adding \(v\), whenever it exists. These pairs are disjoint within each stage because the toggle is an involution. Orient matched incidences upward and other incidences downward. A directed cycle would have to alternate up and down: upward edges cannot occur consecutively, and their number equals the number of downward edges. At the least toggle stage \(v\) occurring on such a cycle, an upward edge adds \(v\), so some downward edge must delete it. Both endpoints of that downward edge were still unmatched at the start of stage \(v\) (each is matched by an upward edge of the cycle at stage \(v\) or later). Thus this edge would have been matched at stage \(v\), contrary to its orientation. The matching is acyclic.

The resulting signed integral Morse complex has chain ranks
\[
\begin{array}{c|rrrrrrr}
 j&5&6&7&8&9&10&11\\\hline
 \operatorname{rank}C_j&1&16&757&73&12&1&1
\end{array}
\]
and no other generators. To compute the Morse differential, for a lower matched face \(\tau\) with upper partner \(\sigma\), use the relation in the signed boundary of \(\sigma\) to replace its \(\tau\)-term using
\[
[\tau]=-\epsilon(\tau,\sigma)\sum_{\substack{\rho\text{ a facet of }\sigma\\\rho\ne\tau}}\epsilon(\rho,\sigma)[\rho],
\]
where \(\epsilon\) is the usual simplicial incidence sign. Acyclicity ensures the expansions terminate. The resulting matrices are the signed gradient-path differential, i.e. the differential after eliminating the matched unit pairs in the augmented integer chain complex.

The computed differential ranks are \(\operatorname{rank}d_6=1\), \(\operatorname{rank}d_7=15\), \(\operatorname{rank}d_8=61\), \(\operatorname{rank}d_9=12\), and \(\operatorname{rank}d_{11}=1\); all other ranks are zero. Consecutive boundary compositions vanish exactly. Reducing each boundary by unimodular integer row and column operations at unit pivots leaves a zero residual matrix. Therefore every nonzero Smith invariant is one. The cokernel of \(d_{j+1}\) has the same torsion as homology in degree \(j\), since their quotient is the free image of \(d_j\). There is thus no torsion, and subtracting adjacent ranks from the chain ranks gives \(757-15-61=681\) in degree seven and zero in all other degrees.

## Verification

Run the accompanying `python3 verify.py` with `corner_morse.cpp` in the same directory and a C++17 `g++` compiler available. It compiles the face and signed Morse boundary generator, checks consecutive boundary compositions, and performs integral unit Smith reduction, requiring zero residual matrices. The \(n=5\) run enumerates 3,302,633 faces including the empty face and computes the two adjacent boundaries of sizes \(757\times73\) and \(16\times757\). The lower-dimensional cases in the checker are consistency tests, not part of the new finding.

## Relationship to prior work

This is the higher-independence complex of Deshpande and Singh at \(r=2\), not a new cubical simplicial functor. Their cycle formulas include \(Q_2=C_4\); their rectangular grid treatment does not supply the five-cube calculation. The Resultary record *The first mixed-dimensional two-independence homotopy in the cubical sequence* already gives the stronger homotopy results for dimensions one through four. Those results motivate checking the next member and are not claimed here. Conant and Thistlethwaite use hyperedges consisting of all four vertices of a square in their cubical square-face construction, unlike the three-corner hyperedges here. The cube hypergraph of Cooley, Machata and Pasch has ternary vertices and coordinate-line hyperedges, also different.

## Limitations

The result gives integral homology, not a homotopy or equivariant classification of \(L_5\). It makes no prediction for \(n\ge6\). The priority comparison is bounded; a possible older source, Salvetti's *Some Combinatorial Constructions and Relations with Artin Groups* (DOI 10.1007/978-3-319-20155-9_22), was not available for full-text comparison.

## References

- P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, https://arxiv.org/abs/2001.05448.
- *The first mixed-dimensional two-independence homotopy in the cubical sequence*, Resultary record [8cb5673474da](https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-the-first-mixed-dimensional-two-independence-homotopy-in-the-cub--8cb5673474da).
- J. Conant and P. Thistlethwaite, *Boolean Formulae, Hypergraphs and Combinatorial Topology*, https://arxiv.org/abs/0808.0739.
- O. Cooley, J. H. M. Machata, and M. Pasch, *Independent sets in hypercubes*, https://arxiv.org/abs/2406.00401.
