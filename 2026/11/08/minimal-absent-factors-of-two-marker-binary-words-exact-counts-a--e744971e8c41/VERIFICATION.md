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

The self-contained `verify.py` compares sets obtained from a generic factor dictionary against the stated structural families for all triples \(a,c\ge0\), \(b\ge1\), \(a+b+c=n-2\) through \(n=45\). It checks 14,190 triples, and independently samples 1,000 longer parameter sets of lengths 46–300. Its finite-population mean and variance outputs approach the analytically derived \(7/18\) and \(25/648\) after normalization. The unbounded theorem rests on the rectangle/corner classification and Dirichlet-limit argument, not enumeration.

Run: `python verify.py`.

No independent audit is claimed or supplied.
