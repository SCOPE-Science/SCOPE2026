# Mixed-dimensional sphere-wedge homotopy of the Heawood general-position complex

## Finding

Let \(H\) be the Heawood graph, the bipartite point–line incidence graph of the Fano projective plane, and let \(\operatorname{GP}(H)\) be the abstract simplicial complex whose faces are all vertex sets containing no three distinct vertices on a common shortest path in \(H\). Then the integral homotopy type is

\[
|\operatorname{GP}(H)|\simeq
\bigvee^{21} S^1\;\vee\;\bigvee^{6} S^3.
\]

In particular, its only nonzero reduced integral homology groups are \(\widetilde H_1\cong\mathbb Z^{21}\) and \(\widetilde H_3\cong\mathbb Z^6\). These statements include absence of torsion and of all other reduced homology; they do not assert a preferred or symmetry-equivariant wedge decomposition.

## Assumptions and scope

Label seven points by \(0,1,\ldots,6\) and seven lines by \(7+i\), for \(i=0,1,\ldots,6\). The line \(7+i\) is incident with the three points whose labels are congruent to \(i\), \(i+1\), and \(i+3\) modulo seven. Every graph edge has length one; distance means ordinary unweighted graph shortest-path distance. The difference set \(\{0,1,3\}\) gives the Fano plane, and hence this explicit graph is the standard fourteen-vertex Heawood graph.

A nonempty set \(\sigma\) is a simplex precisely when, for every triple of distinct elements \(a,b,c\in\sigma\), none is between the other two in the shortest-path metric. Equivalently, none of the three distance equalities \(d(a,b)+d(b,c)=d(a,c)\), \(d(a,c)+d(c,b)=d(a,b)\), and \(d(b,a)+d(a,c)=d(b,c)\) holds. The claim concerns exactly this single simplicial complex and integral (not solely rational or finite-field) homotopy.

## Proof

**1. Exhaustive finite face presentation.** Compute the fourteen shortest-path distance arrays by breadth-first search from the above graph specification. Among the \(\binom{14}{3}=364\) vertex triples, precisely 210 fail the general-position condition: 105 contain two point vertices and one line vertex, and another 105 contain two line vertices and one point vertex. No all-point or all-line triple fails. Since failure is inherited by supersets, inspecting all nonempty fourteen-bit masks gives the face vector, by dimension zero through six,

\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6)
=(14,91,154,147,56,14,2).
\]

Thus there are 478 nonempty faces. These counts and every admissibility test are regenerated from the graph, rather than taken from a published face table.

**2. Explicit acyclic matching.** Order all faces by increasing cardinality and then increasing numerical bit mask. Begin with no faces paired. For pivot vertices \(v=0,1,\ldots,13\), scan the ordered faces. Whenever an as-yet unpaired face \(\sigma\) does not contain \(v\), and \(\sigma\cup\{v\}\) is an as-yet unpaired face, pair these two faces. This is a well-defined partial matching on cover relations of the nonempty-face Hasse diagram. It produces exactly 225 pairs. Its unmatched faces comprise one vertex, 21 edges, and six tetrahedra; there are no critical faces in any other dimension.

For finite, independent verification of acyclicity, orient each cover incidence downward except that the 225 matched incidences point upward. There are exactly 478 vertices and 1,610 directed arcs in the resulting Hasse graph. A complete Kahn topological sort removes all 478 vertices. Consequently that graph has no directed cycles, so the matching is acyclic in the sense of discrete Morse theory. The accompanying standalone script implements the graph reconstruction, all face tests, the matching and the **complete** directed-Hasse check using only exact integer arithmetic.

The unmatched vertex is label \(0\). The six unmatched tetrahedra have vertex sets

```
(7, 9, 10, 11)
(7, 8, 10, 12)
(7, 8, 11, 12)
(7, 9, 10, 13)
(7, 9, 11, 13)
(7, 8, 12, 13)
```

