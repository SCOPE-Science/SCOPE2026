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

The full correctness argument is reconstructed in RESULT.md. At differentiability point \(z\) with \(p=f'(z)
e0\), the semigroup assumption and resolvent inclusion force \(p\in\partial f(z+s p)\) for every \(s>0\). The resulting propagation and monotone-derivative classification prove necessity. The clipped translations prove sufficiency, including affine functions. A complete branch partition of the two-slope proximal map yields the sharp signed composition-error envelope and explicit witnesses.

Run `python3 verify_scalar_prox.py` from the same directory using the standard library. The script was executed successfully and reported `PASS 16529 exact rational checks`, verifying exact piecewise algebra across sampled slope and time grids and the endpoint and witness behavior. These tests are corroborative only; untested parameters are covered by the written proof, not by extrapolating from samples.

Literature comparison was performed against the material specified in AUDIT.json. This is a self-review only. Independent audit and historical-priority certification have not been performed.
