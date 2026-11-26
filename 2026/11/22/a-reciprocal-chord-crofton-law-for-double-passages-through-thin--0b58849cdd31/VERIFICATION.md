---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1,
  "record_status": "passed"
}
---
# Verification of the thin-tube Crofton law

The analytic verification is the signed-distance argument in `RESULT.md`. Its uniform estimates separate the near-support range 
\(\lvert t-t_\pm\rvert\le D r\), whose invariant multiple-hit measure is \(O(r^{5/2})\), from the two-branch region. In the latter region the key bounds are a longitudinal branch separation of order at least \(\sqrt{\delta}\), an inclination cutoff of order \(r/\sqrt{\delta}\), and an allowable orthogonal offset interval of width \(O(r)\). These imply both tightness in the rescaled inclination and integrability near support. The fixed-interior limit uses interval length comparison and does not use an exact \(2r\) upper bound on an oblique projected band's width.

The accompanying `verify_line_tubes.py` is a finite NumPy/SciPy diagnostic for the ellipse integrals and circular tube. Its code samples directions and orthogonal offsets and computes quartic roots at two fixed positive radii, \(0.2\) and \(0.5\) for major radius one. These are sampling diagnostics, not a certification of the exact probabilities or the limit. The order of the circular limit and its constant follow analytically from the theorem and ellipse integration. No formal proof-assistant verification or expert attestation is asserted.
