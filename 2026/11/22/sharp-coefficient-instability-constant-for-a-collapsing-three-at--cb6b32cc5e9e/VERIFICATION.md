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

Run `python3 check.py` with Python 3 standard library. The independent calculation constructs the auxiliary vectors by their Gram recursion and separately calculates the two-pole normalized-Cauchy coefficients for multiple complex vectors, then compares the sequences. It tests the residue functionals' orthogonality and a normalized extremizing family with explicitly bounded geometric tail. Observed output: `THREE_ATOM_KACZMARZ_DIAGNOSTIC_OK 2122`.

The limiting supremum and its constant follow from the analytic proof, not from these finitely many tests. No independent mathematical audit has been performed.
