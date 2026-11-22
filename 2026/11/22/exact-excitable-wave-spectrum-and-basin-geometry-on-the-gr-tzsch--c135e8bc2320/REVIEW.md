# Scientific review

## Correctness — PASS

The vertex and edge definitions in `RESULT.md` determine one unambiguous threshold-one three-state Greenberg–Hastings map on precisely 177,147 configurations. The indegree-elimination proof enumerates every functional-graph component and reconstructs least periods, first-entry times and individual attraction basins, not an experimental sample. An independently implemented trajectory tracer checks the complete period/depth/basin table. A separately implemented cycle-circulation test, invoking the published irrotationality theorem, confirms the 13,887-state extinction basin. An explicit nine-step state verifies sharpness. All checkers were rerun directly from the complete accompanying files.

## Originality — PASS, qualified

The most relevant inspected general-graph results are Gravner–Lyu–Sivakoff (arXiv:1610.07320) and Doba (2018): their extinction/rotation/limiting-activity principles apply to this map but do not provide the Grötzsch-specific exact temporal and basin census. Public research-record searches for Grötzsch/Mycielski aliases and exact period parameters returned results about other graph invariants or excitation on different graphs. The closest archived Grötzsch result concerns **binary majority**, not three-state excitation. Chvátal and Petersen GHM record summaries were compared but their linked full texts could not be inspected, so historical priority remains qualified. No claim that search failure proves absolute novelty is made. Detailed implication checks are in `AUDIT.json`.

## Value — PASS

The first triangle-free four-chromatic Mycielski graph is a canonical test of how a chromatic lift affects excitable-wave recurrence. In contrast to the five-cycle, which has two nonzero period-five attractors, this lift supports exactly 700 period-three, 190 period-four, 330 period-seven and 70 period-ten orbits, sharply settles by nine steps and greatly reduces extinction probability. The complete finite classification, including all basin sizes, provides a benchmark for graph-excitable dynamics; it is more than a routine reproduction of a general theorem.

## Scientific limits

This is a computer-assisted proof for an explicitly finite 11-vertex graph; the standalone exhaustive verifiers are essential evidence. No extension to arbitrary Mycielski graphs, independent external audit or definitive historical-priority certification is claimed.

Self-review: passed. Independent audit: not yet performed.
