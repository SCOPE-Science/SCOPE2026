# Scientific review

## Correctness — PASS
The exact finite theorem has a complete vertex and edge definition and a fully specified tie-retaining synchronous majority rule. Two independently implemented exhaustive algorithms compute and trace **all** 2048 binary states and agree on 20 fixed states, 61 primitive two-cycle orbits, complete basin sizes, and first periodic-entry counts. The first checks \(F^8=F^6\) and the sharp failure of \(F^7=F^5\) for every state; the second verifies the 12 automorphisms and all geometric classes. The tests were executed from the complete candidate package without missing supporting data. A finite exhaustive proof applies only to this graph.

## Originality — PASS, with historical-priority risk
The primary literature of Goles and Olivos and the inspected complete text of Kuhlman–Mortveit–Murrugarra–Kumar (arXiv:1108.2974, Section 3 and Appendix A) establish general recurrence restrictions, but not this graph-specific full functional-graph census. Searches of the relevant literature and published graph-dynamics records for the Herschel graph, exact majority basins, aliases and stronger classifications found no directly dominating claim. The Heawood, Pappus and Chvátal classifications apply to other named graphs; their numerical claims do not imply the 18-edge Herschel census. No exhaustive pre-publication priority proof is claimed; unindexed computations or omitted graph catalogues remain possible.

## Value — PASS
The Herschel graph is a natural, minimal non-Hamiltonian polyhedral graph with a mixed degree sequence; it is a motivated finite benchmark rather than an arbitrary graph slice. The complete exact phase-space classification distinguishes **when** a configuration settles from **which** attractor it reaches, and demonstrates three discrete equilibrium-basin scales, six oscillation-basin scales, and a sharp six-update delay occurring exclusively in fixed-point basins. It further classifies all periodic orbits up to the graph's symmetries. These quantities are not consequences of the known period-at-most-two theorem and are suitable as an independently reproducible reference case.

## Evidence and limits
See `RESULT.md` for the edge list, definitions, full counts, proof and primary references; `check_functional.py` and `check_trajectory_symmetry.py` supply exact reproductions. The work is finite, has not undergone independent audit, and may have an unindexed precedent. A literature search cannot establish absolute priority.

Self-review: passed. Independent audit: not yet performed.
