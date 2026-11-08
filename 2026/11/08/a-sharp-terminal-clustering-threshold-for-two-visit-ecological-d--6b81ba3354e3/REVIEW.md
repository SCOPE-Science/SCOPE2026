# Scientific review: two-visit ecological detection

## Correctness — PASS

The exact two-time occupancy probabilities follow from the two-state continuous-time Markov transition kernel. Inclusion-exclusion for conditionally independent imperfect observations gives the stated objective, and its derivative in the later observation time is strictly positive. Holding that observation at the terminal deadline reduces the remaining optimization to a strictly concave function of an exponential time coordinate. Its one stationary point crosses the admissible boundary exactly at \(H_c\), proving global optimality, uniqueness, the equality case, and the squared improvement formula for all parameter values in the theorem. The independent transition-matrix checker passed 30,800 exact-rational and finite-grid diagnostic assertions; the proof, rather than enumeration, establishes the unrestricted statements. No unverified nonstandard lemma is needed.

## Originality — PASS within inspected evidence, with residual priority risk

A public scientific record search included timing, two-state colonization–extinction, imperfect detection, simultaneous tests, and alternative optimal-surveillance terminology. The nearest records concern two-visit N-mixture identification, stationary renewal-process two-time identification, and first detection in a different physical process. Available prior scholarly material was compared by assumptions and conclusion, not by title. MacKenzie and Royle (2005) consider independent repeat visits and optimize *precision of occupancy estimation* under time-constant occupancy; Pagendam and Pollett (2009) optimize *Fisher information for rate estimation* in an interacting multi-patch birth–death model; Guillera-Arroita et al. (2014) optimize a static-survey cost policy. None of those inspected results states or entails the exact two-snapshot finite-deadline switching law as formulated.

Important limits: the full text of the 1981 general multistate survivor-search theory could not be accessed, so its potentially broader necessary-and-sufficient optimality conditions were not definitively compared. MacKenzie et al. (2003) and Kendall et al. (2013) were inspected only at the abstract/metadata level. This is a provisional literature-based finding, not proof of global historical priority or independent validation.

## Value — PASS

The result resolves the complete temporal design for an ecologically interpretable, reversible, imperfect-detection process. It identifies a sharp dimensionless separation threshold, a surprising short-horizon optimum with simultaneous independent surveys, a rigorous uniqueness classification, and the exact penalty for ignoring temporal staggering. The question follows naturally from the tradeoff between occupancy building up after known initial absence and repeat-detection redundancy; the result is not merely a special numerical case or a routine parameter substitution. It does not claim that a two-visit design should be used operationally under field heterogeneity or cost constraints.

Self-review: passed. Independent audit: not yet performed.
