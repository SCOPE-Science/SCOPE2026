# Independent mathematical audit — 2026-10-01

## Final claim assessed

A local branch-profile criterion forcing maximal monodromy in prime degree

## Correctness — PASS

PASS. For a permutation with cycle partition \(\Lambda\), some power is a single \(q\)-cycle fixing every other letter exactly when \(\Lambda\) contains one part equal to \(q\) and no other part divisible by \(q\). A connected degree-\(p\) cover has transitive, hence primitive, monodromy because \(p\) is prime. Classical Jordan then forces \(A_p\le G\) whenever \(q\le p-3\); branch-cycle parity decides between \(A_p\) and \(S_p\). The deck-group and Galois-closure genus consequences follow from the standard point-stabilizer normalizer and Riemann--Hurwitz formulas.

## Originality — FAIL

FAIL. The monodromy conclusion is mechanically implied by the classical Jordan theorem for primitive permutation groups together with the elementary one-line cycle-power criterion above. Song--Wen--Zhang's 2026 theorem supplies universal realizability of compatible prime-degree branch data, but the forcing statement for every connected realization needs no new Hurwitz-space lemma beyond transitivity in prime degree. Under the required implication standard, packaging these standard ingredients as a passport criterion does not create an original theorem.

### equivalent_formulations

Searches: Jordan primitive group q-cycle prime q <= n-3; prime-degree cover monodromy q-cycle passport

Evidence: Classical Jordan theory states that a primitive subgroup containing such a prime cycle contains \(A_p\); prime-degree transitivity gives primitivity.

Reasoning: The passport criterion is just the cycle-structure condition ensuring that a power of a local branch permutation is the required \(q\)-cycle.

### broader_coverage

Searches: arXiv:2609.20572 prime-degree Hurwitz existence; Jordan's symmetric group theorem; Hurwitz-space applications of Jordan

Evidence: The new existence theorem realizes every compatible datum, while classical permutation-group theory already determines the maximal monodromy consequence once the local cycle is present.

Reasoning: The combined prior ingredients mechanically dominate the advertised forcing theorem.

### exact_database_or_table

Searches: Resultary semantic search for prime-degree Hurwitz maximal monodromy passport criterion

Evidence: No exact textual duplicate was required for the failure because the claim follows directly from standard prior theorems.

Reasoning: Absence of matching wording does not overcome a decisive implication from established theory.

### claim_vs_prior_implication

Searches: Song--Wen--Zhang 2026 abstract; classical Jordan theorem \(q\)-cycle criterion

Evidence: The source guarantees existence of a connected cover for compatible data; Jordan gives \(A_p\) or \(S_p\) for any connected realization with the stated local cycle.

Reasoning: Only routine cycle arithmetic connects the passport condition to the classical theorem, so the final claim is mechanically covered.

## Scientific value — FAIL

FAIL. The criterion is convenient, but after the passport is given it reduces to a textbook cycle-power check followed directly by Jordan's theorem, parity, and standard covering-space formulas. The record does not add a nonstandard structural lemma or a motivated boundary beyond those established ingredients, so it does not clear the value bar against routine deductions.

## Source inspections

- **The Hurwitz existence problem in prime degree** — https://arxiv.org/abs/2609.20572. Material read: Primary abstract and indexed theorem statement. Assessment: EXISTENCE_INGREDIENT. Evidence: The source proves that every compatible branch datum of prime degree over the sphere is realizable by a connected branched cover.
- **Jordan's symmetric group theorem** — https://mathworld.wolfram.com/JordansSymmetricGroupTheorem.html. Material read: Statement and standard references. Assessment: DECISIVE_STANDARD_PRIOR_THEOREM. Evidence: A primitive subgroup of \(S_n\) containing a prime \(q\)-cycle with \(q\le n-3\) contains \(A_n\), hence is \(A_n\) or \(S_n\).
- **Harbater-Mumford subvarieties of moduli spaces of covers** — https://doi.org/10.1007/s00208-005-0680-0. Material read: Abstract and accessible primary-paper context. Assessment: BACKGROUND_HURWITZ_CONTEXT. Evidence: It illustrates established use of finite-group/Hurwitz-space structure; the originality failure already follows from Jordan plus prime-degree transitivity.

## Limitations and residual risks

The branch-profile test is only sufficient. The audit finds the stated conclusion to be a routine specialization of classical Jordan theory once the local cycle is read from the passport; it therefore is not a validated new finding.

- The primary 2026 existence paper was not needed for any whole-document noncoverage claim; the scientific rejection rests on a mechanical implication from classical group theory.

## Disposition

**failed**
