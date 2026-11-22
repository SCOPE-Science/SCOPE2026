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

The explicit proof uses the identity \(F(F(x))-x=8(x^2+3x+3)(x^2+4x+5)\), the derivative congruence \((F\circ F)'(x)\equiv1\pmod4\), and an all-depth valuation lifting lemma. The standalone `verify.py` is checked against the same final packaged bytes; it verifies exact period counts for \(1\le k\le12\). Computation is finite corroboration only. No independent mathematical validation has been performed.
