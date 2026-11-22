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

# Reproducibility and limits

Run `python3 verify.py` with Python 3 and no third-party dependencies. The verifier reconstructs the graph, cycles, all six disjoint triples, degree-three reduced Świątkowski differential, six signed integral product-torus cycles and zero-boundary certificates, six-by-six determinant-one coordinate minor, 6515 integer unit eliminations, three exact residual kernel relations and the mod-101 rank-six check. It terminates with `VERIFY_OK_PAPPUS_THREE_PRODUCT_TORI_PRIMITIVE_RANK_SIX` only if all assertions pass.

The exact integer eliminations and chain boundaries certify all integral claims. Reduction modulo 101 is used solely as a lower bound on rational boundary rank, with the exact integer relation certificates furnishing its upper bound; it is not mistaken for an integral Smith-normal-form computation. The calculation makes no claims about configurations of more particles, other graphs, lower homology degrees or an explicitly embedded non-product generator. Publication priority has not been independently certified.
