# Single-edge stability by elementary collapse in pair-Kneser dissociation complexes

## Finding
For every integer \(n\geq5\), let \(G_n=\operatorname{KG}(n,2)\) be the graph on the two-element subsets of \([n]\), adjacent precisely when disjoint. For a graph \(G\), write \(\operatorname{Ind}_2(G)\) for the simplicial complex of vertex sets whose induced subgraph has maximum degree at most one (equivalently, induced components have at most two vertices). **For every graph edge \(e\) of \(G_n\)**, the larger complex \(\operatorname{Ind}_2(G_n-e)\) collapses by exactly \(12(n-4)\) elementary simplicial free-face pairs onto \(\operatorname{Ind}_2(G_n)\). The former has exactly \(24(n-4)\) additional faces, and the natural inclusion is a simple-homotopy equivalence, hence an integral homology isomorphism in all degrees.

As a consequence of the previously established intact-complex classification, both complexes have homotopy type \(\bigvee^{\binom{n-1}{4}}S^3\). The new result is the explicit all-order *relative simplicial collapse*, not a new derivation of the intact homotopy type.

## Assumptions and scope
All graphs are finite, undirected, and simple; the graph edge deleted from \(G_n\) is an edge between two disjoint two-subsets of \([n]\), not a deletion of a vertex, nor an edge of the geometric realization. The parameter of higher independence is exactly two. A simplicial collapse means deleting a face \(\sigma\) and its unique codimension-one coface \(\tau\), when \(\tau\) is the only strict coface of \(\sigma\) in the remaining complex. A face means any simplex including the empty face; none of the collapses removes the empty face.

By permuting \([n]\), every graph edge is equivalent to the edge connecting the graph vertices `01` and `23`, where `ij` abbreviates the pair \(\{i,j\}\). We use ground labels \(0,\dots,n-1\), so in the argument \(n\ge5\) provides an external ground label \(w\notin\{0,1,2,3\}\).

## Proof
**Step 1: Unique five-label support of every new face.** Put \(X=\operatorname{Ind}_2(G_n)\) and \(Y=\operatorname{Ind}_2(G_n-e)\), with \(e=\{01,23\}\). Deleting an edge can only remove induced adjacencies, hence \(X\subseteq Y\). Take \(\sigma\in Y\setminus X\). Because the two induced graphs on \(\sigma\) differ only in adjacency `01`--`23`, the vertices `01` and `23` both belong to \(\sigma\). Otherwise \(\sigma\) would already belong to \(X\). Some further selected pair must have been adjacent in \(G_n\) to at least one of `01`, `23`; otherwise removing their mutual adjacency would not have repaired a degree-two violation.

Every additional selected pair disjoint from `01` must meet `23`, because a pair disjoint from both would itself have degree at least two in the *faulted* induced graph (it would still be adjacent to both `01` and `23`). Such an additional pair therefore has form `2w` or `3w`, where \(w\notin\{0,1,2,3\}\). Symmetrically a pair disjoint from `23` must be `0w` or `1w`. No selected pair can have both endpoints outside \(\{0,1,2,3\}\), because that would again be disjoint from both `01` and `23`.

There is **exactly one** external label \(w\) among all selected pairs: two pairs `iw` and `jz` with \(w\ne z\) either both meet the same fixed pair `01` or `23`, so that the other fixed pair gets two neighbors, or they come from opposite blocks \(\{0,1\}\) and \(\{2,3\}\), in which case `iw` and `jz` are disjoint and each already has a distinct neighbor among `01`, `23`. Either possibility violates the degree-at-most-one condition. Thus every new face belongs to a uniquely determined five-ground-label system \(\{0,1,2,3,w\}\). Faces with different external labels do not coincide or contain each other.

**Step 2: Complete local certificate.** Work on the ten graph vertices indexed by two-subsets of \(\{0,1,2,3,4\}\). Applying the degree-at-most-one condition before and after deleting `01`--`23` gives exactly 24 new faces: four three-vertex faces, twelve four-vertex faces and eight five-vertex faces. They partition into the following twelve successive face pairs. Each left entry is a free face at that step, and the right-hand item is the unique vertex adjoined to obtain its only remaining strict coface; every pair contains only new faces.

