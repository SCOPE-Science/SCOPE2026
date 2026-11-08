# Scientific review

**Correctness — PASS.** The proof establishes the equivalence between the number of greedy arches and the subsequence-universality index, proves the exact run-index recurrence for every phase, and uses the half-open endpoint test. The nonsingleton case is a floor-count of arithmetic-progression run indices. In the singleton case, the deficiency variable is bounded by the alphabet size, and the possible endpoint equality is excluded by the phase being a run start. The packaged program separately checked 105,476 phase values and 678 small full spectra. These computations are corroborative, not replacements for proof.

**Originality — PASS, subject to residual bibliographic risk.** Closest work: Barker et al. (2020, arXiv:2003.04629), Lemma 20 and Theorem 22; Fleischmann–Germann–Nowotka (2021, arXiv:2104.09063), §§3–4 and Theorem 21; Schnoebelen–Veron (2023, arXiv:2304.11932), §§3–4 and Lemma 4.1. They supply general notions, growth properties and algorithms, but the inspected statements do not give a complete formula for all cyclic phases of these run words or the exact optimizing-phase count. Earlier known binary conclusions and general arch algorithms are not claimed as new. A logically equivalent but unindexed treatment remains possible.

**Value — PASS.** This all-parameter result determines both ordinary and circular subsequence universality for an entire natural class of powers and identifies a sharp singleton-run rigidity boundary. It explains the precise periodic jump in universality and counts exactly which of all position rotations achieve the maximum. In particular, the answer is independent of every run length greater than one, a structural feature not apparent from general algorithms for individual words.

**Scientific limitations.** No repeated letter can occupy two distinct run classes within one period; the theorem does not enumerate individual absent subsequences. All independent audit channels remain unperformed.

Self-review: passed. Independent audit: not yet performed.
