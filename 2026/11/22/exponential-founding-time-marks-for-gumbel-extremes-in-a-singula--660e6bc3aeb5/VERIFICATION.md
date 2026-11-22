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

The analytical proof uses the published Itô entrance law, a direct Poisson mapping, an exact conditional Gaussian-tail integral, local intensity convergence, and an explicit expectation bound controlling mark escape for the highest-ranked particles. The full proof appears in RESULT.md.

Reproduce finite diagnostics from the extracted files with `python3 checker.py`. A previous execution produced the exact text saved in `verification_output.txt`. All 104 assertions passed. These finite computations check normalizations, Gaussian-tail identities, and the direction of the limiting mark law; no finite check can certify a Poisson-process convergence or mathematical originality.

No independent assessment has been conducted. This file records reproducible evidence and analytical limits, not an external certification.
