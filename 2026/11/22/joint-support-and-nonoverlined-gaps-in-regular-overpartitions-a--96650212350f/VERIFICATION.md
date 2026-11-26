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

The final claim and constants are unchanged. Frozen Step 3 invoked consecutive admissible integers and span one to justify a quantitative minor-arc bound; in particular all admissible sizes are odd when ell=2, and span one alone is not a uniform estimate. The corrected RESULT.md gives a uniform bound using the untouched block j=1 mod ell, 1/t<=j<=2/t: a quadratic bound near zero, geometric-sum cancellation away from 2pi k/ell, and strictly positive Riemann-sum integrals in the remaining small arcs. At the saddle, deletion and the deterministic shift perturb the standardized variance by O(t) and the mean by O(sqrt(t) log(1/t)); the odd imaginary linear and cubic terms cancel to first order, and the uniform integrated relative error is O(t log^2(1/t))=o(sqrt(t)). I also checked the shift-only truncation and the joint-tail restrictions, the latter from the exact factor 2q^j/(1+q^j). Geometric/Bernoulli factorization gives both exact coefficient identities, including n=0 and a>=b. The Boltzmann survival is the displayed limit after t_n~pi sqrt(rho)/(2sqrt(n)); the diagonal component has half the mass and the interior derivative gives the stated density. Conditional on the first nonoverlined gap j, the Bernoulli marker makes coincidence probability 1/(1+exp(-tj)); tail summation gives E X=sqrt(pi/(2rho t))+O(1), E X^3=O(t^-3/2). Expansion and the repaired conditioning bound give the stated fixed-weight coefficient pi/(8 rho^(1/4)).

## originality

PASS

The two marginal definitions and the general running-minimum and marked-event mechanisms are not new. The checked contribution is the coupling between nonoverlined absence and full-support absence in regular overpartitions, including the distinct sharp fixed-weight coincidence coefficient. The repair makes the closest known unmarked correction analogy explicit.

## value

PASS

These are two natural mex conventions on the same random overpartition. Their coupling has both a singular and a continuous component, and the actual lattice coincidence probability has a positive first correction that cannot be obtained from the marginal Rayleigh laws or from joint weak convergence. The explicit correction quantifies a marking effect for a fixed-weight ensemble. This remains worthwhile after crediting the existing threshold and unmarked correction analogues.

The dated certificate retains the supplied scientific assessment, sources and limitations.
