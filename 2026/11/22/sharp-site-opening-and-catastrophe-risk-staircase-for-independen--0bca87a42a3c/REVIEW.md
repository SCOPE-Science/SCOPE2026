# Scientific review

## Correctness

PASS. The theorem explicitly defines the feasible integer domain, independent site events and the one-shot establishment objective. Strict concavity from the displayed second derivative gives the unique allocation for any fixed count. Strict concavity of the perspective objective gives the unique continuous count and two-neighbor integer reduction. The integrated monotone-ratio argument shows every adjacent comparison switches at most once in the correct direction, with the endpoint criterion proving existence or absence of switching. Exact root and asymptotic identities give the quantitative limits. A standalone standard-library checker independently evaluates numerical consequences but is not used to infer the universal statements.

## Originality

PASS relative to the material inspected. Duncan et al. (2014; DOI 10.1111/2041-210X.12288) derive independent-founder extinction and discuss environmental site unsuitability but do not optimize an arbitrary number of sites under a fixed opening cost. Berger-Tal et al. (2012; DOI 10.1111/j.1523-1739.2011.01746.x) use a spatially explicit individual-based model with up to four additional release sites, not a site-opening cost or Poisson-lineage closed-form count optimum. Canessa et al. (2014; DOI 10.1111/1365-2664.12253) optimize dynamic stage-specific releases to a reintroduction program rather than the explicit one-shot at-least-one-success criterion. Helmstedt et al. (DOI 10.1111/acv.12319) use a three-site dynamic management model with an abundance objective; it does not state the arbitrary-site fixed-cost single-crossing result. The related 2014 reserve-design paper was not available in full and remains a priority risk, as do general resource-allocation theorems that might imply the result without similar terminology. No unconditional priority or uniqueness across the literature is claimed.

## Value

PASS. Independent site-level catastrophes can make concentration of large release effort wasteful, while fixed opening costs discourage spreading effort excessively. The theorem resolves this conflict for *every* admissible budget, success rate and catastrophe risk with a complete, cheap decision rule and monotone comparative statics. Unlike a one-off numerical optimum, the result rules out re-entrant site-count reductions and supplies exact transition tests. This supplies a baseline against which correlated-risk, mate-limited or dynamic conservation problems can be measured. It is not an operational recommendation without calibrating assumptions.

## Scientific limitations and closest literature

The result assumes independent identical sites, Poisson-number founders, binary site suitability, continuous release effort, no mating or ecological feedback, and an at-least-one-success objective. The reviewed literature above motivates the problem without establishing the exact comparison. General convexity methods are known, and priority remains provisional because complete coverage of older resource allocation work is not assured. Numerical checks do not replace proof and no external expert review was performed.

Self-review: passed. Independent audit: not yet performed.
