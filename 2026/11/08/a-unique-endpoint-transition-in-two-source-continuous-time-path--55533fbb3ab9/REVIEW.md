# Scientific review

## Correctness — PASS

The state-space generator is reconstructed independently for short paths and matched against the product of three Erlang completion CDFs. The path has two exterior infection fronts with rate \(\lambda\) and two interior fronts with aggregate rate \(2\lambda\); disjoint Poisson clocks justify the independence needed for the product. The strict Poisson-tail log concavity follows from a decreasing conditional-tail denominator, which proves the global greedy marginal allocation for every integer path order and positive deadline. The endpoint condition is an exact least-retained versus greatest-available increment comparison. Its power-series coefficients have exactly one negative-to-positive sign change when \(n\ge5\); the resulting strictly increasing normalized series proves one positive crossing. The small-path boundary cases and equality placements are treated separately. The checker provides finite regression evidence, not an infinite proof.

## Originality — PASS within inspected evidence, provisional

Fill–Pemantle (arXiv:math/0404015) establishes the relevant Poisson-edge/first-passage setting but develops hypercube percolation and covering-time bounds, not the two-source path deadline optimization. Kempe–Kleinberg–Tardos (DOI 10.1145/956750.956769 and expanded 2015 full text) develops eventual influence and general approximation guarantees, which do not imply this full-coverage-by-time product or its unique endpoint crossover. Van de Bovenkamp–Van Mieghem (DOI 10.1109/SITIS.2014.82) concerns metastable SIS spreading time, a different stochastic process and objective. Related social spreading and percolation records were compared on hypotheses, response variable, and implications, not just their titles. A previously unpublished or missed one-dimensional first-passage placement calculation is a residual priority risk; no independent historical certification is asserted.

## Value — PASS

The deadline is an operationally meaningful epidemic-response or information-diffusion objective, and the optimum changes structurally as the horizon increases: dispersing seed locations to cover multiple fronts is advantageous at short horizons, whereas the two endpoints become uniquely optimal beyond a single sharp horizon. The result is an exact, all-size optimizer and phase boundary in a classical stochastic growth model, not a numerical toy example or a routine reformulation of final-reach influence. It supplies an analytical benchmark for source placement under latency constraints. It does not claim practical validity without calibration.

## Closest literature and limits

The starting SI model is standard, and static reachability on paths also admits gap-allocation decompositions; those alone do not establish the dynamic Poisson-tail threshold. Historical priority remains provisional in the broad first-passage and epidemic-control literature. The finite checker tests, but does not certify the infinite claims. Scope is homogeneous exponential irreversible SI on one finite path with two simultaneous seeds and a fixed deadline.

Self-review: passed. Independent audit: not yet performed.
