# An exact relative collapse for the Grötzsch two-independence complex

## Finding
Let \(G=\mu(C_5)\) be the eleven-vertex Grötzsch graph, and let \(\operatorname{Ind}(G)\) denote its ordinary independence complex. The two-independence complex \(\operatorname{Ind}_2(G)\) consists of vertex subsets whose induced subgraph has connected components of size at most two. There is an explicit sequence of **105 elementary simplicial collapses**, all relative to \(\operatorname{Ind}(G)\), taking \(\operatorname{Ind}_2(G)\) **exactly onto** \(\operatorname{Ind}(G)\). Consequently, the natural inclusion is a simple-homotopy equivalence, and
\[
\operatorname{Ind}(G)\simeq \operatorname{Ind}_2(G)\simeq S^2.
\]
The stronger conclusion is about the natural inclusion and its relative collapse, not merely an agreement of Betti numbers or abstract homotopy types.

## Assumptions and scope
The graph is finite, simple, and undirected. Label its vertices \(v_i\), \(u_i\) for \(i\in\mathbb Z/5\mathbb Z\), and \(w\). Its twenty edges are
\[
\{v_i,v_{i+1}\},\qquad \{u_i,v_{i+1}\},\qquad\{u_i,v_{i-1}\},\qquad \{w,u_i\}
\]
for all five values of \(i\), with subscripts interpreted modulo five. For the machine-checkable certificate use integer vertex labels \(v_i=i\), \(u_i=5+i\), and \(w=10\), and represent a nonempty subset by the bitmask \(\sum_{j\in S}2^j\).

Write \(K=\operatorname{Ind}(G)\) and \(L=\operatorname{Ind}_2(G)\). A nonempty vertex subset belongs to \(K\) if its induced vertex degrees are all zero, and to \(L\) if its induced vertex degrees are all at most one. This latter condition is equivalent, for a simple graph, to every induced connected component having size at most two. Both complexes include the empty simplex in the conventional abstract-complex sense; the certificate enumerates only their nonempty simplices.

## Proof
**Exact finite face universes.** Exhaustive enumeration of the \(2^{11}-1\) nonempty vertex subsets gives \(102\) simplices of \(K\), with dimension-wise face counts \((11,35,40,15,1)\), and \(312\) simplices of \(L\), with dimension-wise counts \((11,55,110,95,36,5)\). Every face condition is evaluated directly from the twenty displayed graph edges.

**Relative collapse.** The file `verification/relative_collapse_pairs.json` lists, in order, \(105\) pairs of integer masks \((\sigma,\tau)\). At every step, \(\sigma\subset\tau\), \(\tau\) is obtained by adding exactly one vertex, and \(\tau\) is the *only strict coface* of \(\sigma\) remaining in the current complex. Hence the deletion of \(\sigma\) and \(\tau\) is an elementary simplicial collapse. Neither face belongs to \(K\). The supplied program `verification/verify_relative_collapse.py` reconstructs both complexes from the edge definition, verifies every unique-coface claim against the **entire current face set**, checks downward closure after every deletion, and confirms that the \(210\) removed simplices are precisely \(L\setminus K\). Thus the sequence collapses \(L\) onto \(K\), fixing \(K\) pointwise.

**Identification of the remaining homotopy type.** Independently, `verification/verify_sphere.py` constructs an acyclic discrete-Morse matching on \(K\). In the integer labels above, successively toggle available pairs along vertex order \((1,4,5,2,0,6,8,7,9,10,3)\). Exactly \(50\) pairs are formed; the only unmatched nonempty simplices are bitmask \(2\), a vertex, and bitmask \(1033\), a triangle. Reverse matched edges in the complete face-poset Hasse graph and orient all other covering relations downward. The supplied program topologically sorts all \(102\) face nodes and all \(255\) covering relations, proving this matching is acyclic. Discrete Morse theory therefore gives a CW model with precisely one zero-cell and one two-cell. Its unique two-cell must attach to the single point, so its homotopy type is \(S^2\). Composing with the relative elementary collapse proves the assertions.

## Verification
Run both standard-library Python scripts from a directory containing the `verification` subdirectory:

```
python verification/verify_relative_collapse.py
python verification/verify_sphere.py
```

The JSON pair certificate and both scripts are included in this package, as are captured outputs. The first checks all \(105\) actual free-face deletions; the second checks all \(255\) ordinary-complex covering relations and separately computes mod-two simplicial boundary ranks on both full complexes. The mod-two homology calculation is a cross-check only: it is the explicit collapse and acyclic Morse matching that prove the integral homotopy and inclusion statements.

## Relationship to prior work
The higher-independence framework of Deshpande and Singh treats a range of graph families and reports torsion for a *different*, generalized Mycielskian, \(\operatorname{Ind}_2(M_4(C_4))\), in its concluding section. That example neither entails nor contradicts the present exact relative-collapse statement for \(\mu(C_5)\). Sawant's recent results concern higher independence complexes of trees, whereas the Grötzsch graph contains cycles. Earlier results about the ordinary independence complexes of Mycielski graphs, including suspension formulas, can determine the homotopy type of \(K\) but do not establish that the natural larger complex \(L\) collapses *onto* \(K\). The ordinary edge-matching complex of the Grötzsch graph and its graph-metric Čech nerve are different simplicial constructions.

## Limitations
This is a theorem for the explicitly defined eleven-vertex Grötzsch graph, not for all Mycielskians. The finite exhaustive certificates establish their stated full face-universe properties, not an unverified infinite-family extension. The relative collapse need not preserve the graph-automorphism group at each individual step; no equivariant collapse or representation statement is asserted. No independent external scientific audit has been performed. Bibliographic search cannot exclude all unindexed overlapping work.

## References
1. Rutuja Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150, version 1 publicly posted 2026-05-24. https://arxiv.org/abs/2605.25150
2. Priyavrat Deshpande and Anurag Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448; especially Section 6.1 on generalized Mycielskians. https://arxiv.org/abs/2001.05448
3. S. Ghosh and S. Selvaraja, *Shellability of Higher Independence Complexes of Graphs*, arXiv:2505.06614. https://arxiv.org/abs/2505.06614
4. S. Deshpande, A. Roy, A. Singh, and A. Van Tuyl, *Fröberg's theorem, vertex splittability and higher independence complexes*, arXiv:2311.02430. https://arxiv.org/abs/2311.02430
