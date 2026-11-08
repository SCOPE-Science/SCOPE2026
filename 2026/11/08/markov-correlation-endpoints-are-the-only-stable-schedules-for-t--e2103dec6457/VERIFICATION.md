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

Execute `python3 verify.py` with Python 3 (standard library only). The checker runs 67 exact-rational assertions. It proves the displayed \(6	imes6\) determinant polynomial from seven distinct rational evaluations, using the fact that each matrix entry depends affinely on the Markov stay probability and hence the determinant degree is at most six. It additionally tests the invariant positive-definite forms and two-step relative traces at explicit rational parameters. The general Perron–Frobenius and strict log-determinant arguments are mathematical proofs given in RESULT.md and are not replaced by the finite checks. No almost-sure Lyapunov claim or independently audited certificate is asserted.
