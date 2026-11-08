# The Herschel graph's Rips sphere transition and integral symmetry orientation

## Finding

Equip the eleven-vertex Herschel graph \(H\) with shortest-path distance and define its **inclusive graph-metric Vietoris–Rips complex** by
\[
X_r=\{\varnothing\ne A\subseteq V(H):d_H(u,v)\le r\text{ for every }u,v\in A\},\qquad r\ge0.
\]
For all real thresholds, the complete integral homotopy filtration is
\[
X_r\simeq
\begin{cases}
\text{eleven discrete points},&0\le r<1,\\
\bigvee^8 S^1,&1\le r<2,\\
S^3,&2\le r<3,\\
\ast,&r\ge3.
\end{cases}
\]
The nontrivial three-sphere at scale two is an integral homotopy assertion, not merely a homology computation. The complex at scale three **simplicially collapses** to a vertex.

The full automorphism group is \(\operatorname{Aut}(H)=\mathfrak S_3\times C_2\). Let \((\sigma,\tau^e)\) act by permuting the three four-valent vertices and, when \(e=1\), exchanging the two distinguished degree-three vertices and their corresponding neighbors. The integral top homology is the rank-one orientation module
\[
\widetilde H_3(X_2;\mathbb Z)\cong\operatorname{sgn}_{\mathfrak S_3}\otimes\varepsilon_{C_2},
\qquad (\sigma,\tau^e)\mapsto\operatorname{sgn}(\sigma)(-1)^e.
\]
In particular the full-group invariant rational reduced homology vanishes, so \(X_2/\operatorname{Aut}(H)\) is rationally acyclic.

For coefficients in any field, the complete reduced persistence barcode has ten degree-zero intervals \([0,1)\), eight degree-one intervals \([1,2)\), and one degree-three interval \([2,3)\), with no others. Ordinary unreduced degree-zero persistence also has its permanent connected-component interval \([0,\infty)\).

## Assumptions and scope

The graph is simple and undirected, with vertex set \(\{0,1,\ldots,10\}\) and the following complete unordered edge list:

```text
(0,5) (0,6) (0,9) (0,10)
(1,5) (1,6) (1,7) (1,8)
(2,7) (2,8) (2,9) (2,10)
(3,5) (3,7) (3,9)
(4,6) (4,8) (4,10)
```

Thus the three four-valent vertices are \(0,1,2\); vertices \(3,4\) each have degree three and no four-valent neighbors; vertices \(5,\ldots,10\) have degree three and exactly two four-valent neighbors. This characterizes the standard Herschel graph. In this labeling the pairs \((5,6),(7,8),(9,10)\) correspond to the unordered pairs \((0,1),(1,2),(0,2)\), and exchanging \(3\leftrightarrow4\) simultaneously exchanges each of those pairs.

Use nonempty simplices in ordinary face-poset Morse theory; the empty simplex is included only in the usual augmented homological convention. Graph distances are integers, so the displayed four intervals cover every real scale \(r\ge0\). The claim is about the intrinsic shortest-path vertex metric, not Euclidean distances on a drawing and not geometric realization of the graph as a metric graph.

## Proof

**The first two stages.** The diameter is four, and the graph is connected and triangle-free with eleven vertices and eighteen edges. Thus \(X_0\) consists of eleven vertices, whereas \(X_1\) is a connected graph with cycle rank \(18-11+1=8\). It follows that \(X_1\simeq\bigvee^8 S^1\).

**An exhaustive perfect matching at scale two.** Encode a nonempty face by the binary mask \(b=\sum_{i\in A}2^i\). Enumerating the \(2^{11}-1\) nonzero masks using the displayed edge list and breadth-first-search distances gives the face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(11,42,69,46,9,1),
\]
so there are exactly 178 nonempty faces. Start with all faces unpaired. Visit the vertices in the fixed order

```text
9,4,0,10,3,7,2,1,8,5,6
```

At the step for vertex \(v\), pair every still-unpaired face \(A\) not containing \(v\) with \(A\cup\{v\}\) when both remain, then remove both from the unpaired set. This produces exactly 88 pairs. The only critical faces are the zero-face \(\{9\}\) and the three-face \(\{1,5,6,7\}\). To check acyclicity rather than assume it, orient every unmatched nonempty codimension-one cover from higher to lower dimension and reverse each matched cover. The resulting directed graph has exactly 178 vertices and 526 directed cover incidences. A complete Kahn topological sort visits all 178 vertices, hence has no directed cycle. The embedded standard-library checker constructs and checks every incidence, establishing a finite exhaustive acyclic discrete-Morse certificate.

The integral discrete-Morse theorem gives a CW homotopy model with one zero-cell, one three-cell and no cells in any other dimension. Its three-cell attaching map has a point as target. Therefore the model and \(X_2\) are homotopy equivalent to \(S^3\). This verifies the full integral homotopy type, independently of the mod-two boundary-rank consistency check.

**Simplicial collapse at scale three.** Enumerating all pairwise-distance-at-most-three faces gives precisely 1,535 nonempty faces, with dimension-by-dimension counts
\[
(11,54,156,294,378,336,204,81,19,2).
\]
In the current complex, enumerate all inclusion-maximal faces \(T\) and all their codimension-one nonempty faces \(S\). Select among pairs for which \(S\) lies in exactly one maximal face the lexicographically maximal triple \((|T|,\operatorname{mask}(T),\operatorname{mask}(S))\). Remove \(S\) and \(T\), and repeat. On every iteration the verifier checks that \(S\) is free and that \(T\) is its sole maximal coface. Exactly 767 legal elementary collapse pairs remain available, ending at the vertex \(\{0\}\). Thus \(X_3\) is simplicially collapsible. At scale four the diameter bound makes \(X_4\) the full ten-simplex. Consequently \(X_r\) is contractible for every \(r\ge3\).

