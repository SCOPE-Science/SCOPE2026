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

The included `VERIFY.py` recomputes the unsigned incidence matrix from the stable-split compatibility rule and checks the full operation sequence in `SMITH_CERT.json`. Each operation is an invertible integral row/column change. The resulting diagonal is checked coefficientwise, as is the Smith divisibility chain. The exact expected output is:

`VERIFIED_M06_BOUNDARY_INCIDENCE_SNF_1x81_2x9_0x15 1948`

The script uses only Python 3's standard library. It is not a general Smith normal form program; it is a replay checker for the provided exact finite instance. The computation does not establish any corresponding statement about Chow-group relations, topology, or the general family of moduli spaces with an arbitrary number of markings.
