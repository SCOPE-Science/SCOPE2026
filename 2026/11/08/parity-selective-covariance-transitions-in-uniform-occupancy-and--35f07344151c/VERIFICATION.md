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

Execute `python verify_parity_occupancy.py` in a directory containing the supplied standalone checker. Its exact arithmetic uses only the Python standard library. A successful run prints `exact_parameter_cases: 25210`.

The checker performs independent multinomial-vector enumeration for three to five boxes at small sample sizes, including singleton and zero-power boundaries; each weighted direct covariance must agree with the conditional-expectation formula. It also compares exact rational signs for three to twenty boxes, frequencies one to fifteen, and sample lengths through one hundred, checking strict even-frequency negativity, the singleton exception, and no return to nonpositive covariance after the odd-frequency transition.

The finite test grid is explicitly bounded. It neither establishes the infinite parameter theorem nor rules out zeros at larger transition parameters. The proof in RESULT.md establishes the general formula, strict Jensen sign, unimodal odd-frequency transition, and scaling limit independently of this checker. No external independent audit has been performed.
