---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

With x=t/(t+2), the stage recurrence is Y_i=1-x-2x times the off-diagonal weighted sum of prior stages, where the weights are A^I+(r-1)A^E. In particular, Y_1=1-rx and Y_2=1-4rx/3+r(r+2)x^2/9. Exact substitution through the globally stiffly accurate last row gives the stated quartic; changing to the Bernstein basis gives the five listed coefficients. The cubic's derivative has exactly one zero in (0,1), a minimum of the cubic; the cubic starts positive, ends negative, and crosses between 0.22 and 0.221. For 0<r<=rho<1/3, r(3-r)^2<3 and all five coefficients are nonnegative. The zeroth term is strictly positive for any finite t. For rho<r<1 the limiting last coefficient is negative, hence so are all sufficiently large finite steps. At t=4, x=2/3 and R=-H/729; both the Bernstein certificate on [1,3/2] and the positive shifted power certificate on [3/2,infinity) check exactly. H(1)=51 gives -17/243. The root and reciprocal round as stated.

## originality

PASS

The ARS tableau, EIN construction and polynomial/Bernstein methods are not new. The narrow distinct result is the all-step necessary-and-sufficient scalar sign threshold for this unmodified pair and split, including finite-step failure at and above unit ratio. The strongest inspected same-method antecedents concern other invariants.

## value

PASS

For an established third-order EIN method, the sharp ratio gives an actionable necessary scalar test for applications needing nonnegative heat data even at one interior node. It separates the stabilizer needed for this invariant from energy/Fourier stability and gives a finite counterexample outside the sign regime even where large-step limits alone do not settle the matter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
