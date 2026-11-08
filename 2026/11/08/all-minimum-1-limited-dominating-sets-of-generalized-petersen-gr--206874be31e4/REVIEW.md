# Review of the exact \(GP(n,2)\) minimum-set census

## Correctness
PASS. Each \(1\)-limited dominating set has at least half the vertices by double-counting its boundary edges; the two shores attain equality. Equality forces exactly one crossing edge at every vertex. All 256 possible four-column masks and every permitted transition were checked with a self-contained Tarjan enumeration, proving that every periodic walk belongs to two fixed loops or two five-cycles. This finite exhaustive structural lemma plus the closed-walk argument establishes the claim for every \(n\ge5\); direct exhaustive vertex-set census for \(5\le n\le10\) corroborates it. No extrapolation from sampled lengths is used.

## Originality
PASS, provisional priority. The strongest relevant published structural theorem is Radić–Radić–Tepeh (arXiv:2610.26259), which explains the generic perfect-matching-cut equality but does not enumerate the \(GP(n,2)\) cuts or prove the five-period transition. Radić–Tepeh (arXiv:2610.01796) concerns complexity and Goldberg snarks. Beggas et al. (arXiv:1906.11966) concern the distinct \([1,2]\) parameter and hence do not imply the census. Tepeh's Cartesian-product work and general perfect-matching-cut complexity results do not cover the enumeration. No covering statement was found among the directly compared scientific claims and literature. Some broader/unindexed cut literature and inaccessible full text of the Erveš–Tepeh 2026 article remain historical-priority risks.

## Mathematical value
PASS. This is a complete exact classification and count of **all** extremal sets for a canonical infinite cubic graph family containing the Petersen and dodecahedral graphs. The surprise is a sharp period-five jump in the number of optimum solutions, invisible from the minimum domination value alone. The count equivalently classifies perfect-matching boundary partitions, linking two natural structural questions.

## Limits
Only \(GP(n,2)\), \(n\ge5\), and cardinality-minimum solutions; no general \(GP(n,k)\) or nonminimum enumeration. The finite-state proof is reproducible, but no independent review has occurred; historical priority is provisional.

Self-review: passed. Independent audit: not yet performed.
