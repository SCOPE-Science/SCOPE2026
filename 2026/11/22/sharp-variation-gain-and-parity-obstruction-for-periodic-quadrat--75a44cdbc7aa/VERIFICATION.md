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

A unit-cell quadratic with secant Δ_i and left slope m_i has right slope 2Δ_i−m_i, so C¹ matching at every knot including the seam is (I+S)m=2Δ. For even n the nullspace and cokernel are both the alternating line; its pairing with Δ is −2 times its pairing with y. Slopes in the kernel generate the nonzero zero-data splines c(−1)^i t(1−t). For odd n the alternating finite series in S inverts the equation. On an atom Δ=e_p−e_q the slopes are 0, ±2. A nonflat-data cell is monotone and has variation 1; a flat-data cell goes out and back by |m_i|/4, for variation |m_i|/2≤1. Every zero-sum Δ is a nonnegative combination of these atoms with total mass ||Δ||₁/2, so linearity modulo constants proves the bound for every real datum. For the spike at 0, m_0=0 and m_i=2(−1)^i elsewhere, giving variation 1 on every cell, including the seam. Independent cell calculations for n=3 and 5 give ratios 3/2 and 5/2. The exact-arithmetic verifier was inspected, not executed; its reported finite checks are consistent with its loops but do not supply the universal proof.

## originality

PASS

Credit is for the sharp attained finite-circle TV norm, not for cyclic slope equations or a claim of new parity lore. The identical catalogue record is not independent priority evidence. The strongest distinct quadratic-periodic paper overlaps the interpolation/solvability setup, but the available evidence does not establish the n/2 norm. The inspected related catalogue statements concern different operators or domains. This is a best-of-evidence judgment, not an absolute priority claim.

## value

PASS

For the ordinary exact periodic nodal interpolator, parity-based existence is not a stability result. The exact attained gain shows linear growth despite the existence and uniqueness of every odd mesh. A single-site datum produces order-one variation even on each flat-data cell, locating a real instability rather than an artifact of a loose operator bound. The invariant is directly useful when choosing or comparing periodic interpolation schemes in BV.

The dated certificate retains the supplied scientific assessment, sources and limitations.
