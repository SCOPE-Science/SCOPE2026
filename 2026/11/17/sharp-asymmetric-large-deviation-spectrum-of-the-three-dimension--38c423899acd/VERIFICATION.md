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

The accompanying `checker.py` uses the Python standard library and no data files. Run `python3 checker.py` in the directory containing this result.

The executed test returned `TWISTED_BAKER_THREE_STATE_LDP_CHECK_OK words=1022 exact_mgfs=30 cubic_parameters=7 strict_iid_comparisons=6`. It checks finite signed Jacobian products, exact rational finite-step moment-generating functions, rational characteristic-curve cases and sample strict comparisons. Separately, symbolic algebra verified the exact polynomial factorization \(f_u((u+2)/3)=-4(u-1)^3/27\), the parametric derivative formula and its strict positivity.

These calculations only corroborate finite identities. The full-horizon theorem uses exact factorization, Perron–Frobenius theory and the finite-state Markov additive large-deviation principle; no numerical sampling or timeout is treated as proof. The rate applies to normalized Lebesgue initial data and does not determine periodic-orbit eigenvalue distributions or sharp subexponential tail prefactors. Independent validation is not asserted.
