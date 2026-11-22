# Review: exact binary two-channel entropy–transitivity census

## Correctness — PASS

The rank-two finite test is a fully quantified deduction from the cited spectral characterization [2, Theorem 6]: an obstructing irreducible characteristic-polynomial factor either has quadratic degree and unit determinant, or is linear with Laurent-unit root. Polynomial integrality and the highest-degree term in the characteristic equation restrict such roots to the finite stencil interval. For the binary span-one family, both exact root identities are computed in the polynomial ring, rather than as evaluations at 1. The topological entropy formula is normalized exactly as in [1, Theorem 4]. Two separate standalone finite enumerators agree on all 256 rule classifications; the independent coefficient computation verifies each of 32 trace–determinant multiplicities, and the first computes the full 56 onsite-basis orbits. The finite checker does not replace either cited general theorem. The limits exclude general four-symbol nonlinear automata and arbitrary dynamical conjugacy.

## Originality — PASS, within documented search scope

[1] already establishes the general characteristic-polynomial entropy formula, and [2] already establishes the general strong-transitivity criterion. In particular the factorization-free two-channel root test is presented as an explicit specialization, not as a new independent general theorem. The single evaluated joint census (256 rules, a 72-case strongly-transitive stratum, its entropy split, and the 56 onsite-basis orbits with their five-stratum distribution) is not stated in the inspected full relevant sections of [1]–[3]. An exact implication check shows that the general criteria decide individual rules but do not supply the evaluated simultaneous population/orbit statement without further finite counting. Indexed searches of aliases, exact counts, and related classifications found no direct earlier table; this is an evidence-based assessment, not a proof of priority. Kari's relevant 2000 multiple-state-variable paper [4] was discoverable only at abstract level and full-text priority remains unresolved. Other unindexed tables are also a residual risk.

## Value — PASS

The first nonscalar binary group-automaton alphabet with a two-site neighborhood is a natural complete classification domain, not a sparse or ad hoc parameter slice. Jointly quantifying temporal entropy and strong transitivity distinguishes two different modes of dynamics in this small canonical family. The 56 similarity orbits remove redundant onsite coordinate choices, and exact strata allow all rules to be classified and compared reproducibly. This finite evaluated theorem is not claimed to replace the broader general results, and its utility is specifically as a complete baseline for small matrix-valued cellular automata.

## Closest literature and limits

[1] N. Castronuovo, A. Dennunzio, J. Kari, L. Margara, *Topological Entropy of Group Cellular Automata is Effectively Computable*, arXiv:2611.16746 (first public 2026-11-12), especially Theorem 4.

[2] N. Castronuovo, A. Dennunzio, L. Margara, *Strong Transitivity of Group Cellular Automata: Characterization and Decidability*, arXiv:2611.22365 (first public 2026-11-17), especially Theorem 6.

[3] A. Dennunzio et al., *Additive Cellular Automata Over Finite Abelian Groups: Topological and Measure Theoretic Properties*, MFCS 2019, DOI 10.4230/LIPIcs.MFCS.2019.68.

[4] J. Kari, *Linear Cellular Automata with Multiple State Variables*, STACS 2000, DOI 10.1007/3-540-46541-3_9 (abstract only; full text not obtained).

Self-review: passed. Independent audit: not yet performed.
