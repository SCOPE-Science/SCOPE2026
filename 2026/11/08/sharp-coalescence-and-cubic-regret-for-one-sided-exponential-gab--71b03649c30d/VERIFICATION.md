---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The published sharp normalized bounds are Fminus=exp(-t/n)*tanh(t/2)*(t/n)/sinh(t/n) and Fplus=exp(t/n)*coth(t/2)*(t/n)/sinh(t/n). Differentiating gives the submitted stationarity equations; the ratio minimizes exactly at asinh(n), while published theorem establishes uniqueness of the two other extrema. For t=log(2n)+δ with |δ|<=2log(2n)/n, t*csch(t)=(t/n)e^(-δ)+O(t/n³) and (t/n)coth(t/n)=1+t²/(3n²)+O(t⁴/n⁴), proving δ_A=−L/(3n)+O(L²/n²), δ_B=+L/(3n)+O(L²/n²). Second derivatives at these points are ∓1/n+O(L/n²), so quadratic relative regret is (1/(2n))(L/(3n))²=L²/(18n³). Independent bisection/numerical evaluation for n=20,100,1000,10000 shows scaled gaps approaching 1/3 and both scaled regrets approaching 1, without being used to prove asymptotics.

## originality

PASS

PASS with explicit historical risk. Faulhuber and Shafkulovska 2022/23 FULL inspected §§2.3 and 7 establish the exact frame-bound formulas, existence and uniqueness, strict ordering and asinh(n) optimum. The new two-sided logarithmic separation constant 1/3 and paired equal cubic regret 1/18 are additional asymptotic implications derived here; they are not stated in inspected source sections. Published Resultary high-redundancy results for TWO-sided exponential windows or unequal tails have different objective functions and scales and cannot imply the one-sided constants. Janssen 1996 original full text was not accessible, so best-of-knowledge priority remains provisional.

## value

PASS

PASS. Quantifying the sharp asymptotic cost of choosing the condition-number optimum rather than independently optimizing both frame bounds is a natural finite-density frame-design question. The same 1/18 coefficient for distinct lower- and upper-bound regrets provides a precise stability/conditioning tradeoff and refines a previously known qualitative separation of three optimizers, not merely an arbitrary evaluation point.

The dated certificate retains the supplied scientific assessment, sources and limitations.
