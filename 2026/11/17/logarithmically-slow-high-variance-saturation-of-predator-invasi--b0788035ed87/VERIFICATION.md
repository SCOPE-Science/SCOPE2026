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

For fixed 0<p<1, 0<epsilon<min(p,1-p) and all positive model coefficients, stationary OU forcing has N(0,s^2) marginal, so even symmetry reduces the invasion exponent gap to sqrt(2/pi)/s ∫_0^infty Q(t)e^{-t²/(2s²)}dt. Expand arctan t at infinity: Q(t)=A/t+O(t^-2), A positive from strict decrease of Holling-II Phi prime. Subtract A*1_{t>=1}/t to obtain integrable R with B=∫R; dominated convergence gives B. Exact 1/2 E1(1/(2s²)) expansion yields log s+(log2-EulerGamma)/2 and the stated o(1/s). Window identity follows algebraically from its two endpoint definitions, without any sample-path or extinction-probability claim. Independently evaluated the rational benchmark A=96/(1225*pi)=0.0249451012846... and scaled leading coefficient 192/(1225*pi*sqrt(2*pi))=0.01990331118265..., matching the formula. No uniformity in degenerate ecological parameters is claimed.

## originality

PASS

The source 2026 bounded-refuge predator paper supplies exactly the Gaussian expectation, monotonicity in stationary standard deviation, endpoint limit and reversal window; these are credited. Neither its inspected Proposition 8.6 nor earlier bounded-forcing population papers states the sharp (log s)/s rate, explicit endpoint derivative coefficient and finite-part B, and Resultary found no preceding stronger source. Qualified PASS relative to checked primary text.

## value

PASS

A sharp rate and finite-part constant for the high-variance saturation of an ecologically motivated invasion threshold is a specific, usable quantitative refinement of an already known monotone limit. The exact (log s)/s boundary-layer sensitivity and mortality-window deficit can affect finite-noise approximations. Although Gaussian E1 asymptotics are standard, identifying the correct model-specific amplitude and finite part for the nonlinear bounded refuge is not simply restating the original endpoint theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
