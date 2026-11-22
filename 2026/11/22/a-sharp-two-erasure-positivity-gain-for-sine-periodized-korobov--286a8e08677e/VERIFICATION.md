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

# Verification scope

The analytic proof establishes all sufficiently large even-grid assertions. The separate `verify.py` program tests the exact gap-cube identity, independently solves the original dense Gram systems with numerically integrated kernel means, and compares those numerical solutions with local-hat weights and threshold signs. Run `python verify.py` using Python 3 with NumPy and SciPy in the extracted directory. A local execution returned `VERIFY_OK 74 checks; exact formula and threshold diagnostics passed`.

The finite experiment cannot establish a theorem for infinitely many grid sizes or parameter choices. The proof, not the test count, supplies the general quantifiers. No independent audit has been performed, and the literature comparison is a bounded historical-priority check rather than a uniqueness certificate.
