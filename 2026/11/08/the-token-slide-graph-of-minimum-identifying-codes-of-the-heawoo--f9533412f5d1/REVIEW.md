# Self-review: Heawood optimal-code token slides

## Correctness — PASS

The complete 14-vertex state space contains exactly 16384 subsets. For each subset, every required identifying signature is computed as a closed-neighborhood bitmask intersection. The test for fourteen nonempty, distinct signatures is necessary and sufficient. Both checkers enumerate every possible set of size at most seven and agree on exactly 268 minimum size-seven sets, with every individual integer mask checked against `states.txt`. Every possible pair of these states is tested for changing one code vertex and for the original Heawood incidence edge connecting the removed and inserted positions; all 210 resulting legal token-slide edges are reproduced identically. Full component traversals certify 56 claws and two 21-leaf stars. The sharp pairwise reachable-distance spectrum then follows by counting within stars: 210 at one move and 588 at two moves. The proof is exact finite enumeration, with no unproven generalization.

## Originality — PASS, with explicit scope restriction

The known minimum identifying-code count 268 and the previously determined 658-edge, three-component **token-jump** graph on these same codes are not new findings and are not presented as such here. A slide is instead a codeword exchange **along an edge of the original Heawood incidence graph**. No unlabeled abstract representation of the jump graph logically specifies this distinguished edge subset; the complete slide classification 56K1,3 plus 2K1,21 must be recomputed with incidence information. The earlier same-object jump statement does not assert it.

The closest examined published work is Balbuena--Foucaud--Hansberg (arxiv:1407.7263v1), which proves other Heawood code and locating-domination properties, and Mynhardt--Teshima (arxiv:1707.02039v1), which sets up the general identifying-code slide graph and gives realizability of arbitrary targets by constructed input graphs. Relevant chapters of Teshima's 2022 thesis discuss these general frameworks. None of the examined primary text establishes the star forest for the Heawood graph **as input**. An unpublished table containing the same slide edges is a genuine residual priority risk; failure to find one is not a uniqueness proof. Detailed searches, source inspections, implications and aliases are recorded in `AUDIT.json`.

## Value — PASS

The theorem determines the entire move graph for a canonical finite projective-plane incidence object under the original adjacency-restricted model. It gives the non-obvious phenomenon of 58 components but no completely immobile optimal code, with only two nontrivial sizes of reachable states. This is not a mere recount of optimal codes: changing from jumps to slides fragments a previously connected 224-code jump component into 56 isolated claws, establishing precisely which local improvements can be connected without relocating a codeword across a non-edge. The shortest reachable distances, degrees and component geometry are all exact. No generalization is falsely claimed.

## Boundaries and evidence

Evidence consists of the decoded `states.txt`, `slides.txt`, `jumps.txt`, `verify_python.py`, and `verify_cpp.cpp`, all embedded in the same finding as this report. The two independent enumerators use set-based and bitmask-based constructions and compare entire lists, not just totals. They cannot rule out unindexed historical work and do not certify any larger projective-plane family.

Self-review: passed. Independent audit: not yet performed.
