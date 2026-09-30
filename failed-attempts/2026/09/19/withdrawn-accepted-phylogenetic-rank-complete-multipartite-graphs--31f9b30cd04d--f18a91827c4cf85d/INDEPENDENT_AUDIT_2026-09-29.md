# Independent audit — Phylogenetic rank of complete multipartite graphs

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/phylogenetic-rank-complete-multipartite-graphs--31f9b30cd04d`  
**Audited tree:** `dd25339572e3296b144a2184d8b68ea516ffce9d`

## Disposition

**FAILED.** The mathematics is correct, but originality and standalone scientific value fail because decisive earlier repository coverage already contains the result. The record should be relocated to its assigned failed-attempt path.

## Correctness

**PASS.** The formula r_phy(K_{n_1,...,n_r})=max{1,q+1_{s>=2}}, with q the number of nonsingleton parts and s the number of singleton parts, is proved correctly. A star coordinate for each nonsingleton part realizes all required distance-two pairs inside that part while keeping cross-part distances one; when at least two singleton parts occur, one additional half-edge star realizes their mutual distance one. For the lower bound, two distance-two pairs chosen from distinct nonsingleton parts cannot be realized at value two in the same tree coordinate by the four-point condition, forcing q distinct coordinates. If two singleton vertices are present, a coordinate realizing their distance one cannot be one of those q coordinates, again by the four-point condition. Edge cases, including complete graphs and stars, agree with the formula.

## Originality

**FAIL.** The result is not original within the audited repository. The earlier SCOPE record `2026/09/18/phylogenetic-rank-complete-multipartite-graphs--cea9c3369a96` (RESULT.md blob 3f7cf20b91dbfbc2649cecc2404375d76e9cf182) states the same formula `max{1,q+1_{s>=2}}`, with the same star-coordinate upper construction and four-point lower-bound mechanism, and additionally gives a matching-deletion corollary. That record predates the assigned 2026-09-19 record, so the assigned headline theorem is a duplicate rather than an independently new finding.

## Scientific value

**FAIL.** The theorem is mathematically clean, but as a standalone research finding this record adds no substantive scientific value beyond the stronger earlier SCOPE record that already contains the same complete-multipartite classification and proof mechanism. Keeping a second validated copy would create duplicate scientific inventory rather than a distinct contribution.

## Independent checks

- Re-derived the star-coordinate upper embedding for all patterns of singleton and nonsingleton parts.
- Rechecked the four-point incompatibility forcing distinct coordinates for distance-two pairs from different nonsingleton parts and a further coordinate for a singleton pair.
- Compared the full theorem and proof against the earlier 2026-09-18 SCOPE record, which contains the identical formula and argument.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.19372 — Ashworth–Clarke–Giansiracusa–Jones–Quijas-Aceves–Ren source introducing/studying graph phylogenetic rank; the current public record was submitted 2026-09-16 and updated 2026-09-18.
- Repository prior art: `2026/09/18/phylogenetic-rank-complete-multipartite-graphs--cea9c3369a96/RESULT.md` (blob `3f7cf20b91dbfbc2649cecc2404375d76e9cf182`) — Earlier repository theorem gives exactly the same complete-multipartite rank formula and proof mechanism, plus an additional matching-deletion corollary.

## Limitations

- The failure is about originality/scientific inventory, not mathematical correctness.
- The external source paper establishes the surrounding phylogenetic-rank setting; the decisive priority comparison here is the earlier SCOPE repository record, which was read in full.

## Repository identity

The assigned source-tree SHA `dd25339572e3296b144a2184d8b68ea516ffce9d` matched the current tree at the audited path after comparison at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`, source-tree checked commit `253a0fe5d0217455660a277f9adb940030e567ad`, and current `main`. GitHub was read only during this audit.
