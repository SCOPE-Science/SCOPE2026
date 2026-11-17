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

# Verification

Use `python3 check.py` (requires NumPy). The actual run on the embedded program reported `VERIFY_OK cases=56 escape_spectra=all_m_2_to_8 finite_order=all_n_2_to_7`. It constructs the finite Markov matrices and directly computes their eigenvalues for full-lap counts 2 through 8, tests strict parity comparisons for horizons 2 through 7, and independently calculates geometrically pulled-back survivor intervals for counts 2 through 5, horizons 1 through 4. The exact algebraic proof is in RESULT.md. This finite test is neither a proof for all integer m nor independent certification.
