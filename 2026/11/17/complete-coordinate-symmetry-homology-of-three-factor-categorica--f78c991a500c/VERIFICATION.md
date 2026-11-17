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
A standalone Python program `verify.py` reconstructs the specified categorical graph products, enumerates fixed simplices in the cross-cover model, and calculates signed fixed-face characters. It checks 104 cross-complex character cases, and 19 cases independently by direct fixed-face enumeration in the full independence complex. An independent mod-two boundary-rank calculation on the full simplicial complexes checks \((m,n)=(2,2),(2,3),(3,3)\), with respective top Betti numbers \(1,4,14\). See `verify.out` for measured results and its final `VERIFY_OK` line.

The finite computations are not proofs for all parameters. Universal validity comes from the explicit fixed-face classification and the published nonequivariant concentration theorem. No integral equivariant decomposition or independent external audit has been performed.
