---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The full proof is analytic and applies to all Borel couplings on the unit square. It uses (i) the conditional Brownian-bridge decomposition into independent gap bridges, (ii) the exact polynomial dual minorant \(12V(x,y)\ge\phi(x)+\phi(y)\), (iii) integration against fixed uniform marginals, and (iv) the characterization of equality support as the graph of the half-period translation. The infinite-dimensional conclusion cannot be inferred from numerical optimization or grid checks alone.

Run `python verify.py` using Python 3.10+ and the standard library. The verifier checks the dual inequality and equality support with exact rational arithmetic over finite rational grids; checks mixed- and same-half polynomial bounds; compares the gap formula to a direct exact \(2\times2\) Gaussian regression calculation for many distinct interior rational observation pairs; and checks exact integral constants for shifted, independent, and centrally reflected uniform designs. The run's package source passed 22,248 rational assertions. A missing assertion or changed package must be rechecked before relying on it. None of these finite tests certifies novelty or replaces the analytic proof.

The exact risk values are \(1/64\) (uniquely optimal coupling), \(1/40\) (independence), and \(5/192\) (reflection). The optimality statement is restricted to uniformly distributed individual observation sites and the expected conditional integral variance of the pinned Brownian bridge; its unrestricted deterministic two-site comparator has risk \(1/108\), smaller by design because it has no marginal-uniformity constraint.
