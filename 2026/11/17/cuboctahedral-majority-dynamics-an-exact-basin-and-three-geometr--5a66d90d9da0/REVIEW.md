# Self-review

## Correctness — PASS

The theorem fixes the twelve vertices as the lexicographically ordered edges of the three-cube and defines the synchronous four-neighbor, tie-retaining majority update without ambiguity. The proof is a finite exhaustive proof over exactly \(2^{12}=4096\) states, not a numerical sample. Two separately implemented supplied programs agree on all six first-entry/period classes, all basin sizes, all twenty primitive two-orbits, the sharp update-four witness, and every two-cycle phase's indegree one. The Python checker also constructs the full 48-element spatial automorphism group, whose completeness has an independent triangle-incidence argument, and verifies its orbit sizes. The C++ checker validates each hardcoded neighborhood against the cube-edge incidence definition. The exact claim is therefore supported by the package; there is no inference to larger graphs.

## Originality — PASS with historical-priority risk

Actual mathematical-record searches used the aliases cuboctahedral majority, \(L(Q_3)\) majority, cube-edge voting, exact 146 fixed and 20 primitive two-cycles, isolated two-cycles, and spatial orbit counts. The closest inspected public records are the exact majority censuses for the dodecahedral graph and the four-cube, which concern different underlying graphs and do not imply the stated counts or three-class decomposition. The original arXiv:1405.2486v1 was inspected in its introduction and parts on random four-regular graphs: it gives a general period bound and random/infinite-graph behavior, not this finite exact census. The 2004 full text of Tošić and Agha was inspected, including its one-dimensional setup, Lemma 5, and conclusion: its broad no-incoming-transients assertion means that isolated oscillation **alone is not claimed new**, but it supplies none of the cuboctahedral numerical, basin, or geometric facts. The original 1980 Goles–Olivos article was not available in full and priority remains qualified, though its stated theorem does not enumerate this graph. A search with exact numbers and graph aliases found no covering source. No novelty claim depends merely on a title mismatch.

## Mathematical value — PASS

This is a complete natural graph-specific dynamical invariant for the edge-incidence graph of the smallest ordinary cube, a vertex-transitive four-regular Archimedean skeleton with a transparent 48-element symmetry group. The result distinguishes isolated oscillatory orbits from the overwhelmingly fixed-point attraction basins, identifies three geometrically different oscillation families, and gives a sharp complete entrance-time distribution. It is a motivated finite benchmark for symmetry-sensitive threshold dynamics, not an arbitrary subset or random integer tabulation. Its scope is deliberately finite: neither a general line-graph theorem nor an infinite-family formula is asserted.

## Closest comparisons and limits

Benjamini et al., arXiv:1405.2486v1 (2014), provides general period-two context; Tošić and Agha (2004) studies one-dimensional cellular automata and makes a broadly stated incoming-transient assertion; the two accessible finite-graph majority censuses cover the dodecahedron and four-cube, respectively. No exact cuboctahedral table was found. The Goles–Olivos original full text and potentially unindexed enumerations remain uninspected. Programs prove a finite exact computation only, without independent external certification.

Self-review: passed. Independent audit: not yet performed.
