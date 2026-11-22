# Independent mathematical audit

## correctness

PASS

The exact labelled Heawood graph is the Fano incidence j-i in {0,1,3} mod 7; the four-state threshold-one update is deterministic and refractory nonzero states advance unconditionally. Both supplied C++ programs construct this Fano graph and classify all 2^28 states by independent functional-graph algorithms: forward path and indegree pruning, with CSV of 64 nonzero (entry,period) bins. An independently coded C++ exhaustive indegree-pruning implementation was compiled and run locally in 15.72 s using 2.1 GB peak RSS, and found precisely 268435456 total, 3753 periodic states, 531 cycles, maximum transient 14 and 64 nonempty bins; its period-0 table is {1:1,4:896,5:420,6:252,10:840,14:1344}, and its sole time-14 bin is (14,5):2688. The code detects degree and period/depth overflows; graph incidence and update were inspected. This is exhaustive for this finite labelled four-state map, not a general graph theorem.

## originality

PASS

Four-state threshold-one Heawood exhaustive census not implied by classical three-state theory or previous labelled three-state Heawood table; no broader same-parameter complete census identified.

## value

PASS

A natural four-state refractory extension on the uniquely smallest cubic girth-six graph changes the exact recurrent period spectrum and sharp entrance delay relative to the already published three-state Heawood census. A complete 268-million-state deterministic benchmark with 64 entry/period classes is a meaningful exact classification, not a generic restatement of finiteness or a handful of discovered cycles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
