# A dihedral five-sphere in the two-matching complex of the Wagner graph

## Finding

Let \(W\) be the eight-vertex Wagner graph (the four-rung Möbius ladder) on \(\mathbb Z/8\mathbb Z\), with an undirected edge between \(i\) and \(i\pm1\), and between \(i\) and \(i+4\), indices modulo eight. Let \(X=M_2(W)\) have one simplicial vertex for each of the twelve graph edges and have a face for each edge set inducing maximum graph degree at most two. Then

\[
|X|\simeq S^5.
\]

The complete graph automorphism group is the dihedral group \(D_8=\langle r,s\mid r^8=s^2=1,\ srs=r^{-1}\rangle\), acting by \(r(i)=i+1\) and \(s(i)=-i\). Its action on the integral generator of \(\widetilde H_5(X;\mathbb Z)\cong\mathbb Z\) is the one-dimensional character

\[
r_*=-1,\qquad s_*=-1,\qquad (r^k)_*=(-1)^k,\qquad (sr^k)_*=(-1)^{k+1}.
\]

In particular, the ordinary quotient by the full graph symmetry has vanishing reduced rational homology in every degree:

\[
\widetilde H_j(|X|/D_8;\mathbb Q)=0\qquad\text{for all integers }j.
\]

## Assumptions and scope

This concerns the *degree-two matching complex* \(M_2(W)\), also called the bounded-degree-two edge-subset complex. It is not the ordinary matching complex \(M_1(W)\), the perfect-matching-extendibility complex, the discrete-Morse complex, nor the vertex two-independence complex. Here \(D_8\) has sixteen elements. No result for larger Möbius ladders or integral quotient homology is asserted.

Use the lexicographic edge order

`(0,1), (0,4), (0,7), (1,2), (1,5), (2,3), (2,6), (3,4), (3,7), (4,5), (5,6), (6,7)`.

A face is a bitmask \(b\) of these twelve edges for which no three-edge star of a graph vertex is fully selected. This gives exactly \(1696\) nonempty faces, with face counts in dimensions \(0,1,\ldots,7\) equal to

\[
(12,66,212,423,516,352,108,7).
\]

Its maximal faces have dimensions six and seven, so the original simplicial complex is not pure.

## Proof

**Homotopy calculation.** For each position \(j=0,\ldots,11\) in the displayed edge order, traverse the currently unmatched face masks in increasing numerical order. Whenever both \(b\) and \(b\cup\{j\}\) are still unmatched and \(j\notin b\), pair the two and remove them. Treat the empty face as available at this construction stage. Exhaustive application pairs \(848\) disjoint face pairs and leaves only the six-edge face with integer mask `2646`. Its vertices in the edge-subset complex are graph edges

`(0,4), (0,7), (1,5), (2,6), (4,5), (6,7)`.

Discard the matching pair containing the empty face and restrict to the ordinary nonempty-face poset. There are now \(847\) pairs, exactly one unmatched vertex (graph edge `(0,1)`) and exactly one unmatched five-dimensional simplex (mask `2646`). There are no other critical cells. For completeness, orient every Hasse incidence from the larger face to the smaller face, except reverse the incidence of each matched pair. The standalone verifier enumerates every incidence and performs a complete topological sort of the resulting directed graph on all \(1696\) nonempty faces. It visits all \(1696\) faces, proving that the matching is acyclic. Forman's discrete-Morse theorem yields a CW complex with one zero-cell, one five-cell, and no other cells. The attaching map of that five-cell has a point as its target, so its geometric realization is \(S^5\). This is an integral homotopy equivalence, not an inference from a field homology computation.

**Full symmetry group.** There are exactly four four-cycles in \(W\). Each of its eight cycle edges belongs to exactly one four-cycle and each of its four opposite-vertex edges belongs to exactly two. Every automorphism thus preserves the underlying rim cycle, so it is a dihedral automorphism of that cycle. All eight rotations and eight reflections preserve the opposite-vertex edges. Therefore \(\operatorname{Aut}(W)=D_8\).

