# Scientific review: a three-patch competing-colonizer extinction race

## Correctness — PASS

The state space, event rates, initial allocations and win event are explicit. Finite-state absorption gives an almost-surely determined first lost species. Species-label exchange and endpoint reflection reduce the three placement probabilities to \(P_C\), \(1-P_C\), and \(1/2\); two exhaustive first-event equations yield the exact rational expression. The comparison with \(1/2\) has numerator \(c-(\mu-1)(\mu+2)\) and a strictly positive denominator, which proves the entire phase diagram, including boundaries. A second implementation enumerates all \(12\) two-type states and checks \(81\) positive rational parameter pairs exactly, plus three designated boundaries. Rational diagnostics corroborate the symbolic proof; they are not offered as an infinite proof.

## Originality — PASS within the inspected evidence

The closest full-text primary studies are Chan–Durrett–Lanchier (2009, https://arxiv.org/abs/0910.4014), Valesin (2010, https://arxiv.org/abs/1004.1958), and Mountford–Barrios Pantoja–Valesin (2018, https://arxiv.org/abs/1803.01533). Their relevant theorems address coexistence, interfaces, or infinite-lattice asymptotics, with spatially uniform death rates. The finite three-patch, site-heterogeneous first-extinction allocation probabilities do not follow from those results as stated. The original Neuhauser (1992) paper (https://doi.org/10.1007/BF01192067) was available only through bibliographic theorem summaries, and an indexed competing-patch ecology article (https://doi.org/10.1080/17513758.2010.535126) could not be inspected completely. Both remain residual historical-priority risks.

Equivalences checked include neutral species exchange, reflection, alternate terms 'two-type contact process', 'competition-colonization', 'first type extinction' and 'outlasting competitor'. Broader coverage was checked for infinite-lattice ergodic and coexistence theorems and general finite-state absorption methods; the latter supply a technique, not the specialized threshold. Searches for exact first-extinction tables and the quadratic switching curve found no matching record. The closest accessible prior results about single-species immigration placement on three sites, and extinction times after corridor placement, have nonidentical objects and do not imply this two-species race result. Failure to find a covering work is not a guarantee of novelty.

## Value — PASS

There are exactly three initial allocation types for two distinguishable competitors on the minimal three-site path. The theorem ranks every type for every positive colonization and center-mortality rate. It locates a unique, interpretable switch between a high-connectivity seed and a lower-mortality peripheral seed, rather than reporting one numerical counterexample. This small complete classification can benchmark spatial competition approximations and seeding-site heuristics. It does not predict indefinite coexistence, large-graph behavior, or applied ecological benefit.

## Limitations and evidence

The conclusion assumes neutral per-edge births, independent site-specific exponential deaths, exclusive occupancy and no immigration. The proof is a complete first-step calculation on the reachable states, and `checker.py` offers independent exact finite diagnostics using the standard library. Some historical sources were available only in partial form; independent historical priority and independent mathematical audit are not established.

Self-review: passed. Independent audit: not yet performed.
