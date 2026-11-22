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

# Verification of the stated mathematical result

The derivative and strict concavity of the logarithmic joint detection objective are established algebraically in the proof. The finite-budget boundary is justified by the strictly increasing exponential-increment ratio; both strict inequalities and the equality boundary are handled. The signed derivative and global optimum are checked by standalone `check.py` under three regimes and supplementary random inputs. Exact fractions verify the sign of the illustrative boundary polynomial at two rational endpoints. Run `python check.py` using standard Python 3. Numerical optimizations and finite tests do not establish the theorem over all positive real parameters; that domain is covered by the analytic inequalities.

No independent audit or field calibration has been performed. The decision model excludes correlated encounter noise, imperfect occupancy, extra visit costs and incomplete season accessibility.
