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

# Checks and limits

The reproducible program `verify_integral_cyclic_triplets.py` uses the exact vertex set and cyclic-distance rule in the theorem. For each integer \(m\) from 2 through 8 it constructs every one- and two-simplex, the signed simplicial boundaries, and the signed action of the one-third rotation. It verifies \(\partial_1\partial_2=0\), invariance of triangle boundaries under rotation, boundary ranks modulo 2, 3, and 5, and the Lefschetz trace. It additionally computes nullspaces over \(\mathbb F_3\) and the ranks induced by \(g-I\) and \((g-I)^2\) on first homology. All comparisons agree with the uniform module formula.

The checked finite values do not establish the infinite theorem. The proof in `RESULT.md` independently establishes the full integral module for every parameter using exact group-ring elimination. No independent audit is claimed.
