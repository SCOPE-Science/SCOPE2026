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

# Reproducibility

Run `python3 verify_nesterov.py` in the directory containing the extracted package file. It should print `VERIFY_OK 227 exact rational equalities/inequalities` without imports beyond the Python standard library. The checker enumerates every \(\{0,1\}\) sampling path for eleven finite horizons and separately computes the renewal generating coefficients. It checks four success probabilities by four momenta and symbolic critical parameter examples via exact fractions.

The infinite-time assertions are established by the analytic renewal argument in `RESULT.md`: positivity and aperiodicity of the squared-amplitude renewal kernel, its unique dominant pole, and exact rational evaluation at the unit argument. Short-horizon path enumeration cannot establish an asymptotic equivalence or exhaustive originality. No independent audit has been conducted.
