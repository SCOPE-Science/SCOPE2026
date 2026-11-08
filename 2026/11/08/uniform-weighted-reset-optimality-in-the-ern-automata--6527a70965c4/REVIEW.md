# Scientific review

**Correctness — PASS.** The inverse-preimage proof establishes the exact local gate, the forced order of first appearances of all predecessor states, and a spacing of at least \(n-1\) rotations between successive first appearances. Counting effective inverse merges establishes the independent merging-letter bound. Equality conditions force the unique displayed word. A separate full-subset search over twelve automaton sizes and five cost pairs confirms the claimed cost and unique optimizer; finite checks are corroboration, not an infinite proof.

**Originality — PASS (best-knowledge, qualified).** Direct comparisons of the claims, rather than their titles, distinguish the coordinatewise lower bound for every reset word from the classical minimum-total-length claim and from published approximation/complexity results for weighted automata. Ruszil (2021, arXiv:2103.16185) studies general positive letter weights but not this exact all-cost classification. Fominykh–Martyugin–Volkov (2012, arXiv:1205.2174) study a broader transition-cost setting, yet do not state a universal exact optimum for this family. Historical early-deficiency, pair-distance and avoiding thresholds do not imply the number of rotations in arbitrary-length resets. An unindexed equivalent via another inverse-automaton formulation is a residual risk.

**Value — PASS.** The complete Pareto-minimum vector and its unique witness settle a natural, motivated exact-weight specialization of the shortest-reset problem, and explain why the optimizer here cannot change when one symbol becomes much more expensive, unlike in general weighted automata. The inverse-gate argument gives a structural mechanism beyond replaying the usual unweighted shortest word.

**Limits.** The result is for the standard labeled two-letter Černý automata, not arbitrary synchronization, nonpositive weights or state-dependent costs. Primary bibliographic comparisons were broad but not exhaustive; independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
