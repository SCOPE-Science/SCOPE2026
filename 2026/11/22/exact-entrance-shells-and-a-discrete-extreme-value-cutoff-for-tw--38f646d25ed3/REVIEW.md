# Scientific comparison and self-review

## Correctness — PASS

The identity \((F^t x)_i=\bigvee_{j=0}^t x_{i-t-j(s-1)}\) is proved by shift commutation and OR idempotence. Its residue-class saturation proves that the entire recurrent set is precisely the class-constant set, with sharp entrance time \(m-1\). A finite automaton counts the exact circular zero-run obstruction, and class independence gives the transient shells; direct preimage enumeration gives the basin weights. The critical Poisson law follows from explicit rare-block factorial moments. Direct exhaustive tests across 55 parameter pairs with \(n\le12\), independent transfer tests for 104 parameter cells, and exact phase-fiber checks all passed. Risks: the Poisson theorem is limited to fixed \(g,c\) and independent fair input; numerical checks do not establish the infinite limit, for which the factorial-moment proof is provided.

## Originality — PASS, with limitations

Jarrah–Laubenbacher–Veliz-Cuba (2008) describes the periodic necklace skeleton and associated cycle lengths on connected OR networks; this component is expressly excluded from novelty. Gao–Chen–Başar (2016) studies single-bit perturbation stability, not the complete labelled basin or first-entrance shell law. Gadouleau (2021) treats images, periodic points and fixed points of disjunctive networks, rather than the displayed forbidden-word transient census. Goles–Noual (2012) addresses scheduling and has been checked at title/abstract level only. Generic circular-run and Poisson approximation methods are known, but the complete two-jump network classification and gcd-sensitive clocks were not identified as pre-established in the inspected primary literature. Closest related indexed records concerned sequential bi-threshold cycle basins, cyclic Rule 178 relaxation, and contact dynamics on complete graphs; none implies this result without new analysis of the two-shift disjunctive map. Priority uncertainty persists for unindexed equivalent one-dimensional OR-rule results or inaccessible full texts; these are not represented as fully excluded.

## Mathematical value — PASS

The dynamics supplies an infinite arithmetic family in which changing a single input jump can change the sharp convergence time and every entrance-shell count without changing network size. Exact basin weights refine the familiar recurrent necklace classification, and the rare-block result determines a discrete asymptotic distribution for the time taken to reach recurrence. The classification is natural because the same denominator \(\gcd(n,s-1)\) controls connected cyclic classes, deterministic worst-case propagation, exact time populations, and stochastic entrance. It does not purport to be a broad graph theorem or a new Poisson approximation technique.

Self-review: passed. Independent audit: not yet performed.