| Step | Free face (graph vertices) | Adjoin |
|---|---|---|
| 1 | `01 14 23 34` | `13` |
| 2 | `01 14 23 24` | `12` |
| 3 | `01 04 23 24` | `02` |
| 4 | `01 13 23 34` | `03` |
| 5 | `01 02 04 23` | `03` |
| 6 | `01 04 23 34` | `03` |
| 7 | `01 04 23` | `03` |
| 8 | `01 23 34` | `03` |
| 9 | `01 12 23 24` | `02` |
| 10 | `01 13 14 23` | `12` |
| 11 | `01 14 23` | `12` |
| 12 | `01 23 24` | `02` |

This is a finite *exhaustive local proof certificate*, not an inference from a bounded sample of graph orders. In the ten-vertex local graph, the exact face condition is checked on every subset of its vertex set; each row's candidate has exactly the single indicated strict coface in the current complex. Every new local face occurs once in the twelve two-face intervals. The self-contained `verify.py` replays those assertions using the graph definition and integer subset masks, without external packages.

**Step 3: Lift to all \(n\).** For every external label \(w=4,\ldots,n-1\), transport the twelve-row certificate by replacing the ground label `4` with \(w\). Step 1 proves that all newly admitted faces lie in exactly one such local block, and that strict cofaces of a new face cannot pass into a different block or into \(X\) (the latter is downward closed). Consequently each transported row remains an elementary free-face collapse in the full complex, regardless of which other blocks were processed. The \(n-4\) blocks contain exactly \(24(n-4)\) new faces, and their \(12(n-4)\) collapses remove all and only those faces, leaving exactly \(X\). Every graph edge \(e\) is equivalent to `01`--`23` under a ground-set permutation, completing the proof.

## Verification
Run `python3 verify.py` in this directory, with Python 3.8 or newer. It constructs the original and faulted graph directly from pair disjointness, enumerates *all* admissible simplices for \(n=5,6,7\), verifies that each new face has one external ground label, checks the bijection to local blocks, and replays every free-face collapse by testing the **entire set of strict cofaces**, not merely the proposed facet. Outputs are: for \(n=5\), 261 old faces, 285 faulted faces, 24 additional faces and 12 collapses; for \(n=6\), respectively 747, 795, 48 and 24; for \(n=7\), 1751, 1823, 72 and 36. It ends with `UNIVERSAL_5_LABEL_COLLAPSE_CORE_PASS`.

The unrestricted conclusion follows from the proved five-label localization and the complete local certificate. Enumerations at the three sample orders are independent reproducibility checks, not the sole justification for arbitrarily large \(n\). No integral homology matrix computation is necessary: a sequence of elementary collapses directly proves the claimed simple-homotopy equivalence over the integers and with arbitrary coefficients.

## Relationship to prior work
Deshpande and Singh introduced the higher-independence framework and classified several graph families, but not the faulted pair-Kneser complex. Brešar and Dravec proved the relevant pair-Kneser dissociation-number bound and the fixed-four-label containment of *intact* dissociation faces, but their statement does not address the larger face set after graph-edge deletion, an induced inclusion, or elementary collapses. Previously published work on pair-Kneser two-independence complexes identifies the intact homotopy type and integral symmetric-group module; neither classification by itself implies that the specific inclusion after a graph-edge fault is a simple-homotopy equivalence. A published dissociation enumerator and maximal-face classification likewise concern the intact graph; knowing the intact face polynomial does not determine the homotopy of a different faulted complex or the natural map. Those previous results are credited, not reasserted as novel.

## Limitations
The statement concerns a **single** deleted Kneser graph edge and higher-independence parameter two; it does not cover multiple deleted edges, vertex deletion, or general \(\operatorname{KG}(n,k)\) with \(k>2\). The collapse is not claimed to be equivariant for every arbitrary choice of local pair order. The proof uses a complete finite five-label certificate after a structural reduction; no partial enumeration or unproved extrapolation is used. Targeted literature comparisons do not exclude every unindexed or unavailable equivalent proof; no independent external audit has been performed.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, first posted 2020-01-15. https://arxiv.org/abs/2001.05448
2. B. Brešar and T. Dravec, *On the Dissociation Number of Kneser Graphs*, arXiv:2108.10801, first posted 2021-08-24; especially Proposition 2.1. https://arxiv.org/html/2108.10801v1
3. *Three-sphere wedges and integral symmetry in two-independence complexes of two-subset Kneser graphs*, published mathematical record, 2026-10-18. https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-three-sphere-wedges-and-integral-symmetry-in-two-independence-co--5e44dcadc7a9/RESULT.md
4. *Dissociation polynomials and maximal-set purity of \(KG(n,2)\)*, published mathematical record, 2026-11-08. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-dissociation-polynomials-and-maximal-set-purity-of-kg-n-2--2b36dd2818f0/RESULT.md
