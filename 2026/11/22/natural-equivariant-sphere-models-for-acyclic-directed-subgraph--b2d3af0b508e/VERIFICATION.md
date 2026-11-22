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

The mathematical result is proved in `RESULT.md` using the published equivariant poset fiber criterion and an explicit contraction of each lower fiber. No external or independent mathematical verification is claimed.

The standalone `checks/verify.py` uses only the Python 3 standard library. It constructs orbit-barycenter fixed simplices directly from automorphism actions on arc sets; for every included sample it compares all eligible fixed-orbit faces to acyclic subgraphs of the vertex-orbit quotient digraph, evaluates the reduced Euler characteristic, and checks the SCC-orbit formula. The program exhaustively enumerates all loop-free simple digraphs on two and three vertices, with every cyclic automorphism action, and additionally tests seeded samples for four and five vertices with at most sixteen eligible arc orbits. The deterministic run prints:

```
VERIFY_OK graphs_with_automorphisms= 2811 checked_fixed_faces= 362900
```

This confirms exact finite consistency for the tested cases. It is neither exhaustive for all graphs on four or five vertices nor a substitute for the general equivariant proof. In particular, the code does not itself test the existence of an equivariant homotopy inverse or a cellular sphere homeomorphism. Boundary conventions for the empty complex and for singleton SCCs are addressed in the proof.
