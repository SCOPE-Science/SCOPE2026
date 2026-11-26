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

The stationary density h=k(1+b^-1 1_I), I=[0,1/b), follows by summing the m full inverse branches and the last branch on I, then normalizing with k=b^2/(b^2+1). The same branch sum sends u=xh to b^-1 u plus the piecewise-constant correction k m(m-1)/(2b^2)+(k m/b^2)1_I. Thus there is no -b^-3 component already at the starting slopes: u and the two constant pieces span an invariant three-dimensional subspace. With e=1-b 1_I of mass zero, P e=-b^-2 e. Center u by subtracting mu h; its one-step action is b^-1(u-mu h)+delta e, where delta is the e component of the correction. Pairing with x and solving the recurrence gives B=-delta int(xe)/(b^-1+b^-2) and A=Var(X_0)-B, for all lags including zero. Independent symbolic replay /workspace/reviews/replay1.py recovers the stated coefficients and variance rational function and checks that the numerator of -V' after clearing the positive denominator has all positive coefficients in b-1. The manuscript's shifted positivity polynomials also give A>0 and bA>B, controlling odd lags; B>0 follows directly. Stationarity gives the finite covariance sum, absolute summability gives the Green–Kubo limit, and the strict decrease of the rational expression for b>1 applies to the increasing admissible integer-family bases. Only this family and stationary starts are covered, and no CLT is proved. The frozen check.py was read, not executed.

## originality

PASS

Best-of-knowledge pass for the explicit ordered transport-variance result, supported by the stationary-coordinate calculation. The density and piecewise-affine spectral action are prior, and the spectral origin and exponential form of the covariance are direct consequences of that action, not independently new operator or decay theorems. The distinct conclusion is the evaluated Green–Kubo coefficient and its strict parameter ordering; the ordering does not follow from the prior spectral asymptotics.

## value

PASS

The coordinate is a canonical observable and these bases are the natural two-step quadratic greedy family, not a sample chosen after computing. The evaluated long-run variance and its strict ordering compare stationary cumulative fluctuations across the entire integer family. That comparison cannot be inferred from faster contraction rates alone because the weights change and the second mode alternates; the additional positivity argument gives an exact sign and limiting noise scale. The affine spectral construction itself is not the novel or valuable claim here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
