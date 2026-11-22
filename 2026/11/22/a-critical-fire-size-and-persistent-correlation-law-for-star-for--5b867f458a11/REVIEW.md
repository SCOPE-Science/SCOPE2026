# Self-review

## Correctness — PASS

The claim specifies a finite star, per-site exponential growth/lightning clocks, the distinction between hub-containing and singleton leaf fires, the exact finite-size marked law, and both critical and stationary weak limits. The hub fire resets every vertex, giving an exact regenerative decomposition. Before hub growth each leaf is an independent two-state birth–death process; afterward the marked killing hazard is \(\lambda(1+K)\). Integrating independent killed leaf paths yields the stated finite rational law. A separate continuous-time Markov-chain generator gives identical exact rational absorption probabilities in 30 parameter cases. The weak limit follows from a uniform leaf law of large numbers and the integrated hazard; uniform renewal tails justify passing to stationarity. The covariance formula follows from exchangeability and variance convergence, and its strict positivity from the nondegenerate age law. The numerical/exact checks are supportive, not a substitute for the all-size proof.

## Originality — PASS on bounded examined evidence

Searches of the primary model literature and relevant public mathematical-result records found no statement of the exact hub-fire size law, its growing-degree star scaling \(n\lambda_n\to c\), and the stationary persistent-leaf covariance. The closest scientific mechanisms are Drossel–Schwabl's original forest-fire model; van den Berg–Brouwer and Stahl's spatial continuous-time fires; Volkov's half-line boundary ignition; Graf's fixed-branching rooted trees; and an independent-patch catastrophe model with an exogenous constant-rate reset. Their graph geometries, ignition rules, or observables differ, and the last model's reset-time mixture does not imply the state-gated, occupancy-dependent hazard here. These are statement-level comparisons, not novelty claims based only on title differences. The original 1992 full paper was not accessible in this review; hidden earlier finite-star or catastrophe-PDMP analyses remain possible.

## Mathematical value — PASS

The precise hub-fire event is natural on a high-degree star because only those fires reset the entire graph; it is not an arbitrary finite coefficient. The aggregate scale \(n\lambda_n\) balances leaf lightning with tree regrowth. The result supplies a complete nondegenerate critical burst-size density, an exact finite rational law, and a stationary correlation mechanism which remains positive between any two distinct leaves even as the population grows. The full-fire to uniform-fire transition, and the limiting covariance of \(1/12\), distinguish time-sampled stationary forests from event-sampled fires. The result is an analytically testable benchmark for state-dependent collective-reset dynamics.

## Closest literature and limitations

- Drossel and Schwabl, *Physical Review Letters* 69 (1992), 1629; model origin, not the growing-degree star theorem.
- Van den Berg and Brouwer (2004), arXiv:math/0412488; continuous-time square lattice and critical time.
- Volkov (2009), *ALEA* 6, 399–414; boundary ignition on the half-line; the full-text introduction and theorem statements concern a different geometry and ignition regime.
- Stahl (2012), arXiv:1203.5533; stationary existence on \(\mathbb Z^d\), not the finite-star marked distribution.
- Graf (2014), arXiv:1404.0325; full text treats finite-depth subtrees of fixed branching factor, unlike a one-level star with diverging degree.
- “Exact catastrophe-rate staircase for the most probable number of occupied habitat patches,” public RESULT.md (2026); independent constant-rate global catastrophes and modal ranks, not endogenous occupancy-dependent hub fires.

The finding does not give the fire-size law sampled over all lightning events, spatial lattice universality, or a simultaneous \(c\)-and-\(n\) limit. Complete historical priority is not certified.

Self-review: passed. Independent audit: not yet performed.
