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

# Finite proof checks

Run `python3 verify_hexagonal_prism.py` in the same directory as `prism6_certificate.json`. The standard-library checker rebuilds the labelled prisms for \(n=3,4,5,6\), exhaustively checks all size-\(n\) edge subsets for being perfect matchings, and calculates exact traces over every support of cardinality at most four. The four face vectors are (1,9,3,0,0), (1,12,42,0,0), (1,15,60,5,0), and (1,18,117,138,0). The certificate independently lists all twenty hexagonal-prism perfect matchings and a sixteen-leaf adaptive query tree. Every edge-response path, leaf witness, edge index, matching-index lookup and cardinality bound is checked.

The graph is finite and all edge subsets, support subsets and tree branches relevant to the claim are examined; this is exhaustive finite proof, not a sample. No results about higher cycle lengths, global minimality, or complete literature priority have been verified.
