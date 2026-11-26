---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Verified computations

The accompanying Python 3 verifier replays independent modular Legendre recurrence and Cartier coefficient extraction for all 21 smooth marked parameters in \(\mathbb F_{23}\) and all 527 smooth marked parameters in \(\mathbb F_{529}\). The coefficient extraction uses the geometrically isomorphic plus-sign model: each diagonal entry changes by at most the sign \((-1)^i\) and the geometric rank agrees at every parameter. It checks the exact divisibility by \(Q(t)=(t^{23}-t)/(t^2-1)\), all four and five rank-frequency strata, the smaller-prime minimality checks and \(H(3\omega)=\omega\).

The ground-field quotient sign, genus and rank transfer are justified separately in `RESULT.md`; the script checks arithmetic and does not establish these geometric steps. No full Weil polynomials or abstract isomorphism classifications are asserted by the verifier.
