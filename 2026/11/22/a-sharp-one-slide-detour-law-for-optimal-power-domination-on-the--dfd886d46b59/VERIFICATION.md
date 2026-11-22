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
# Finite proof verification

The three files `check_direct.py`, `check_orbit.py` and `root_spheres.json` are complete and standalone. They need Python 3 standard library only. Run both scripts in the directory containing the root certificate.

`python3 check_direct.py` returned:

```
DIRECT_OK optimal=68 jump_edges=476 slide_edges=272
JUMP_PAIRS 1:476 2:1700 3:102
SLIDE_PAIRS 1:272 2:1088 3:918
SLIDE_MINUS_JUMP 0:1258 1:1020
```

`python3 check_orbit.py` returned:

```
ORBIT_OK all 68 nonedges affine equivalent, power domination opposite to adjacency
BASE_JUMP_PROFILE 1,14,50,3; BASE_SLIDE_PROFILE 1,8,32,27
BASE_LOCAL_PENALTY 0:38 1:30; TOTAL_UNORDERED 0:1258 1:1020
```

The direct checker enumerates the complete pair space and every all-pairs shortest path, with bitset propagation. The orbit checker implements finite-field residues and a separate graph construction, confirms the affine orbit is transitive, and checks the rooted BFS transport. Both check each of the 68 rooted-distance certificate entries. The proof does not infer any statement about arbitrary graph order from enumeration. Human independent mathematical verification has not been performed.
