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

Run `python3 verify.py` with Python 3. The script evaluates the sparse block inverses, exact tangent remainder, all independent-sign pair product distributions for sample counts \(1,2,4,7\), variances, and the two-eigenvalue comparison using rational arithmetic. The executed local test reported `VERIFY_OK 2501 exact-rational assertions`.

The infinite-family conclusion is established algebraically in `RESULT.md`; tests over finitely many dimensions are corroboration, not a proof of asymptotics or universal correctness. Matrix-function actions and the correction are assumed exact; accuracy and finite-tolerance costs of numerical inner iterations are not tested. No independent mathematical audit has been performed.
