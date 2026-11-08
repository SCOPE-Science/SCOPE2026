# Scientific assessment: square-switch metric on \(Q_4\)

## Correctness — PASS

The claim is a finite, fully specified theorem. Rooted Hamilton tours are exhaustive because each Hamilton cycle contains vertex \(0\); fixing its orientation eliminates the single reversal duplication. All \(24\) coordinate squares are enumerated, every disjoint opposite-edge switch is considered, and the result is admitted only if it belongs to the exhaustive Hamilton tour list. Connected components are determined by complete traversal, and every vertex in the unique nontrivial component is used as a BFS source; this reconstructs radius and diameter, not estimates. Independent C++ path-inversion and Python face-switch implementations agree; a complete table of \(1344\) vertex masks and their adjacencies is separately checked. The equivariant quotient is verified under all \(384\) cube automorphisms. Risks: implementation mistakes are bounded by separate paradigms and reproducible code/certificate; no assertion is made for dimensions other than four.

## Originality — PASS, historically qualified

The 2018 work of Contassot-Vivier, Couchot and Héam already defines the exact local move, discusses isolated cycles and gives isolation percentages for dimensions up to five. Gilbert (1958) predates the nine-type classification. None of these ingredients is claimed new. In the inspected substantive main text of the 2018 paper, the **complete metric structure**—one \(1104\)-state mobile component, radius \(10\), diameter \(12\), eccentricity spectrum and orbit-adjacency quotient—is not asserted. The 2016 Gray-code construction paper concerns existence and generation, not distances between arbitrary optimal cyclic listings. Conceptual equality of square switch and subsequence inversion was explicitly checked. The 2018 Table 2 numerical cells were not readable in the available HTML; possible overlap concerning the isolate count is excluded from the originality rationale. Unindexed or inaccessible exact-data sources remain a historical-priority risk.

## Value — PASS

The exact connectivity and metric of an explicitly defined natural local-reconfiguration model answer whether inversion-based generation can reach all movable cyclic Gray codes and establish the worst-case number of moves for \(Q_4\). The symmetry quotient distinguishes two mobile degree-eight types from three frozen types and exposes structural local transition counts. These invariants are not recovered from the known \(1344\) cycle count or the existence of frozen instances; no general higher-dimensional claim or application to mixing is made.

## Closest literature and limits

Gregor–Mütze (arXiv:1607.08806) concerns Gray-code existence and generation. Contassot-Vivier–Couchot–Héam (DOI:10.3390/math6060098) uses the same inverse-subpath operation and reports isolation phenomena but not the complete metric and quotient in the available material. Gilbert (DOI:10.1002/j.1538-7305.1958.tb03887.x) counted types. Historical priority is qualified because the printed numeric table could not be fully extracted, and external independent assessment has not occurred.

Self-review: passed. Independent audit: not yet performed.
