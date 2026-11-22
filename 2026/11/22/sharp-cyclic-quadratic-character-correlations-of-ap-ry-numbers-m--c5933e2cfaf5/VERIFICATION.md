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

# Verification scope

The proof establishes the Lucas digit product, the exact two-branch cyclic carry recurrence, the full extremizer induction, and the ordered-pair-count inversion for every integer depth \(r\ge1\). The standalone script `CHECK.py` uses only Python standard-library exact integer arithmetic, direct binomial sums, and direct cyclic correlation counts.

Run `python3 CHECK.py` from the directory containing the extracted file. The recorded successful output is `PASS: 3098 independent exact assertions; cyclic depths 1..6`. Exact comparisons cover Apéry values at indices 0 through 100, all shifts for cyclic blocks of depth 1 through 4, extrema and equality-shift sets through depth 6, and sign-pair counts. The checker is finite corroboration, not an independent proof of the all-depth theorem.

A second-person, independent mathematical audit has not been performed. Historical priority risk from implicit general digit-correlation specializations remains, and no statement about modulus 49 or unwrapped correlations is checked or claimed.
