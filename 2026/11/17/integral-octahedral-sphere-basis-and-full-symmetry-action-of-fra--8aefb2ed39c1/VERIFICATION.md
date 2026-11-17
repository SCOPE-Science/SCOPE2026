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

# Reproducible scientific verification

Run `python check_franklin.py` with a Python environment providing `networkx` and `sympy`. The accompanying output file records a completed exact run. The verifier enumerates all independent faces and graph automorphisms, checks an acyclic 95-pair face-poset matching, builds integral simplicial boundary matrices, verifies all octahedral 2-cycles and their orbit sizes, and calculates the Smith invariants for an explicit integral basis. It further computes all 48 integral action matrices, checks every pairwise group multiplication identity, identifies an explicit \(S_4	imes C_2\) splitting and standard-module twist, and reports all conjugacy-class traces.

The finite computation is exhaustive for this exact finite graph; it does not prove any uniform statement for larger crossed prisms. The character calculation is justified by the proved homological concentration. The quotient assertion is rational only. Independent mathematical review remains outstanding.