**All twelve symmetry actions.** The degree pattern forces every automorphism to permute \(0,1,2\), and independently either fix or exchange \(3,4\). Each of the six remaining vertices is uniquely specified by its two neighbors among \(0,1,2\) and by its neighbor in \(\{3,4\}\). Hence there are at most \(3!\cdot2=12\) automorphisms; the specified coordinate actions preserve all eighteen edges and realize all twelve.

For a permutation \(g\) of the vertices, the simplicial chain trace in dimension \(d\) is the signed count of \(g\)-fixed \(d\)-faces, with sign given by the ordering permutation of their vertices. The finite signed Lefschetz sum is
\[
L(g)=\sum_d(-1)^d\operatorname{tr}(g\mid C_d(X_2;\mathbb Q)).
\]
The checker enumerates every face for every one of the twelve automorphisms and obtains the following values; \(\operatorname{tr}_3=1-L\) because only ordinary \(H_0\cong\mathbb Q\) and \(H_3\cong\mathbb Q\) remain:

| Type of \(\sigma\) | \(e\) | Number | \(L(g)\) | \(\operatorname{tr}_3(g)\) |
|---|---:|---:|---:|---:|
| Identity | 0 | 1 | 0 | 1 |
| Identity | 1 | 1 | 2 | -1 |
| Transposition | 0 | 3 | 2 | -1 |
| Transposition | 1 | 3 | 0 | 1 |
| Three-cycle | 0 | 2 | 0 | 1 |
| Three-cycle | 1 | 2 | 2 | -1 |

Because \(H_3(X_2;\mathbb Z)\cong\mathbb Z\), each action has integral degree \(\pm1\). The exact rational Lefschetz trace identifies that degree and proves the stated integral rank-one orientation character. Averaging the nontrivial character gives zero invariant rational homology; for a finite group acting simplicially the rational cohomology of the quotient agrees with the invariant rational cohomology, proving the rational acyclicity assertion.

**Persistence.** The scale-zero reduced \(H_0\) has rank ten and dies on connecting the graph at scale one. The only nonzero reduced homology at scale one is free rank-eight \(H_1\), which vanishes at scale two. The only nonzero reduced homology at scale two is free rank-one \(H_3\), which dies at scale three. There are no other possible births, so all-field persistence decomposes into exactly the specified intervals.

## Verification

Run the provided `verify_rips.py` using Python 3 standard library:

```text
python3 verify_rips.py
```

It rebuilds all eleven-by-eleven shortest-path distances twice (breadth-first search and Floyd–Warshall), enumerates all 2,047 nonempty vertex subsets, checks every scale and face count, independently computes mod-two homology for the two nontrivial higher stages, validates all 526 scale-two matched and unmatched cover incidences by a complete topological sort, checks all 767 scale-three elementary free-face collapses, proves the complete twelve-element automorphism list by degree invariants, and computes exact signed Lefschetz numbers on every group element. Recorded output is supplied as `verification_output.txt`; the terminal line is `ALL_CHECKS_PASS`.

## Relationship to prior work

Michał Adamaszek, *Clique complexes and graph powers*, first publicly posted April 3, 2011 (arXiv:1104.0433v1), develops the general graph-power perspective. Its girth-stability proposition requires girth at least seven at the second power, whereas the Herschel graph contains four-cycles. Its clique-neighborhood criterion does not determine the sphere transition here, and its explicit family calculations concern cycles, subdivisions, and line graphs rather than this graph. The full accessible article, including its graph-power stability criteria and cycle-power classifications, was examined for implication, not just its title.

An accessible 2026 exact calculation of the *ordinary independence complex* of the Herschel graph gives a wedge of two two-spheres with a vertex-deletion profile. Ordinary independence requires selecting nonadjacent vertices of \(H\); the present \(X_2\) instead selects cliques of its **distance-two power**. Neither complex contains the other in a way implying the claimed Rips sphere, filtration, or symmetry action. Other indexed finite-graph Rips classifications concern different named graphs and do not furnish a universal statement forcing these results.

## Limitations

This calculation is specific to the Herschel graph and the intrinsic shortest-path metric on its eleven vertices. It does not classify all non-Hamiltonian polyhedral graphs, nor claim a relationship between Hamiltonicity and Rips homotopy. The finite exact checker proves the stated finite claims but is not an independent external audit. Publication-priority searches cannot exclude unindexed equivalent computations or an obscure stronger theorem. The quotient conclusion is rational only, not a contractibility or integral torsion assertion.

## References

- M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433v1, first public April 3, 2011, https://arxiv.org/abs/1104.0433.
- R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145, https://doi.org/10.1006/aima.1997.1650.
- *Herschel graph*, standard eleven-vertex eighteen-edge construction and symmetry data, https://en.wikipedia.org/wiki/Herschel_graph.
- *The Herschel graph independence complex and its complete vertex-deletion profile*, publicly archived October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-herschel-graph-independence-complex-and-its-complete-vertex--e6d752a4b77d.
