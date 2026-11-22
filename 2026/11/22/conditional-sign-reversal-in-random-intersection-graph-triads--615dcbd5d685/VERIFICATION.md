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

# Verification and limits

Run `python3 verify.py` after extracting that file from this package. It uses only the Python standard library and exact `fractions.Fraction` arithmetic. The program reconstructs the complete three-edge distribution by convolving all eight possible vertex memberships of each independent attribute, then compares it against the analytic probabilities of every labelled graph pattern.

Checked cases: every length from one through four from the five rational membership probabilities \(1/5,1/3,1/2,2/3,4/5\), totaling exactly 780 heterogeneous parameter sequences. Each verifies probability normalization, all three strict covariance signs, and full pattern-by-pattern equality. For one attribute with probability \(1/2\), conditional covariances are exactly \(-1/36\) and \(1/4\).

These finite calculations do not certify the infinite parameter family. The universal correctness argument is the exact product formula plus two elementary strict polynomial inequalities in RESULT.md. No external symbolic service, expert review, or independent mathematical audit has been performed.
