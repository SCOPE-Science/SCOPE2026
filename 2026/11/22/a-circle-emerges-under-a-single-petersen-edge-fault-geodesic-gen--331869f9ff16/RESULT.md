# A circle emerges under a single Petersen edge fault: geodesic general-position homotopy

## Finding

Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph. For any edge \(e\) and any vertex \(v\), the geometric realizations of the graph-geodesic general-position simplicial complexes satisfy

\[
|\operatorname{GP}(P)|\simeq S^3,\qquad
|\operatorname{GP}(P-e)|\simeq S^1\vee\bigvee^3 S^2,\qquad
|\operatorname{GP}(P-v)|\simeq\bigvee^2 S^2.
\]

In particular, deleting one graph edge creates a fundamental group isomorphic to \(\mathbb Z\), whereas deleting one graph vertex does not: the latter complex remains simply connected. The faults here change the graph metric, not merely the vertex or face set of a fixed simplicial complex.

## Assumptions and scope

The graph \(\operatorname{KG}(5,2)\) has ten vertices, namely the two-element subsets of \(\{0,1,2,3,4\}\); two are adjacent precisely when disjoint. All graphs are finite, simple, undirected, unweighted; geodesics are shortest graph paths. For connected \(G\), a nonempty set \(\sigma\subseteq V(G)\) belongs to \(\operatorname{GP}(G)\) if and only if none of its triples \(\{a,b,c\}\) has any ordering for which \(d(a,b)+d(b,c)=d(a,c)\). The empty face is included implicitly. Removing an edge does not remove its endpoints, and vertex deletion yields the induced graph on the other nine vertices.

All fifteen edge choices are equivalent under the natural \(S_5\) action, as are all ten vertex choices. Hence verifying the lexicographically first edge \(e=\{\{0,1\},\{2,3\}\}\) and first vertex \(v=\{0,1\}\) determines every single-fault case. The full vertex/edge-orbit transitivity is explicitly checked by enumerating the 120 permutations of the five ground labels.

## Proof

First enumerate all forbidden unordered vertex triples in the relevant graph by breadth-first shortest-path distances and the equality above. A face is any nonempty bitmask of graph vertices containing no forbidden triple. The exact resulting counts are:

| Graph | Forbidden triples | Nonempty face vector, dimensions increasing | Total faces |
|---|---:|---|---:|
| \(P\) | 30 | \((10,45,90,80,30,5)\) | 260 |
| \(P-e\) | 50 | \((10,45,70,38,6)\) | 169 |
| \(P-v\) | 33 | \((9,36,51,24,3)\) | 123 |

Next, on the **nonempty** faces, visit vertex labels in increasing order. At each label \(j\), pair every still-unpaired face \(\sigma\) not containing \(j\) with \(\sigma\cup\{j\}\), whenever both remain unpaired. Discard the paired faces and proceed. This is a discrete-Morse matching; to independently exclude directed cycles, orient each matched Hasse incidence upward and every other one downward. A complete topological sort visits all faces (260, 169 and 123), respectively, with 860, 482 and 336 directed Hasse incidences. The numbers of pairs are 129, 82 and 60.

The unmatched critical-cell counts are, by dimension:

| Graph | Critical zero-cells | Critical one-cells | Critical two-cells | Critical three-cells |
|---|---:|---:|---:|---:|
| \(P\) | 1 | 0 | 0 | 1 |
| \(P-e\) | 1 | 1 | 3 | 0 |
| \(P-v\) | 1 | 0 | 2 | 0 |

For completeness, all integral Morse differentials are computed using oriented faces in increasing vertex order. If \(a\) is a matched lower \(p\)-face paired to an upper \((p+1)\)-face \(b\), with incidence \(\varepsilon=[b:a]\in\{\pm1\}\), the projection of \(a\) to critical \(p\)-faces is computed recursively as

\[
\Pi_p(a)=-\varepsilon^{-1}\sum_{t\subset b,\ \dim t=p,\ t\ne a}[b:t]\Pi_p(t).
\]

The projection of a critical \(p\)-face is itself; that of a matched upper \(p\)-face is zero. The resulting signed Morse differential of a critical cell \(c\) is \(\sum_{t\subset c}[c:t]\Pi(t)\). The recursion terminates by the verified Hasse acyclicity. **Every positive-degree integral Morse differential is zero** for each of the three complexes.

The resulting CW complex for \(P\) has one zero-cell and one three-cell, hence is \(S^3\). The complex for \(P-v\) has one zero-cell and two two-cells, hence is a wedge of two two-spheres. For \(P-e\), the unique critical one-cell yields a circle. Every critical two-cell attaching map is a map \(S^1\to S^1\), whose degree equals the signed Morse boundary coefficient. All three degrees are zero, so all three maps are nullhomotopic, and the CW complex is a wedge of that circle and three two-spheres. Discrete-Morse reduction preserves homotopy type. This proves the three statements integrally, not only their Betti numbers.

## Verification

The self-contained `verify.py` implements the graphs, exact shortest-path test, complete face enumeration, vertex-toggle matching, exhaustive directed-Hasse acyclicity check, integer Morse projection and differential computation, and a separate full-simplicial-boundary rank check over \(\mathbb F_2\). It additionally verifies transitivity of the fault orbits by all 120 permutations of ground labels.

Run `python verify.py` using Python 3.9 or later (standard library only). The checker succeeds for all three cases, outputs the face and matching counts above, and finds vanishing integer Morse differentials. The separately computed mod-two Betti numbers match the integral CW models. The mod-two calculation is corroboration, **not** the basis for claims about integral torsion or homotopy type; those follow from the signed Morse reduction and attaching-map argument.

## Relationship to prior work

Manuel and Klavžar introduced the graph-geodesic general-position problem (arXiv:1708.09130, 2017). Iršič, Klavžar, Rus and Tuite (arXiv:2401.05696, 2024; *Results in Mathematics* 79, article 110) list the ten maximal general-position vertex sets of the **intact** Petersen graph and derive its counting polynomial. Their complete facet list provides a strong prior combinatorial description of the intact complex, but does not give the graph-edge-deleted or graph-vertex-deleted metric complexes in this statement. The intact \(S^3\) calculation here is a comparative baseline, not presented as an independent new family of results.

The present claim computes both complete single-fault homotopy types. The published general-position polynomial or maximal-facet description for intact \(P\) does not determine shortest-path forbidden triples after deleting a graph edge or vertex; neither deletion operation is an ordinary simplicial restriction on the pre-existing complex.

## Limitations

Only zero or one graph edge or vertex is deleted; simultaneous faults and larger Kneser graphs are not classified. The calculations establish nonequivariant integral homotopy types, not the action on homology of each fault stabilizer. Originality is assessed against the explicitly compared literature and indexed mathematical results, not against every potentially unpublished or unindexed computation. The mathematical verification is a finite exact computation with source code available here, not a formal proof-assistant certificate.

## References

1. P. Manuel and S. Klavžar, *A general position problem in graph theory*, arXiv:1708.09130v1 (first public version 2017-08-30), https://arxiv.org/abs/1708.09130.
2. V. Iršič, S. Klavžar, G. Rus and J. Tuite, *General position polynomials*, arXiv:2401.05696v1 (first public version 2024-01-11), https://arxiv.org/abs/2401.05696; *Results in Mathematics* 79 (2024), article 110, https://doi.org/10.1007/s00025-024-02133-3.
