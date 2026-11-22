# Self-review

## Correctness — PASS

The two-stage NOR update factors exactly into opposite nonbranching Boolean shifts with hard resets to one. Each cyclic fault gap contributes \((g-t)_+\) independent surviving bits per stream after \(t\) return steps; multiplying the two free-bit counts gives the exact first-entry spectrum, and a divisor-lattice argument gives the entire no-fault orbit census. Standard disjoint-block and union-bound arguments prove the random-fault asymptotic. The supplied graph-based exhaustive check and a separate source-transport check agree. Scientific limits: the computation covers finite sizes, and the unbounded claims rest on the algebraic and probabilistic proof, not extrapolation.

## Originality — PASS with remaining historical risk

Searches for matching switching, NOR, reset dynamics, periodic Boolean networks, alternate lower approximations and fault gap first-entry formulas found no equivalent complete result. The closest alternating rough-approximation finding uses the lower AND operator and random initial-state cutoff, not a NOR network with random fixed deletions; its conclusions do not imply the present individual faulty-map basins. The temporal matching-infection finding uses monotone OR reachability, not complement-and-reset. Fixed-network NOR matchings on a biclique/rook graph do not cover a time-switched cycle. Veliz-Cuba et al.'s AND-NOT universality and steady-state results, and Melliti et al.'s asynchronous two-cycle attractor results, neither assert this exact stroboscopic mapping and distributions. Novelty is best-knowledge, not an exhaustive guarantee. The inaccessible full text of a plausible later NOR dynamics survey is an explicit residual risk.

## Value — PASS

A single edge outage causes a genuine phase change from a permutation on all \(4^m\) phase-zero states to an attracting unique two-phase orbit. The location-dependent and size-dependent exact basin-depth formula is not merely a small enumeration; it determines sharp finite synchronization for every fault pattern and exhibits a meaningful fixed-one-fault linear versus independent-density logarithmic timescale. The use of canonical alternating perfect matchings makes the boundary natural and serves as an exact benchmark for time-dependent inhibitory Boolean networks.

## Closest literature and limits

Veliz-Cuba et al. (2012) describes AND-NOT networks; Melliti et al. (2013) studies asynchronous intersecting Boolean cycles. Related alternating matching lower-approximation, temporal infection and fixed NOR findings are compared by update semantics and implication. The result is confined to alternating matchings, with no independent outside validation.

Self-review: passed. Independent audit: not yet performed.
