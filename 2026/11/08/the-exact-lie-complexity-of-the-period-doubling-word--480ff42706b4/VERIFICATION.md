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
# Verification notes

The proof in RESULT.md is symbolic and valid for every positive length; `verify.py` checks finite cases independently. The executable expands the actually occurring source pairs `00`, `01`, and `10` into adjacent blocks of substituted length at least the requested factor length. Any factor of that length lies in two such blocks, making the enumerated finite factor set complete for that length. It counts the fully represented cyclic orbits for each length from 1 through 160 inclusive and checks explicit low-length orbit representatives.

Actual local execution output:

`VERIFY_OK lengths=1..160 exact-factor-cover=adjacent-substitution-blocks factor_instances= 20267 lie_formula=PASS`

This finite enumeration cannot, by itself, prove the full theorem, exclude all equivalent earlier literature, or establish independent audit.
