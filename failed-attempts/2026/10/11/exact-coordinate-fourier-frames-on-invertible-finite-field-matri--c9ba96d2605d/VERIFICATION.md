---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The rank-one and rank-two Fourier coefficients were rederived by averaging first and second linearly independent columns, yielding -a and b. The rook-graph eigenspaces give C,R,D and the coupled real 2x2 block with L_±, with multiplicity sum 1+m²(q-1). Positive definiteness follows from a nonconstant zero-entry count and positivity of the other blocks; comparing det(DI-H) recovers the m=2q upper-mode switch. Independently enumerated all GL_3(F_2) (168) and GL_4(F_2) (20160) matrices and recomputed full one-coordinate Walsh Gram matrices; complete numerical eigenvalues matched the submitted spectrum at ≈1e-15. Universal prime-power result comes from the algebra, not GF(2) enumeration.

## originality

FAIL

The entire five-block Gram spectrum, every equality eigenspace, lower L_-, upper D/L_+ with the same strict m=2q transition, and asymptotic condition number are already explicitly proved for the same GL_m(F_q) family in a separate published Resultary theorem that even allows m=2. The submitted m>=3 restriction is a literal special case, not an independently uncovered mathematical finding.

## value

FAIL

FAIL: Once the stronger all-parameter GL_m(F_q) spectral and extremizer theorem is acknowledged, the submitted narrower m>=3 diagonalization, identical crossover and asymptotic are known corollaries. The finite independent checker and alternate derivation enhance reproducibility but leave no independently new natural invariant or boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
