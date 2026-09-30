# Independent audit — Weighted-cosine Hadamard bound fails exactly from dimension three

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/18/weighted-cosine-hadamard-bound--6cfd50338ed1`  
**Audited tree:** `e87fda1adb2b60b2e608e237f4dd1a448cae7267`

## Disposition

**FAILED.** Correctness passes, but originality and standalone scientific value fail because an earlier SCOPE record already contains the same substantive finding. The package should be relocated to the designated failed-attempt path without discarding its evidence.

## Correctness

**PASS.** The assigned theorem is mathematically correct. Exact symbolic recomputation gives U_3 U_3^T=I and B_3=U_3 diag(10,2,1) U_3^T with the displayed entries. Correlation normalization gives ||C||_F^2=1800677/320013, while the conjectured right side is 945/169; the exact gap is 1902128/54082197>0. For the block extension with r=n-3 and t=105/13, the gap simplifies to 4(10386273 r+475532)/(320013(105r+169))>0 for every r>=0. The separate n=2 frame-operator proof is valid and establishes the sharp dimensional boundary.

## Originality

**FAIL.** The repository already contains the earlier 2026-09-17 record `2026/09/17/weighted-cosine-hadamard-bound-counterexample--2c5eeb2ecf13`, which proves the same substantive result: an exact common-frame counterexample in dimension three, validity in dimensions one and two (hence dimension three is minimal), an open/robust counterexample family, and an order-four witness beating the real Hadamard benchmark. The assigned record uses different numerical witnesses and an all-n block formula, but its central theorem and scientific conclusion were already established the previous day.

## Scientific Value

**FAIL.** The calculations are clean and the all-dimension block family is a useful alternative witness, but it does not add a materially new scientific conclusion beyond the earlier record, which already settles the conjecture's exact dimensional validity boundary and the Hadamard-order failure. The later package is therefore duplicative rather than a separate finding.

## Independent checks

- Recomputed U_3 U_3^T and U_3 Sigma U_3^T exactly using symbolic radicals.
- Recomputed the normalized Frobenius value 1800677/320013 and exact positive gap 1902128/54082197.
- Simplified the n-dimensional block-extension gap to the stated positive rational function for all r>=0.
- Compared the theorem against the earlier 2026-09-17 SCOPE counterexample, which already proves minimal dimension three and an order-four Hadamard-frame separation.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.17947 — Loe, Huang and Needell (2026), source Appendix-A weighted-cosine conjecture.
- https://github.com/SCOPE-Science/SCOPE2026/tree/main/2026/09/17/weighted-cosine-hadamard-bound-counterexample--2c5eeb2ecf13 — Decisive earlier SCOPE record: exact dimension-three counterexample, proof of validity for n<=2, and order-four Hadamard witness, published one day before the assigned record.

## Limitations

- Failure is based on originality and standalone scientific value, not correctness.
- The assigned all-n block family is a different witness but does not change the conjecture-resolution or dimensional-boundary conclusions already established earlier.

## Repository identity

The assigned source-tree SHA `e87fda1adb2b60b2e608e237f4dd1a448cae7267` exactly matched the current tree at the audited path on `main`; no stale-tree substitution was used. GitHub was read only during this audit.
