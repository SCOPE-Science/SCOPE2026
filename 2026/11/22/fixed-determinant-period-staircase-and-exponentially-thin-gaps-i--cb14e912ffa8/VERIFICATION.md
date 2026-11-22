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

The analytic proof uses the exact generating function and root monotonicity. `python check.py` provides reproducible, high-precision finite diagnostics only. It checks strict parameter ordering, the actual max-plus recurrence to the claimed reset time and the return state, and the normalized gap/window constants for four fixed values of \(r\) and three different high-period indices.

**Limits:** This checker is not an exhaustive scan in all indices or real parameters; the infinite theorem rests on the proof. The full text of Ohmori–Yamazaki (arXiv:2402.06230v1) was inspected. An indexed prior related result about the \(T=D\) path was compared using its publicly retrieved abstract, not a full proof, so equivalent unpublished work remains possible. Independent mathematical audit has not been performed.
