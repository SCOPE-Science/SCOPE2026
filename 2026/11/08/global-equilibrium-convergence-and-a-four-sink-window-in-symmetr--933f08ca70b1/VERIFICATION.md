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

# Verification of the convergence and four-sink theorem

The separately supplied `verify.py` is executable with Python 3 and only the standard library. It checks the nonuniform equilibrium equations and three exact Jacobian mode identities with rational coefficients; it also samples strict negativity of the rational planar Dulac divergence and checks the homogeneous transition eigenvalues. A successful run prints `PASS: 348 exact arithmetic assertions; finite support only`.

Critical noncomputational steps are the invariant ordering identity, the monotone adjacent-gap ratio, uniform positive/upper population bounds, and the reduction of a compact omega-limit set to an equality plane. Every omega-limit set of an autonomous bounded orbit is internally chain transitive. The planar restricted system has finitely many equilibria, and the strictly negative Dulac divergence excludes periodic or closed heteroclinic/homoclinic cycles. Therefore the planar internally chain transitive limit set is a single equilibrium. The proof in `RESULT.md` covers all positive values of \(a,\mu\) and both critical boundaries; the finite checker is neither exhaustive over parameters nor a machine certification of this limit-set theorem.

The original source's fold and homogeneous local stability are not considered newly established here. Independent mathematical audit has not been performed.
