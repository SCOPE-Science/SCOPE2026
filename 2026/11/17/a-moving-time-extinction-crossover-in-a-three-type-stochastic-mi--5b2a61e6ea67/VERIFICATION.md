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

The actual three-coordinate stochastic map at 2b=1 preserves unit sum and yields s_{n+1}=s_n^2+r(1-(3/2)s_{n-1}(1-s_{n-1}))s_n, r=2alpha(1-alpha), B in [5/8,1]. At alpha=0 it squares exactly; for fixed 0<alpha<1, u_n<=max(alpha,1-alpha) and the product (s_{n+1}/(r s_n)) has summable deviations and strictly positive finite limit. With r_N=cq^{2^{N-1}}, log(s_N/s_1^{2^{N-1}}) is squeezed by r_N 2^{N-1}/s_1^{2^{N-2}} ->0 (q=a0a2<1/4). Since s_1=q+O(r_N), s_N/r_N->1/c; recurrence then gives (1+c)/c² at offset 1 and all fixed higher offsets by induction. Independently rederived exact scalar recurrence and iterated original map at 100-digit precision with c=1.7 and N=4,5,6, matching limits.

## originality

PASS

The original Example 3.9 provides fixed-parameter dynamics, not a simultaneously N-dependent mixing weight and N-dependent observation time. A published 2026 five-phase edge-cycle result proves an analogous scalar quadratic crossover with coefficient c+c², imposing substantial method priority, but its invariant one-dimensional map and 5-iteration clock are different from this coupled three-species recurrence with the state-dependent B(s_{n-1}). No direct stronger implication located. This is originality of application and exact coefficient, not of the generic quadratic mechanism.

## value

PASS

The 2024 source model has two fundamentally distinct endpoint and interior extinction rates; the exact crossover profile identifies how and when the rate changes in the natural singular perturbation scaling. The state-dependent two-step coupling makes the explicit coefficient nontrivial and potentially useful in nearby stochastic-mixture analyses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