The 21 unmatched edges are exactly those printed by the deterministic certificate's stated face order, with endpoints

```
(1,7), (2,7), (3,7), (1,8), (2,8), (4,8), (2,9),
(3,9), (5,9), (3,10), (4,10), (6,10), (1,11), (4,11),
(5,11), (1,12), (5,12), (6,12), (1,13), (2,13), (6,13)
```

**3. Homotopy rather than just homology.** The acyclic matching yields a CW complex homotopy equivalent to \(|\operatorname{GP}(H)|\), with precisely one zero-cell, 21 one-cells and six three-cells. Since there are no two-cells, its one-skeleton is a wedge of 21 circles. Every three-cell attaches along a map \(S^2\to\bigvee^{21}S^1\), which is nullhomotopic because a graph is aspherical and has \(\pi_2=0\). Since all six three-cells attach to the one-skeleton, the CW complex is homotopy equivalent to the claimed wedge of circles and three-spheres. This proves the **integral** homotopy type, not merely its Betti numbers.

## Verification

Run `python3 verify_heawood_gp.py` in the directory containing this document. The standalone checker requires only Python 3's standard library, constructs the incidence graph rather than reading fixed face data, tests all 16,383 nonempty subsets, and checks every cover relation in the 478-face poset. Its successful output confirms 210 forbidden triples, the seven face counts, 225 matched pairs, the critical-cell multiplicities, and the exhaustive topological-sort acyclicity test. As a separate check, exact signed boundary matrices are reduced modulo 2, 3, 5 and 101; they have ranks \((13,57,97,44,12,2)\) in dimensions one through six. These modular computations are corroboration only: the integral homotopy conclusion follows from the acyclic matching and attaching-map argument.

## Relationship to prior work

Graph-geodesic general-position sets and their maximum cardinalities were established by Manuel and Klavžar [1] and studied in several subsequent works. Iršič, Klavžar, Rus and Tuite [2] give general-position **counting polynomials** for particular graph classes and enumerate maximal general-position sets for the Petersen graph. Their complete accessible article does not treat the Heawood graph or calculate the homotopy type of its general-position complex. Ceballos and Doolittle [3] study generalized Heawood graphs and related triangulated tori, not complexes of all graph-geodesic general-position subsets.

Published calculations for the Fano cap complex concern subsets of **seven points** avoiding collinear triples, whereas this complex uses **fourteen point and line vertices** and shortest-path avoidance. Their identical occurrence of six-dimensional homology ranks in different degrees does not establish an implication between homotopy types. Published general-position topology for bipartite-corona and rook graphs concerns different graphs with different geodesic triple systems. No prior result inspected supplies the specific mixed-dimensional integral wedge decomposition above; this is not a claim of exhaustive worldwide uniqueness.

## Limitations

The calculation is for one fixed fourteen-vertex graph. It does not establish a uniform formula for incidence graphs of arbitrary finite projective planes, nor an equivariant decomposition under the Heawood automorphism group. The complete finite certificate proves an exact homotopy statement for this graph, but does not resolve whether some unindexed prior work obtained an equivalent statement. No independent external audit is asserted.

## References

1. P. Manuel and S. Klavžar, *The graph theory general position problem on some interconnection networks*, first public arXiv version dated 2017-09-30, https://arxiv.org/abs/1710.00244 .
2. V. Iršič, S. Klavžar, G. Rus and J. Tuite, *General Position Polynomials*, first public arXiv version dated 2024-01-11, https://arxiv.org/abs/2401.05696 ; open full text https://link.springer.com/article/10.1007/s00025-024-02133-3 .
3. C. Ceballos and J. Doolittle, *Generalized Heawood Graphs and Triangulations of Tori*, first public arXiv version dated 2023-07-21, https://arxiv.org/abs/2307.11859 .
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, https://doi.org/10.1006/aima.1997.1650 .
