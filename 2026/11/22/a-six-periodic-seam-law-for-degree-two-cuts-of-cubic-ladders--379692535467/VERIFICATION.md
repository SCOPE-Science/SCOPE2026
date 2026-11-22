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

# Verification

The standalone `verify.py` requires Python 3 with no third-party packages. It creates the 16-state transfer from the explicitly stated binary predicate and computes the characteristic polynomials on the ten- and six-dimensional row-swap eigenspaces over the integers. It separately constructs edge lists for straight and crossed seam cubic ladders and tests every binary colouring on six small orders, then tests the seam involution directly. Finally it checks exact recurrence identities and the signed correction for lengths through 100. The checker prints `VERIFY_OK` only if every assertion passes.

These checks certify finite matrix calculations and independent finite comparisons. The infinite-parameter conclusions follow from the matrix-trace identity and the monic polynomial recurrences, not from bounded enumeration. The count excludes empty-side partitions and identifies globally complemented colourings. The mathematical proof has not undergone independent audit.
