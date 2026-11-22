# Scientific assessment

## Correctness — PASS

The leaf-coverage cap is \((k-1)^2+1\) for \(k\) ignitions. Equality forces disjoint time-labelled intervals of lengths \(2k-3,2k-5,\ldots,3,1,1\), precisely the claimed source types. The proof checks both the final singleton's parent core and the strict pairwise ignition-distance constraints, establishing an exact bijection, not only a construction. Fixing all but one time-coordinate determines every leaf interval, making the exchange graph a disjoint matching. An independent breadth-first-search C++ enumeration verifies all legal sequences for \(k=3,4,5\); a distinct cyclic-tiling Python checker verifies constructions for \(k=3,\ldots,7\) and exchange adjacency for \(k=3,4,5\). Neither finite test is offered as an infinite proof.

## Originality — PASS with residual priority uncertainty

The earliest cited public conceptual source is the 23 July 2015 original arXiv version of *How to burn a graph*. Jenifer–Shanthi (2026, Theorem 3.4, fully inspected) gives the scalar sunlet burning number only; its formula is expressly treated as already known. Searches for sunlet burning histories, optimal source counts, critical pendant tilings, and single-round exchange geometry in external literature and mathematical-result records did not identify a covering statement. The closest reconfiguration records concern undecorated paths and cycles, where the pendant-coverage constraint is absent. Unindexed prior counts remain a priority risk; negative searches alone do not establish novelty.

## Value — PASS

The previously studied minimum number of rounds leaves open *which* source schedules realize it and whether optimum schedules can adapt when one source changes. At a natural infinite sequence of tight capacity boundaries, the answer has factorial multiplicity but maximally fragmented mobility: the exchange graph has only two-vertex components. The exact structural bijection and mobility obstruction distinguish this result from merely recomputing the known scalar burning number and provide a baseline for slack-length schedule reconfiguration.

## Limits and closest literature

The result applies only to saturated one-leaf cycle coronas, standard strict deterministic burning, and source replacements at a fixed round. The 2026 scalar theorem and standard 2015 burning definitions are acknowledged. Related bare-cycle schedule classifications have different domains and do not imply the sunlet result. Priority uncertainty persists for inaccessible or unindexed sources. No external independent proof check has been conducted.

Self-review: passed. Independent audit: not yet performed.
