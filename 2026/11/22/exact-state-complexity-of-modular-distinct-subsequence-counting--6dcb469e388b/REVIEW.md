# Scientific review

## Correctness
**PASS.** The wordwise distinct-subsequence recurrence is exact. Modular shear matrices have determinant one. The legal blocks `0` and `10` positively generate the entire finite special linear group, which is transitive on primitive columns, proving all proposed states reachable. The row-separation lemma constructs accepting suffixes distinguishing any two modular vectors even for composite moduli; a leading-one suffix separates the last-bit classes. The sink is separated by accepted continuations. State counting follows from the second Jordan totient. A standalone checker verifies all 2–20 moduli and 38,893 direct language decisions. The group proof, not the checker, proves the infinite statement.

## Originality
**PASS, subject to historical priority risk.** Żak (2022, arXiv:2210.00342) treats the coprime-pair interpretation and unrestricted string counts, but does not impose a forbidden `11` factor or classify its minimal DFA. Kovačević–Vukobratović (2021, arXiv:2105.04617) treat RLL enumerative rates rather than modular distinct-subsequence state minimization. The closest checked prior modular automata count scattered occurrences of particular patterns, not the total number of distinct subsequence words. A previously recorded unrestricted modular result has one primitive-state layer; it neither supplies run-constrained reachability nor the exact distinction between the two last-bit layers. Source searching cannot exclude unindexed equivalent work.

## Value
**PASS.** A run restriction and a global subsequence statistic arise naturally together in constrained-sequence recognition. This supplies a complete exact all-modulus DFA memory law and reveals a sharp cost of the local constraint: both primitive layers survive and only one rejecting sink is added. The matching lower bound is nontrivial because a product construction alone does not show that the restricted alphabet of legal continuations can distinguish all counter states.

## Limits
This is a claim for zero residue, complete deterministic automata, and binary words avoiding only `11`; no extension to other residues or constraints is implicit. The novelty assessment is best-knowledge, not an exhaustive priority certificate.

Self-review: passed. Independent audit: not yet performed.
