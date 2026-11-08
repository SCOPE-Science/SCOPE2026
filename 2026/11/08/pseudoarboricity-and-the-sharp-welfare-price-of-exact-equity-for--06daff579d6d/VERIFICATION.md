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

The standalone scientific check is `python3 verify.py` (Python 3 standard library only). It enumerates all multiplicity patterns on singleton and pair approvals for five small parameter pairs; checks the density identity, constructibility by bipartite matching, exact equitability, literal EF1 inequalities, and sharp welfare envelope; and independently enumerates complete allocations for sampled cases. It also verifies the explicit extremal family and each feasible pseudoarboricity layer in additional sample dimensions. A passing finite check supports the algebra and implementation, but does not constitute an exhaustive proof for all sizes; the universal conclusion rests on the Hall argument, the degree bound, and the extremal edge-count proof in RESULT.md. No external independent audit is claimed.
