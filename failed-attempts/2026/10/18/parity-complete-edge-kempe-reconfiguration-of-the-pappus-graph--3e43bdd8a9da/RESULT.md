# Parity-complete edge-Kempe reconfiguration of the Pappus graph

## Finding

Let \(H\) be the Pappus graph, regarded as the Levi graph of the affine \((9_3)\) configuration over \(\mathbb F_3\) described below. Form a simple graph \(\mathcal K(H)\) whose vertices are proper three-edge-colorings of \(H\) modulo permutation of the three color names. Distinct colorings are adjacent exactly when one is obtainable from the other by interchanging two colors on a single connected bichromatic cycle. Then

\[
\boxed{\mathcal K(H)\cong 2\bigl(K_1\vee(K_3\sqcup K_3\sqcup K_3)\bigr).}
\]

Here \(\sqcup\) is disjoint union, \(\vee\) is the graph join, and the prefix \(2\) means two disjoint copies. Each ten-vertex component is three copies of \(K_4\) sharing exactly one common vertex. In particular, \(H\) has \(42\) perfect matchings, \(20\) unordered one-factorizations, \(120\) proper colorings with three named colors, and \(36\) distinct nontrivial single-cycle switch adjacencies between unordered one-factorizations.

For a perfect matching \(M\) the incidence bijection from the nine points to the nine lines has sign \(\operatorname{sgn}(M)\in\{-1,+1\}\) with respect to the fixed orders below. For a coloring \(F=\{M_1,M_2,M_3\}\) put

\[\varepsilon(F)=\prod_{i=1}^3\operatorname{sgn}(M_i).\]

**Exact parity criterion.** Two proper three-edge-colorings of \(H\), considered modulo global renaming of colors, are edge-Kempe equivalent if and only if their values of \(\varepsilon\) agree. Each sign occurs in precisely ten unordered colorings. Within one sign class any two colorings are related by at most two single-cycle switches; across signs no such sequence exists.

Of the twenty colorings, two have all three bichromatic spanning two-factors comprising three disjoint six-cycles, and each of these two colorings has nine distinct switching neighbors. The other eighteen have one bichromatic two-factor comprising three six-cycles and two Hamiltonian eighteen-cycles, and each has exactly three distinct neighbors. The two degree-nine colorings lie in opposite sign classes.

## Assumptions and scope

Write the point vertices as \(p_{x,y}\), \(x,y\in\mathbb F_3\), and the line vertices as \(\ell_{m,b}\), \(m,b\in\mathbb F_3\). Adjacency is exactly

\[p_{x,y}\sim\ell_{m,b}\quad\Longleftrightarrow\quad y=mx+b\pmod3.\]

Thus the vertex bipartition has nine points and nine (nonvertical affine) lines, and the graph has 27 edges, three at each vertex. We order the points by \(3x+y\) and the lines by \(3m+b\), with coordinates represented by \(0,1,2\). The verifier additionally checks an explicit vertex isomorphism from this incidence model to the conventional Pappus LCF presentation \([5,7,-7,7,-7,-5]^3\). Hence no graph identification is assumed from a name alone.

A one-factorization is an unordered partition of all 27 edges into three perfect matchings. For each matching \(M\), every point has exactly one matched line; the order-fixed bijection defines \(\operatorname{sgn}(M)\). Exchanging either ordering reverses all three matching signs simultaneously and therefore reverses the sign assigned to every coloring; equality versus inequality of signs, and the partition into two sign classes, is independent of this convention. Relabeling the three colors does not change their product.

A *single-cycle switch* means one component of the two-colored spanning two-factor is switched, not an arbitrary simultaneous collection of components. A switch that merely permutes the global color names does not give an edge of the simple reconfiguration graph. No claim is made for other finite configurations, other coloring rules, or arbitrary cubic graphs.

## Proof

**1. Parity obstruction.** In any bipartite cubic graph with equally sized fixed ordered vertex classes, let the three color classes induce bijections \(\pi_1,\pi_2,\pi_3\). Consider a bichromatic cycle of length \(2k\), using colors \(a,b\). Exchanging these colors along that cycle composes the corresponding two bijections with a \(k\)-cycle on one side (up to conjugation or inversion). Each individual sign is consequently multiplied by \((-1)^{k-1}\). Their product, and therefore the triple product \(\varepsilon\), is unchanged. Thus different \(\varepsilon\)-values obstruct all sequences of single-cycle switches. This step is a direct elementary observation and is not claimed as a new general invariant.

**2. Exhaustive and complete state enumeration.** Label point \(p_{x,y}\) by \(3x+y\), label line \(\ell_{m,b}\) by \(9+3m+b\), and sort the 27 incident edges lexicographically, giving the bit order in `kempe_certificate.json`. Recursively process points \(0,1,\ldots,8\), branching over all incident lines not used at earlier points. At the ninth point, every resulting assignment is a bijection, so it is a perfect matching. Conversely each perfect matching has exactly one corresponding sequence of nine branches. The exact enumeration gives 42 distinct matchings. For each pair of these 42 matchings having disjoint edge masks, form the remaining-edge mask and retain the triple precisely when that mask is another one of the enumerated matchings. Sorting the three masks identifies permutations of colors. This generates *all* 20 unordered one-factorizations: any factorization contains such a pair, and every accepted triple partitions the full edge set into perfect matchings.

