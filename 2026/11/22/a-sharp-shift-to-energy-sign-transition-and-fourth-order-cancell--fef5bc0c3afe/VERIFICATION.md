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

# Verification notes

The analytic proof in `RESULT.md` establishes the exact positive-branch recurrence, modified-energy decay, global uniform \(O(h^2)\) auxiliary-manifold error, midpoint quadrature asymptotic, and exact radical sign transition. This is a deterministic asymptotic argument, not a claim of computer certification of infinitely many steps.

Run `python check_quartic_sav.py` with Python 3; no nonstandard libraries or external files are required. The checker tests the polynomial antiderivative algebra, energy decay identity, positive branch, sign of two test cases, decreasing coefficient error under refinement, and the fourth-order cancellation test. A finite-step simulation stops at a small positive state, so its reported defect is \(r_n-f(x_n)\), not a numerically assumed exact \(r_\infty-\sqrt C\); the proof supplies that limit. The checker is a supplement and does not establish originality or replace the proof.

Primary-method full-text access was incomplete. The independently conducted mathematical audit has not been performed.
