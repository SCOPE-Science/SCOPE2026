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

Run `python3 verify.py` in the directory containing this file and `RESULT.md`. This uses only the Python standard library. The independent code path computes moment vectors by inverting the two-state phase-resolved stationary generator, not by expanding the claimed characteristic function. It then performs exact-rational equality checks with the closed-form inverse coefficients and dual-branch map.

The supplied test run returned `PASS: 906 exact-rational assertions across 81 positive parameter tuples` and recorded 27 one-branch and 54 two-branch examples. Symbolic algebra also checked the dual invariance, the quadratic discriminant and positivity-factor identity. Their general validity is explained in the finite-step analytic proof, so numerical or finite rational testing is not offered as an infinite proof.

Check the parameter domain carefully: \(D_0,D_1\) are known and distinct, \(0<D_0<D_1\), \(r,\alpha,\beta>0\), and the hidden state is redrawn at stationary weights at every positional reset. The equality boundary of the dual feasibility condition is excluded because it produces a zero switching rate. Equality of the two inverse roots occurs only when the internal occupancy is balanced.

All scientific conclusions are mathematical within the specified ideal stochastic model. The main text of the closest forward-model article was not fully inspectable; source-priority risk remains. This verification is not an independent scientific audit or an external certification.
