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
# Verification

## Proof and replay

The fixed-size probability law and moment cutoff follow analytically from a multiple-root polynomial test, the conditional product of reciprocal chords in an inverse square Vandermonde matrix, and iterated Hölder applied to a cyclic family of subframes sharing one conditioned node. The full proof is in `RESULT.md`; neither simulation nor any claim of verified software is needed. Replay the crucial exponent by counting the \(m-1\) windows and the \(N-1\) factors involving each residual variable. Each window supplies a square-tail exponent \(1/2\); conditional Hölder gives \((m-1)/(2(N-1))\), exactly the collision exponent. The proof separately treats the critical inverse moment with the lower, not the upper, estimate.

Run `python3 CHECK.py` for a finite exact consistency check of the incidence counts, inverse-moment threshold arithmetic, coefficient normalization, and the design-column identity. The check does not estimate the limiting tail or prove a continuous or infinitely quantified statement. No formal verification or expert attestation is claimed.
