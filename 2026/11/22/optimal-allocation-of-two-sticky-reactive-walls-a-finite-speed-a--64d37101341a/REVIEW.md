# Scientific review: finite-speed reactive-wall allocation

## Correctness — PASS

The backward generator and two sticky-state equations uniquely determine the exact mean time. At fixed \(K\), the derivative of the allocation-dependent quotient has a numerator whose derivative is strictly positive and whose endpoint signs are strict, proving exactly one interior global minimum. Implicit differentiation proves the strict budget-ordering law. Uniform local expansion at the interior large-budget root proves its sharp minimized-time coefficient; the finite-speed distant-wall fraction follows by specializing to an endpoint launch. The standalone checker compares independent boundary-equation solutions to the formula, tests global optimality numerically without using the analytic optimum as its solver, and checks both limits. Boundary cases \(x=0,L,L/2\), finite positive rates, and \(K\downarrow0,K\to\infty\) are covered. No test is presented as an infinite proof.

## Originality — PASS, qualified

Bressloff, *Encounter-based model of a run-and-tumble particle II* (2023, arXiv:2302.01158), §§2 and 5, provides the sticky-wall kinetic model and different wall killing rates but not the fixed-sum global optimizer. Angelani, *Optimal escapes in active matter* (2024), changes tumbling/release parameters and mostly treats a single reactive wall. The closest published fixed-budget Brownian result (2026-10-26) concerns continuous diffusion with Robin killing and has a vanishing remote-wall allocation fraction at boundary launch in the large-budget limit. The closest persistent-particle allocation result (2026-11-02) uses zero-time instantaneous reflection and per-collision capture probabilities, producing an incompatible bang-bang/symmetric phase diagram. A sticky-wall fluctuation-optimization result (2026-11-08) varies bulk tumbling, not a two-wall reactivity split. Reading the relevant full results and the source's material shows the proposed theorem is not a stated or implied instance of these results. Generic prior optimal-control formulations and unindexed equivalents remain a publication-priority risk, not an established uniqueness claim.

## Mathematical value — PASS

The constraint is a natural design budget for two reactive boundary coatings. The theorem proves global interior optimality for all physical parameters, an exact and strictly budget-ordered allocation law, and both endpoint scaling limits. In particular the strong-budget nonzero distant-wall fraction at a boundary start is a qualitative finite-speed distinction from the Brownian reaction problem, where the distant fraction vanishes. The result is a structural design theorem rather than a fixed numerical sample or restatement of an already known first-passage mean.

## Scientific limitations

Finite positive bulk reversal and common bound-state release rates; unbiased initial velocity; known release position; one-dimensional interval; independent memoryless events; linear sum budget in physical killing rates. Other costs, biased launches, non-Markov waiting times, heterogeneous wall release, and distributional optimization may have different optima. The underlying mean can be obtained from established boundary equations; novelty is the full constrained allocation classification and crossover. The published evidence does not eliminate all historical priority uncertainty.

Self-review: passed. Independent audit: not yet performed.
