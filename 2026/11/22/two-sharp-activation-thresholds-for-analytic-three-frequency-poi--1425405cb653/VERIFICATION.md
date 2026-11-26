---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and scope of verification

From the package directory, install the dependency from `requirements.txt`, then execute `python3 checker.py`. The relevant assertions test exact Fourier convolution, the resonant sum-of-squares identity, and the sharp onset expansion. The script also tests nonresonant identities and numerical examples for comparison; the nonresonant activation staircase is not claimed as a new result here.

The proof in `RESULT.md` uses the single midpoint collision, the sum of squares at criticality, a strict first-order gain over every boundary support above criticality, and an implicit-function argument for the unique near-critical profile. Finite checks do not certify all radii or replace the proof. The exact resonant global norm and uniqueness of its amplitude profile away from the onset are not claimed.
