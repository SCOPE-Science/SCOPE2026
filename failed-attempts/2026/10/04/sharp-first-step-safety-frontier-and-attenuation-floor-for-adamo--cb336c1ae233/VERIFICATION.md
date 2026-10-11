---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Because the smoothing state is nonnegative, the published recurrence contains the current raw rate with coefficient \(1-\beta_3\), so the clipping lower bound follows immediately and is attained at the first step. Standard first-step Adam bias correction makes the corrected moments exactly the current gradient and its square. Substitution into the scalar quadratic gives the package's objective ratio, and solving the elementary square inequality gives the necessary-and-sufficient threshold and neighborhood. Fresh numerical substitution confirms the boundary behavior.

## originality

FAIL

The formulas are correct, but the mathematical content is mechanically implied by the defining published recurrence. Positivity gives \(s_t\ge(1-\beta_3)\eta_t\) in one line, and at the first step equality is immediate from \(s_0=0\). Substituting the standard first-step Adam bias corrections into a scalar quadratic and solving \((1-K)^2\le1\) gives the rest. Under the audit rule that direct corollaries are covered even without identical wording, this does not clear originality.

## value

FAIL

The safety interpretation is potentially useful pedagogically, but the attenuation theorem is a one-line positivity consequence of the defining recurrence and the quadratic frontier is routine first-step algebra. It does not add a nonstandard structural lemma, later-time dynamics, or a motivated nontrivial boundary beyond what the published update already mechanically determines.

The dated certificate retains the supplied scientific assessment, sources and limitations.
