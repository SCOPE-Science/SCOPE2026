# Self-review

**Correctness — PASS.** The greedy weak-descent budgets are exact for subsequences of repeated permutations. Maximality forces both budgets to saturate; a zero-cost-insertion analysis of the two adjacent-swap orders gives a complete path language, including endpoint swaps. The formula for each length and the diagonal rational-function coefficient are derived algebraically. The finite verifier reproduces 46 complete maximal-word sets, 106600 independent budget tests and 25 coefficient levels. A finite census is not substituted for the infinite proof.

**Originality — PASS, subject to bibliographic uncertainty.** Closest inspected full texts: Sakai (CPM 2018, DOI 10.4230/LIPIcs.CPM.2018.1), Hirota–Sakai (arXiv:2307.10552), Conte et al. (arXiv:2307.13695). Their general MCS algorithms and compact representation do not explicitly give the symbolic adjacent-swap-period length spectrum. Existing special families include swapped ternary and reversed-permutation powers; their claims neither imply the appearance of shorter maximal words for larger alphabets nor the refined \(C_{k,r}\) formula. An older generic MCS study by Fraser–Irving–Middendorf (1996) was identified but not fully inspected, so an equivalent specialist result cannot be excluded.

**Mathematical value — PASS.** Maximal common subsequences are the generators of the common scattered-subsequence language and need not be longest; identifying a natural unbounded gap alongside an exact full spectrum and size-independent total is a substantive structural classification. Unlike a fixed small numerical instance, the claim applies to every exponent and alphabet size in its stated family.

**Limits and risks.** The 1996 study and unindexed results remain possible bibliographic overlap. Broader permutation-pair and repeated-symbol families are unproved. Mathematical correctness has not been independently audited.

Self-review: passed. Independent audit: not yet performed.
