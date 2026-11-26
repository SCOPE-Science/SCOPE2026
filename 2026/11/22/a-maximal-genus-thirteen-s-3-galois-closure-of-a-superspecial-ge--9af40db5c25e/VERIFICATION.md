---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1,
  "record_status": "passed"
}
---
# Verification of the marked trigonal descent

The invariant-field identification is proved algebraically in `RESULT.md`: from the ordered reciprocal roots, the two fourth powers are recovered by a three-term Fourier sum using a cube root of unity; adjoining one fourth root has degree exactly four. Conjugation followed by exchange fixes all three ordered reciprocal roots and the marked parameter. Branch inertia and genus are derived by local factorization and tame Riemann–Hurwitz, not by extrapolation from point counts.

The finite-field certificate is the exhaustive loop in `RESULT.md`. Field elements are integers modulo 11 or all 121 pairs \((a,b)\) modulo 11 with multiplication \((a,b)(c,d)=(ac-bd,ad+bc)\). A nonzero pair has inverse \((a,-b)/(a^2+b^2)\), because \(-1\) is nonsquare in the base field. The two histograms are \((4,5,2,0)\) and \((48,0,12,61)\). This verifies the finite splitting table, not historical priority or the function-field argument. The original standalone verifier computes the same histograms by a direct root loop rather than the inverse-fiber loop.
