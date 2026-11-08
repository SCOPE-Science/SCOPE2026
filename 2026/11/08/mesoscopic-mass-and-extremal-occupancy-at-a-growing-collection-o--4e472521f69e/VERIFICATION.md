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

# Verification of the stationary scaling law
Run `python check.py` with Python 3.10 or newer. The standalone standard-library script checks finite conserved-state generator balance, normalization, exact total-mass weight ratios, the quadratic mode identity, finite total-occupation scale/variance diagnostics, and exact conditional factorial moment evaluations. The run yielded `PASS 130 finite and asymptotic diagnostic checks`.

The proof in RESULT.md supplies the all-size justification: the mode and uniform Gaussian envelope follow from differentiating the exact logarithmic weight ratio; the local curvature is twice the bulk inverse variance; conditional weak compositions give exponential selected-site tails and Gumbel exceedances. These mathematical steps, not the finite experiments, imply the stated limits. The asymptotic results require exactly the hypotheses stated, and the Gumbel limit has an additional logarithmic defect-growth restriction. No independent audit was performed.
