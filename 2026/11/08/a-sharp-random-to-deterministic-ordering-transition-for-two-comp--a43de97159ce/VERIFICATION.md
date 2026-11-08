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

The complete mathematical proof is in `RESULT.md`. To reproduce exact arithmetic checks, run `python verify.py` with Python 3's standard library; no datasets, APIs, or external dependencies are required. The recorded output is in `verification_output.txt` and reports 15,624 passing exact-rational assertions. These include affine composition offsets, stationary means and second moments, the positive second derivative of stationary risk, optimality checks for a rational parameter grid, and complete verification of the displayed rational examples.

The proof's claims for all real \(a>b>0\), \(u\ne v\), \(h>0\) and \(p\in[0,1]\) do not rely on exhaustive enumeration or numerical evidence. The finite verifier cannot certify literature originality or extensions to more than two components. The independent audit channel has not been performed.
