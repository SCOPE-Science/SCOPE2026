# The two edge-orbit Morse fault types of the triangular prism

## Finding
Let \(P=C_3\square K_2\) denote the **one-dimensional**, unfilled triangular-prism graph. Let \(\mathcal M(G)\) denote the ordinary simplicial Morse complex of the graph \(G\), whose vertices are primitive vertex-edge incidence matchings and whose faces are acyclic discrete vector fields. Then every single graph-edge deletion has one of the following two integral homotopy types:
\[
\boxed{\begin{aligned}
\mathcal M(P-e)&\simeq\bigvee^{9}S^3\vee\bigvee^{9}S^4 &&\text{if }e\text{ is a rung},\\
\mathcal M(P-e)&\simeq\bigvee^{16}S^4 &&\text{if }e\text{ is a triangle-rim edge}.
\end{aligned}}
\]
The two types exhaust every graph edge, because the graph automorphism group acts transitively on the three rungs and separately on the six triangle edges. In particular, deleting a rung creates integral third-homology classes, while deleting a rim edge leaves third homology zero. These are actual wedge-of-spheres homotopy statements, not just mod-two Betti numbers.

## Assumptions and scope
The graph \(P\) has vertices \(\{0,1,2,3,4,5\}\) with triangle edges \(01,12,02\) and \(34,45,35\), and rungs \(03,14,25\). The two chosen representatives are the rung \(25\) and the rim \(01\). The two triangles are graph cycles: they are **not filled** as two-simplices. A vertex of \(\mathcal M(G)\) is an incidence \((u,\{u,v\})\), represented by an arrow \(u\to v\). A set of these incidences is a simplex exactly when no graph vertex is used twice as a source, no graph edge is used twice, and the chosen arrows contain no directed cycle. This criterion is equivalent to absence of closed nontrivial discrete gradient paths for a one-dimensional graph. A simplex of cardinality \(k\) has dimension \(k-1\). All chain groups carry the orientation induced by increasing incidence-bit index and use integral coefficients unless expressly specified.

## Proof
**1. Exhaustive finite model.** For a chosen edge deletion, order the remaining eight graph edges as they appear in the displayed prism list. Each edge contributes two possible arrows, giving exactly 16 primitive incidence vertices. Exhaust all \(2^{16}\) possible bit masks and retain those satisfying the three conditions above. For a missing rung this gives 960 faces **including the empty face** and the nonempty face vector by dimension
\[
(f_0,f_1,f_2,f_3,f_4)=(16,98,284,381,180).
\]
For a missing rim edge this gives 1008 faces including the empty face and
\[
(f_0,f_1,f_2,f_3,f_4)=(16,98,286,397,210).
\]
The included `verify_faults.py` enumerates every mask explicitly and enforces the edge and directed-cycle conditions; none of these counts relies on an unexamined partial enumeration.

**2. Exact acyclic face matching.** On all **nonempty** faces, process incidence coordinates in increasing order. At each coordinate pair every still-unpaired face missing that coordinate with its one-element extension, provided the extension is also still available. For a missing rung, the resulting matching has 463 pairs and exactly one unmatched zero-cell, 16 unmatched three-cells, and 16 unmatched four-cells. For a missing rim edge, it has 491 pairs and exactly one unmatched zero-cell, four unmatched three-cells, and 20 unmatched four-cells. The certificate reconstructs every codimension-one face relation, reverses each matched relation, and topologically sorts the resulting directed Hasse diagram, visiting all 959 and 1007 nonempty faces respectively. Thus both matchings are genuinely acyclic. Forman's discrete Morse theorem gives CW models with cells only in dimensions zero, three and four, in the stated counts. In particular each model's three-skeleton is a wedge of three-spheres.

**3. Integer attaching degrees and integral cancellations.** Fix signed boundary coefficients \([g:f]=(-1)^j\) when the \(j\)-th ordered vertex is removed. For every matched lower three-face \(f\) paired with an upper four-face \(g\), replace the contribution of \(f\) by
\[
-\,[g:f]^{-1}\sum_{t\subset g,\ t\ne f}[g:t]\,t.
\]
Because \([g:f]\in\{1,-1\}\) and the matching is acyclic, recursive substitutions terminate. Applying these substitutions to the boundary of each critical four-face computes the exact integer matrix of cellular attaching degrees from critical four-cells to critical three-cells. The standalone checker carries out the substitutions with signed arbitrary-precision integers; it does not infer integer ranks from mod-two data.

