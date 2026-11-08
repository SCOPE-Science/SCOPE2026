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

The package contains two Python 3 standard-library programs, `exact_profile.py` and `independent_prefix.py`.

1. `python3 exact_profile.py` evaluates the 9-residue factor-frequency recurrence with exact rational arithmetic, then asserts the complete 5-by-5 normalized consecutive-run table, all row and column sums, symmetry, total probability one, mean length, and selected shorter factor frequencies. The expected success marker is `EXACT_RUN_PROFILE_OK`.
2. `python3 independent_prefix.py` derives 200,001 parity symbols by repeated extraction of the rational-base digits, independently constructs 200,000 Toeplitz difference symbols, compares them bit-for-bit, enumerates consecutive run lengths and compares the empirical 79,997 run pairs with the exact probabilities. The success marker is `INDEPENDENT_PREFIX_OK 200000 run_pairs 79997`.

The crucial infinite arguments are the vanishing-density periodic approximants, the gcd-based equidistribution on source arithmetic progressions, and the exact boundary-pattern/run-index correspondence. These are in `RESULT.md` and are not claimed to follow from finite enumerations. The code is a reproducibility check, not an independent mathematical audit or external certification.
