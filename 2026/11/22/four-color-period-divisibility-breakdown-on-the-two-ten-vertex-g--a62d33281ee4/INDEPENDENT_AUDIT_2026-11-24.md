# Independent mathematical audit

## correctness

PASS

The prescribed generalized Petersen edges give 15 undirected edges per graph. Base-four encoding bijects all labelled colorings with 0..2^20-1. For each map all coordinates of the new state read the same old state: CCA takes a successor only on contact with that color; GHM advances each nonzero state and activates a zero only on contact with 1. In a finite successor graph, a first repeat on the current trace identifies exactly a primitive cycle; each predecessor outside the cycle inherits its target's period and adds one to its entry time. Equivalently, peeling states without incoming edges leaves exactly the cycles; reverse peel order propagates both values. Counting the two classifications at the identical input index is essential. A separate NumPy implementation enumerated all four maps and reproduced every joint cell, both totals of 1048576, mismatches 275570/272460, nondivisibility counts 258660/245820, and entry maxima (11,8)/(11,11). The nondivisibility cells are (1,4),(1,5),(4,5),(5,4), plus (6,4) on the prism. Direct stepping of seeds 2054 and 6, respectively, gave the two (1,5) witnesses with fixed-state/five-cycle entry times (5,3) and (4,1). Replay: `python3 /workspace/branches/903424a3-8467-4629-91cf-89aa740d0b53/independent_census.py`; full_census.log beside it ends EXHAUSTIVE_CLASSIFICATION_OK. To eliminate possible narrow-buffer wraparound or joint-key collisions, an additional check with wide indegrees and unbounded cycle-length and round counters (`python3 /workspace/branches/automata-range-check.py`) gave actual cycle-length sets {1,4,5,6}, {1,4,5}, {1,4,5}, {1,4,5} in graph/CCA-GHM order, and 11,8,11,11 parallel peeling rounds. Every removed state reaches a cycle in at most the number of rounds. The frozen programs and outputs are supporting evidence, not the independent run. This proves the stated finite counters to extending the three-color divisibility theorem, not a minimum counterexample order or a result for all cubic graphs.

## originality

PASS

Matched-input three-color analysis for exactly these graphs, and four-state GHM marginals on each graph, are demonstrably covered by prior or same-day records and are not the new contribution. The checked statements do not give the matched four-color cross-rule pairing, nondivisibility cells and counts. The same-day prism GHM record is a real overlap on the marginal and is credited as such without inferring priority from its date.

## value

PASS

The first increase beyond the three-color setting tests the actual boundary of a period-divisibility theorem. The two graphs are the natural ten-vertex generalized Petersen pair, with an existing three-color comparison, not arbitrary sampled instances. The same-input witnesses settle failure in both, and the full census measures its prevalence and shows genuinely different joint behavior even with known GHM marginal laws. It is not a repeat of either marginal census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
