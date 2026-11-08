---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The `coreplus_check.py` file uses exact rational arithmetic and the standard Python library. Execute `python3 coreplus_check.py` from the directory containing that file.

The finite test iterates populations from 1 through 8, inventories of each of the three candidate support classes from 0 through 4, all admissible committee sizes and all allocations of the private winners after saturating the common candidates. For every instance satisfying the theorem's scalar quota conditions, it computes group-constant payment amounts and verifies the full budget identities, maximum-per-payment reserve restrictions, payment caps and losing-candidate reserve caps. For each instance not meeting the quota condition it checks the mathematically necessary reserve obstruction. On the packaged implementation, the observed output is `exact instances 80000 certificates 70370 quota obstructions 9630`.

The proof in `RESULT.md` is the source of the universal quantifiers. Finite tests do not prove results beyond their enumerated domain. All comparisons involving strict inequalities use exact rational numbers. The boundary example is additionally verifiable directly from reserves \(1/2+1/4>2/3\). No external or independent audit has been conducted.
