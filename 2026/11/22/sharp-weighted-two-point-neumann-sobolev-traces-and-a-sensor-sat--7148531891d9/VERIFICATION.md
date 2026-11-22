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

The proof is analytic. Differentiating \(K(s,t)=1/3-\max(s,t)+(s^2+t^2)/2\) in \(t\) and integrating against the derivative of a mean-zero \(H^1\) function confirms the reproducing property. The low-imbalance phase uses a strictly positive trace-one dual matrix and a positive diagonal Hessian; its gradient vanishes at the proposed design. The high-imbalance phase is certified by the heavier evaluation's universal diagonal bound, whose equality requires its midpoint and zero correlation. These certificates hold for every positive weight ratio, not only a numerical grid.

Run `python3 check.py` from the unpacked file bundle. It validates kernel identities, two-point eigenvalues, low-phase Gram scalarity, dual feasibility, dual criticality and 150,000 randomized comparisons, with floating-point tolerances. It does not independently certify a universal theorem, assess historical uniqueness, or substitute for the written analytical proof.
