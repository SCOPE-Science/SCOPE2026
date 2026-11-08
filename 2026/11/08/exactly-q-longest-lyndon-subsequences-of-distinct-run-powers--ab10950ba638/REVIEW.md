# Scientific review: optimal Lyndon subsequences of distinct-run powers

## Correctness

**PASS.** The claim has exact quantifiers \(q\ge2\), \(k\ge2\), pairwise distinct run labels beginning with the least label, and positive integer run lengths. For a one-position deletion, every candidate is handled: the first copy, a middle copy, and the last copy. The first/last comparisons reduce exactly to inequalities at adjacent run labels, with the cyclic terminal boundary treated separately. Proper suffixes beginning inside a least-letter run are explicitly treated, not discarded; other suffixes begin with a larger symbol. The unmodified power is not Lyndon, yielding the sharp upper bound. The distinct-word count follows from different deleted Parikh coordinates. Direct tests of all single deletions corroborated \(2447\) parameter profiles without mismatch, including \(1647\) exhaustive small profiles; these tests are not substituted for the universal proof.

## Originality

**PASS, with bibliographic qualification.** The primary full-text comparison is Bannai–I–Kociumaka–Köppl–Puglisi, *Computing Longest Lyndon Subsequences and Longest Common Lyndon Subsequences* (arXiv:2201.06773; Algorithmica online 2023). Its general algorithms compute a longest Lyndon subsequence, while its unique-character special case excludes repeated powers. Neither the inspected Section 4 nor its conclusions gives the simultaneous closed forms: longest length \(kp-1\), exactly \(p\) qualifying deletion positions, exactly \(q\) distinct optimal words, and the ascent/descent deletion-location rule. These numerical claims are not implied merely by a general polynomial-time optimization algorithm. Urabe and coauthors (2018) concern edited *substrings*, not scattered subsequences; Glen–Simpson–Smyth (2017) count Lyndon *factors*. Focused literature and semantic index queries did not identify the same theorem. Such search does not exclude unindexed equivalents, and the conclusion is not a claim of independent priority certification.

## Mathematical value

**PASS.** This is a natural complete classification of every optimizer on an unbounded family of nontrivial repeated-run instances of a recognized optimization problem. The optimum is always one deletion away, but the optimizing copy switches at each rise or fall of adjacent ordered run labels. Every run contributes exactly its run length to an optimal deletion count, producing the invariant \(p\), while collapsing equivalent deletions yields the different invariant \(q\). These are exact position-sensitive and output-sensitive answers not furnished by the unconstrained optimization algorithm. The proof's elementary comparison method may serve as a closed-form test family for Lyndon-subsequence implementations; no unproved downstream implication is asserted.

## Closest comparisons and limitations

The primary source and the two related sources are listed with links in `RESULT.md`. Relevant full article Sections 1, 2, 4 and 7 were read via the accessible journal HTML; the other two sources were consulted at title/abstract and bibliographic level, and their clearly distinct problem types do not support an assertion about uninspected technical appendices. The result does not extend, without new work, to cycles with repeated labels in separate runs or to arbitrary cyclic phases. Independent scientific validation and exhaustive historical coverage remain unperformed.

Self-review: passed. Independent audit: not yet performed.
