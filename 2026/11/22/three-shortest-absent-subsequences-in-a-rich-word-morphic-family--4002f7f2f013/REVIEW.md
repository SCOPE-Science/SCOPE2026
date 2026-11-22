# Scientific review: three-word shortest-absent-subsequence law

## Correctness — PASS

The universal claim concerns every full-support word \(U\) over \(L\), every block count \(m\ge2\), and every tail avoiding the distinguished letter \(a\). The proof supplies an explicit unique greedy arch factorization, counts exactly \(2m\) occurrences of \(a\), and proves universality through length \(2m\). Prefixes just before the successive occurrences of \(a\) give the exact rightmost-embedding recurrence; the base missing-pair set is \(\{aa,ba,bb\}\). This reconstructs all three missing words without extrapolating from experiments. The ruler-word recursion proves both morphic identities, and direct word-level arguments handle the earlier two iterates. The standalone checker evaluated 630 morphic/generic instances, with 22 direct exhaustive comparisons at the shortest-absent length; these are corroborating checks, not the proof.

## Originality — PASS against inspected sources

Dvořáková, Mol and Pelantová's 2026 paper introduces the exact rich-word morphism and develops a repetition-threshold structure theorem, not a scattered-subsequence or shortest-absent-language theorem. Kosche, Koß, Manea and Siemer give general arch-based criteria and algorithms for shortest absent subsequences; their Theorem 3.4 does not give the parameter-uniform three-word language or the first-full-alphabet transition. The 2025 paper by Manea, Ringleb, Siemer and Winkler concerns generic optimal enumeration, a different type of claim. Related morphic shortest-absent results concern other substitutions or objects; a published all-multinacci arch factorization uses another morphism. Comparison used the actual displayed statements and implications, not title difference alone.

The strongest remaining risks are an unindexed closed-form specialization of the general arch theory and incomplete inspection of the 2025 enumeration paper's full text. Searches and full-text checks have not established global uniqueness. The novelty assessment is correspondingly a same-model, evidence-based assessment rather than independent verification.

## Mathematical value — PASS

The first three iterates of the newly prominent rich-word family to use its entire alphabet have a sharp, uniform shortest-absence transition in size \(d+1,d+1,3\). The three-value collapse is not simply a one-parameter numerical example: the stronger theorem proves that it persists across all alphabet sizes, arbitrary full-support internal blocks and all later block counts with a-free tails. This gives an exact complete missing-language invariant and a constructive explanation from the positions of rare letters. The object and invariant are motivated independently by the 2026 rich-word construction and established scattered-subsequence theory; no external application is asserted.

## Scope and outstanding risks

The conclusion is restricted to the specifically factored block family and the first three full-alphabet morphic iterates, not every later iterate. Finite tests do not establish the infinite quantifiers. General algorithms can compute individual instances and may hide an equivalent symbolic formulation; that publication-priority question needs independent literature review.

Self-review: passed. Independent audit: not yet performed.
