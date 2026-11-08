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

The standalone `verify.py` reconstructs the 16-state transfer from the one-limited domination definition and symbolically checks its degree-16 characteristic polynomial. It compares coefficients against an independently built labelled graph and all \(2^{2n}\) subsets for \(3\le n\le8\). It separately checks the minimum coefficient through \(n=20\) using exact transfer powers.

Reproduce with Python 3 and SymPy installed: `python verify.py`. The observed run terminated with `VERIFY_OK`. The infinite-family proof is the formal closed-walk identity and the perfect-crossing-matching classification, not the finite computations.

The primary mathematical literature was compared by mathematical implication. Historical-priority and independent mathematical reviews remain outstanding; the newest structural-aspects preprint was accessible only at abstract level in this round.
