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

# Reproduction and limits
Execute `python3 CHECKER.py` in the package directory using Python 3 with no optional dependencies. The checker uses exact rational arithmetic for the sharp witnesses, verifies the selected middle-rank count formula for all radii from \(1\) through \(30\) and every permitted trim level, verifies endpoint extension for radii through \(10\), exhaustively checks the small rank chambers for radii \(1,2\), and performs \(1500\) seeded two-input floating-point inequalities. It prints `ALL_TRIMMED_MEAN_VARIATION_CHECKS_PASS` when successful.

These finite checks do not independently prove unbounded radii or signal lengths. The mathematical proof is the common-core order-statistic lemma, single-jump decomposition, integration over ranking chambers, and the exact parity construction in RESULT.md. Historical priority is unresolved for inaccessible early primary sources. Independent audit has not been performed.
