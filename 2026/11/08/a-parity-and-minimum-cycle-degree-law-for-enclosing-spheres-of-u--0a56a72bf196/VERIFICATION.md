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

The exact-arithmetic executable is `verify.py` (Python 3, standard library only). It enumerates all canonical unicyclic constructions through eight vertices, 4,245 configurations in total, comparing exact maximum squared norm and the set of distinct sphere contacts for \(t=1,2\): 8,490 cases, all passed. Independently, it enumerates both cube-generator and edge-generator endpoint signs for 216 cases through six vertices; all passed. The algebraic proof, not enumeration, establishes the formulas for every finite connected simple unicyclic graph and all real \(t>0\).

The unicyclic enumeration covers every unlabeled graph shape because a cycle may be relabeled first and all attached tree vertices may be ordered with parents preceding children. Some isomorphic shapes appear more than once. Both checks measure the Euclidean norm in the explicit vertex-coordinate realization. The proof and computation make no claim concerning multiple independent cycles, arbitrary edge coefficients, or \(t=0\).

Self-review completed. No independent audit or independent validation has been performed.
