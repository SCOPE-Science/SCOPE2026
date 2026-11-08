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

# Computational verification of the linear ternary spectrum enumerator

Run `python3 verify.py` and `python3 verify_independent.py` from the extracted directory. Both scripts use only the Python standard library and generate their own data; neither reads the other's output.

`verify.py` computes rational-series coefficients using integer polynomial multiplication and the exact denominator recurrence, then exhaustively examines every nonnegative \(3\times3\) integer matrix with up to nine total edges, checking divergence and connectivity. The actual replay printed `MATRIX_ENUM_OK [1, 9, 24, 65, 156, 342, 683, 1272, 2226, 3708]` and `RATIONAL_COEFFS_OK` followed by coefficients through twenty edges.

`verify_independent.py` performs an independent exhaustive enumeration of all ternary words with lengths one through twelve, derives each complete nine-entry adjacent-pair multiplicity spectrum directly, and compares the deduplicated counts to a separately implemented signed-flow expansion. The actual replay printed `DIRECT_WORD_ENUM_OK [1, 9, 24, 65, 156, 342, 683, 1272, 2226, 3708, 5919, 9120]` and `SIGNED_FLOW_SERIES_OK` followed by a matching series through eighteen edges. `census.csv` provides coefficients through twenty edges for convenience.

These finite calculations verify the claimed initial values and independently test the symbolic corrections. They do not certify an infinite identity; the formal series derivation and complete Euler-support classification in `RESULT.md` are the all-length proof. Neither independent external audit nor further alphabet-size verification was performed.
