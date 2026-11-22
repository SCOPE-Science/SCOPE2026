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

# Verification of the Gaussian normal-cone law

The symbolic proof in `RESULT.md` is the source of the all-dimension statements. `verify.py` performs checks independent of the symbolic derivation: it lists each vertex of the fractional clique stable-set polytope; tests feasibility, full active-constraint rank and the Gaussian argmax classifier against independent linear programming in six dimensions; and checks the three-support event probability by simulation. The finite checks establish consistency on tested instances, not an infinite or literature novelty proof.

Run `python3 verify.py` using NumPy and SciPy. Observed output markers include `VERTEX_AND_GAUSSIAN_SUPPORT_LP_PASS 1500`, `THREE_SUPPORT_ANGLE_PASS`, and `CLIQUE_GRAPH_POLYTOPE_CHECK_PASS`.

The principal nonstandard steps independently requiring scrutiny are completeness of the vertex list, the argmax classification when at most two entries are positive, the Gaussian tail moment identities, and the normalization of the conditional collision law. Each is proved explicitly in `RESULT.md`. No independent mathematical audit has been conducted.