**3. Exhaustive and complete switch enumeration.** For each one-factorization and each of its three unordered pairs of color classes, its union is a spanning two-regular graph. Follow its edges to list all connected cycles. For each such cycle interchange the two colors on exactly its edges, sort the three resulting matching masks, and record an adjacency unless the canonical triple is unchanged. Every permitted elementary move occurs in this procedure, and every recorded move is valid. The resulting 20 canonical vertices and 36 unordered adjacency pairs are embedded in `kempe_certificate.json`, along with their bichromatic cycle profiles, sign values, and connected-component partition.

Direct graph checks on the complete 36-edge adjacency list show that its two components each contain ten vertices, each has a single degree-nine vertex adjacent to all other nine vertices, and the nine remaining vertices form three disjoint triangles. This is exactly \(K_1\vee(3K_3)\) per component. The sign values are constant on each component and opposite across components; each value occurs ten times. Therefore sign equality is also *sufficient* for connectivity. Every component has diameter two, proving the asserted sharp switch bound. The degree and bichromatic-profile counts follow from the same exhaustive state list.

**4. Independent enumeration cross-check.** `verify_colorings.cpp` does not enumerate perfect matchings first: it assigns one of three colors directly to each of the 27 edges, pruning only when an endpoint already carries that color. At a terminal assignment, every edge is colored and each cubic vertex has one edge of each color, so the assignment is proper. The recursion branches over every locally allowed color, hence omits no proper coloring. It finds exactly 120 labeled colorings, canonicalizes them into 20 unordered states, and independently reconstructs the 36 adjacencies, bichromatic profiles, sign classes, and two windmill components. Agreement of these different exhaustive constructions checks the finite certificates without treating sample computations as an infinite proof.

## Verification

With `verify_factorizations.py`, `verify_colorings.cpp`, and `kempe_certificate.json` in the same directory, the complete finite proof is reproducible with only Python 3 and a C++17 compiler:

```sh
python3 verify_factorizations.py --check-certificate kempe_certificate.json
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_colorings.cpp -o verify_colorings
./verify_colorings
```

The Python verifier checks the standard LCF isomorphism, all 42 point-to-line perfect matchings, every factorization, every bichromatic cycle switch, the exact certificate, all parity labels, the two ten-vertex components, and the three disjoint peripheral triangles of each component. The C++ verifier independently assigns edge colors and checks the same component structures. Both executions succeeded on the exact source files included with this result. `kempe_certificate.json` provides the ordered 27-edge incidence list, twenty canonical triples of hexadecimal 27-bit masks, thirty-six adjacency pairs indexed into those triples, parity signs, cycle profiles, connected components, and the Pappus LCF isomorphism.

## Relationship to prior work

Belcastro and Haas [1] develop edge-Kempe equivalence and count its classes for broad families of cubic graphs; in particular they establish two isolated three-edge-coloring classes for \(K_{3,3}\), but do not give the Pappus graph's complete 20-vertex move graph. Goedgebeur and Östergård [2] tabulate the numbers of equivalence classes for all connected cubic graphs through order 30 and bipartite cubic graphs through order 36; their paper gives a general exact enumeration algorithm, but the published tables do not give the Pappus graph's full adjacency, parity criterion, or windmill decomposition. Their public accompanying dataset [3] describes graph instances attaining maximal class counts and code for computing the class count; that is important methodological overlap, but no source-inspected Pappus-specific adjacency certificate was found.

Dejter [4] discusses tight one-factorizations in girth-regular graphs and depicts the Pappus graph as the base of a prism. Its edge-girth-coloring problem is not the single-cycle three-edge-Kempe reconfiguration of the base graph. These comparisons credit the previously available definition, switching framework, and census instead of claiming the existence of two Kempe classes or the elementary sign obstruction alone as novel. The specific proposed contribution is the exact **complete move graph**, together with the sign criterion being sufficient and the two-switch diameter in each sign class.

## Limitations

The theorem concerns exactly the specified 18-vertex graph and the stated quotient by color-name permutations. The elementary sign obstruction holds more generally, but the sign *sufficiency* statement and windmill decomposition are established only for \(H\). The finite computations are exhaustive for this graph and do not imply any classification of larger graphs. Earlier unindexed computations, ancillary datasets, or code-derived tabulations of the same full Pappus adjacency graph could affect historical priority; a separate literature audit remains desirable. Neither general mixing-time bounds nor applications beyond this reconfiguration problem are claimed.

## References

1. S.-M. Belcastro and R. Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, arXiv:1209.1730, first posted 8 September 2012; Discrete Mathematics 325 (2014), 77–84. https://arxiv.org/abs/1209.1730
2. J. Goedgebeur and P. R. J. Östergård, *Switching 3-edge-colorings of cubic graphs*, arXiv:2105.01363, first posted 4 May 2021; Discrete Mathematics 345 (2022), 112963. https://arxiv.org/abs/2105.01363
3. J. Goedgebeur and P. R. J. Östergård, *Dataset and code for Switching 3-edge-colorings of cubic graphs*, Zenodo, released 21 April 2021, DOI:10.5281/zenodo.4707696. https://doi.org/10.5281/zenodo.4707696
4. I. J. Dejter, *Tight factorizations of girth-\(g\)-regular graphs*, arXiv:2102.06956, first posted 13 February 2021. https://arxiv.org/abs/2102.06956
