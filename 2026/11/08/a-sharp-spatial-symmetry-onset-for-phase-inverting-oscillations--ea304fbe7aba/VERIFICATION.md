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

# Reproducible checks

Run `python3 verify.py` in the same directory. The checker uses exact rational values and a 4-by-4 periodic Moore lattice. It evaluates all 65536 binary patterns at 10 parameter values, verifies the explicit cut-degree eligibility inequalities, and checks both synchronous updates of each eligible pattern. It includes stripe checks at λ=2/3, 3/4, 7/8 and 1, and an arbitrary small nonuniform rational perturbation at λ=3/4. The result should print `VERIFY_OK`.

The finite checks do not prove the all-grid theorem, which follows from the analytic argument in RESULT.md. At equality of switching thresholds local attraction is not asserted. Independent scientific audit has not been performed.
