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

# Finite verification and proof limits

Execute `python3 verify.py` with standard Python 3. It constructs every matching for sizes one through seven, computes both statistics independently, and compares all coefficients of the isolation-weighted crossing polynomial to the convolution formula. It also compares rational covariances with the closed-form sum and checks their signs for all sizes two through 249. Recorded result: `PASS exact assertions 339` with 135135 matchings enumerated at seven chords.

The infinite-size statements are proved analytically in `RESULT.md` from the isolated-chord decomposition and the two-sided geometric tail bound. No numerical asymptotic fit is used as proof. The checker does not establish exhaustive coverage of the mathematical literature, the full joint probability law of both statistics, or an independent audit. There are no external software or data dependencies.
