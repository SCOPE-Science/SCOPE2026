# Scientific audit — 2026-09-30

## Final claim assessed

For every linear 3-uniform hypergraph on n at least 6 vertices, the fraction of six-vertex sets containing a spanning loose triangle is at most 120 times n minus one divided by the product of n minus two, n minus three, n minus four, and n minus five, and hence the corresponding asymptotic density is zero, even without the Fano-free restriction.

## Correctness — PASS

Each hit six-set contains at least one spanning loose triangle. Counting a loose triangle through any of its three corner vertices gives at most four completions per unordered pair of incident edges, so three times the triangle count is at most four times the sum over vertices of the number of incident-edge pairs. Linearity bounds every degree by half of n minus one, yielding a triangle count at most one sixth of n times the square of n minus one and exactly the stated normalized bound. Independent exact arithmetic reproduced the threshold values and monotonicity.

## Originality — PASS

Searches found standard loose-triangle extremal literature and Fano-plane edge-extremal literature, but not this six-set-density statement or the same explicit bound. The Fano-free hypothesis is irrelevant to the proof, which is a separate normalization from the edge-extremal problems in the inspected sources.

The comparison explicitly checked equivalent formulations, broader coverage, exact databases or tables, and implication from prior results. Structured searches, source inspections, checked sources, and residual risks are recorded in `INDEPENDENT_AUDIT_2026-09-30.json`.

## Scientific value — FAIL

The result mainly exposes a normalization mismatch: linearity forces only cubic-order many loose triangles, while the denominator counts sixth-order many vertex sets. The proof is a short incidence estimate, the Fano-free condition drops out entirely, and no natural extremal constant or structural boundary remains after the zero limit is observed. Under the stated bar this is a cheap normalization disproof rather than a substantive mathematical gap.

## Disposition

**FAILED**. This assessment records the mathematical status of the claim and does not assert formal verification or external certification.
