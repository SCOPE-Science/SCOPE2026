---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A unit coefficient f is restricted nilpotent just when the coefficient of t^(p−1) in 1/f is zero: integrating the other terms gives the normal form (1+b u^(p−1))∂u, whose p-power is −b times itself. The condition solves linearly for the last coefficient with invertible coefficient on the unit open, giving G_m × A^(p−2). Valuation one is excluded by the action on (t)/(t²); valuations at least two raise degree. In a bracket with f of valuation r, the initial term for a coefficient of valuation s≠r is f_r g_s(s−r)t^(r+s−1) if that exponent is below p. If s=r, subtract a multiple of f first. This gives the exact centralizer and regular projection using division by the nonzero leading coefficient. For an independent class computation let a=(p−1)/2 and L=[A¹]. Partition triples by the minimum valuation and the first position attaining it. The unit case contributes L^(p−2)(L³−1), and the all-high case (valuation at least a+1) contributes L^(3a), since that ideal is abelian. For each minimum r from 2 through a, the valuation-r entry has base class (L−1)L^(p−r−1); preceding entries range over the high ideal of dimension r−1, and following entries over the abelian centralizer of dimension r. Summing over positions yields (L−1)(1+L+L²)L^(p+r−3). All charts and inverses are regular over k, without perfection assumptions; summing produces the stated class. Point counting over extensions and the exponential definition of the zeta function give the claimed consequences. The uploaded checker is finite diagnostic evidence only and was not executed.

## originality

FAIL

The prior indexed full-Witt census is not just a total number. It computes the same valuation-by-valuation centralizer kernels, the auxiliary high-ideal pair polynomial and the same subsequent triple sum. Its strata lift by the constant-rank kernel construction; removing the nonnilpotent line triples is then a direct subtraction. The difference in stated scope and the formal substitution of a motivic variable do not supply a distinct substantive triple computation.

## value

FAIL

The reduced motivic class is a natural invariant and the expression is correct, but the central repeated calculation is already supplied by the full-Witt census. The remaining operations are the routine constant-rank lift and subtraction for line triples; the point counts and zeta function then require no new structural calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
