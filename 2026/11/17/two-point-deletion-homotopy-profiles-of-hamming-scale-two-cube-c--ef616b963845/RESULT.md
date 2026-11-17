# Two-point deletion homotopy profiles of Hamming-scale-two cube complexes through dimension five

## Finding
Let \(Q_n=\{0,1\}^n\), with Hamming distance \(d_H\). For a pair of different vertices \(u,v\) with \(d_H(u,v)=d\), let
\[K_{n,d}=\operatorname{VR}_{\le2}(Q_n\setminus\{u,v\}),\]
the flag complex on the remaining words whose simplices have all pairwise Hamming distances at most two. Cube automorphisms identify all choices of the pair at fixed distance. The complete **integral homotopy types for dimensions three through five** are

| \(n\) | \(d=1,2\) | \(d=3,4\) when admissible | \(d=5\) when admissible |
|---|---|---|---|
| 3 | contractible | \(S^2\) for \(d=3\) | not applicable |
| 4 | \(\bigvee^{3}S^3\) | \(S^3\) | not applicable |
| 5 | \(\bigvee^{32}S^3\) | \(\bigvee^{29}S^3\) | \(\bigvee^{29}S^3\) |

The genuinely new finite classifications concern deleting a pair of distance at least three in the four- and five-cubes. The adjacent-pair and distance-two cases are already consequences of an earlier all-order initial-segment theorem, while the three-cube boundary follows from the cross-polytope model.

## Assumptions and scope
The metric on the *remaining* set is the restriction of the original Hamming metric, not the shortest-path metric of the induced punctured cube graph. The Vietoris–Rips scale is inclusive (diameter at most two). All complexes are unfilled abstract simplicial flag complexes, with empty simplex omitted only from the face-poset certificate. The domain is exactly \(3\le n\le5\) and \(1\le d\le n\). To represent a pair one may take the integer-encoded words \(u=0\), \(v=2^d-1\).

## Proof
**Step 1: exhaustive reduction to pair distances.** Translations and permutations of binary coordinates act transitively on unordered pairs with each fixed Hamming distance. Moreover, the map \(x\mapsto(x,\operatorname{parity}(x))\) embeds \(Q_n\) into the even-word half of \(Q_{n+1}\). Two words of Hamming distance \(d\) map to words differing in \(d+(d\bmod2)=2\lceil d/2\rceil\) coordinates. The scale-two adjacency graph is the distance-two graph on even words, whose coordinate-permutation group acts transitively on pairs differing in a fixed number of coordinates. Hence \(K_{n,2k-1}\cong K_{n,2k}\) whenever both distances exist. This explains one symmetry reduction but does not identify the larger-distance homotopy types.

**Step 2: reproducible exact Morse certificate.** The attached `verify_two_puncture.py` contains a complete list of \(12\) pivot orders, one for every pair \((n,d)\). It enumerates **every** nonempty clique in the graph whose vertices are the remaining binary words and whose edges join words of Hamming distance at most two, by recursion through strictly increasing vertex orders. Given one recorded pivot order, at each pivot \(v\) it pairs every as-yet-unused face \(\sigma\) not containing \(v\), whenever \(\sigma\cup\{v\}\) is also unused, with that coface. Thus the program constructs an explicit disjoint partial matching of the entire face poset, not a guess from homology ranks.

For every matched coface-cover relation it reverses the usual high-to-low orientation of the Hasse graph, and keeps all other codimension-one relations directed high to low. An exhaustive topological-sort check certifies that this directed graph has **no directed cycles**. All critical faces are enumerated and counted. In dimensions four and five, the only critical cells are exactly one zero-cell and respectively \(3\), \(1\), \(32\), or \(29\) three-cells, as displayed in the finding. For dimension three, the distance-one and distance-two complexes have one critical zero-cell, whereas the distance-three complex has one critical zero-cell and one critical two-cell.

Forman's discrete Morse theorem therefore provides a CW model with precisely those cells. A CW complex with one zero-cell and only cells of a single positive dimension at least two is a wedge of spheres in that dimension: there are no nontrivial attaching maps to the point. In the sole case with just one zero-cell it is contractible. This proves the **integral** homotopy assertions, not only a field-homology computation.

**Step 3: exact profiles.** For \(n=3\) the numbers of nonempty simplices and Morse pairs are respectively \(35,17\) at distance one or two and \(26,12\) at distance three. For \(n=4\) they are \(258,127\) at distances one and two and \(240,119\) at distances three and four. For \(n=5\) they are \(1427,697\) at distances one and two and \(1392,681\) at distances three, four and five. Each instance has one unmatched vertex; remaining critical cells have the stated dimensions and multiplicities. The embedded verification script checks these counts and every Hasse orientation.

## Verification
Run `python3 verify_two_puncture.py` using Python 3.10 or newer (`int.bit_count` is required). The script uses only the Python standard library. It independently calculates all reduced mod-two Betti ranks using binary boundary-matrix elimination in addition to the complete acyclic discrete-Morse certificate. The recorded output is `verification_output.txt`. All twelve cases passed. The proof for each finite case is the exhaustive directed-Hasse certificate together with the standard discrete Morse theorem; the independent homology calculations corroborate it rather than replacing it.

## Relationship to prior work
Adamaszek and Adams [1, Theorems 1 and 8, Lemma 7] classify the complete scale-two Hamming-cube Rips complex and its initial consecutive binary-word subsets. By cube symmetry and the even-word embedding above, their result also covers **two removed vertices at distances one or two**. Those cases are reported for completeness only, not as a novel part of this claim. For \(n=3\), the distance-three result can also be read from the standard cross-polytope boundary model at scale \(n-1\). The new material is the exact homotopy classification for deletion distances at least three in the four- and five-cubes, including the nonisomorphic distance-three and antipodal punctures in the five-cube having the same \(29\)-sphere type. Indeed, the distance-five deletion graph is 14-regular on all 30 remaining vertices, while the distance-three deletion graph has degree counts \(6,18,6\) in degrees \(13,14,15\), respectively.

The 2026 work of Bendersky, Elia and Grbić [2] studies full-cube connectivity, cohomology and classes detected by ghost vertices, but provides no two-point-deletion homotopy classification. Galetto, Montaño and Wellner [3] calculate equivariant homology representations of **full** cubes; these results likewise do not determine the punctured cases. The small-dimension census and acyclic certificates address the first second-order missing-data test cases not settled by [1].

## Limitations
No assertion for \(n\ge6\), higher scale, triples or arbitrary larger deletion sets, or equivariant actions on the punctured complexes. The result does not provide a uniform all-dimensional two-point deletion theorem. Every verified finite case has a separate complete matching, rather than extrapolating a common recurrence. Equality of homotopy types for distinct pair distances does not assert simplicial isomorphism. No independent human audit has been performed.

## References
[1] M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (first submitted 2021-03-01), Theorems 1 and 8, Lemma 7.

[2] M. Bendersky, S. Elia and J. Grbić, *Cohomological properties of the Vietoris–Rips Complex of a Hypercube Graph*, arXiv:2605.00705 (first submitted 2026-05-01), Sections 1, 2 and 5.

[3] F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784 (first submitted 2026-06-18), Sections 1 and 3.
