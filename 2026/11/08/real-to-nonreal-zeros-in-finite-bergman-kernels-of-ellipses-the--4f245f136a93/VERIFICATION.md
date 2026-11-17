---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

From the actual ellipse Chebyshev planar orthogonality, reconstructed K_2m(z,0)=sum_{k=0}^m (-1)^k(2k+1)U_2k(z/c)/U_2k(t), with identical odd-degree center slice. Thin-ellipse limit is (−1)^m U_m(2(z/a)²−1), giving exactly 2m simple interior real roots for sufficiently small b/a. Near-disk rescaling yields P_m(v)=sum_{k=0}^m (−1)^k(2k+1)v^k; its negative-real exclusion and Newton inequality contradiction for m≥2 show ≥4 nonreal roots. Independently recomputed K4 rational quadratic in x=(z/a)² and Δ=64(u−1)²u⁴Q(u+1/u), with Q(y)=225y⁴−600y³−14600y²−44000y−32624. Unique root y>2 gives strict four-real/two-double/four-nonreal transition; degree2 threshold x<1 iff u<1/3. Symbolic identities checked independently, not only a packaged VERIFY_OK.

## originality

PASS

The 2019 ellipse orthogonality and Coulomb-gas articles directly supply the exact finite kernel but do not establish the center-fiber aspect-ratio zero bifurcation, the all-m thin and near-circle dichotomy, or the exact degree-four algebraic critical ratio. Earlier published disk weighted-kernel zero families are different domains/weights. Accept best-of-knowledge with residual unindexed elliptic Christoffel-zero risk.

## value

PASS

The root locus of the finite complex polynomial reproducing kernel on an ellipse is a natural analytic question, unlike generic infinite Bergman zeros. It yields a sharp first degree and exact shape transition with a nontrivial Newton obstruction for arbitrary degree; the explicit algebraic cutoff is reusable in finite-rank planar kernel studies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
