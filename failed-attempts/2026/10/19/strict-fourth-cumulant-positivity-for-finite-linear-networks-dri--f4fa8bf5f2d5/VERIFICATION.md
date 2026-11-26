---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Hurwitz stability makes each response exponentially decaying; the input has finite fourth moment 24D²/r² from its exponential age, so the stationary convolutions exist in L⁴. Conditioned on the reset clock, Brownian increments on separate gaps are independent. An increment at backward age u between T_j and T_(j+1) enters the response with coefficient equal to the integral of h on [T_j,u]. Itô isometry gives the stated V, finite almost surely, and the conditional fourth moment 3V² ensures its finite second moment. The Gaussian mixture formula and independence give 3 times the sum of the variance contributions, with no term from independent Gaussian thermal forcing. If a nonzero response had constant V, Mecke's identity would force insertion of a clock point to preserve it for almost every clock and almost every insertion time. In each gap the continuous change is 2D F(t)[(b−t)F(t)−2 integral_t^b F], for F(t)=integral_a^t h. It must vanish everywhere in the gap. On a component where F is nonzero, differentiation forces F(t)=C(b−t); continuity and F=0 at its left boundary give C=0, a contradiction. All gaps then force h to vanish. This handles signed and unobservable channels, with strictness iff at least one response is nonzero. The covariance of the reset input is (2D/r)exp(−r|lag|), by survival across the lag, and the Gaussian OU replacement has exactly that covariance, so all linear output cross-covariances at all lags agree. An independently written exact generator solve reproduced both scalar formulas and the signed e^(−s)−2e^(−2s) example (variance 1/9, fourth cumulant 481/33075); these checks are corroborative. The frozen source was read but not run.

## originality

FAIL

The inspected chain theorem is narrower as a stated theorem, but its proof explicitly gives the conditional age-mean formula and derivative for an arbitrary signed exponentially decaying filter. The formulas themselves imply the frozen strict sign, including at transfer-function zeros, by a direct two-case argument. This is demonstrated coverage by implication in the accessible catalog, not a claim that an exact general theorem was printed earlier or that the alternate gap-splitting proof already appeared.

## value

FAIL

A sign theorem that distinguishes covariance-matched linear outputs despite sign changes is well motivated. But the exact strictness result is mechanically implied by the existing all-kernel conditional age-mean identity, and the matching second-order statistics follow by linearity from the known input covariance. The record provides an alternate proof rather than an additional exact invariant or structural consequence that survives the coverage check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
