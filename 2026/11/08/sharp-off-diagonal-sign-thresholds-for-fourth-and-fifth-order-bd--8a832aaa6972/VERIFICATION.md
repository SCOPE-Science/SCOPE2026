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

Normalizing δ_k(z)=Σ_{j=1}^k(1-z)^j/j gives p4 and p5 exact rational polynomials and [z²]p4^α=α(1152α-252)/625, [z²]p5^α=300α(150α-13)/18769. BDF6 has [z²]p6^α=α(150+7200α)/2401>0. At each threshold, the derivative recurrence nW_n=Σ_{j=1}^{min(k,n)}(((1+α)j-n)p_j W_{n-j}) gives rational signs W1<0, W2=0, W3..W999<0 (independently recomputed exactly). Schur reductions certify all zeros of q4 lie outside 7/5, q5 outside 4/3, which allows Cauchy eta-coefficient bounds; the explicit half-tail bounds for n>=1000 have C1/1000=.34125 or .3912, plus <.01 remainder, below q(1)^α. Thus W_n<0 for all n>=1000 analytically, not by finite exhaustion. Positive-series fractional composition transfers strict negativity for smaller α. Independent numeric root moduli and rational tail-bound checks corroborated.

## originality

PASS

The inspected BDF2 and BDF3 sign theorems are for different multistep polynomials and thresholds. Lubich’s 1986 foundational CQ treatment and Schädle et al 2005 fast CQ algorithm give generating symbols, not a sharp BDF4/5 every-index sign classification or BDF6 obstruction. No dominating theorem or exact table was located in bounded specialist search. Best-of-knowledge priority remains provisional.

## value

PASS

Sign definiteness of every off-diagonal fractional history weight matters to comparison and discrete-energy arguments. Exact admissibility thresholds for two higher BDF orders and the sharp sixth-order obstruction, backed by an infinite-tail proof, address a structural property a small numerical coefficient scan cannot establish. No solver-level maximum principle is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
