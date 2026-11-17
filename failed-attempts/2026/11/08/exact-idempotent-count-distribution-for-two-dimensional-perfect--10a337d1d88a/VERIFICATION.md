---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Uniform GL₂ structure matrices are bijective under transpose-inversion to invertible 2×2 N; each nonzero idempotent corresponds to exactly one rational projective root of the binary cubic F_N=bY³+aXY²−dX²Y−cX³. The matrix-to-cubic map is a linear isomorphism. Irreducible cubic counting yields N₀=L/3. Three-root and two-root binary cubic enumerations, subtracting rank-one factorizations (v₁X+v₂Y)(u₁Y²−u₂X²), give N₂=(q−1)³ for odd q, N₂=0 for even q, N₃=(L−3N₂)/6, N₁=(L−N₂)/2. Independent exhaustive direct idempotent equations on GL₂(F₂), GL₂(F₃), GL₂(F₅) yield counts [2,3,0,1], [16,20,8,4], [160,208,64,48], respectively. Symbolic count proves every prime power; experiments are finite corroboration.

## originality

FAIL

The published 2026-11-02 theorem Exact finite-field idempotent law for two-dimensional perfect evolution algebras already gives precisely the complete 0/1/2/3 distribution for uniformly sampled invertible labeled 2D structure matrices for every finite field, with the same 1/3 rootless probability and odd/even split. Multiplying its stated probabilities by L=(q²−1)(q²−q) produces exactly submitted N₀=L/3, N₁=(L−h)/2, N₂=h, N₃=(L−3h)/6. The older proof uses PGL₂ projectivity and factorial moments instead of binary-cubic classification; the conclusion is identical.

## value

FAIL

Uniform labeled idempotent-count distribution is a natural exact invariant, but the complete law was already published. An alternative binary-cubic enumeration and the same finite-field histogram do not provide an independent classification or new mathematical boundary; reject the covered finding without denying the correctness of its proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