**Integral symmetry character.** For each \(g\in D_8\), let \(\tau_j(g)\) be the signed permutation trace on oriented \(j\)-simplices of \(X\): only setwise invariant faces contribute, each with the sign of the induced permutation of their graph-edge labels. The reduced simplicial Lefschetz number is

\[
\widetilde L(g)=-1+\sum_{j=0}^{7}(-1)^j\tau_j(g).
\]

The `-1` is the augmentation contribution from the empty simplex. Since the only reduced homology group is integral \(H_5\cong\mathbb Z\), the induced sign on this group equals \(-\widetilde L(g)\). Exact face-permutation enumeration gives

\[
\begin{array}{c|cc}
g&r&s\\ \hline
\widetilde L(g)&1&1\\
\operatorname{tr}(g_*\mid \widetilde H_5)&-1&-1
\end{array}
\]

For rotation \(r\), the only nonzero alternating chain-trace contributions are \(+1\) in dimensions three and seven. For reflection \(s\), the alternating contributions in dimensions zero through seven are \((2,4,-8,-7,12,6,-6,-1)\), which sum to two. The full enumeration also checks all sixteen automorphisms and their expected character signs. This proves the two generator signs and therefore the stated character on all elements, including over \(\mathbb Z\) since automorphisms of \(\mathbb Z\) are multiplication by \(\pm1\).

**Rational quotient.** The rational homology of a finite simplicial-group quotient equals the invariant rational homology of the original complex (for example, after barycentric subdivision and averaging). Since \(r_*=-1\) on the only nonzero reduced rational homology group, the full-invariant subspace is zero; every reduced rational homology group of the quotient vanishes.

## Verification

Run `python3 verify_wagner.py` from the extracted package directory. It uses only the Python standard library. The program regenerates the graph and all simplices, checks the full face vector, constructs the matched-pair list deterministically, checks all matched covers and nonreuse, proves acyclicity by topologically sorting the entire oriented Hasse graph, identifies both critical cells, distinguishes the two graph-edge orbits by four-cycle incidence, and enumerates signed Lefschetz traces for all sixteen dihedral automorphisms.

The supplied script was executed from its delivered source, and returned `PASS`, with \(847\) nonempty matched pairs, one critical vertex, one critical five-cell, all \(1696\) Hasse vertices visited, and both generator traces equal to \(-1\). A complete finite enumeration is decisive here because the theorem concerns one specified finite graph and its finite automorphism group. It is not used to justify an unproved infinite-family claim.

## Relationship to prior work

Vega's paper introduced the present degree-two matching terminology and studies clawed graphs, wheels, and caterpillars. Its clawed-graph sphere theorem assumes subdivided graph edges and induced claw units, which do not occur in this cubic Wagner graph; no Wagner degree-two matching type or dihedral action is stated there. The known cube calculation for the other natural eight-vertex cubic ladder gives three five-sphere summands, whereas the Wagner graph has one. The twist-sensitive comparison motivates this precise computation, but the cube result is not claimed anew. Recent results on ordinary independence and perfect-matching complexes of Möbius ladders involve distinct simplicial complexes and do not by themselves imply this homotopy equivalence or its integral symmetry character.

## Limitations

The result is finite and exact for the eight-vertex Wagner graph; it does not classify all cubic graphs, other ladder sizes, or integral homology of the orbit space. Novelty is assessed against the cited literature and indexed published findings; an unindexed equivalent statement remains possible. A recent paper on independence and perfect matching of Möbius ladders was accessible in abstract, but a complete text inspection was not available; this limits the breadth of the bibliographic check, although its stated invariants differ from degree-two matchings.

## References

- Julianne Vega, *2-Matching Complexes*, first arXiv public version September 23, 2019, arXiv:1909.10406, https://arxiv.org/abs/1909.10406 . Full open text: https://ar5iv.labs.arxiv.org/html/1909.10406 .
- Anshu Agarwal and Biplab Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601 (2026), https://arxiv.symmetricfunctions.com/paper/2608.30601v2 . (Different simplicial invariants; comparison based on available abstract.)
- *The two-matching complex of the three-cube is a wedge of three five-spheres*, publicly indexed mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-the-two-matching-complex-of-the-three-cube-is-a-wedge-of-three-f--17687c557e9f . (Different graph; comparison based on public summary.)
