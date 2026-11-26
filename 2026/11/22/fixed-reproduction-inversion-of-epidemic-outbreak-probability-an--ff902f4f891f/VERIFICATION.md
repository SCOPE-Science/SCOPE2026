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

The type-to-type next-generation matrix is an outer product with sole nonzero eigenvalue R(1-p+pA). Integrating the susceptible and removed balances on the positive vanishing-seed branch gives q=R[(1-p)(1-exp(-q))+p(A/c)(1-exp(-cq))]. After division by q, the right side of the normalized equation decreases strictly from 1-p+pA to zero; there is exactly one positive root. Writing h=cq and f(u)=integral_0^1 exp(-tu) dt, the root q decreases with c at fixed equation level, whereas reparametrizing by h shows h increases. For the population sum, implicit differentiation with D=(1-p)f'(q)+pAc f'(h)<0 gives the sign of T' as the opposite of the sign of A G(h)-G(q), where G(u)=exp(u)(-f'(u)) is strictly increasing. Since h>=q and A>1, T'<0. For survival, independent Poisson births only conditional on the shared exponential lifetime yield the joint rational offspring generating function. Its nonzero survival fixed point has class probabilities z/(1+z) and w/(1+w), w=Az/c. The scalar balance is strictly decreasing in z from a supercritical initial level. Comparing it at fixed z and then at fixed w proves z increases and w decreases. Population weighting and elimination with the same equation give P=1-1/(AR)-(1-p)(1-1/A)/(1+z), hence P is strictly increasing. The strictly monotone level-set comparisons include the endpoints. These are results about two distinct mathematical limits, not finite-population identities.

## originality

PASS

Credit prior rank-one heterogeneous SIR equations, product-dependent thresholds, concordance comparisons and the qualitative distinction between size and outbreak probability at matched reproduction. The supported distinct claim is the simultaneous strict opposite ordering for the whole specified fixed-product path at every supercritical rate, with class-resolved directions. Closest available general and catalogue statements do not imply it under their comparison hypotheses. Harris et al., Kawagoe et al. and Nandi–Allen were not independently inspected in full; priority on those comparisons remains qualified, not ruled out.

## value

PASS

The result isolates a structural limitation of a threshold summary in an abstract stochastic and deterministic epidemic model: identical invasion eigenvalues do not jointly rank the probability of escaping the initial branching phase and the positive macroscopic attack fraction. The all-allocation strict law and founder-class/population distinction are substantive compared with a sampled or endpoint-only example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
