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

Each shifted layer has uniformly bounded atom count on a unit horizontal window, and the weights are summable. The heights converge to ±1 without attaining either endpoint. Poisson summation for the half-period shift gives the factor (−1)^k and spacing 2^(−q), and the absolute layer masses sum on each compact frequency interval, justifying measure identity and regrouping shared atoms. For large positive t the triangle inequality and point count give a sum with phase a q^β+2πb(t−1)q^(−γ). For the lower bound the nearest integer to t lies strictly in the window and every layer has positive phase there; its sum has an extra (log 2)q penalty. The phase's continuous minimizer has size t^(1/(β+γ)); integer rounding and the linear penalty are o(t^s) since β>1. A polynomial-size index cutoff contributes only a logarithmic factor, and the remaining tail is dominated by exp(−a q^β). The bounds thus give the displayed coefficient L and exponent s, with negative t following by evenness. In the quadratic case f''≥2 yields a uniformly bounded lattice Gaussian sum after factoring out the continuous minimum; rounding costs O(1). On [m,m+1), the character test with frequency 2^(N_m−1) leaves exactly q=N_m in the frozen sum: the normalized geometric sum is nonzero only when 2^q divides 2^(q−1)+2^(N_m−1), exactly when q=N_m. The freeze error is bounded by a q^(−1)-weighted sum, which is o(main) by splitting at half the saddle location and using strong convexity below it. The decaying branch after e^(−2πx) normalization is exponentially negligible. Variation dominates the resulting character integral and [floor(t),floor(t)+1) lies in the required open window even for integer t. This gives the bounded error uniformly in real t.

## originality

PASS

The shifted-lattice measure architecture and Poisson expression are credited to Değer–Favorov. The qualified pass is for the explicit asymptotic deficit with tunable exponent and coefficient and, in the quadratic model, the uniform two-sided sharpened envelope despite cancellations. Existing growth-type estimates and the available indexed claims do not directly imply this quantitative statement. The closest example section could not be read directly, so this is not an exclusion of full-text overlap there.

## value

PASS

The natural exponential-scale bound loses information when support approaches but does not meet its boundary. Keeping the same limiting tube, the construction realizes every fractional logarithmic deficit scale and gives matching constants in the leading exponent. The quadratic projection resolves the obstruction that signed overlapping layers need not sum in variation; it yields a uniform two-sided envelope, not just values along a sequence or a bound before cancellation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
