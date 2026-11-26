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
# Reproduction

From the directory containing these files, run `python3 verify.py`. The script uses the Python standard library. Its 7,264 finite comparisons give numerical diagnostics for the angular normalization, extrema, signs at selected exponents and geometric witnesses. These checks do not prove a result for a continuum of exponents and weights.

# Analytic checks

The exact minimax proof uses the heaviest-node and largest-empty-gap witnesses, both attained by the equal orthogonal rule. Strict worsening of both extremes at every other rule proves uniqueness. The norm reduction follows by integration and a thin-rectangle limit. The polarity statement is a corollary of the prior order-four phase-moment comparison via the axis value and uniform phase mean. The cited moment analysis, not the finite samples, controls its strict signs.
