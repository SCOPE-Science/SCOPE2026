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
# Reproducibility and limits
The `verify.py` file is a Python 3 standard-library-only checker. Execute `python3 verify.py` from the extracted package directory. Expected output: `VERIFY_OK labeled_masks=260100 compressed_pairs=4900`.

The first loop enumerates all \(2^{c+m}\) binary profiles for every \(1\le c,m\le8\), constructs the graph's actual edge set, evaluates each player's opposing and agreeing neighbors separately, and checks the full equilibrium characterization, labeled equilibrium counts, maximum cut, and minimum Nash cut. The second loop checks 4900 independent occupancy-level examples for \(1\le c,m\le70\), including binomial multiplicity and all welfare formulas. Counts are checked using integer arithmetic only.

This finite empirical coverage is not an all-size proof; the all-size argument is in RESULT.md, based on direct best-response inequalities and a concave quadratic. The data are exact integer counts, not simulated samples. No independent external scientific audit was performed.
