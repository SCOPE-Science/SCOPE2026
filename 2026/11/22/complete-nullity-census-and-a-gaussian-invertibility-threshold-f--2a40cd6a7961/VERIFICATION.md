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

The self-contained `check.py` re-enumerates the matrices directly over the prime fields of orders two, three and five, and over the four-element extension field. It compares the complete nullity spectrum, not just totals or nonsingular counts, for eleven small parameter combinations. It separately enumerates the nonsingular symmetric matrices up to dimension three whenever the finite search is below 60,000 candidates. `check_output.txt` contains the exact invocation outcome and all passing cases.

The general-dimensional proof uses two block congruences, a surjective restriction map on symmetric matrices, standard finite-field rank enumerators, a kernel union bound and the binomial central limit theorem. Finite enumeration cannot establish the universal statements or the asymptotic limit. No independent review or external validation has been performed.
