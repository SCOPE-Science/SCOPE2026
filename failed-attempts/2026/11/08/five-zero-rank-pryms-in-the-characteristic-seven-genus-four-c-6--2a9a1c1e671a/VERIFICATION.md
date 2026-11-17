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

The characteristic-seven polynomial f=x(x^9+x^6+a x^3+b) has squarefree condition b*Delta≠0 and degree10, hence genus four; the cube-root automorphism has elliptic quotient. Independently reconstructed the characteristic-seven Cartier coefficient matrix, whose block decomposition has determinant 3b²uv², with u=a³+6ab+3b² and v=3a(a+1)-b. On v=0, b=3a(a+1), u=-a²(a+2)² and Delta=2a(a+2)^3, so the two Hasse components do not meet in the smooth locus. The 2x2 rank-one block has stable rank zero exactly when ab²+(a+1)^7=0; its restriction factors as (a+1)^2(2a³+(a+1)^5), and the quintic factors (a-2)(a-3)(a³+3a²-1) over F7. The five nonboundary roots give Prym rank0 with the geometric parameter count 2+3; all four Jacobian (a-number, rank) strata and no Prym rank2 follow. Symbolic checks confirm these identities; direct algebraic semilinear reasoning, not finite-field samples, supplies the all-geometric-parameter proof.

## originality

FAIL

DECISIVE prior coverage: a Resultary theorem published on November 2, 2026, for the identical characteristic-seven genus-four family establishes the same Cartier matrix, full geometric Jacobian rank/a-number strata, precisely five rank-one Jacobian coefficient parameters, doubled Hasse component, and their Frobenius-orbit counts. Its elliptic quotient is ordinary along v=0, so subtracting its rank one identifies precisely the same five zero-rank Pryms. The candidate is the identical classification with variables u=L and v=R, rather than an independent result.

## value

FAIL

The genus-four Prym a-number/rank stratification and five exceptional coefficient pairs are mathematically natural invariants, but as submitted they reproduce the exact previously published all-parameter theorem. The earlier theorem includes stronger Hasse geometry and Frobenius counts. Recomputing a known complete classification with an equivalent block factorization is not an original valuable contribution, notwithstanding correctness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
