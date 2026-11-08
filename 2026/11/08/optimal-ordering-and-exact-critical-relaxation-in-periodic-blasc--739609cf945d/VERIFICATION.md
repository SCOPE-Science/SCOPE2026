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
# Verification of the stated radial switching theorem

The attached `verify.py` is a standalone Python 3 script using SymPy and mpmath. Execute `python verify.py` in the directory containing this document and the script. It checks two symbolic conjugacy/recurrence identities, four exact rational coefficient words, three exhaustive small-multiset order comparisons, and twelve 75-digit radial computations (up to 20,000 complete blocks each). The observed result was `VERIFY_OK symbolic_cayley=2 exact_coefficient_cases=4 exhaustive_ordering_multisets=3 high_precision_runs= 12 max_sweeps=20000 precision_digits= 75`.

These are finite reproducibility checks. The proof of the infinite theorem is the exact recurrence and its positive-sum/telescoping estimates in `RESULT.md`. No computer search is interpreted as exhaustive over infinite parameters. The data do not independently validate historical priority. The excluded initial state \(x_0=1\), nonreal inputs, and nonperiodic driving are not tested or claimed.
