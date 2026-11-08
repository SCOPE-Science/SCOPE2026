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

Use Python 3 and run \(\texttt{python3 verify.py}\) in a directory containing the attached checker. No third-party packages or data downloads are needed. The checker reconstructs each root-to-leaf branch indicator from explicit tree tuples, enumerates all taxon-survival subsets, and expands each probability into an integer polynomial in extinction probability. It checks the entire four-leaf probability-generating-function difference, the mean-response difference, and the half-initial-PD probability difference for each size from four through eleven leaves. It also confirms the rooted binary shape counts through four leaves. All checks passed in the documented run.

The proof of the exact statement for all \(n\ge4\) is given in RESULT.md through the common-root graft generating-function identity and coefficient calculation. Finite enumeration does not constitute an infinite proof, empirical ecological validation or independent certification. The theorem excludes correlated extinction, non-unit edge lengths and non-rooted PD scores.
