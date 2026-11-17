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

Correct cyclic forbidden-language reduction and run-pair enumeration: the eight finite factors characterize periodic good binary words (the two exceptional heteroclinic configurations are nonperiodic); cyclic difference ones occur in runs of length exactly 2 or 4 separated by zero-runs of length at least 2; every cyclic code has two binary lifts. The marked-run identity P_n−2=2n Σ_{m≥1} [z^n]((z^4+z^6)/(1−z))^m/m gives zeta 1/(1−z−z^4−z^6)^2, recurrence and Möbius orbit counts. The displayed alternative transfer determinant equals the same rational function; all-period conclusion follows from exact generating-series algebra, not finite tests.

## originality

FAIL

FAIL: two published October 25, 2026 theorems prove the same ALL-n periodic point and primitive-orbit counts before this November 8 package. The first gives zeta [(1+z^3)(1−z−z^3)]^{-2}, IDENTICAL because (1+z^3)(1−z−z^3)=1−z−z^4−z^6. The second gives the strictly STRONGER transition-refined generating series −2z ∂_z log(1−z−u²z⁴−u⁴z⁶), whose u=1 specialization is exactly the present P_n series; its Möbius inversion and run-pair counting are already explicit. Titles and formulas were compared by full-text algebra, not mere search matches.

## value

FAIL

FAIL as a new scientific contribution: the exact rational zeta, every count and Möbius orbit inversion are fully established in prior published work, and the claimed run-pair technique is exactly their proof. Correct re-verification and alternative finite-state certificates do not create a distinct unknown invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
