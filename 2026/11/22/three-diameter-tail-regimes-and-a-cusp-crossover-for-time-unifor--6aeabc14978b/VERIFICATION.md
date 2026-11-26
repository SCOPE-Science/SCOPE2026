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

At fixed positive gap Δ<2π, the squared chord length is maximized uniquely at midpoint π. The maximal distance at that gap is F=Δ+2β sin(Δ/2), whose derivative gives the endpoint and interior maximizers in RESULT.md. The diameter excess above 2π is the integral of 2 sqrt(β²−1)/β from 1 to β, giving the stated 3/2-power coefficient. In the endpoint coordinates s,u the subcritical deficit is (1−β)(s+u)+O((s+u)^3), and at β=1 it is (s³+u³)/6+O((s+u)^4); the triangular and cubic sublevel areas give the two constants, including the factor 2/(4π²) for the orders. At a prolate maximum the coefficients of (Δ−Δβ)^2 and (midpoint−π)^2 are qβ/4 and qβΔβ/Dβ, respectively, and the gap-midpoint change of variables has unit Jacobian. In the moving window compactness localizes both orders at the critical endpoints. With w=s+u the chord never exceeds F(2π−w); thus for small w the deficit is bounded below by c w³−|β−1|w uniformly near β=1. This gives bounded rescaled support. The rescaled deficit converges uniformly there to M(λ)+(x³+y³)/6−λ(x+y); the limiting level boundary has measure zero and the sublevel has positive area. The indicator densities converge in L1, and their normalized versions prove the branchwise total-variation claim. The branch probabilities are in fact exactly equal once localization holds. For λ=−L the scale L^−1 gives a unit triangle; for λ>0 set x0=√(2λ) and write the one-coordinate rise as (x−x0)^2(2x0+x)/6, which both confines and proves convergence to the local disk at scale x0^−1/2. This yields both matching constants without needing a uniform-in-λ convergence statement.

## originality

PASS

The classical curve and same-day geometric and asymptotic analogues are credited. The closest result for the same critical curve uses a measure vanishing at the cusp in phase coordinates. The closest moving-window theorem concerns a different curve, degeneracy, and parameter. Neither supplies the stated phase-uniform cubic window and mark law. No equivalent or dominating statement was established in the examined sources; same-day catalogue dates do not settle priority.

## value

PASS

The tracer-radius threshold cancels the linear endpoint deficits and moves the unique maximizing pair off the parameter boundary. The unified quantitative description gives both the change of exponent and where near-diameter pairs actually occur in the transition, information missing from fixed-parameter or arclength results. The distinction is directly useful for phase-uniform rolling experiments and is not just a rewording of the classical geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
