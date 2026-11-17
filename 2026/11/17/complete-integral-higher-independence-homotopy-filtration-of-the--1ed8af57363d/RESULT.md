# Complete integral homotopy filtration of the fifteen-vertex full binary tree

## Finding

Let \(T\) be the full rooted binary tree of height three. For every integer \(r\ge1\), the higher-independence complex \(\operatorname{Ind}_r(T)\) has the following exact integral homotopy type:

\[
\operatorname{Ind}_r(T)\simeq
\begin{cases}
\text{point},&r=1,2\text{ or }r\ge15,\\
S^5,&r=3,\\
\bigvee^9S^7,&r=4,\\
\bigvee^9S^9,&r=5,\\
S^{11},&r=6,\\
\bigvee^{\binom{7}{r-7}}S^{r-1},&7\le r\le14.
\end{cases}
\]

In particular the homotopical dimension falls from eleven to six between thresholds six and seven, despite inclusion of complexes. The final eight noncontractible thresholds have binomial sphere multiplicities. All positive-degree integral persistent-homology intervals are the one-step intervals \([r,r+1)\), with multiplicity equal to the sphere count at threshold \(r\).

## Assumptions and scope

The finite graph \(T\) has vertex set \(\{0,1,\ldots,14\}\). For each integer \(0\le i\le6\), its only edges are \(\{i,2i+1\}\) and \(\{i,2i+2\}\). Thus it is the complete two-branching rooted tree with levels of sizes one, two, four, and eight. A vertex subset \(F\) is a face of \(\operatorname{Ind}_r(T)\) precisely when every component of the induced subgraph \(T[F]\) contains at most \(r\) vertices. The empty face is included. The threshold is an integer \(r\ge1\); all spaces are ordinary geometric realizations, with integral homotopy equivalences.

## Proof

An exhaustive, finite discrete-Morse certificate is supplied as `verify.py`. Its mathematical certificate covers **every** one of the \(2^{15}=32768\) vertex subsets at each threshold, not a sample. It determines admissibility by traversing each induced component of the precisely specified tree.

For each threshold, the verifier contains an explicit fixed permutation \(p_r\) of the fifteen vertices. Starting with the entire face poset, including the empty face, and following this permutation, pair each still-unmatched face \(F\) not containing the current vertex \(v\) with \(F\cup\{v\}\) whenever the latter is also a still-unmatched face. Pair the empty face with \(\{v\}\) in the same manner if both remain unmatched. The program verifies all pairs are disjoint cover relations. It then constructs **every** cover relation of the face poset and orients it upward exactly when matched, and downward otherwise. A complete Kahn topological sort confirms this directed graph has no cycle for each of the fifteen thresholds. This is an acyclic matching in Forman's discrete-Morse sense.

The resulting critical faces, with the empty face paired, have the following counts by dimension:

| Threshold \(r\) | Nonempty faces | Critical dimensions and counts |
|---|---:|---|
| 1 | 2305 | none |
| 2 | 9297 | none |
| 3 | 18448 | dimension 5: 1 |
| 4 | 23544 | dimension 7: 9 |
| 5 | 27128 | dimension 9: 9 |
| 6 | 29552 | dimension 11: 1 |
| 7 | 30992 | dimension 6: 1 |
| 8 | 31752 | dimension 7: 7 |
| 9 | 32196 | dimension 8: 21 |
| 10 | 32492 | dimension 9: 35 |
| 11 | 32658 | dimension 10: 35 |
| 12 | 32730 | dimension 11: 21 |
| 13 | 32758 | dimension 12: 7 |
| 14 | 32766 | dimension 13: 1 |
| 15 | 32767 | none |

If the empty-face matching is omitted, its formerly matched vertex becomes the sole critical zero-cell. Every other critical face has the single positive dimension given in the table. In Forman's discrete-Morse CW model, the complex therefore has exactly one zero-cell and the specified number of cells in a single dimension at least five. Every attaching map for those cells maps its entire boundary to that unique zero-cell; all are nullhomotopic. Consequently the homotopy type is the indicated wedge of spheres, or a point if no positive-dimensional critical cells exist. This proves the integral result without inferring it from field-valued Betti numbers.

The simplicial inclusions as \(r\) increases induce zero on positive-degree reduced homology because no two consecutive noncontractible stages have nonzero homology in the same degree. This determines the complete positive-degree persistence barcode over \(\mathbb Z\) and over every field.

## Verification

Run `python3 verify.py` using only Python's standard library, and compare its exact output with `verification_output.txt`. Each line verifies all admissible masks, matched pairs, all directed Hasse cover relations, gradient acyclicity, critical cell dimensions, and agreement of simplicial and Morse Euler characteristics. The source checks assertions at every stage and ends with `PASS`. The certificate is fully finite and exhaustive; its validity requires no assumption about infinitely many graphs.

## Relationship to prior work

Sawant's 2026 theorem proves vertex decomposability of higher-independence complexes of every tree; it does not provide the fifteen-vertex tree's precise sphere multiplicities, dimensions, or the complete threshold barcode. Ghosh and Selvaraja's 2025 work establishes shellability for broad tree classes but not the exact homotopy spectrum above. Earlier calculations for height-two rooted trees do not determine this height-three tree. This classification refines the known general existence of sphere-wedge decompositions by identifying every integral homotopy stage of a canonical nontrivial rooted tree.

## Limitations

The classification is for this fixed fifteen-vertex full binary tree, not for all tree heights or branching numbers. It does not determine equivariant homology actions or attaching maps between the homotopy wedge models, although every positive-degree induced homology map between consecutive thresholds is zero. An independently performed mathematical audit is not claimed. Equivalent results not indexed by the searched literature sources remain a bibliographic risk.

## References

1. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1, first posted 2026-05-24. https://arxiv.org/abs/2605.25150
2. A. Ghosh and S. Selvaraja, *Shellability of Higher Independence Complexes of Graphs*, arXiv:2505.06614, first posted 2025. https://arxiv.org/abs/2505.06614
3. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145. Standard acyclic-matching theorem.
