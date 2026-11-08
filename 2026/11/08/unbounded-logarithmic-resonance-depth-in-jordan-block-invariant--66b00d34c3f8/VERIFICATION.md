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

The proof is analytic and is independent of the finite checker. Run `python3 verify.py` in a standard Python 3 environment. Exact rational tests verify 2700 polynomial-recurrence cases, 640 finite orbit identities, and the nilpotent-shift range test for dimensions \(m=1,\ldots,8\) and forcing orders \(k=2,\ldots,6\) at \(\lambda=1/2\). The universal results for arbitrary \(m,k,\lambda,v\) follow from Pascal's identity, nilpotence, and the proof of the remainder and smoothness estimates, not extrapolation from these tests. The checker has no dependencies beyond the Python standard library.
