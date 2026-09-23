# Independent audit — 2026-09-22 campaign

**Source path:** `2026/09/07/023`  
**Audited repository state:** `253a0fe5d0217455660a277f9adb940030e567ad`  
**RESULT.md blob:** `dedc657c57c2639a88412a56cdb85cc362c112b9`  
**Review date:** 2026-09-23 UTC  
**Reviewer:** separate AI independent audit; no Lean verification or expert attestation is claimed.

## Claim audited

Certified fixed-angle equiangular-line bounds in dimensions 6-8, including a claimed open/conjectural status 28 <= N_{1/3}(8) <= 29 and nonextendability of the triangular 28-line configuration.

## Correctness — FAILED

The stored Gram witnesses, Delsarte-polynomial arithmetic and nonextendability calculation are mathematically consistent as calculations. However, RESULT.md makes a material factual claim that N_{1/3}(8)=28 is only conjectural and that the exact dimension-8 value remains open. That claim is false: the classical fixed-angle result gives N_{1/3}(d)=28 for 7 <= d <= 15. A later full-text source, Kao and Yu's *Four-point semidefinite bound for equiangular lines* (arXiv:2203.05828), explicitly records this classical result and in Corollary 4.7 gives 28 for 7 <= d <= 14 while Remark 4.8 attributes the d<=15 statement to Delsarte-Goethals-Seidel/Lemmens-Seidel. Because the record's central knowledge-status statement is wrong, correctness fails under this audit even though its finite certificates are valid.

## Originality — FAILED

The dimension-8 exact value and the 28-line construction are prior art. The claimed new interval 28 <= N_{1/3}(8) <= 29 is strictly weaker than the known exact value 28. The triangular 28-line system is also the classical extremal configuration; later work records uniqueness in the relevant dimensions. Thus the record does not establish a new fixed-angle extremal result.

## Scientific value — FAILED

Once the known exact value is restored, the advertised dimension-8 tightening and 'open gap' disappear. The remaining machine checks certify already-known bounds/configurations and a nonextendability fact that does not change the optimum. That residual package is not a substantial new scientific contribution under this campaign's value criterion.

## Search and independent checks

Independent checks:

- independent verification of the rational Delsarte identities and saved Gram witnesses
- independent check of the nonextendability arithmetic
- full-text literature comparison establishing the already-known exact fixed-angle value

Literature/search queries:
- `N_1/3(8) equiangular lines 28 exact`
- `Lemmens Seidel alpha 1/3 dimensions 7 15`
- `four point semidefinite equiangular lines 1/3 28`

Sources:
- https://doi.org/10.1016/0021-8693(73)90123-3
- https://arxiv.org/abs/2203.05828

## Repair / salvage attempt

A wording correction to replace 'conjectural' by the known exact value would remove the record's main claimed contribution. No bounded repair leaves a correct, original and worthwhile theorem.

## Final disposition

**FAILED.** The record is withdrawn from the accepted findings tree because at least one of originality or scientific value fails after decisive prior-art comparison.
