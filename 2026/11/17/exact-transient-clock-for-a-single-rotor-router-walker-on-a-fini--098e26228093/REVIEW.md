# Self-review

## Correctness

**PASS.** The conserved offset \(p-k\) reduces the full system to a binary-word flip at its own Hamming-weight index. Two monotone displacement functions prove termination at one of two explicitly described sorted-word families and count upward/downward steps, giving the exact preperiod for every size. A strict extremizer analysis and direct expectation calculation give the all-size maximum, its population and the exact mean. Independently structured functional-graph and direct-walk programs match every state at tested sizes; they are supplementary to the proof.

## Originality

**PASS, with stated historical risk.** The 1996 Eulerian-walker sources introduce the deterministic rotor mechanism and describe Euler circuits/recurrent configurations, not the exact statewise first-entry clock on cyclic graphs. The 2008 unicycle criterion and 2014 orbit-size theorem determine recurrent states or their cycles, not how many steps a specific transient state takes to reach one. The 2016 ring-rotor work studies multiwalker cover times and reports quadratic single-walker asymptotics, but the exact preperiod formula, worst-case extremizer count and uniform mean are not stated in the inspected portions. Searches for the exact formula and alternative wording found no matching published-finding corpus entry. The 2003 single-walker patrolling paper and an earlier report could not be fully inspected; priority is not guaranteed.

## Mathematical value

**PASS.** This fills a natural dynamical gap between knowing the eventual Euler tour and knowing the waiting time from arbitrary initialized rotors. The result supplies a complete computable initial-state observable, the sharp global settling-time cutoff, its exceptionally small maximizing population, and exact average behavior. These are not consequences of counting recurrent states or knowing asymptotic cover-time order; the distinction is relevant for initialization and deterministic graph exploration.

## Boundaries

This is not a result about multiwalker systems, cover times, or arbitrary finite graphs. Earlier closed-graph rotor work supplies the conceptual framework, and inaccessible archival material remains a residual priority risk. The attached finite tests are not independent publication-level validation.

Self-review: passed. Independent audit: not yet performed.
