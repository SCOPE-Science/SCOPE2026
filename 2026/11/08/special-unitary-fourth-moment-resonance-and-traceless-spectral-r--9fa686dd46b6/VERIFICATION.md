---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

# Verification and scope

Run `python su4_fourth_checker.py` with Python 3, SymPy and NumPy installed. The script checks the two-pair unitary Weingarten inverse and alternating-tensor contractions, tests rational diagonal profiles and exact examples of the extrema, and generates 48,000 numerical Haar samples on \(\mathrm{SU}(4)\) by QR decomposition with determinant-one normalization. It also retains diagnostics on trace-zero Hermitian examples, which are not an independent novelty claim. The expected final line is `ALL_SU4_FOURTH_MOMENT_CHECKS_PASSED`; the numerical tolerance for the fourth-moment ratios is 0.20.

The all-matrix theorem rests on the moment reduction and sharp singular-value and determinant bounds in `RESULT.md`. The sampled and finite checks do not establish parameter-uniform inequalities, equality classes or literature priority.
