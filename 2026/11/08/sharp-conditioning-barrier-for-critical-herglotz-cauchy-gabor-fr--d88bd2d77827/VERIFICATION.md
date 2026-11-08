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

# Verification of critical Cauchy mixture bounds

The exact claim is proved in `RESULT.md` by critical Zak diagonalization, a pointwise positive-resolvent inequality, sharp one-sided essential boundary limits, and a scalar perfect-square identity. The finite script `check_critical_cauchy.py` uses only the Python standard library and can be run with `python check_critical_cauchy.py`.

The embedded checker was executed and reported `CRITICAL_CAUCHY_FRAME_CHECKS_PASS 6062`. It exercises positive mixtures with one through six poles, randomized lattice scales and weights, direct raw-window truncated Zak series, boundary approaches, and exact conditioning-deficit comparisons. Truncation and sampling cannot prove the universal statement; the argument in the proof is required. No independently audited proof or external formal certificate is asserted.

Known single-pole Zak bounds are explicitly credited to Belov–Kulikov–Lyubarskii (arXiv:2212.08915). The frame-set premise for positive Cauchy mixtures is credited to Belov–Kulikov–Lyubarskii (arXiv:2103.08959), although the positive-resolvent argument also directly yields positive critical lower bounds here. The originality assessment is provisional with the risks stated in `REVIEW.md`.
