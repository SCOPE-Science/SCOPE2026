---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Reconstructed the centered y_i=a_i(x_i-x_i*) and scaled-dual sweep, triangular row reductions, R_{i+1}-R_i=(lambda-1)y_i, cyclic bidiagonal determinant and removable lambda=1 factor, establishing the full (n+1)-degree polynomial including zero multiplicity. Direct Schur inequalities establish n=3 convergence at all positive penalties. Independent exact-rational matrices and characteristic polynomials were computed for n=2..5 under multiple permutations. The finite computation is corroboration, not the proof for arbitrary n.

## originality

PASS

The evaluated novelty is full fixed-order isospectrality for every n>=2 and heterogeneous strictly convex scalar blocks with one scalar constraint; the known equal-curvature three-block optimal-penalty result and general randomized/Gauss-Seidel ADMM analyses do not imply this all-order characteristic identity. No searched prior record establishes its full statement. This is best-of-knowledge, not proof of global priority; the three-block Schur corollary may overlap specialist results.

## value

PASS

Order-dependent convergence rates matter for multiblock ADMM. Proving that every fixed cyclic order has the same complete eigenvalue multiset for this natural rank-one constraint class, while finite-time vectors differ, is a structural algorithmic result beyond textbook parameter substitution; heterogeneous arbitrary n is essential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
