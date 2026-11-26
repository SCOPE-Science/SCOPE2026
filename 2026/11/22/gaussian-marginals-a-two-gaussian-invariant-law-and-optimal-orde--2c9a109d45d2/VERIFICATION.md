---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and limits

The proof in `RESULT.md` uses the contraction in the Hessian norm, the second-moment fixed point and an exact completed-square identity after the last coordinate update. With \(c=1/2,u=9,v=4\) the formulas can be checked by hand: \(a=32/3\), \(d=20/3\), \(L_{12}=6\), \(L_{21}=7\), and \(L(1/2)=6.5\).

The accompanying `verify.py` uses Python, NumPy and SymPy. Its symbolic checks include the second-moment equations, the contraction matrices, the exact objective and its derivative. Its seeded simulation compares selected moments with predictions at \(c=3/5,u=4,v=1,p=2/5\), using 5,000 burn-in epochs and 210,000 retained epochs. Additional covariance and fourth-cumulant checks in the script are supplementary distributional calculations, not assertions of originality for the stationary law. The script is a finite diagnostic, not a proof of the ordering criterion.
