# Independent audit — 2026-09-22 campaign

**Source path:** `2026/09/07/021`  
**Audited repository state:** `253a0fe5d0217455660a277f9adb940030e567ad`  
**RESULT.md blob:** `4707f2c35eca0c4f7ae9be2d58f6409044640732`  
**Review date:** 2026-09-23 UTC  
**Reviewer:** separate AI independent audit; no Lean verification or expert attestation is claimed.

## Claim audited

A complete four-orbit census of 6-dimensional 2-step nilpotent Lie algebras over F2 with 2-dimensional centre, including orbit/stabilizer and automorphism orders.

## Correctness — PASSED

The finite computation is internally consistent and was independently reproduced in the audit: the centre-exact fibre has 3360 adapted brackets, partitioned into four orbits of sizes 84, 1260, 1680 and 336, with stabilizers 1440, 96, 72 and 360. The stated derived dimensions and rank-type invariants separate the representatives, and the factor 256 from central shears gives the reported automorphism orders. No correctness defect was found in this census itself.

## Originality — FAILED

The novelty claim does not survive the literature check. Cicalò, de Graaf and Schneider, *Six-dimensional nilpotent Lie algebras* (Linear Algebra Appl. 436 (2012), arXiv:1011.0361, DOI 10.1016/j.laa.2011.06.037) explicitly classify all 6-dimensional nilpotent Lie algebras over arbitrary fields, including characteristic 2. Their central-extension framework identifies step descendants with automorphism-group orbits on allowable subspaces of H^2, and for the 4-dimensional abelian algebra their Theorem 4.4 determines the GL(4)-orbits on 2-dimensional subspaces of the exterior square. That is precisely the orbit problem underlying this fixed-centre stratum. The record's contextual assertion that characteristic 2 was outside the classified six-dimensional theory is therefore false.

## Scientific value — FAILED

After subtracting the published arbitrary-field classification, the remaining contribution is a small finite tabulation of orbit sizes/stabilizers and automorphism orders for a stratum already classified. Those quantities are routine consequences of the same finite group action and do not provide a new regime, theorem, classification, or reusable method sufficient to meet the campaign's scientific-value criterion.

## Search and independent checks

Independent checks:

- independent F2 orbit enumeration of the 3360 centre-exact pairs
- independent stabilizer/orbit-size and automorphism-order checks
- full-text comparison with arXiv:1011.0361, including the central-extension orbit framework and the GL(4) two-subspace classification

Literature/search queries:
- `6 dimensional nilpotent Lie algebras characteristic 2 classification`
- `GL(4) orbits two dimensional subspaces exterior square nilpotent Lie algebra`
- `2-step nilpotent dimension 6 centre 2 F2 classification`

Sources:
- https://arxiv.org/abs/1011.0361
- https://doi.org/10.1016/j.laa.2011.06.037

## Repair / salvage attempt

No bounded wording or proof repair restores originality/value: the central classification claim is already covered. A materially new theorem beyond the known classification would be new research rather than a repair.

## Final disposition

**FAILED.** The record is withdrawn from the accepted findings tree because at least one of originality or scientific value fails after decisive prior-art comparison.
