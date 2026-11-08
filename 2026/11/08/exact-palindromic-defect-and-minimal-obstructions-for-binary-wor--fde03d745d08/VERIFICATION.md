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

Run `python3 check_pal_defect.py` from the directory containing this document and the accompanying standalone checker. The Python standard library is sufficient; the checker enumerates each word's distinct nonempty palindromic contiguous factors directly, independently of the mathematical counting identities.

Observed pass counts: 8 one-run, 64 two-run, 512 three-run, 2,401 four-run, 16,807 five-run, and 15,625 six-run exhaustive parameter profiles, with run-length upper bounds 8, 8, 8, 7, 7, and 5 respectively. It also passed 1,200 deterministic pseudorandom five- and six-run profiles with lengths up to 16, 180 explicit forbidden-family members, and binary-word enumeration for minimal non-rich words of lengths 1 through 12. The seven-run boundary witness was separately checked via direct palindromic-factor enumeration.

Finite tests alone cannot certify the formulas for all positive integer parameters; the proof is the run-classification argument in RESULT.md. The theorem has not received an independent scientific audit. Originality could be affected by unindexed sources or by contents of journal versions not fully inspected.
