# Review of the descending greedy cumulative-envy threshold

## Correctness — PASS

The signed-discrepancy reduction is an exact equivalence between two-agent allocations and signed prefix sums. For every length two through six, every greedy linearity region and every alternative sign pattern is covered by a rational linear-programming dual with nonnegative multipliers. The 1,364 individual dual equations have been replayed with `Fraction`, as has the exhaustive 64-allocation seven-good optimum. Zero items, equal values, sign ties and homogeneous scaling are included. The seven-good witness uses strictly positive values and exhibits a genuine cost reduction from 20 to 18. The proof does not extrapolate from finite numerical samples.

## Originality — PASS, qualified

The closest full-text primary manuscript is Goldberg, Robinson and Teh, arXiv:2610.09843, especially its fixed-order objective and hardness/DP sections, binary-identical Proposition 1, and Section 5 including appendices on ascending order and descending LPT. This work does not state the universal sharp descending fixed-order six/seven threshold, and neither its hardness statement nor an algorithm for general instances directly implies it. Elkind et al., arXiv:2410.14593, optimize a distinct temporal-EF1 feasibility requirement rather than the area under maximum envy. Classic LPT work addresses final makespan. Published-record semantic searches with the actual normalized claim, signed-prefix alias and LPT alias yielded no equivalent result. Search is not proof of novelty: earlier unindexed scheduling or discrepancy literature, and the preliminary conference version's details, remain residual risks.

## Value — PASS

The theorem resolves the natural smallest-horizon exact optimality boundary of a standard least-loaded policy under the descending order used in scheduling and temporal fairness. Its all-real, not merely integer, guarantee and explicit first failing instance show exactly where local imbalance minimization ceases to minimize accumulated unfairness. This is a substantive algorithmic boundary distinct from a single arbitrary example or a routine finite test.

## Checked primary sources and limitations

- Goldberg, Robinson and Teh, *Minimizing Cumulative Envy in Allocating a Sequence of Items* (2026), [arXiv:2610.09843](https://arxiv.org/abs/2610.09843): full accessible article text and appendix sections on objective, greedy rules, approximation, and examples read.
- Elkind et al., *Temporal Fair Division of Indivisible Items* (2024), [arXiv:2410.14593](https://arxiv.org/abs/2410.14593): full accessible article text including generalized binary greedy algorithm and TEF1 statements inspected.
- Della Croce and Scatamacchia, *Longest Processing Time rule for identical parallel machines revisited* (2018), [arXiv:1801.05489](https://arxiv.org/abs/1801.05489): abstract and objective inspected; no full-text exclusion claim.
- Conference presentation: [SAGT 2026 September 16 program](https://www.uni-augsburg.de/de/fakultaet/fai/conferences/sagt-2026/) records the work before its October open manuscript.

All mathematical claims are scoped to two agents and descending order. Full independent validation and exhaustive publication-priority coverage have not been established.

Self-review: passed. Independent audit: not yet performed.
