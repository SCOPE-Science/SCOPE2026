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

# Reproducibility and verification

`check.py` is a standalone Python diagnostic requiring Python 3, NumPy and SciPy. Execute `python check.py` with the code and this Markdown file in the same directory; it prints `PASS 1283 deterministic diagnostics` and reference roots. The checker numerically differentiates the entire no-capture/first-species probability vector, forms the resulting Fisher matrix, and tests the determinant against the independently derived closed expression for multiple species counts and heterogeneous positive rates. It also tests candidate solutions against unequal exposure durations, the monotone species-count effect and selected large-count expansions.

These are numerical diagnostics only. The complete universal proof, including the strict derivative sign and parameter domain, is in `RESULT.md`. No separate symbolic computation, unrestricted computational search, empirical trapping data, or external independent audit is claimed. The likelihood assumes the first capture is classified perfectly and times are discarded; if timestamps are retained, its information matrix differs as calculated in the proof.
