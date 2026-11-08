# Scientific review: exact sunlet propagation time

## Correctness

**PASS.** The process is precisely the synchronous independent-attempt probabilistic zero-forcing rule on a cycle with one pendant leaf at every cycle vertex. The proof accounts separately for the one-white-cycle-vertex boundary, all two-front states, initial single-core states, and the deterministic final leaf-clearing round. Three exact frontier recurrences have a unique rational generating-function solution with nonzero denominator constant terms; coefficient extraction yields the claimed formula. An independent full-blue-subset Markov-chain computation agrees for the complete graphs at cycle sizes five and six. The numerical tests do not serve as an infinite proof.

## Originality

**PASS, qualified by independent historical-priority risk.** The primary 2019 preprint and 2020 open-access journal paper explicitly conjecture the increment \(11/16\) based on numerical experiments. Their Markov transition table and general inverse-matrix formula make finite numerical computations possible but do not furnish the symbolic generating functions or an all-size proof of the increment. The newer general bounds by Jelassi, Portier and Sarkar give no sunlet equality and do not imply the all-size formula. Exact-phrase, graph-alias, closed-form and stronger-coverage searches did not reveal a publication proving the specific formula. This absence of a retrieved match is not a proof of world-first priority.

## Value

**PASS.** The theorem directly resolves a published, naturally parametrized probability/Markov-chain conjecture with an all-size expression, not merely a slight numerical improvement. The boundary-state decomposition also explains the two alternating decay modes and proves the cycle-start versus leaf-start strict ordering, which was only a numerical observation in the original paper.

## Limits and closest literature

Chan et al., *Using Markov chains to determine expected propagation time for probabilistic zero forcing* (2019 preprint, 2020 ELA article), Section 2 sun-graph table and conjecture, is the decisive self-review. Geneson and Hogben (2018) treat paths and cycles, not sunlets. Narayanan and Sun (2019) and Jelassi, Portier and Sarkar (2025) provide nonexact global bounds. Undiscovered source priority and independent reproduction of the symbolic derivation remain risks. The proof assumes finite simple sunlets, one initially blue vertex and the specified synchronous update rule.

Self-review: passed. Independent audit: not yet performed.
