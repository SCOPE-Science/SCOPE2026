# Self-review

## Correctness — PASS

For each binary alternating run skeleton, the proof supplies exact coordinate-box criteria for subsequence occurrence. Single-letter deletion conditions determine the minimal absent frontier, including equality and singleton-run boundaries. The exhaustive ten-row skeleton table gives exactly seven unconditional and six conditional words; patterns of six or more runs cannot be minimal because their proper subsequences contain an absent five-run alternating pattern. The independent standalone program verifies 1024 exhaustive parameter tuples, plus 116099 deletion witnesses and 6600 randomized membership checks on larger tuples. Its finite checks are supplemental, not a substitute for the symbolic proof.

## Originality — PASS (with residual bibliographic uncertainty)

The closest primary material is Kosche et al., *Absent Subsequences in Words* (arXiv:2108.13968), sections on general minimal absent subsequence characterizations and compact representations; it defines and algorithmically characterizes the same objects, but does not state the five-run closed basis in the inspected sections. Adamson et al., arXiv:2407.18599, bounds counts of absent subsequences at given lengths and universality indices, a different quantity. The later general enumeration results of Manea et al., arXiv:2504.21471, do not state the symbolic parameter classification in inspected material. Searches for the five-run template and its equivalent subsequence-antidictionary formulation did not disclose a direct equivalent. A related 2023 conference paper's full text was unavailable; therefore this remains a possible overlap risk. A general algorithm's ability to compute a specific case does not amount to an already-stated symbolic formula, though it lowers the conceptual distance.

## Mathematical value — PASS

A five-run host is the first family with three interior run multiplicities interacting through singles, two adjacent products, and a triple product. The complete minimal forbidden-subsequence antichain is a canonical description of its entire subsequence downset, and the result identifies an unexpected absence of cardinalities 11 and 12 and the exact threshold for the maximum of thirteen. This is a natural complete infinite-parameter classification rather than an isolated numeric slice or a restatement of membership testing.

Self-review: passed. Independent audit: not yet performed.
