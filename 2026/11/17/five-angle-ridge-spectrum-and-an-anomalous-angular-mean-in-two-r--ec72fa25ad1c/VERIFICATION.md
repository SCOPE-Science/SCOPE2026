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

The enclosed standalone `verify_monge_ridges.py` builds the published vertices directly, verifies their facet incidences, and checks every facet-pair intersection by exact rational affine ranks for \(q=2,3,4,5,6,7\). It confirms the complete combinatorial classification, six separate facet-pair counts, and the squared odd-integer ridge total. The general theorem is proved by the analytic construction and normal products in `RESULT.md`; this finite calculation is corroborating evidence only.

Separate arithmetic checks compared the direct angle-weighted mean with the simplified formula at \(q=2,3,4,5,25,1000\) and the claimed asymptotic constant. The probability of order \(1/q\) and rescaled magnitude of order \(q\) of the rare acute contribution explains why the rescaled first moment is not the first moment of the weak limit; no uniform-integrability claim is made.

Independent mathematical audit has not been performed.
