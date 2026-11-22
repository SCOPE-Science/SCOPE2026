---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For F9=F3[u]/(u^2+1), all four primitive odd multiplicative characters e=1,3,5,7, the 126 four-label sets partition into affine orbits of 72,18,36 members; inspected verify_f9.py constructs the finite-field matrices in Z[X]/(X^8-X^4+1), uses exact trace/Newton identities to compare all eight characteristic coefficients against Q72^2, Q18^2, Q36^2, and rational sign-change isolations. Antiunitary J with J^2=-1 enforces even eigenvalue multiplicities; complete quartic positivity yields four-plane spanning. Independently recomputed the affine orbit counts and numerical roots; Q36 has least root ≈0.52990359, so sharp lower fusion bound ≈0.06623795, Q72 greatest root ≈15.75534744 giving upper ≈1.96941843. Numerics corroborate but do not replace the exact certificate logic.

## originality

PASS

The prior order-nine harmonic frame theorem gives complete rank strata but expressly excludes smallest-positive-singular-value bounds; the current three exact characteristic-polynomial squares and orbit-sensitive sharp constants are stronger spectral invariants. General EITFF construction and 13-plane Paley spectra do not imply this F9 octic census. Best-of-knowledge originality subject to unindexed equivalent spectra.

## value

PASS

The natural F9 harmonic EITFF has erasure robustness, but exact sharp frame bounds and orbit-specific conditioning are independent, motivated invariants: even a known full-rank 4-subset can be arbitrarily ill-conditioned. This complete 126-configuration finite classification supplies precise worst erasure pattern and constants across all odd characters, without claiming a new frame construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
