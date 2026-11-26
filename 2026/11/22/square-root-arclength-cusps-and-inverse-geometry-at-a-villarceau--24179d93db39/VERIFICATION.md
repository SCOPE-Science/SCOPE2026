---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The exact boundary-length quadrature in `RESULT.md` follows from the radial solutions. Near each node the proof uses exact smooth coordinates for a hyperbola, controls the error from replacing the varying plane metric by its value at the node, and evaluates the signed length comparison using complete elliptic integrals. The corrected conversion from the hyperbola scale to angle uses \(m=R/(ra)\), \(\eta\sim a\sqrt{|k|}\) and \(k\sim 2ra(\beta-\beta_*)\).

Run `python checks/torus_section_checker.py` from the package root with NumPy and SciPy. The recorded run reports 174 assertions concerning five aspect ratios, one-sided coefficient convergence, endpoint lengths, chord sums from the radial parametrization, and sampled inverse ordering. Quadrature and chord sums use different numerical length estimators for the same radial parametrization. These finite-precision diagnostics do not prove the pointwise limiting law, establish historical priority, or constitute expert or formal certification.
