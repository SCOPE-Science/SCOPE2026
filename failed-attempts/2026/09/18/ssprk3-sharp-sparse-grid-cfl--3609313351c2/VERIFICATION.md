---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The proof was reconstructed independently. Huang's guarded spatial result gives the contraction \(H=I-B/m\) with extremal eigenvalues \(+1\) and \(-1\). For SSPRK(3,3), the cubic stability polynomial reduces the upper bound to the origin-tangent disk. Re-expanding the boundary modulus gives the stated quadratic Bernstein form; its coefficients are nonnegative exactly through the unique positive root of \(2\mu^3-3\mu^2+3\mu-3=0\). The \(-1\) eigenmode maps to \(-2\mu\) and yields the matching necessity above that root. The repository verifier was inspected only as corroboration, not as the proof.

## originality

FAIL

The final sharp CFL statement is mechanically implied by two published ingredients. Huang proves the exact contraction normalization and the \(±1\) extremal modes for this sparse-grid operator. Dahlquist–Jeltsch's classical Runge–Kutta stability-disk analysis computes the largest origin-tangent scalar stability circle for third-order formulas and records its radius at about 1.25. For a three-stage third-order explicit method the stability polynomial is the same cubic used here; applying the standard polynomial contraction/von Neumann implication and Huang's \(-1\) mode gives the submitted if-and-only-if threshold. The exact algebraic root is a refinement of a already-covered scalar constant, not a surviving new theorem under the audit's implication bar.

## value

PASS

The sharp source-specific time-step ceiling is mathematically and practically useful: it replaces a merely sufficient SSP-coefficient restriction by an exact if-and-only-if condition and quantifies a roughly 25.6 percent improvement. Failure is scientific originality, not value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
