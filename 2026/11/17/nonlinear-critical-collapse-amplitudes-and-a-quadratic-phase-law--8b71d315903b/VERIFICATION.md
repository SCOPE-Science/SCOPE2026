---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Exact log-odds conjugacy at alpha=2 gives (a,b)->(|a-kappa(b)|,|b-kappa(a)|), kappa(s)=log((1+exp(s))/2), and strict order persists. Larger log-odds decreases and the summability of kappa(smaller) plus its recurrence forces both coordinates to zero. If second coordinate never crosses b<=kappa(a), the positive order gap strictly increases despite convergence, contradiction; the smooth cone is forward invariant by kappa 1-Lipschitz. There T=Lz+q(z)+O(|z|^4), L=[[1,-1/2],[1/2,-1]], L^2=(3/4)I and Q=Lq+q o L =(-3a²+4ab-8b²,-4ab-b²)/32. Since the two-step multiplier rho=3/4 dominates quadratic errors, products show nonzero W=lim rho^-n z_even and summable corrections yield exact second coefficient -Q(W)/(rho(1-rho)), validated independently by SymPy. Odd phase is L W; max coordinate remains positive in both parities, so nonlinear max ratios converge to 3/4, not merely linearly approximated. On diagonal scalar multiplier 1/2 with quadratic correction A²/2 gives two-step 1/4. Remainder and normalizations checked; tie-labelled original system interpretation is expressly excluded.

## originality

PASS

Prior Satur Section 5.2 explicitly states Theorem 2 gives no rate and presents 3/4 as numerical/leading-order piecewise-linear calculation; it does not prove a nonzero nonlinear phase W, quadratic coefficient or sharp diagonal asymptotic. Related switching-manifold stability results do not specialize to explicit all-orbit coefficients automatically.

## value

PASS

The nonlinear global-to-local normal form identifies sharp two-phase asymptotics and a universal quadratic correction in a natural singular critical map; it resolves a rate explicitly left unproved in source and explains the discontinuity of phase behavior at diagonal initial data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
