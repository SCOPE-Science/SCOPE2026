# Scientific review: optimal four-pebble distributions on the Petersen graph

## Correctness — PASS
The finite result is fully specified over labelled distributions on \(\operatorname{KG}(5,2)\). A one-move recurrence is proved complete by first-move decomposition and termination by a strictly decreasing pebble count. Independent recursive Python and queue-based C++17 programs exhaust all \(715\) configurations of weight four and \(286\) configurations of smaller weights. Their results agree on all five occupancy classes and all six possible four-singleton support geometries; an independent \(S_5\)-orbit check finds \(17\) classes with \(8\) successful ones. All code and the orbit table are supplied. This is a finite exhaustive proof, not an extrapolation from experiments.

## Originality — PASS, with historical risk
Belford and Sieben (arXiv:0707.4256, Proposition 9.2) previously proved that the optimal rubbling and pebbling *numbers* of the Petersen graph both equal four; that claim is not new. The paper's relevant full-text discussion gives the stacked placement but not the complete spectrum or conditional geometric characterization. The earlier thesis discusses different Petersen thresholds, and Katona–Papp (arXiv:1411.0923) treat different graph families. Targeted searches of published mathematical-result records for labelled four-pebble rubbling configurations and matching parameter aliases did not find an implication covering \(175\) versus \(10\). An unindexed computation remains a residual risk; a negative search is not a uniqueness certificate.

## Value — PASS
Equality of the optimum totals hides a substantial feasible-configuration difference: strict rubbling admits \(165\) additional arrangements, including \(90\) with all pebbles separate, while ordinary pebbling admits only ten four-pebble stacks. The four-singleton support forest and double-plus-single triangle characterizations give concrete structural tests, rather than a bare re-tabulation of the known optimum. Such complete configuration classifications are natural inputs for resource-placement and robustness questions about nonlinear graph transport. Scope is deliberately limited to this canonical graph.

Self-review: passed. Independent audit: not yet performed.
