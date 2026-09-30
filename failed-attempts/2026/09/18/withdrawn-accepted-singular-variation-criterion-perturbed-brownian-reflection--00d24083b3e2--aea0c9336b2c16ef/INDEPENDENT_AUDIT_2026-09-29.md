# Independent audit — Singular-variation criterion for subcritical perturbed Brownian reflection

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/18/singular-variation-criterion-perturbed-brownian-reflection--00d24083b3e2`  
**Audited tree:** `fdc4ddfd835591a59e392aa6167cdfed02bc9d4c`

## Disposition

**FAILED.** Correctness passes, but originality and scientific value fail because a stronger earlier repository finding already subsumes this record. The complete package should be relocated to the assigned failed-attempt path.

## Correctness

**PASS.** The regulator/local-time calculation is mathematically correct. The subcritical orthant Skorokhod map gives the unique candidate and V/(1-nu)=M(W)-x. Tanaka's formula for X=W-b yields K-L^0(X)/2=A-nu J. Since the contact set has zero Lebesgue measure, only singular boundary variation contributes. For increasing b, J<=A and the identity implies K=L/2 iff A=0 for every nu<1/2; locally absolutely continuous boundaries therefore give strong existence and pathwise uniqueness.

## Originality

**FAIL.** A stronger equivalent result had already been published in the same repository at 2026-09-18 05:06:25Z as 'Boundary-charge criterion for subcritical perturbed Brownian reflection' (commit 51734d3619...). That earlier record gives the signed-measure identity d(K-L/2)=1_{X=0,F>0}db+(1-nu)1_{X=0,F=0}db, proves the exact iff criterion |db|({X=0})=0 for general finite-variation boundaries, and derives both the locally absolutely continuous and increasing-boundary corollaries. The assigned record was added only at 22:59Z and its A-nu J formulation and consequences are subsumed by that earlier theorem.

## Scientific Value

**FAIL.** Although correct and clearly written, the record does not add a distinct validated finding beyond the stronger earlier same-day boundary-charge theorem. Its singular-variation decomposition, absolutely continuous corollary, and increasing-boundary criterion are all contained in the earlier result, so separate publication would duplicate an existing finding.

## Independent checks

- Re-derived V/(1-nu)=M(W)-x from the second coordinate and the one-dimensional Skorokhod lemma.
- Applied Tanaka to X=W-b and independently recovered K-L^0(X)/2=A-nu J.
- Used quadratic variation <X>_t=t to verify the contact set has zero Lebesgue measure and therefore the absolutely continuous part of db contributes zero.
- Checked the finite-variation identity on F=M(W)-b and the support of dM to obtain J=int 1_{M=b} db_s.
- For increasing b, verified 0<=J<=A and that A=nu J forces A=0 for nu<1/2.
- Compared line-by-line with the earlier boundary-charge record; its signed-measure theorem is strictly stronger and implies every substantive conclusion of the assigned record.

## Literature and prior-art boundary

- https://arxiv.org/abs/2609.20491 — Chengshi Wang (2026), source moving-boundary perturbed Brownian problem; positive theorem uses the Brownian-scale condition (PB).
- https://github.com/SCOPE-Science/SCOPE2026/commit/51734d361912d5f6b4832d920bf3e7400d116ec6 — Earlier same-day SCOPE record proving the stronger boundary-charge identity and all key corollaries, at 2026-09-18T05:06:25Z.
- https://doi.org/10.1007/978-1-4757-2418-9_7 — Williams (1995), subcritical orthant Skorokhod well-posedness input.

## Limitations

- The failure is not a mathematical-correctness failure; it is due to prior repository coverage and lack of distinct standalone scientific value.
- The subcritical restriction nu<1/2 is essential to the orthant uniqueness argument used here.
- For general singular boundaries, the contact-set criterion remains path dependent.

## Repository identity

The assigned source-tree SHA `fdc4ddfd835591a59e392aa6167cdfed02bc9d4c` exactly matched the current tree at the audited path on `main`; no stale-tree substitution was used. GitHub was read only during this audit.
