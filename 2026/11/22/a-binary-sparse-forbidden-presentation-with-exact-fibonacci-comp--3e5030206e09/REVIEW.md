# Mathematical review

## Correctness — PASS
The word-language characterization follows directly from the one-sided propagation forced by `1000` and `1110`, and the sparse family excludes transitions from a zero tail to a one tail. Conversely all three permitted types admit two-sided extensions. Counted factors split into a no-triples Fibonacci core and two disjoint one-tail types, yielding exactly \(2F_{N+2}-2\). Exhaustiveness and minimality of the displayed antidictionary follow from deletion of the first and last letter. Perron growth of the primitive four-state triple-avoiding shift yields \(h_M=\log\varphi\), and the sparse quadratic generator lengths yield \(h_G=0\). Code independently checks all words through length sixteen; no finite computation is substituted for infinite proof.

## Originality — PASS within inspected evidence
Wu and Zhang's direct precedent (arXiv:2611.03758v1, Example 1(2)) already proves the *qualitative* entropy separation for four distinct symbols. The current final claim is the direct binary guarded-language model, its entire minimal forbidden language, and exact Fibonacci factor count, not the general phenomenon or mere existence over two symbols. Two highly relevant published full results and recoverable prior claims were compared and do not cover these exact formulas. Generic binary coding, overlooked sofic descriptions, and unindexed prior results remain priority risks.

## Mathematical value — PASS
A sharp low-alphabet explicit realization is useful for examining the boundary of the new generating-forbidden entropy invariant. The complete Fibonacci word complexity and complete antidictionary give independently reusable test objects and make the distinction between the two obstruction entropies transparent without a four-symbol marker alphabet. This is not offered as a new maximal-measure theorem, and its significance lies in exact classification of a natural finite-guard/sparse-generator system, not merely in the availability of a coding trick.

## Limits and verification
Only the two-sided binary model and literal language formulas are proved. The checker validates 135165 finite strings but cannot certify asymptotics. The inspected record cannot exclude all historical isomorphisms and no independent mathematical validation was performed.

Self-review: passed. Independent audit: not yet performed.
