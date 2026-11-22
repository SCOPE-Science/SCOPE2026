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

# Reproducibility and limitations

The enclosed `verify.py` runs using Python's standard library with `python verify.py`. It replays 802 exact rational-height square inequalities, the affine isotropy moment identities of both four-contact regular tetrahedra, rational scale and volume-factor identities, and 10,001 floating-point support-curve containment diagnostics. The successful invocation reported: `PASS: 802 rational slack identities, two four-point isotropic certificates, exact ellipsoid scale and volume identities, 10001 curve samples.`

The exhaustive assertions are the exact displayed square inequalities, all-parameter trigonometric generator inequality and general John–Löwner moment theorem, not finite experiments. The latter cannot establish infinite containment on its own. Source inspection confirmed the body's prior parabolic-cylinder representation, so that representation is not claimed as a new discovery. The specific ellipsoid optimization remains subject to independent historical and mathematical audit.
