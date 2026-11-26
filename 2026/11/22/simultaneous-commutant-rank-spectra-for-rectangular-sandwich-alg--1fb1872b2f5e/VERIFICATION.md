---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Work with A:U→V and e_i:V→U. The projections E_i=e_iA on U and F_i=Ae_i on V commute within each family. A intertwines these families, and each e_i is also an intertwiner in the reverse direction. On an active signature σ, take i with σ_i=1: A and e_i are inverse isomorphisms on the joint spaces, and each e_j there is σ_j times A inverse. On the zero signature each e_j vanishes. On im A the joint eigenspaces W_σ form an ordered direct-sum decomposition, counted by the stated GL quotient. The active spaces in U are independent sections of A over W_σ, contributing q^((m-r)D); the zero space is A^{-1}(W_0). The active spaces in V are the W_σ themselves; the zero space modulo W_0 is a complement to W_active in V/W_0, contributing q^((n-r)D). These choices construct all tuples without overcount. A matrix Y centralizes the tuple exactly when E_iY=YF_i for all i, hence is an unrestricted diagonal family of maps between equal signatures. The active square algebra factors use invertible A, and the residual rectangular factor uses A of rank d_0. Ordinary ranks add, with rank-j rectangular maps counted by the full-rank two-factor count divided by |GL_j|. This proves the stated polynomials including all-zero tuples, r=0, zero-size factors, ordered repetitions and arbitrary characteristic. The claimed independence means fixing the active multiplicities; the literal full type includes d_0 and determines r. Fresh bounded corroboration: python3 /workspace/reproductions/trace_and_commutant.py gives 113 triples over F_4 at m=n=2 and a non-diagonal rank-one A: the zero type occurs once and each active bit pattern 16 times, with active commutant coefficients (1,6,9) and zero-type coefficients (1,75,180). The frozen checker was inspected, not run.

## originality

PASS

Credit the established one-idempotent rank formula, the commuting idempotent pair census, and simultaneous projection/Peirce methods. The supported distinct claim is the complete ordinary-rank polynomial for an unrestricted common centralizing element, with its rectangular residual block, and the resulting all-arity mixed census. The available comparisons do not establish this as a specialization of an earlier enumerator.

## value

PASS

This yields the full rank distribution of the commutant of each tuple, not just the number of compatible idempotents. It resolves which data control the distribution: active signatures matter even at the same marginal ranks (the displayed 32 versus 8 example), whereas changes in the residual sandwich rank do not affect the ordinary-rank polynomial. This is a useful uniform invariant for studying the common commutants of these nonunital matrix algebras.

The dated certificate retains the supplied scientific assessment, sources and limitations.
