# Scientific review

## Correctness — PASS
The matrix exponential gives the two concentrations exactly. A finite-state Feynman–Kac representation proves strict global convexity of source residual concentration as a function of the cleaning-rate imbalance, including endpoints; it prevents an unsupported local-to-global step. The strictly increasing hyperbolic endpoint derivative has exactly one zero, so the optimal allocation has a unique time transition. The remote-room function increases strictly with absolute imbalance. The asymptotic expansion is proved from the interior first-order condition and is supported, not replaced, by deterministic numerical checks. See RESULT.md and check.py.

## Originality — PASS on inspected evidence
Published tracer transport, indoor air-cleaner placement, two-box exchange, and general compartmental control work were compared at the level of objects, controls, constraints, objectives and implied statements. A general optimal-control theorem for time-variable interventions does not determine the unique fixed-total, time-constant cleaner split for a terminal pulse criterion. Two-box exchange-rate optimization does not vary removal allocations. No inspected material contains the exact constant-budget, source-versus-remote, time-threshold classification. Similarity of the matrix exponential to classical two-state Feynman–Kac formulas is acknowledged; historical mathematical priority remains uncertain, so this is not an assertion of exhaustive novelty.

## Value — PASS
At one fixed filtration budget, the mathematically optimal distribution depends qualitatively on whether cleanup is assessed soon after an impulse or long afterward and on the monitored room. The result gives an exact switch time, unique allocations, a long-horizon scaling law and a distinct universal optimum for the remote-room objective; these help separate placement questions from network-exchange and source-intensity effects. The assumptions are deliberately idealized, so the theorem is a reproducible benchmark rather than a practical installation rule.

## Closest literature and limitations
Matthews et al. (2024) give multizone tracer data; Pei et al. (2024) and Kikumoto–Ooka (2022) address practical placement; Blanchini et al. (2023) supply general compartmental control context. None of these inspected texts was found to imply this exact constant-in-time fixed-budget terminal formulation. Other unpublished, differently indexed, or inaccessible treatments might; independent historical-priority verification is outstanding. Ideal mixing, equal modeled volumes, fixed exchange, and a single source pulse are essential limitations.

Self-review: passed. Independent audit: not yet performed.
