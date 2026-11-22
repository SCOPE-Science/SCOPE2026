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

# Verification details

The theorem uses a global argument: inclusion-exclusion implies the 2-adic approximation once the index is at least \(\max\{8,k+5\}\); exact binomial-series coefficients yield two distance-preserving maps, which are permutations at each finite power of two. Finite checks cannot replace these steps.

Run `python3 check.py`. The script verifies direct Stirling recurrence values, parity-branch formulas, residue histograms through \(2^{10}\), valuation differences through \(2^{12}\), and initial binomial-series coefficients. No externally certified proof or independently performed audit is claimed.
