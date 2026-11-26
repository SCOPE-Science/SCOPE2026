# Independent mathematical audit

## correctness

PASS

The proof covers q,m≥2, rejects the empty word, accepts the one-letter word 0, counts overlapping directed pairs including loops, and requires the initial/final symbol 0. For a modular edge vector with the boundary of an s-to-t walk, take nonnegative residue representatives c. The integer imbalance (e_s−e_t−∂c)/m sums to zero, so route its positive mass to its negative mass using available directed edges. Add m times these flows and then m copies of every edge. The support is strongly connected and has the exact prescribed Euler-trail imbalance, giving the desired walk even for composite m. Root-star incidences generate the sum-zero module, of order m^(q−1), so each endpoint fiber has size m^(q²−q+1). All its states are reachable. A live state (s,r) can accept a suffix beginning with any letter a because the remaining residue −r−e_sa has boundary e_a−e_0. Equal last letters and distinct residues cannot accept the same suffix; for different last letters s,t, equivalence would force r′−r=e_sa−e_ta for every a, impossible since the vectors are nonzero in distinct columns even modulo two. The initial state and dead state are distinguished from live states by these suffix possibilities, and from one another by the suffix 0. For uniform input the live chain is strongly connected by residual walk realization, with degree q in and out, so the stationary law is uniform. The total edge residue increases by one per step and a loop-letter return of length m exists, so the period is exactly m. Each class contains q m^(d−1) states via translation of one loop coordinate on every endpoint fiber. Along n−1=0 mod m the periodic return probability converges to the reciprocal class size; the independent first-letter requirement contributes 1/q. Other lengths cannot be accepted. This reconstructs both exact formulas without treating finite case outputs as universal evidence.

## originality

PASS

The closest available catalogue works separately address modular scattered pairs or exact contiguous profiles; primary literature supplies exact k-abelian or Markov types, modular letter Parikh vectors, general counter automata, or subword frequencies in infinite words. The inspected results do not give the joint anchored adjacent-pair minimum DFA and periodic finite-word density. The standard Euler and Markov tools are not part of the originality claim.

## value

PASS

This is a natural complete finite-language test: retain all neighboring-symbol transition statistics modulo m and require return to the anchored symbol. The incidence relations remove q−1 independent coordinates, but discovering the exact complexity requires showing that every surviving residue/endpoint is reachable and distinguishable. The same structure yields a nontrivial period-m acceptance limit with an exact class mass; this quantifies both deterministic memory and typical acceptance for the same monitor, including composite moduli. Neither is a numerical coincidence or merely the existence of a counter automaton.

The dated certificate retains the supplied scientific assessment, sources and limitations.
