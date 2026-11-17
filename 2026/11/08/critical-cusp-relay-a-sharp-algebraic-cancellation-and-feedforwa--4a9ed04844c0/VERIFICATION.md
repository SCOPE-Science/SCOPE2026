---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The RESULT.md normalization 2F(2s)-1=tanh(s) and row sums 1 give a,b scalar flows s′=-(s-tanh s) and relay u′=-u+tanh(pa-(1-p)b). For s>0, g(s)>0, g(s)=s^3/3+O(s^5), so s~sqrt(3/2)t^-1/2 and t^3/2 g(s)~sqrt(3/2)/2. Uniqueness of autonomous flow gives exact signed shift tau=int_b0^a0 ds/g(s), and a(t)-b(t)=int_(t-tau)^t g(b(s))ds~sqrt(3/2)tau/(2t^3/2). Exponential convolution preserves the leading forcing coefficients, proving off-balance t^-1/2 and exactly balanced t^-3/2, with a0=b0 identically zero forcing and relay u(t)=u0 e^-t. For p_T=1/2+lambda/T, frozen terminal flows give T^3/2 u(T) -> sqrt(3/2)(tau/4+2lambda). Our separate solve_ivp/quadrature gave balanced 1.291757 at T=1300 vs 1.291849 target and crossover 4.96647 vs 4.96608. Finite checks are corroboration only; no uniform-in-lambda or general network claim.

## originality

PASS

At the same critical logistic model, known cusp and row-stochastic global convergence are prior, but the reducible mixed-sign relay, exact finite signed time-shift coefficient, exceptional exponential cancellation, and O(1/T) coupling crossover are not derived by the inspected stronger global comparison/irreducible logarithmic law. The Resultary search returned the present record plus the separately fully read Nov 1 global theorem, which bounds all amplitudes but has no mixed-sign cancellation coefficient.

## value

PASS

A three-node feedforward cusp is a natural minimal reducible network: cancellation changes the extinction exponent by a full power, and a measurable initial-state quadrature plus sharp crossover distinguish transient regimes hidden from spectral linearization. It is a useful structural boundary result, not just a fitted decay exponent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
