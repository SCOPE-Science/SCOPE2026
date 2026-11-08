# Seventy-eight five-spheres in the first asymmetric triple-product forest complex

## Finding
Let \(G=K_2\times K_3\times K_4\) be the categorical graph product, and let \(\mathcal F_1(G)\) be the simplicial complex of vertex subsets inducing subgraphs of maximum degree at most one. Then the complete integral homotopy type is
\[
\mathcal F_1(K_2\times K_3\times K_4)\simeq\bigvee^{78}S^5.
\]
In particular, \(\widetilde H_5(\mathcal F_1(G);\mathbb Z)\cong\mathbb Z^{78}\), and every other reduced integral homology group vanishes. This is the first asymmetric member \((3,4)\) beyond the two-equal-factor subfamily of the explicit triple-product forest-filtration question in [1].

## Assumptions and scope
The vertex set is \(V(G)=\{(a,b,c):0\le a<2,\ 0\le b<3,\ 0\le c<4\}\), with distinct vertices adjacent if and only if all three coordinates differ. Coordinates are ordered lexicographically, and vertices are indexed from \(0\) to \(23\). This graph has \(24\) vertices, degree \(6\) at each vertex and \(72\) edges. The simplicial complex includes the empty face, but its ordinary (nonaugmented) face poset excludes that face when constructing discrete-Morse matchings.

Because an induced subgraph of maximum degree at most one is a disjoint union of isolated vertices and edges, its acyclicity is automatic. Thus this is exactly the first forest-filtration complex and also the induced-degree-one (dissociation) complex. No assumption is made about other categorical-product parameters or higher filtration levels.

## Proof
**Exact face set.** Represent a vertex subset by a \(24\)-bit integer mask. A mask is a face precisely when every selected vertex has at most one selected neighbor. Independently, it is a face precisely when it avoids every centered path on three vertices, viewed simply as a forbidden triple: a chosen center together with two of its neighbors. The latter construction yields \(360\) distinct forbidden triples. The two independent generation procedures in `verify_product.py` produce identical face sets: \(34{,}910\) faces including the empty face. The dimensions and counts are recorded in `verification_output.json`. The maximal faces have dimensions \(5,6,7,11\), with respective counts \(52,504,435,2\).

**An explicit matching.** Begin with all nonempty faces unmatched. For \(v=0,1,\ldots,23\), pair every still-unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) when that face is also still unmatched. Since an individual pair has a unique lower face with respect to the pivot vertex, this prescription is independent of iteration order within each stage. The reconstructed matching has \(17{,}415\) pairs and leaves exactly one unmatched vertex and \(78\) unmatched five-dimensional simplices, with no other unmatched faces.

**Acyclicity and homotopy.** To certify that the matching is a discrete-Morse matching, orient every incidence of a nonempty simplex with a codimension-one face downward, except matched incidences, which are oriented upward. The certificate generator constructs **all** \(191{,}232\) such incidences and uses a complete topological-sort test of the directed Hasse graph. The sort visits all \(34{,}909\) nonempty faces, so the directed graph has no cycle. This is a finite exhaustive verification, not an inference from a numerical homology experiment. By discrete Morse theory, the realization has a CW model consisting of one zero-cell and \(78\) cells of dimension five, and no other cells. All five-cell attaching maps land in a point, proving the displayed wedge equivalence.

## Verification
Running `python3 verify_product.py` with Python's standard library regenerates the graph, both exact face enumerations, three complete matchings and their directed Hasse-graph acyclicity checks. The reverse-vertex-order matching independently leaves the same critical-cell dimensions and counts. A third, mixed-order matching leaves one zero-cell, nine four-cells, \(95\) five-cells and eight six-cells; its mod-two Morse boundary ranks are \(9\) in degree five and \(8\) in degree six, reproducing fifth Betti number \(95-9-8=78\) independently of the two wedge certificates. The complete deterministic output, including matching digests, is `verification_output.json`. The Euler characteristic check agrees with the wedge claim.

## Relationship to prior work
Carnero Bravo [1], first made public July 25, 2023, defines these complexes and asks in Question 44 for the homotopy types of \(\mathcal F_d(K_2\times K_m\times K_n)\) for positive \(d\). Its Corollary 43 treats the different two-equal-small-factor family \(K_2\times K_2\times K_n\), not the present graph. Antolín Camarena and Carnero Bravo [2] classify \(\mathcal F_0(K_2\times K_m\times K_n)\), the independence-complex case; for the present graph, their formula gives \(\bigvee^{30}S^3\) at level zero, not the level-one theorem here. Carnero Bravo [3] studies polyhedral joins and forest filtrations of **lexicographic** graph products; those constructions are not the categorical triple product. The already recorded balanced \(K_2\times K_3\times K_3\) level-one example has a different underlying graph, and its numerical result does not imply the present asymmetric classification.

Targeted searches under forest-filtration, higher-independence, dissociation, categorical/direct/tensor product and equivalent sphere-wedge descriptions did not locate a prior result that implies the theorem. This is evidence-limited originality, not a claim of global uniqueness.

## Limitations
The theorem is for exactly the categorical product with factor sizes \(2,3,4\) and for degree bound one. It does not establish an all-parameter formula, higher-degree forest filtration, persistence maps, or an equivariant homotopy decomposition. A complete finite verification of the matching constitutes a proof for this single complex but not an infinite-family proof. Unindexed or inaccessible literature could contain an equivalent classification. Independent external audit has not been performed.

## References
[1] Andrés Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271 (first submitted July 25, 2023), especially Section 4.2.2, Corollary 43 and Question 44. https://arxiv.org/abs/2307.13271

[2] Omar Antolín Camarena and Andrés Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401 (first submitted July 23, 2023), Section 4. https://arxiv.org/abs/2307.12401

[3] Andrés Carnero Bravo, *Polyhedral joins and graph complexes*, arXiv:2307.14321 (first submitted July 26, 2023), Sections 1 and 5. https://arxiv.org/abs/2307.14321
