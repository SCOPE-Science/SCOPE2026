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

# Verification and scope

The mathematical proof reduces the square-function calculation to two eigenvalues on each graph part and uses the exact integral \(\int_0^\infty t\lambda\mu e^{-(\lambda+\mu)t}dt=\lambda\mu/(\lambda+\mu)^2\). It gives a fully quantified all-size fourth-power deficit and the contractivity/equality classification. The \(\delta=1/4\) scalar witness supplies a negative deficit whenever a part contains at least three vertices.

`checker.py` is standalone and was executed with Python 3. It checks exact rational eigenvalue identities and witnesses on ordered part sizes through twenty, and sample complex-valued deficits in the four contractive cases. These finite checks are supplementary, not an exhaustive proof of the all-size statement. No independent review or external mathematical certification was performed. The older graph square-function literature is an acknowledged originality risk.
