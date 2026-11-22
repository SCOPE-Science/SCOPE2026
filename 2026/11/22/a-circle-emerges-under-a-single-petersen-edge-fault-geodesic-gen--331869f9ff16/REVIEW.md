# Scientific review

## Correctness — PASS

The two required fault constructions were verified from shortest-path distances and all face masks, without assuming that graph deletion is simplicial deletion. The acyclic matching certificates and signed integer Morse projections are fully reproducible with `verify.py`. The directed Hasse graph is checked exhaustively, and the sole critical one-cell in the edge-fault case has three zero-degree two-cell attachments. This last homotopical step establishes the circle–sphere wedge rather than merely rational or modular homology. The vertex-fault complex has one critical vertex and two critical two-cells. Checks cover every possible single edge or vertex via explicit label-permutation transitivity.

## Originality — PASS against inspected evidence

The closest primary source, Iršič–Klavžar–Rus–Tuite (arXiv:2401.05696), provides a complete maximal-facet list and general-position polynomial for the *intact* Petersen graph. This covers the combinatorial baseline and its directly implied properties, but is not a formula for graph-metric edge or vertex faults. The source's relevant sections were inspected, alongside foundational Manuel–Klavžar (arXiv:1708.09130) scope and indexed mathematical findings on other graph-geodesic complexes. No covering deletion homotopy claim was located. The possible existence of unindexed equivalent computations remains a residual risk, and complete universe-wide novelty is not asserted.

## Value — PASS

Exact metric-fault homotopy is a natural robustness invariant for the highly symmetric Petersen graph. The first edge fault creates a nontrivial fundamental group and three two-dimensional spheres, while the first vertex fault remains simply connected with two two-sphere summands. These integral homotopy distinctions are not implied by the intact graph's general-position maximum or polynomial. The result addresses both natural one-fault orbits and stops short of unproved general fault laws.

## Scope and limitations

The claim classifies exactly one edge deletion or exactly one vertex deletion, plus the intact baseline. It is nonequivariant and makes no assertion for two simultaneous faults or other Kneser graphs. No independent audit or proof-assistant certification has been performed. The executable evidence is finite exhaustive verification of explicitly bounded ten- and nine-vertex objects, not extrapolation to an infinite family.

Self-review: passed. Independent audit: not yet performed.
