# Self-review

**Correctness — PASS.** The proof identifies all output collisions through nearby pairs. On disjoint bond events, the equality graph has one four-cycle per two distinct bonds, giving its exact rank defect; other common-deletion collisions introduce at most one exceptional slide per nearby nonbond pair, and disjoint-deletion collisions use only nearby endpoints. The nearby-pair count is tight, bond overlaps disappear, and factorial moments prove a Poisson(2) limit. The executable finite tests pass but are not used as a replacement for the asymptotic proof.

**Originality — PASS against inspected sources.** The PID deletion framework of Wu et al. establishes code constructions; Ray–West studies insertion upper shadows; the existing unseparated-pairs Poisson theorem explains the bond count, not the two-deletion deficit comparison. Similarity searches for exact reformulations and broad coverage found no equivalent result. Priority uncertainty remains from unindexed mathematical work.

**Mathematical value — PASS.** This is a nontrivial first-order limiting distribution for the size of the two-deletion output sphere in a contemporary permutation channel. The tight correction identifies the precise local collision mechanism. This can inform typical-case ambiguity estimates, independently of worst-case code bounds.

**Scope and risk.** Uniform random permutations, exactly two standardized deletions, no finite-length exact distribution; independent expert validation not performed. Relevant literature might contain an unindexed equivalent statement.

Self-review: passed. Independent audit: not yet performed.
