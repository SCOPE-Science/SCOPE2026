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

# Verification and scope
Run `python3 verify_torus4x7.py` with Python 3.10 or later; no nonstandard packages or network calls are required. The script constructs the graph with \(28\) vertices and \(56\) edges and enumerates all \(96{,}433\) faces (the empty face included). Matching A produces \(48{,}214\) pairs with critical dimensions \(-1,0,5,5,6\) and has signed Morse boundary \((0,0)\). Matching B independently produces \(48{,}211\) pairs with five critical five-faces, four critical six-faces, and a rank-three, primitive integral boundary. Both check acyclicity on the complete oriented Hasse diagram, with \(623{,}476\) cover relations. The recorded stdout in `verification_output.txt` ends in `TORUS_4X7_TWO_FIVE_SPHERES_ONE_SIX_SPHERE_PASS`.

The proof of integral homotopy type depends on a standard discrete-Morse equivalence plus the standard Hurewicz theorem for a four-connected wedge. The finite computations are exhaustive for this graph only. Repeating with an independent implementation or mathematically auditing the code has not occurred; this is an exact self-review, not independent validation.
