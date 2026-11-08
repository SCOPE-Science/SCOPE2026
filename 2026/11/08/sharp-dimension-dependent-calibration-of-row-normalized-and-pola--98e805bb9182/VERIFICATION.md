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

# Reproduction of finite checks

Run `python verify.py` in an environment with Python 3 and NumPy. The checker constructs random full-row-rank matrices, evaluates all spectral quantities directly, uses positive and negative equicorrelation matrices as explicit sharpness witnesses, tests near-singular branches indirectly through the limiting formula, and checks exact rational Gram eigenvalue and trace identities for the increasing-dimensional witness family.

The completed run reported: `PASS: 10699 finite, spectral, rational and extremal checks`.

These finite assertions corroborate the proof, but cannot replace the all-dimensional Gershgorin--Cauchy--Schwarz argument or establish originality. No independent audit has been performed.
