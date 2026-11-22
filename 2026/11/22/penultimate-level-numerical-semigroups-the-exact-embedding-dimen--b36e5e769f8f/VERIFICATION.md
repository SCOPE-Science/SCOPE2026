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

# Verification record

The proof is self-contained through four reductions: divisible residues, extremal cyclic zero-sum sequences, symmetric gap reflection for a two-generated subsemigroup, and uniqueness of the remaining defective tuple. The full proof appears in RESULT.md.

`verification.py` performs an independent finite experiment using Kunz coordinates, an additive decomposition test for minimal generators, and exhaustive Apéry-level tuple checks. The program checks 2,344 semigroups (multiplicities 3 through 7) and prints `VERIFY_OK 2344`. Those finite tests do not certify the infinite assertion; the proof handles unbounded multiplicity and unbounded semigroup elements.

No computer algebra, unpublished downloaded paper or external certificate is required. Historical literature overlap cannot be ruled out categorically, and independent mathematical auditing has not occurred.