The missing-rung matrix has shape \(16\times16\) and reduces by seven successive unit pivots, using integer elementary row and column operations, to \(\operatorname{diag}(I_7,0_9)\). The missing-rim matrix has shape \(20\times4\) and reduces by four unit pivots to \(\begin{pmatrix}I_4\\0\end{pmatrix}\) (matrix transposition according to cell-boundary convention does not affect the unit factors). The checker asserts that **all** entries outside those unit blocks vanish exactly. In the one-vertex, three-/four-cell CW models, an attaching map \(S^3\to\bigvee S^3\) is classified by its integer degree vector, since the Hurewicz map from \(\pi_3\) to \(H_3\) is an isomorphism. Unimodular changes of the sphere bases and cancellation of each unit pair therefore yield exactly nine surviving three-spheres and nine four-spheres for the missing rung, and sixteen four-spheres with no three-spheres for the missing rim. This proves the **integral homotopy** classifications.

**4. Independent exact homology check.** Independently of the face matching and integer Morse differential, the program constructs every original mod-two simplicial boundary and computes its rank by bit-vector elimination. For the rung deletion, ranks in degrees one through four are \((15,83,201,171)\) and reduced mod-two Betti numbers in dimensions zero through four are \((0,0,0,9,9)\). For the rim deletion, ranks are \((15,83,203,194)\) and Betti numbers \((0,0,0,0,16)\). These separate boundary computations corroborate the integer homotopy proof; they do not replace it.

## Verification
Run `python3 verify_faults.py` with a standard Python 3 interpreter. The checker has no third-party dependencies or external inputs. It independently performs the complete finite face enumeration, validates the actual oriented Hasse graph of the finite matching, recursively constructs exact integral Morse attaching degrees, diagonalizes the two matrices using **unit** pivots, and obtains the original mod-two homology via a second boundary-rank calculation. The terminal output has separate `rung` and `rim` summaries and ends with `ALL CHECKS PASSED`. These checks are exhaustive for the two representative graphs; graph symmetry covers all remaining one-edge deletions.

## Relationship to prior work
The definitions and graph-Morse techniques originate in Donovan, Lin and Scoville [1], whose full manuscript studies leaves, cycles with a leaf, centipedes, paths and graph disjoint unions, not either edge-deleted triangular prism. Donovan and Scoville [2] also work with ordinary graph Morse complexes, using star clusters and other methods for path, cycle, tree and windmill-type families; their classifications do not subsume the two fault cases here. A previously published computation [3] establishes mod-two Betti numbers for the **intact** prism Morse complex, and later published integral-homology and symmetry calculations [4,5] refine that intact case. The existing intact homotopy equivalence \(\mathcal M(P)\simeq\bigvee^{64}S^4\) is background and **not claimed as new**. The strong Morse complex studied elsewhere is a different simplicial complex, not an equivalent formulation of \(\mathcal M(P-e)\). The two exact edge-fault statements and their differing integral homotopy types have not been identified in the inspected sources; this comparison does not establish universal novelty.

## Limitations
This is a complete single-edge fault classification **for the six-vertex triangular prism only**; it asserts no general theorem for \(C_n\square K_2\) at larger \(n\), no equivariant cell-level classification, and no persistence statement about the inclusion of either damaged Morse complex into the intact one. The homotopy proof relies on an exhaustive finite certificate provided in reproducible form. Full access to all potentially relevant unindexed theses or manuscripts could not be established; an equivalent unpublished or unindexed computation cannot be excluded. No independent external mathematical audit is asserted.

## References
1. C. Donovan, M. Lin, N. A. Scoville, *On the homotopy and strong homotopy type of complexes of discrete Morse functions*, first public 2019-09-25, arXiv:1909.11440, https://arxiv.org/html/1909.11440v2 .
2. C. Donovan, N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, first public 2022-07-27, arXiv:2207.13780, https://arxiv.org/abs/2207.13780 .
3. *Mod-two homology of the triangular-prism Morse complex*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-mod-2-homology-of-the-triangular-prism-morse-complex--4af8059de6d1 .
4. *Integral \(C_2\)-homology lattice of the triangular-prism Morse complex*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-integral-c-2-homology-lattice-of-the-triangular-prism-morse-comp--741905f1ea33 .
5. *Full prism-symmetry character on the Morse complex of the triangular prism*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-full-prism-symmetry-character-on-the-morse-complex-of-the-triang--cb5204d7444b .
6. N. A. Scoville, M. C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481, https://arxiv.org/abs/2004.10481 .
