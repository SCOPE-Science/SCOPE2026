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

# Mathematical verification

Run `python verify_or3.py` with SymPy available. The actual checker was run on the embedded source and passed. It confirms the full symbolic mixed derivative, the fixed-product affine dependence, exact axis/diagonal identities, and the rational Taylor bracket bounding \(e^{7/3}\).

The universal parameter-domain proof is analytic, using the inequalities in RESULT.md. No finite sample or grid is used in place of proving all \((x,y)\in[0,1]^2\), all \(b\ge0\), or all admissible \(a\). The 2022 general transformation theory is acknowledged; its full text could not be accessed, so historical comparison is not independently definitive.

No external independent audit or certification has been performed.
