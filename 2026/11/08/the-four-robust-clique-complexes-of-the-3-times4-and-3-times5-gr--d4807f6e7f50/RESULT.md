# The four-robust clique complexes of the \(3\times4\) and \(3\times5\) grids are wedges of 20 and 56 five-spheres

## Finding
Let \(G_{3,n}=P_3\square P_n\), where \(n\in\{4,5\}\). The four-robust clique complex \(K_n=\mathsf{Cliq}_4(G_{3,n})\) consists of all vertex subsets whose induced graph contains no independent set of four vertices. There are exact **integral homotopy equivalences**
\[
K_4\simeq\bigvee^{20}S^5,\qquad K_5\simeq\bigvee^{56}S^5.
\]
For these two widths the number of spheres equals \(\binom{2(n-1)}3\), the number of triples of unit squares in the \(3\)-row grid. This numerical agreement is stated only for these two widths.

## Assumptions and scope
The graph has vertices \((i,j)\), \(0\le i<3\), \(0\le j<n\), with an edge exactly when the Manhattan distance equals one. Simplices include the empty set. A set is allowed precisely when it contains no independent four-subset. In the included verifier the vertex \((i,j)\) is encoded by \(in+j\), a simplex by an integer bit mask, and the dimensions are simplex cardinalities minus one.

The bipartition by parity of \(i+j\) is independent in the grid. Every seven-vertex subset has at least four vertices in one parity class; hence every allowed face has at most six vertices. This bounds exhaustive enumeration independently of any computation.

## Proof
**Complete face census.** Enumerate all four-element vertex subsets and retain those having no grid edge. A vertex subset is an allowed simplex if and only if it contains none of those independent four-subsets. The executable verifies this literal condition over all \(2^{3n}\) vertex subsets, without relying on a homology solver. For \(n=4\), the face counts by cardinality \(0,1,\dots,6\) are \((1,12,66,220,434,466,217)\); for \(n=5\), they are \((1,15,105,455,1089,1323,654)\).

**Explicit acyclic matchings.** Work initially on the augmented face poset, including the empty face. For each grid-vertex index \(v\) in the prescribed order, pair each currently unpaired face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), provided that latter face is present and currently unpaired. Remove both members of every pair before the next stage. The exact ordered vertex lists, using zero-based row-major indices, are:

\(n=4\): `1,9,8,5,10,2,3,7,4,0,11,6`;

\(n=5\): `7,8,9,6,5,14,13,12,11,10,4,3,2,1,0`.

No ambiguity from iteration order arises because all pairs within one stage are disjoint. Every pair is a codimension-one face incidence. The verifier builds the **entire** oriented Hasse graph: unmatched incidence arrows run from larger to smaller face and matched incidence arrows run in the reverse direction. It topologically sorts that graph, confirming no directed cycles for either width. This is a complete finite acyclicity check, not a sample or random trial. The augmented matchings leave only 20 and 56 unmatched simplices, all of cardinality six. In both cases the empty face is paired with a singleton; deleting that single matching pair and excluding the empty face leaves one critical vertex and the same 20 or 56 critical five-simplices. The full ordinary face-poset Hasse digraph is again exhaustively checked acyclic after this change.

**Homotopy consequence.** The discrete-Morse CW theorem gives a complex with exactly one zero-cell and respectively 20 or 56 five-dimensional cells, and no other cells. Every attaching map of a five-cell to its zero-skeleton is constant. The Morse CW complex is therefore the asserted wedge of five-spheres, establishing the integral homotopy result without a passage from field homology ranks. In particular all positive reduced integral homology vanishes except \(\widetilde H_5\cong\mathbb Z^{20}\) or \(\mathbb Z^{56}\), respectively.

## Verification
The standalone `verify.py` requires only the Python standard library and runs with `python verify.py`. It reconstructs each complex, checks every face against the explicit forbidden-independent-four-set criterion, applies the recorded matching orders, checks every oriented Hasse incidence for acyclicity, and prints all critical-cell counts. Its recorded output is in `verification_output.txt`. It checks 1,415 and 3,641 nonempty faces; the oriented Hasse graphs have 6,160 and 16,470 incidences, respectively. The full output ends in `ALL_VERIFY_OK`. Reproduction is complete for these finite cases; no results for larger widths are inferred from it.

## Relationship to prior work
M. Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, first posted February 11, 2026, proves the sphere-wedge formula for all rectangular grids at robustness two or three and for arbitrary robustness in square sequences assembled only by edge gluing (Theorem 1.1 and Corollary 1.3). Conjecture 1.5 asks for sphere wedges in general square sequences, and its discussion explicitly identifies the corner-gluing step for robustness greater than three as a difficulty. The two rectangular graphs treated here require corner gluing in the natural square-sequence construction, so the present four-robust results are not consequences of the cited edge-only corollary. The earlier total-cut results summarized in that paper cover different robustness thresholds. Prior exact classifications of the four-robust square grids and of the three-by-three four-robust grid concern different graphs and do not imply these two homotopy statements. Comparisons were made on the precise graph, robustness threshold, and homotopy statement, including the Alexander-dual total four-cut interpretation.

## Limitations
This is an exhaustive finite result for exactly two rectangles, not an infinite-width theorem, a proof of the general square-sequence conjecture, or an equivariant homotopy decomposition. The numerical agreement with the binomial prediction does not establish a recurrence. Neither a direct integral cycle basis nor symmetry representation is supplied. An unindexed equivalent calculation may exist; independent mathematical audit is not performed.

## References
- Marek Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first public version 2026-02-11; especially Theorem 1.1, Corollary 1.3 and Conjecture 1.5. https://arxiv.org/abs/2602.11365
- Himanshu Chandrakar, Nisith Ranjan Hazra, Debotosh Rout and Anurag Singh, *Topology of total cut and cut complexes of grid graphs*, arXiv:2408.07646 (2024), as compared via the discussion and references of Filakovský's paper. https://arxiv.org/abs/2408.07646
- Robin Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145; the standard acyclic-discrete-Morse matching theorem.
