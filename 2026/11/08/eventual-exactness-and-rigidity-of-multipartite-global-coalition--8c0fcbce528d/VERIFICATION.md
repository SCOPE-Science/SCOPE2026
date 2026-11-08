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

Run `python3 verify.py` with Python 3's standard library. A successful replay ends with `VERIFY_OK`. The script independently constructs the complete multipartite adjacency relation and checks all vertex partitions for five small graphs (up to ten vertices); checks the upper-bound deficit arithmetic for \(4\le r\le24\); builds exact coalition partitions for four large unequal part profiles; and verifies the injective hub-label allocation count for two small profiles. These are finite tests.

The universal statement is proved in `RESULT.md` by the structural inequality \(E\ge s(r-2)+(r-s)(m-s)/2\), the integrality boundary for \(s=r-1\), the explicit matching construction, and equality rigidity. Review of the mathematical argument was same-model only. No external or independent audit, mechanical formal proof, or global literature-completeness certificate is claimed.
