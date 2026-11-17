# The first cuboctahedral forest-filtration jump: thirty-two three-spheres and a thirty-six-sphere cofiber

## Finding
Let \(Q_3\) be the graph on binary triples whose edges connect words differing in one coordinate, and put \(C=L(Q_3)\), its cuboctahedral line graph. The first forest-filtration transition is
\[
\mathcal F_0(C)\simeq\bigvee^{4} S^2,\qquad
\mathcal F_1(C)\simeq\bigvee^{32} S^3,
\qquad
\mathcal F_1(C)/\mathcal F_0(C)\simeq\bigvee^{36} S^3.
\]
The inclusion \(\mathcal F_0(C)\hookrightarrow\mathcal F_1(C)\) is null-homotopic. The level-zero equivalence is a reproducibly checked baseline, not claimed new; the first positive stage and the precise transition/cofiber are the finding.

## Assumptions and scope
All graphs are finite and simple, spaces are geometric realizations of abstract simplicial complexes, and all homotopy equivalences are ordinary (nonequivariant). For \(d=0,1\), a simplex of \(\mathcal F_d(C)\) is a subset \(U\subseteq V(C)\) inducing a forest whose degrees are at most \(d\). Thus \(\mathcal F_0(C)=\operatorname{Ind}(C)\), and \(\mathcal F_1(C)=\operatorname{Ind}_2(C)\), since all induced components must then have at most two vertices. Exactly 12 cuboctahedral graph vertices correspond to the 12 cube edges.

The cube vertices are integers from 0 through 7 interpreted as three-bit words. Its undirected edges are all sorted pairs \((u,u\mathbin{\mathrm{xor}}2^j)\), with \(j\in\{0,1,2\}\) and the first endpoint smaller. The cuboctahedral vertices are indexed by these edges in lexicographic order, and two are adjacent precisely if the corresponding cube edges share an endpoint. This defines the graph and the bit-mask model without auxiliary data.

## Proof
**1. Complete face census.** For each of the \(2^{12}=4096\) masks, one predicate checks that every selected vertex of \(C\) has at most \(d\) selected neighbors; an independent graph traversal checks that every induced connected component has at most \(d+1\) vertices. For \(d=0,1\) the predicates agree identically. The two complexes have, including the empty face, 108 and 456 faces respectively. The nonempty face vectors are
\[
(f_0,f_1,f_2,f_3)(\mathcal F_0)=(12,42,44,9),
\]
\[
(f_0,f_1,f_2,f_3,f_4)(\mathcal F_1)=(12,66,164,177,36).
\]
The first has eight 2-dimensional and nine 3-dimensional facets; the second has forty-five 3-dimensional and thirty-six 4-dimensional facets.

**2. Complete discrete-Morse matchings.** At each pivot in a prescribed permutation of the twelve indexed vertices, pair every currently unmatched face not containing that pivot with its one-vertex extension if both faces remain unmatched; each face is used at most once. The included standard-library verifier generates this pairing on the augmented face poset and checks the full directed Hasse graph for acyclicity by topological sorting. For \(\mathcal F_0\), either increasing or decreasing pivot order produces 52 matched pairs and exactly four remaining augmented critical faces, all of dimension 2. For \(\mathcal F_1\), pivot orders
\[
(5,2,9,1,8,3,10,7,0,11,4,6)
\quad\text{and}\quad
(9,0,7,4,8,10,1,11,2,3,5,6)
\]
both produce 212 matched pairs and precisely 32 remaining augmented critical faces, all of dimension 3. The checker tests every one of the respective 264 and 1524 Hasse incidences for an acyclic orientation (matched covers upward, other covers downward). In both complexes the empty simplex is paired with one vertex. Removing that pair and the empty face from the ordinary face poset leaves exactly one critical vertex and, respectively, four critical 2-cells or thirty-two critical 3-cells; the ordinary matching is separately verified acyclic.

The discrete-Morse CW theorem therefore gives a CW complex with one 0-cell and all other cells in a single positive dimension. Every such attaching map lands in a point, so the resulting CW complex is a wedge of 4 two-spheres or 32 three-spheres as asserted. No integral boundary or torsion issue remains: the homotopy decomposition already establishes all integral homology.

**3. The filtration transition.** The first stage is a subcomplex inclusion and hence a cofibration. Since the target has homotopy type \(\bigvee^{32} S^3\), it is 2-connected. Since the source is homotopy equivalent to \(\bigvee^{4}S^2\), every map from it to the target, in particular the natural inclusion, is null-homotopic. The cofiber of a null-homotopic cofibration is homotopy equivalent to the wedge of the target and the suspension of the source, yielding \(\bigvee^{32+4}S^3\). This proves the cofiber statement.

## Verification
Run `python3 verify.py` using Python 3.9 or newer without any nonstandard modules. The script recomputes all \(4096\) candidate masks at both levels; compares two different face-membership implementations; constructs and tests four matchings; enumerates facets; and independently computes boundary ranks over \(\mathbb F_2\) from unreduced simplicial chain groups. The latter yields reduced Betti numbers 4 in degree 2 for the baseline, 32 in degree 3 for the first stage, and 36 in degree 3 for the quotient chain complex, with zero in all other degrees. The complete generated log is `verification_output.txt`. These modular checks are corroboration; the integral homotopy proof rests on the acyclic Morse matchings and the cofiber argument, not on field ranks.

## Relationship to prior work
Deshpande and Singh (first public submission 15 January 2020) define higher-independence complexes and calculate homotopy types for complete multipartite, fully whiskered, path, cycle and perfect-ary-tree families. Their result does not directly calculate \(\operatorname{Ind}_2(L(Q_3))\). Carnero Bravo (first public submission 25 July 2023) identifies \(\mathcal F_1\) with \(\operatorname{Ind}_2\) and studies paths, cycles, double stars, cactus graphs, joins and specified graph products; the inspected results do not give this line-graph case.

A previously published cube matching-complex calculation gives the baseline \(\mathcal F_0(L(Q_3))=\mathcal M(Q_3)\simeq\bigvee^{4}S^2\). It does **not** determine the distinct complex \(\mathcal F_1(L(Q_3))\), with its additional 348 faces and new degree-3 homotopy. The cuboctahedral *matching complex* \(\mathcal M(L(Q_3))\) has 24 vertices (graph edges), not these 12, so its published 57-sphere calculation cannot be substituted. Cuboctahedral cut, metric nerve and configuration-space complexes are likewise different constructions. No inspected primary result or searchable published mathematical record was found to imply the new first-stage/cofiber theorem; a search is not a proof of global novelty.

## Limitations
The result concerns one canonical 12-vertex graph and the first two levels only. It does not classify forest filtrations of arbitrary line graphs or higher-dimensional hypercubes, does not assert equivariant decompositions, and does not determine every later level. The originality comparison was limited to material that was accessible and inspected; some relevant public records were available only as summaries, and unindexed equivalent calculations remain possible. Independent external validation has not been performed.

## References
1. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448, initially public 15 January 2020. https://arxiv.org/abs/2001.05448
2. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, initially public 25 July 2023. https://arxiv.org/abs/2307.13271
3. *The cube matching complex is a wedge of four 2-spheres*, published mathematical research record, (published 11 October 2026; record identifier and access caveat in AUDIT.json).
4. *The cuboctahedral matching complex is a wedge of 57 three-spheres*, published mathematical research record, (published 11 October 2026; record identifier and access caveat in AUDIT.json).
