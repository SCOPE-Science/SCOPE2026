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

# Reproducibility and proof limits

Invoke `python3 CHECK.py` with Python 3.9 or newer and no third-party packages. The checker constructs every binary outcome for \(1\le a,b\le3\), \(0\le c\le2\), and \(1\le L\le7\), enumerates every nonempty voter group, and tests PJR, EJR and EJR+ directly from their temporal definitions. It compares 6,858 such cases against the claimed two-quota interval. Additional rational binomial probability and optimizer comparisons cover horizons up to nine, for a combined 7,758 finite cases. Four further examples calculate the Gaussian critical-window probability with stable log-gamma sums, comparing it to the normal limit.

All tests completed successfully in the reviewed environment. The checker is auxiliary: a finite enumeration is not a proof for arbitrary voter counts or horizons. General validity follows from the structural argument, binomial derivative, Stirling estimates, large-deviation bounds and central-limit reasoning in `RESULT.md`. Source comparison is limited by literature indexing and does not establish definitive publication priority. No independent audit or validation is asserted.
