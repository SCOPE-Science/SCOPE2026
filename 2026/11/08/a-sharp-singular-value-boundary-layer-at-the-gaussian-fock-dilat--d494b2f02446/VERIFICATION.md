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

# Reproducible checks and their limits

The theorem was checked analytically through five independent identities: the exact Hilbert–Schmidt trace \(\operatorname{Tr}(T^*T)=X^{-1/2}\), the Gaussian reproducing kernel, the Gaussian fixed-point eigenfunction identity, the trace-sum equality \(L/(1-q)=X^{-1/2}\), and the coherent-kernel lower bound outside the bounded regime. The critical essential-norm proof additionally uses a normalized weakly null family of squeezed Gaussian vectors and a coefficientwise monotonicity comparison. The singular-value layer is an asymptotic expansion of \(q\) and \(L\) with the floor error uniform on compact scales.

Run `python checker.py` with Python 3, NumPy and SciPy. It constructs finite monomial sections of the *weighted composition operator itself*, compares nine largest singular values in each of six parameter sets against the analytic prediction, checks both first and second Gaussian trace moments, checks the fixed-point parameters, and samples the limiting boundary layer at shrinking distances to the compactness threshold. The executed checker reported **96 passed finite assertions**. Finite sections and numerical tolerances are diagnostic only, not exhaustive verification or proof of infinite-dimensional claims.

A separate proof reconstruction checked the parameter boundaries \(t=0\), \(t=1-a^2\), \(t>1-a^2\), \(a\in(0,1)\), and \(p>0\); the count law is only asserted for fixed \(0<\varepsilon<a^{-1/2}\). No claims about independent external certification are made.
