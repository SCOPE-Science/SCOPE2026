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
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Under the equal-effort independent Poisson model with a fixed common phase, maximizing worst detection is exactly maximizing the minimum total mean. Center the two visits, set q=cos(Δ/2), z=2q²−1 and x=cos φ; the harmonic part divided by 2c is rqx+z(2x²−1). For 0<r<4 the branch minimized at x=−1 runs from q=0 to the unique positive junction q₀ given by rq₀=4(2q₀²−1). Its envelope is strictly convex in q, so only endpoints compete. On the vertex branch the envelope is −r²/16−z−r²/(16z), uniquely maximized at z=r/4 by AM–GM; there rq<4z strictly, so the junction has strictly smaller value. Compare the attained −r/2−r²/16 against the q=0 value −1 to get the exact crossing 4(√2−1) and only the two claimed ties. For r≥4 the vertex branch is absent since 2q²−1≤q; the competing endpoint q=1 gives 1−r<−1. Substitution gives the stated probability, and the unshifted derivative −sin φ(b+4c cos φ) gives two strict maxima for 0<r<4. The time conversion is 4.36868 hours at the crossing on a 24-hour period. VERIFICATION.md and checker.py were inspected, not run; the continuum proof, not the finite grid, establishes the claim.

## originality

PASS

The distinct claim is the exact optimizer set and sharp switch for two equal measurements against one arbitrary phase in the stated aligned two-harmonic model. The closest inspected results share non-antipodal design and switch phenomena but not the optimized functional or the exact threshold. This is not a claim of priority over Poisson zero-count reduction, harmonic identities, or basic scalar optimization.

## value

PASS

The result resolves exactly when equal half-cycle spacing ceases to be optimal in a minimal model where both harmonics matter. The switch between two separated global designs is discontinuous and precedes the loss of the second intensity maximum; knowing the mere presence of two peaks cannot recover the optimal design. This is a meaningful model benchmark for robust timing, not a field prescription for real eDNA signals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
