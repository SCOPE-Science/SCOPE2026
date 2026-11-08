# Scientific review: exact first-entry-time law for three-state bipartite excitation

## Correctness — PASS

The claim is restricted to positive shore sizes and synchronous three-state threshold-one Greenberg–Hastings updates. On a complete bipartite graph, each vertex in a shore sees the same binary external excitation signal. Consequently the pair of nonempty color supports evolves autonomously under a fully specified 49-state map. The displayed complete support-distance table can be reconstructed entry-by-entry, with only three recurrent support components: all-rest, all-three-colors on both shores, and a two-support alternating pair. Direct examination of the pointwise update shows that these correspond exactly to full-state least periods 1, 3 and 4, respectively. Thus the support distance equals the actual first-entry time even in the period-four case. Surjection counts for each exact color support yield the ten joint time/period formulas for all positive parameters. Two separate Python 3 programs reproduced the support coefficients and directly iterated 63,972 labelled configurations; no finite simulation is used as the all-parameter proof.

## Originality — PASS, qualified

General periodic-orbit behavior, activity, and irrotationality criteria are established for three-state excitable cellular automata by Gravner–Lyu–Sivakoff (2016) and Doba (2018). Earlier Greenberg–Hastings work establishes the model, and existing all-color complete-bipartite work enumerates the recurrent configurations. Those results do not state the full period-refined first-entry time law. Prior studies of one-edge-defective bipartite and complete tripartite three-state excitation have different underlying graphs and cannot be specialized to the intact two-shore map; the previously known four-step upper bound for the intact graph is not claimed as new. Here the specifically assessed object is the ten-class finite-time distribution \(N_{t,p}(m,n)\), its last-entry extinction count and the exact time-resolved split of basins. Literature searches for complete-bipartite Greenberg–Hastings entrance distributions and coefficient data did not identify an equivalent formula. Search incompleteness remains a priority risk, not a proof of novelty.

## Value — PASS

The intact complete bipartite graph is a natural mean-field excitable network on which every vertex in a shore shares the same input. The finite-time distribution makes that dynamical symmetry quantitatively useful: it distinguishes rapid periodicity from extinction, proves exactly which transient classes can reach a four-cycle, and counts a sharp fourth-step extinction population. It provides a complete baseline for interpreting how changing the connection pattern alters entrance-time statistics, whereas a census of periodic configurations alone cannot recover any of these time-dependent counts. The result is a mathematically motivated all-size temporal classification, not an arbitrary numerical slice.

## Closest literature and limitations

Greenberg–Hastings (1978) defines the model. Durrett–Griffeath (arXiv:patt-sol/9303002, 1993) examines lattice asymptotics. Gravner–Lyu–Sivakoff (arXiv:1610.07320, 2016) determines general fixation and activity; Doba (DOI 10.25088/ComplexSystems.27.2.101, 2018) gives an arbitrary-finite-graph cycle-density law. Neither inspected full-text result supplies the ten time/period coefficients. An uncatalogued exact enumeration may nevertheless exist. The theorem excludes higher-color, stochastic, asynchronous, and non-complete-bipartite models. An independent mathematical assessment has not been carried out.

Self-review: passed. Independent audit: not yet performed.
