# Independent audit — SCOPE-20260919-e2e1dceda65c

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

For every subgroup \(B\leq\mathbb Z\), the Euler-characteristic subcategory has a complete ideal cotorsion pair while the associated object pair is complete exactly for \(B=\mathbb Z\), with truncated Euler characteristics giving the exact object-approximation criteria.

## Correctness

**PASS** — Euler characteristic is additive on degreewise split conflations, so the subgroup subcategory is extension closed and weakly idempotent complete. Contractible cone sequences remain inside it and give the Frobenius structure. Splitting complexes into cohomology plus contractible summands and adjoining correction stalks of prescribed Euler characteristic proves the object-ideal factorizations; the standard degreewise-split Ext formula gives orthogonality. The special ideal constructions have correction terms of Euler characteristic zero, while the long exact cohomology sequence gives the stated necessary and sufficient truncated-Euler criteria. Proper subgroups omit \(1\), giving the stated two-stalk obstructions, and every ambient complex becomes a summand after a suitable Euler correction.

## Originality

**FAIL** — FAIL because an earlier published SCOPE record from 2026-09-18 already states the arbitrary Euler-subgroup theorem with the same complete ideal pair, exact truncation obstruction classes, object completeness iff the subgroup is all of \(\mathbb Z\), and idempotent completion; it is strictly broader, also proving the sharp total-Betti extension-closure boundary. The present record itself additionally acknowledges same-day duplication.

The audit separately checked equivalent formulations, broader coverage, exact database/table overlap, and claim-versus-prior implication. Full source-inspection details and residual risks are recorded in the companion JSON.

## Scientific value

**PASS** — PASS in intrinsic mathematical value: the arbitrary-subgroup classification cleanly identifies the invariant behind the parity example and the exact boundary for descent from ideal to object completeness. Coverage by earlier work defeats originality, not the mathematical interest of the statement.

## Disposition

**FAILED.** A validated finding requires correctness, originality, and value all to pass. The original scientific files and reproducibility artifacts are retained with the failed-attempt package.
