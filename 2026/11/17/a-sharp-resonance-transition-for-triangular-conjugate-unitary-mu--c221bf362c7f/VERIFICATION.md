---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For arbitrary b in L-infinity of circle, the fibre matrix is [[e^{-i theta},b(theta)],[0,e^{i theta}]]. Its exact nth upper entry is b sin(n theta)/sin theta, and the fibre singular norm is Phi(|upper|); spectrum is the full circle. A bounded shear with upper b/(2i sin theta) conjugates the operator to U* direct-sum U exactly when b/sin theta is bounded; conversely uniformly bounded powers require this ratio by the almost-everywhere lower bound sup_n |sin(n theta)|>=sqrt3/2, and a Kreiss bound near both spectral crossings +/-1 forces its local vanishing. Riemann-Lebesgue mixing of oscillating sine against a positive-measure near-norm set proves all power norms converge when bounded. For b=c|sin theta|^alpha, rescale theta=x/n or theta=epsilon*x near crossings for sharp alpha<1 growth and resolvent coefficients. At alpha=1, retaining the diagonal singular value yields sqrt(1+c²/4), unlike alpha>1 value 1. Independent scalar fibre norm grid for c=1.3, alpha=0,.4,1,1.5, epsilon=0.0002 matched 1.3,0.78817,1.192686,1 within scale error. Finite grids corroborate; universal measurable-symbol equivalences and asymptotics follow from proof.

## originality

PASS

Best-of-knowledge comparison against actual published findings, the identified primary literature, and explicit mathematical implication checks distinguishes known ingredients from this result; residual inaccessible or unindexed literature is not assumed absent.

## value

PASS

The diagonal unitary spectra collide at theta=0 and pi; exact resonance of the triangular coupling is a naturally motivated operator-growth problem. One family realizes a continuum of sharp fractional power and resolvent exponents, isolates the exact Kreiss/similarity threshold and nontrivial critical resolvent constant; this is substantive quantitative information beyond known one-step singular norms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
