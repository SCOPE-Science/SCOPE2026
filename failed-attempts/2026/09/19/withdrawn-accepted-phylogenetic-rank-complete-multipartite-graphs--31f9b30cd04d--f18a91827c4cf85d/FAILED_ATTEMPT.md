# FAILED ATTEMPT — NOT A VALIDATED FINDING

Record: `2026/09/19/phylogenetic-rank-complete-multipartite-graphs--31f9b30cd04d`  
Independent audit date: 2026-09-29 (UTC)  
Task: `2dc78f4140c1ae514bc56394355e0895`

The underlying mathematics was independently checked and is valid, but the record is not acceptable as a distinct validated research finding because its principal theorem was already present in earlier SCOPE repository work.

## Correctness retained

The formula r_phy(K_{n_1,...,n_r})=max{1,q+1_{s>=2}}, with q the number of nonsingleton parts and s the number of singleton parts, is proved correctly. A star coordinate for each nonsingleton part realizes all required distance-two pairs inside that part while keeping cross-part distances one; when at least two singleton parts occur, one additional half-edge star realizes their mutual distance one. For the lower bound, two distance-two pairs chosen from distinct nonsingleton parts cannot be realized at value two in the same tree coordinate by the four-point condition, forcing q distinct coordinates. If two singleton vertices are present, a coordinate realizing their distance one cannot be one of those q coordinates, again by the four-point condition. Edge cases, including complete graphs and stars, agree with the formula.

## Decisive prior-art issue

The result is not original within the audited repository. The earlier SCOPE record `2026/09/18/phylogenetic-rank-complete-multipartite-graphs--cea9c3369a96` (RESULT.md blob 3f7cf20b91dbfbc2649cecc2404375d76e9cf182) states the same formula `max{1,q+1_{s>=2}}`, with the same star-coordinate upper construction and four-point lower-bound mechanism, and additionally gives a matching-deletion corollary. That record predates the assigned 2026-09-19 record, so the assigned headline theorem is a duplicate rather than an independently new finding.

## Scientific-value consequence

The theorem is mathematically clean, but as a standalone research finding this record adds no substantive scientific value beyond the stronger earlier SCOPE record that already contains the same complete-multipartite classification and proof mechanism. Keeping a second validated copy would create duplicate scientific inventory rather than a distinct contribution.

## Consequence

This package is relocated as a failed research attempt rather than silently deleted. It may remain useful as an alternative exposition or verification example, but its headline must not be represented as an independently original validated finding.

## Prior repository evidence

- `2026/09/18/phylogenetic-rank-complete-multipartite-graphs--cea9c3369a96/RESULT.md` (blob `3f7cf20b91dbfbc2649cecc2404375d76e9cf182`): Earlier repository theorem gives exactly the same complete-multipartite rank formula and proof mechanism, plus an additional matching-deletion corollary.
