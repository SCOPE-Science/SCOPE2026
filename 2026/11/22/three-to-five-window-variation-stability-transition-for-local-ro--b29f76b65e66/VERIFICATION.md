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

# Reproducibility

Execute `python3 check.py` in this directory; it uses only Python's standard-library `fractions` and `itertools`. The script uses exact rational primal-dual KKT verification for the six five-site windows of each of two specified rational inputs. For every window, strict fused-edge dual bounds and strict unfused-edge signs are checked, and the unique proximal solution is recovered through its fused block means. The exact output-difference coefficients are \(0,1/3,0,1,2/3,1\), input-difference variation is \(1/1000\), and output-difference variation is \(7/3000\).

The all-size three-site contraction is proved symbolically from its four possible center-block Jacobians and step decomposition in `RESULT.md`; a finite test cannot independently certify that universal inequality. The five-site certificate only supplies a realized lower bound, not a claim of exact global five-site sharpness. Independent audit has not been performed.
