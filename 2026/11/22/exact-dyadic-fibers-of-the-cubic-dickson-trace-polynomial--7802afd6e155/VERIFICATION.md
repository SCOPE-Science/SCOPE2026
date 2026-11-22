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

Execute the accompanying standalone `check_trace_cubic.py` using Python 3. Its two independent procedures are direct modular enumeration of \(x^3-3x\) and evaluation of the closed odd-branch fiber formula. The checker compares all outputs at every residue level \(2^k\) for \(4\le k\le17\) and checks branch congruences and normalization.

The checker completed successfully on the packaged source. This provides finite computational checks only; the complete proof of the unrestricted classification, the inverse-limit root counts, and the Haar measure is the argument in `RESULT.md`.

The archival comparison includes accessible primary full texts and an explicitly named inaccessible 1991 paper. Historical priority is not independently certified. Independent mathematical audit has not been performed.
