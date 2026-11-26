---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The invariant edge restrictions give H_t and V_s; the four corners count once and the open-edge roots are disjoint. Only V_s can be the zero polynomial, with exactly the stated three coefficient conditions. Two upper horizontal interior roots force a<0 because the two endpoint signs agree with a and the values sum to −2; two lower interior roots similarly force a>0. For a<0 the opposite horizontal polynomial is a(u²−1)+1+(λ−b)u and is strictly positive inside even at |λ−b|=1; for |λ−b|>1 it has exactly one interior root by opposite endpoint signs and degree two. The reflected argument handles a>0. The two-root test follows from the vertex, discriminant, and endpoint signs. Independent exact algebraic root counts reproduced the eight finite witnesses; all four transverse polynomial gcds are constant and the four corner eigenvalue pairs are nonzero at the sharp witness. This certifies simultaneous hyperbolicity there and nearby, not at every parameter in the chamber. Replay: python3 /workspace/evidence/bounded_checks.py 4, with proof details in /workspace/evidence/mathematical_checks.md. The packaged rational checks are corroboration only and were not executed.

## originality

PASS

The exact six-parameter vector field and invariant lines are prior; the distinct supported claim is the complete attainable boundary count spectrum, sharp eleven chamber and a simultaneous hyperbolicity witness in that family. No stronger result giving those facts was established by the measured comparisons, which are not a priority guarantee.

## value

PASS

Boundary stationary points are a natural invariant of the introduced invariant-square flow: they determine where boundary trajectories can connect along the edges. The coefficient obstruction sharpens the naive bound, and the exact chamber and hyperbolic realization identify when the maximal boundary configuration is robust. This is useful without any claim about interior limit cycles or global phase portraits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
