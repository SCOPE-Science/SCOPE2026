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

# Reproducibility and verification

The exact proof in `RESULT.md` solves the two-state forward equation and differentiates the resulting finite-horizon objective. The critical one-crossing comparison is the explicit strictly positive identity for \(\mathcal B_t\mathcal B-q\mathcal B_q\); this is the mathematical basis for uniqueness, independent of any finite experiment. The integral representation verifies comparative statics. All endpoint cases, including no appreciation and the zero-extinction boundary comparison, are stated in the proof.

Run `python check.py` using Python 3 standard library in the same directory as the result. The checker exercises the derivative-sign identity, threshold behavior, example, a dense grid of feasible construction dates for selected parameters, and a separate forward-ODE integrator. The checker's deterministic tests passed 4498 assertions on the recorded package candidate. These numerical tests cannot establish the infinite continuum of parameter choices or prior-art absence; those limits are addressed by the proof and the qualified literature review, respectively.

The benchmark \(a=\mu=H=r=1\) has threshold \(4/(e^2+1)\) and an optimal delay near \(0.3640459757\). The two-state model deliberately excludes finite source supply, stochastic funding, habitat-area feedback and changing environmental rates. Independent audit and validation are not performed.
