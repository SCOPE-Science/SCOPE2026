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

# Verification and limitations

The result is proved analytically by interval invariance, exact affine recurrences and a strict first-step overshoot construction. The checker `verification/check.py` uses the Python standard library and was run from the actual bundle files; it produced `PASS: orderings=72, rational_witnesses=5, invariance_steps=136`. The 72 orderings are the 24 permutations with each of three relaxation values. Five supercritical rational parameters independently verify strict one-step separation. These checks supplement, but do not substitute for, the all-real-parameter proof.

The source model is available as HTML at https://arxiv.org/abs/2610.16406, including its median tie rule, Theorems 9 and 11, and supplement. The earlier asynchronous model is available at https://arxiv.org/abs/2212.08808. The relevant indexed record on directional opinion rings could not be retrieved as full text; priority remains bounded by accessible scientific comparisons. No independent audit has been performed.
