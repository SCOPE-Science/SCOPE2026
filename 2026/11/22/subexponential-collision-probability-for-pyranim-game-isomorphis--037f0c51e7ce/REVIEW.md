# Review: Subexponential collision probability for Pyranim game isomorphism

## Correctness

**PASS.** The stable-position definition and game/graph equivalence are reproduced from the first public source. The exact connected-type formula comes from the 2010 counting theorem. The block construction makes all \(r!\) states legal, different and isomorphic. The central-binomial bound gives enough pairwise nonisomorphic connected components, and Stirling turns the resulting class mass into an all-size asymptotic bound. A standalone program corroborates small cases; no finite experiment is treated as an infinite proof.

## Originality

**PASS (provisional historical priority).** Binyamin and Kniffen explicitly pose the limit in section 5.3, question 4. Saitoh and coauthors count connected proper interval types, not collision probabilities for uniform Pyranim positions. published-finding corpus and literature comparisons examined aliases involving Dyck paths, proper interval graphs, entropy/collision probability and component permutations. The new connection is a factorial-size fiber at nearly Catalan exponential scale. An undiscovered equivalent theorem remains possible. The exact connected-type formula itself is prior art.

## Value

**PASS.** An explicit new paper asks for this precise limiting value; the proof gives an unconditional answer and a subexponential lower bound for a natural combinatorial probability. It identifies a structural mechanism rather than computing an isolated example. The actual asymptotic decay and whether the probability tends to zero remain unresolved by this claim.

## Sources and limits

- Binyamin and Kniffen, *Enumerating Pyranim Isomorphisms*, arXiv:2611.16153v1 (2026-11-12), sections 2–5, https://arxiv.org/abs/2611.16153 .
- Saitoh et al., *Random Generation and Enumeration of Proper Interval Graphs*, IEICE Transactions on Information and Systems (2010), Theorem 1, https://doi.org/10.1587/transinf.E93.D.1816 .
- OEIS A005217, https://oeis.org/A005217 , type-count database rather than collision law.

Self-review: passed. Independent audit: not yet performed.
