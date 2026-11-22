# Independent mathematical audit

## correctness

PASS

For two vertically open rows and horizontal ring n>=3, the exact column rule is: 0->2 iff neighbor occupancy v=3; 2->2 iff v in {1,2}; a singleton either dies (v<=1), becomes full (v=2), or persists unchanged (v=3). No singleton is created. If S decreases then (n+1)S+D decreases by at least one, since 0<=D<=n. If S is conserved every singleton requires neighbors of types 1 and 2, so empty-to-full birth is forbidden, and every other change decreases D; hence Phi=(n+1)S+D strictly decreases on nonfixed steps. Bound Phi<=n(n+1) proves fixation; lexicographic finite (S,D) proves finite-support infinite-strip fixation, without a uniform bound. One-row no births; an explicit three-row four-column blinker proves sharp width. Fixed points are exactly closed walks in a 16-pair-state transfer graph, and exact Newton identities give det(I-zT)=1-z-5z^3+4z^4-4z^5+4z^6. An independently written pure-Python/SymPy check verifies determinant, counts 16,5,26,82,43,213 for n=3..8 and strict decrease for all two-row states through n=6. Finite tests corroborate, not prove, all n; n=1,2 excluded.

## originality

PASS

Qualified best-of-knowledge; exact two-row vertically dead boundary potential and full all-n zeta denominator not implied by general Life oscillator construction papers or separate periodic vertical torus work. Literature review searched alternate boundary names and still-life count sequences; no decisive earlier exact result identified.

## value

PASS

A sharp impossibility boundary for all temporal periods on a natural minimum-width strip is structural, and a closed rational generating function for every fixed-point count is a reusable exact invariant, not a small-instance tabulation. The proof is an explicit descent principle in otherwise oscillatory cellular automata.

The dated certificate retains the supplied scientific assessment, sources and limitations.
